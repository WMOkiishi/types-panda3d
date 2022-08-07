import logging
from collections.abc import Sequence
from itertools import combinations, zip_longest
from typing import Final

from . import special_cases
from .reps import Alias, File, Function, Parameter, Signature
from .typedata import (
    combine_types, get_param_type_replacement, process_dependency,
    subtype_relationship
)
from .util import flatten

_logger: Final = logging.getLogger(__name__)

_absent_param: Final = Parameter('', 'Never', is_optional=True, named=False)

REQUIRED_SIGS: Final = {
    '__eq__': Signature(
        (Parameter.as_self(),
         Parameter('other', 'object', named=False)),
        'bool'),
    '__ne__': Signature(
        (Parameter.as_self(),
         Parameter('other', 'object', named=False)),
        'bool'),
    '__setattr__': Signature(
        (Parameter.as_self(),
         Parameter('name', 'str', named=False),
         Parameter('value', 'Any', named=False)),
        'None'),
}

DEFAULT_RETURNS: Final = {
    '__int__': 'int',
    '__str__': 'str',
    '__bytes__': 'bytes',
    'get_data': 'bytes',
    'get_subdata': 'bytes',
}


def merge_parameters(p: Parameter, q: Parameter, /) -> Parameter | None:
    if p.named and q.named and p.name != q.name:
        return None
    if p.is_self != q.is_self:
        return None
    t, u = p.type, q.type
    if (t and not u) or (u and not t):
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


def process_signatures(
        signatures: Sequence[Signature],
        *, infer_opt_params: bool = True,
        ignore_coercion: bool = False) -> list[Signature]:
    """Sort and compress the given sequence of function signatures."""
    depths = get_signature_depths(signatures)
    sorted_signatures: list[Signature] = []
    for i, depth in sorted(enumerate(depths), key=lambda x: x[1]):
        signature = signatures[i]
        if depth == 0 and not ignore_coercion:
            account_for_casts(signature)
        sorted_signatures.append(signature)

    merged_signatures: list[Signature] = []
    for new in sorted(sorted_signatures, key=Signature.get_arity):
        for i, old in enumerate(merged_signatures):
            if not infer_opt_params and len(old.parameters) != len(new.parameters):
                continue
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


def process_function(
        function: Function,
        *, infer_opt_params: bool = True,
        ignore_coercion: bool = False) -> Function:
    name, scoped_name = function.name, function.scoped_name
    param_override_info = special_cases.PARAM_TYPE_OVERRIDES.get(scoped_name)
    if param_override_info is not None:
        i, j, param_override = param_override_info
        param = function.signatures[i].parameters[j]
        if param.type:
            _logger.debug(f"Changed type of parameter '{param}'"
                          f" in {function} to {param_override}")
        param.type = param_override
    if (required_sig := REQUIRED_SIGS.get(name)) is not None:
        new_sigs = [required_sig]
    else:
        new_sigs = process_signatures(
            function.signatures,
            infer_opt_params=infer_opt_params,
            ignore_coercion=ignore_coercion,
        )
    default_return = DEFAULT_RETURNS.get(name)
    return_override = special_cases.RETURN_TYPE_OVERRIDES.get(scoped_name)
    if (default_return or return_override) is not None:
        for sig in new_sigs:
            if return_override is not None:
                return_type = return_override
            elif default_return is not None and not sig.return_type:
                return_type = default_return
            else:
                continue
            if sig.return_type:
                _logger.debug(f"Changed return type of {function} from"
                              f" {sig.return_type} to {return_type}")
            sig.return_type = return_type
    function.signatures = new_sigs
    return function


def process_dependencies(file: File) -> None:
    current_dir = '.'.join(file.this_namespace())
    seen = set[str]()
    for name in file.get_dependencies():
        if name in seen:
            continue
        seen.add(name)

        def if_alias(definition: str) -> None:
            alias = Alias(name, definition, is_type_alias=True)
            file.nested.append(alias)

        def if_import(module: str) -> None:
            if not module.startswith(current_dir):
                if (end := module.find('._')) > 0:
                    module = module[:end]
                file.imports[module].append(name)

        processed = process_dependency(name, if_alias, if_import)
        if not processed:
            _logger.warning(f"Unknown type '{name}' in '{current_dir}'")
