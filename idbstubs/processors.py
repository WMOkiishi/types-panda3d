import logging
import re
from collections.abc import Sequence
from itertools import combinations, zip_longest
from typing import Final

from .reps import (
    Alias, Class, File, Function, Parameter, Signature, TypeVariable
)
from .special_cases import (
    ATTRIBUTE_NAME_SHADOWS, DEFAULT_RETURNS, INPLACE_DUNDERS,
    PARAM_TYPE_OVERRIDES, RETURN_TYPE_OVERRIDES
)
from .typedata import (
    combine_types, get_param_type_replacement, process_dependency,
    subtype_relationship
)
from .util import flatten

_logger: Final = logging.getLogger(__name__)
_absent_param: Final = Parameter('', 'Never', is_optional=True, named=False)

VECTOR_NAME_REGEX: Final = re.compile(
    '((?:Unaligned)?L(?:VecBase|Vector|Point))([2-4])([dfi])'
)
RETURN_SELF: Final = [
    '__floordiv__',
    '__pow__',
    '__round__',
    '__floor__',
    '__ceil__',
]


def merge_parameters(p: Parameter, q: Parameter, /) -> Parameter | None:
    if p.named and q.named and p.name != q.name:
        return None
    if p.is_self != q.is_self:
        return None
    t, u = p.type, q.type
    if (t and not u) or (u and not t):
        return None
    if not t and not u and not p.is_self:
        return None
    t_subtypes_u, u_subtypes_t = subtype_relationship(t, u)

    # Make sure assigning an argument by name will still work
    if p.named and not q.named and not u_subtypes_t:
        return None
    if q.named and not p.named and not t_subtypes_u:
        return None

    # We've already checked the subtype relationship, so use it if possible
    if u_subtypes_t:
        merged_type = t
    elif t_subtypes_u:
        merged_type = u
    else:
        merged_type = combine_types(t, u)

    return Parameter(
        p.name if p.named else q.name,
        merged_type,
        is_optional=p.is_optional or q.is_optional,
        named=p.named or q.named,
        is_self=p.is_self
    )


def merge_signatures(a: Signature, b: Signature, /) -> Signature | None:
    """If possible, return a signature equivalent to the two supplied.
    Otherwise, return `None`.
    """
    if abs(a.min_arity() - b.min_arity()) > 1 or abs(a.max_arity() - b.max_arity()) > 1:
        # If the min or max arity differs by more than 1, the signatures can't be merged
        return None
    if not (a.return_type and b.return_type):
        # Don't merge signatures if we're not sure what the return types are
        return None
    # Signatures with differing return types can only be merged if their parameters are identical
    w1_locked = w2_locked = a.return_type != b.return_type
    merged_params: list[Parameter] = []
    for p, q in zip_longest(a.parameters, b.parameters, fillvalue=_absent_param):
        pq = merge_parameters(p, q)
        if pq is None:
            return None
        # Ensure we don't lose information about which sets of arguments are allowed
        p_changed, q_changed = p != pq, q != pq
        if (w1_locked and p_changed) or (w2_locked and q_changed):
            return None
        w1_locked |= q_changed
        w2_locked |= p_changed
        merged_params.append(pq)
    merged_return = combine_types(a.return_type, b.return_type)
    return Signature(merged_params, merged_return)


def get_signature_depths(signatures: Sequence[Signature]) -> list[int]:
    """Return a list of integers such that if the given signatures are ordered
    according to the integer appearing at the same index, a type checker will
    understand which to use.
    """
    # A list of lists of the indices of the signatures that should be defined
    # after the signature at the outermost index
    define_after: list[list[int]] = [[] for _ in signatures]
    for (i, w1), (k, w2) in combinations(enumerate(signatures), 2):
        if w1.min_arity() != w2.min_arity():
            continue
        w1_first = w2_first = True
        w1_params = (p for p in w1.parameters if not (p.is_self or p.is_optional))
        w2_params = (p for p in w2.parameters if not (p.is_self or p.is_optional))
        for p, q in zip(w1_params, w2_params):
            if not (w1_first or w2_first):
                break
            p_subtypes_q, q_subtypes_p = subtype_relationship(p.type, q.type)
            w1_first &= p_subtypes_q
            w2_first &= q_subtypes_p
        if w1_first:
            define_after[i].append(k)
        elif w2_first:
            define_after[k].append(i)
    sig_depths = [0 for _ in signatures]
    for i, others in enumerate(define_after):
        seen = {i}.union(others)
        while others:
            sig_depths[i] -= 1
            next_others: list[int] = []
            for k in flatten(define_after[j] for j in others if j not in seen):
                if k in seen:
                    continue
                seen.add(k)
                next_others.append(k)
            others = next_others
    return sig_depths


def process_signatures(signatures: Sequence[Signature]) -> list[Signature]:
    """Sort and compress the given sequence of function signatures."""
    depths = get_signature_depths(signatures)
    sorted_signatures: list[Signature] = []
    for i, depth in sorted(enumerate(depths), key=lambda x: x[1]):
        signature = signatures[i]
        if depth == 0:
            account_for_casts(signature)
        sorted_signatures.append(signature)

    merged_signatures: list[Signature] = []
    for new in sorted(sorted_signatures, key=Signature.get_arity):
        for i, old in enumerate(merged_signatures):
            if (merge_result := merge_signatures(old, new)) is not None:
                # The signatures were successfully merged
                merged_signatures[i] = merge_result
                break
        else:
            # The signature couldn't be merged with any already in merged_signatures
            merged_signatures.append(new.copy())
    return merged_signatures


def account_for_casts(signature: Signature) -> None:
    for param in signature.parameters:
        replacement = get_param_type_replacement(param.type)
        if replacement is not None:
            param.type = replacement


def process_function(function: Function) -> Function:
    new_sigs = process_signatures(function.signatures)
    default_return = DEFAULT_RETURNS.get(function.name)
    return_overrides = RETURN_TYPE_OVERRIDES.get(function.scoped_name, {})
    param_overrides = PARAM_TYPE_OVERRIDES.get(function.scoped_name, {})
    if isinstance(return_overrides, str):
        return_overrides = {i: return_overrides for i in range(len(new_sigs))}
    for i, sig in enumerate(new_sigs):
        if sig.return_type:
            return_override = return_overrides.get(i)
        else:
            return_override = return_overrides.get(i, default_return)
        if return_override is not None:
            if sig.return_type:
                _logger.debug(f'Changed return type of {function} from'
                              f' {sig.return_type!r} to {return_override!r}')
            sig.return_type = return_override
        for j, param in enumerate(sig.parameters):
            param_override = param_overrides.get((i, j))
            if param_override is not None:
                if param.type:
                    _logger.debug(f'Changed type of parameter {param}'
                                  f' in {function} to {param_override!r}')
                param.type = param_override
    shadowed_names = ATTRIBUTE_NAME_SHADOWS.get('.'.join(function.namespace))
    if shadowed_names is not None:
        for sig in new_sigs:
            for param in sig.parameters:
                if param.type in shadowed_names:
                    param.type = 'core.' + param.type
            if sig.return_type in shadowed_names:
                sig.return_type = 'core.' + sig.return_type
    function.signatures = new_sigs
    match function:
        case Function(
            name='__eq__' | '__ne__',
            signatures=[
                Signature(
                    parameters=[
                        Parameter(is_self=True),
                        Parameter() as other_param,
                    ]
                )
            ]
        ):
            other_param.type = 'object'
            other_param.named = False
        case Function(
            name='__setattr__',
            signatures=[
                Signature(
                    parameters=[
                        Parameter(is_self=True),
                        Parameter() as name_param,
                        Parameter() as value_param,
                    ]
                ) as sig
            ]
        ):
            name_param.type = 'str'
            value_param.type = 'Any'
            sig.return_type = 'None'
        case Function(
            name='assign',
            namespace=[*_, class_name],
            signatures=[
                Signature(
                    return_type=return_type,
                    parameters=[
                        Parameter(is_self=True) as self_param,
                        Parameter(type=param_type) as copy_param,
                    ]
                ) as sig
            ]
        ) if class_name == param_type == return_type:
            self_param.type = 'Self'
            copy_param.type = 'Self'
            sig.return_type = 'Self'
        case Function(
            name=name,
            namespace=[*_, class_name],
            signatures=[Signature(return_type=return_type), *_] as signatures,
        ) if name in INPLACE_DUNDERS and return_type in (class_name, ''):
            for sig in signatures:
                sig.parameters[0].type = 'Self'
                sig.return_type = 'Self'
    return function


def process_dependencies(file: File) -> None:
    current_dir = '.'.join(file.this_namespace())
    seen = set[str]()
    for name in file.get_dependencies():
        if name in seen:
            continue
        seen.add(name)

        def alias_of(definition: str) -> None:
            alias = Alias(name, definition, is_type_alias=True)
            file.nested.append(alias)

        def as_type_var(bounds: Sequence[str], variance: str) -> None:
            type_var = TypeVariable(name, bounds, variance)
            file.nested.append(type_var)

        def import_from(module: str) -> None:
            if not module.startswith(current_dir):
                file.imports[module].append(name)

        processed = process_dependency(
            name, if_alias=alias_of, if_import=import_from,
            if_type_var=as_type_var
        )
        if not processed:
            _logger.warning(f'Unknown type {name!r} in {current_dir!r}')


def process_vector_class(vector: Class) -> None:
    """Process a representation of a Panda3D vector class whose name
    matches `VECTOR_NAME_REGEX`, applying various special cases.
    """
    name_match = VECTOR_NAME_REGEX.match(vector.name)
    assert name_match is not None
    kind, dimension, suffix = name_match[1], name_match[2], name_match[3]
    class_body = dict(vector.body)
    if kind.endswith('VecBase'):
        class_body.pop('get_data', None)
        class_body.pop('getData', None)
    if suffix == 'i' and not kind.startswith('Unaligned'):
        class_body.pop('__truediv__', None)
        class_body.pop('__itruediv__', None)
    for name in RETURN_SELF:
        match class_body.get(name):
            case Function(signatures=[
                Signature(parameters=[
                    Parameter() as self_param, *_
                ]) as sig
            ]):
                self_param.type = 'Self'
                sig.return_type = 'Self'
    match class_body.get('__len__'):
        case Function(signatures=[Signature() as sig]):
            sig.return_type = f'Literal[{dimension}]'
    vector.body = class_body
