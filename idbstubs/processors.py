import logging
import re
from collections.abc import Mapping, Sequence
from itertools import combinations, zip_longest
from typing import Final

from .reps import (
    Alias,
    Attribute,
    Class,
    File,
    Function,
    Package,
    Parameter,
    Signature,
    StubRep,
    TypeVariable,
)
from .special_cases import (
    ATTR_TYPE_OVERRIDES,
    ATTRIBUTE_NAME_SHADOWS,
    DEFAULT_RETURNS,
    INPLACE_DUNDERS,
    PARAM_TYPE_OVERRIDES,
    RETURN_TYPE_OVERRIDES,
)
from .typedata import (
    combine_types,
    get_mro,
    get_param_type_replacement,
    process_dependency,
    subtype_relationship,
)
from .util import flatten

_logger: Final = logging.getLogger(__name__)
_absent_param: Final = Parameter('', 'Never', is_optional=True, named=False)

PTA_NAME_REGEX: Final = re.compile(r'(?:Const)?PointerToArray_(\w+)')
VECTOR_NAME_REGEX: Final = re.compile(
    r'((?:Unaligned)?L(?:VecBase|Vector|Point))([2-4])([dfi])'
)
RETURN_SELF: Final = frozenset({
    '__neg__',
    '__mul__',
    '__truediv__',
    '__floordiv__',
    '__pow__',
    '__round__',
    '__floor__',
    '__ceil__',
    'normalized',
    'project',
})
OBJECT: Final = Class(
    'object',
    body={
        # TODO: would this cause issues?
        # '__init__': Function(
        #     '__init__',
        #     [Signature([Parameter('self')], 'None')],
        #     is_method=True,
        # ),
        '__repr__': Function(
            '__repr__',
            [Signature([Parameter('self')], 'str')],
            is_method=True,
        ),
        '__str__': Function(
            '__str__',
            [Signature([Parameter('self')], 'str')],
            is_method=True,
        ),
    }
)


def merge_parameters(p: Parameter, q: Parameter, /) -> Parameter | None:
    if p.named and q.named and p.name != q.name:
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
        w1_params = (p for p in w1.parameters if not p.is_optional)
        w2_params = (p for p in w2.parameters if not p.is_optional)
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
        seen = {i, *others}
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


def process_function(function: Function) -> None:
    return_overrides = RETURN_TYPE_OVERRIDES.get(function.scoped_name, {})
    param_overrides = PARAM_TYPE_OVERRIDES.get(function.scoped_name, {})
    if isinstance(return_overrides, str):
        return_overrides = {
            i: return_overrides
            for i in range(len(function.signatures))
        }
    for i, sig in enumerate(function.signatures):
        return_override = return_overrides.get(i)
        if return_override is None and not sig.return_type:
            return_override = DEFAULT_RETURNS.get(function.name)
        if return_override is not None:
            sig.return_type = return_override
        for j, param in enumerate(sig.parameters):
            param_override = param_overrides.get((i, j))
            if param_override is not None:
                param.type = param_override
    new_sigs = process_signatures(function.signatures)
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
                        Parameter(),
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
                        Parameter(),
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
                        Parameter() as self_param,
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


def process_class(class_: Class) -> None:
    for item in class_.body.values():
        match item:
            case Class():
                process_class(item)
            case Function():
                process_function(item)
            case Attribute():
                type_override = ATTR_TYPE_OVERRIDES.get(item.scoped_name)
                if type_override is not None:
                    item.type = type_override
    class_body = dict(class_.body)
    match class_body:
        case {
            '__len__': _,
            '__getitem__': Function(
                signatures=[
                    Signature(
                        parameters=[
                            Parameter(),
                            Parameter(type='int'),
                        ],
                        return_type=item_type,
                    )
                ]
            )
        }:
            iter_return_type = f'Iterator[{item_type}]' if item_type else 'Iterator'
            class_body['__iter__'] = Function(
                '__iter__',
                [Signature([Parameter('self')], iter_return_type)],
                is_method=True,
                namespace=(*class_.namespace, class_.name),
                comment="Doesn't actually exist",
            )
    class_.body = class_body
    if PTA_NAME_REGEX.match(class_.name):
        process_pointer_to_array_class(class_)
    elif VECTOR_NAME_REGEX.match(class_.name):
        process_vector_class(class_)


def process_package(package: Package) -> None:
    classes: dict[str, Class] = {'object': OBJECT}
    for module in package:
        for file in module:
            for item in file.nested:
                match item:
                    case Class():
                        process_class(item)
                        classes[item.name] = item
                    case Function():
                        process_function(item)
    for cls in classes.values():
        remove_redefinitions(cls, classes)


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


def process_pointer_to_array_class(pta: Class) -> None:
    """Process a representation of a Panda3D vector class whose name
    matches `PTA_NAME_REGEX`, applying various special cases.
    """
    match pta.body.get('set_data'):
        case Function(
            signatures=[
                Signature(
                    parameters=[
                        Parameter(),
                        Parameter(name='data', type='') as param,
                    ]
                )
            ]
        ):
            param.type = 'bytes'
    match pta.body.get('get_data'):
        case Function(signatures=[Signature(return_type='') as sig]):
            sig.return_type = 'bytes'
    match pta.body.get('get_subdata'):
        case Function(signatures=[Signature(return_type='') as sig]):
            sig.return_type = 'bytes'
    match pta.body:
        case {
            '__getitem__': Function(
                signatures=[Signature(return_type=array_of)]
            ),
            '__init__': Function(signatures=signatures),
        } if array_of:
            for sig in signatures:
                match sig:
                    case Signature(
                        parameters=[
                            Parameter(),
                            Parameter(name='source') as param,
                        ]
                    ):
                        param.type = f'Sequence[{array_of}]'


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
    replaceable_names = {vector.name, ''}
    for name in RETURN_SELF & class_body.keys():
        match class_body[name]:
            case Function(signatures=[
                Signature(
                    parameters=[
                        Parameter() as self_param, *_
                    ],
                    return_type=return_type,
                ) as sig
            ]) if return_type in replaceable_names:
                self_param.type = 'Self'
                sig.return_type = 'Self'
    match class_body.get('__len__'):
        case Function(signatures=[Signature() as sig]):
            sig.return_type = f'Literal[{dimension}]'
    match class_body.get('get_num_components'):
        case Function(signatures=[Signature() as sig]):
            sig.return_type = f'Literal[{dimension}]'
    vector.body = class_body


def remove_redefinitions(class_: Class, classes: Mapping[str, Class]) -> None:
    """Remove items in a class body that are implied by inheritance."""
    class_body = class_.body
    if not class_body:
        return
    nested_names = frozenset(class_body.keys())
    inherited = set[str]()
    seen = set[str]()
    for base_class_name in get_mro(class_.name)[1:]:
        base_class = classes.get(base_class_name)
        if base_class is None:
            continue
        base_class_body = base_class.body
        intersection = nested_names & base_class_body.keys() - seen
        seen |= intersection
        for name in intersection:
            match class_body[name], base_class_body[name]:
                case Class() | Alias(of_local=True), _:
                    continue
                case (
                    Function(doc=doc_1),
                    Function(doc=doc_2)
                ) if doc_1 and doc_1 != doc_2:
                    continue
                case (
                    Attribute(doc=doc_1),
                    Attribute(doc=doc_2)
                ) if doc_1 and doc_1 != doc_2:
                    continue
                case a, b if a == b:
                    inherited.add(name)
    new_nested_names = nested_names - inherited
    new_nested: dict[str, StubRep] = {}
    for rep in class_body.values():
        if isinstance(rep, Alias) and rep.of_local:
            name_to_check = rep.alias_of
        else:
            name_to_check = rep.name
        if name_to_check in new_nested_names:
            new_nested[rep.name] = rep
    class_.body = new_nested
