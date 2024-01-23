import logging
import re
from collections import Counter
from collections.abc import Iterable, Mapping, Sequence
from itertools import combinations, zip_longest
from typing import Final

import attrs

from . import typecmp as tc
from .reps import (
    Alias,
    Attribute,
    Class,
    File,
    Function,
    Parameter,
    Signature,
    StubRep,
    TypeAlias,
    TypeVariable,
)
from .typedata import get_mro, get_param_type_replacement, process_dependency

_logger: Final = logging.getLogger(__name__)
_absent_param: Final = Parameter('_', tc.BottomType(), is_optional=True, named=False)

PTA_NAME_REGEX: Final = re.compile(r'(?:Const)?PointerToArray_(\w+)')
VECTOR_NAME_REGEX: Final = re.compile(
    r'((?:Unaligned)?L(?:VecBase|Vector|Point))([2-4])([dfi])'
)
RETURN_SELF_IN_VECTORS: Final = frozenset({
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


def merge_parameters(p: Parameter, q: Parameter, /) -> Parameter | None:
    if p.named and q.named and p.name != q.name:
        return None
    if (p.type and not q.type) or (q.type and not p.type):
        return None

    # Make sure assigning an argument by name will still work
    if p.named and not q.named and not q.type <= p.type:
        return None
    if q.named and not p.named and not p.type <= q.type:
        return None

    return Parameter(
        p.name if p.named else q.name,
        p.type | q.type,
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
    if a.doc and b.doc and a.doc != b.doc:
        docstring = a.doc + '\n\nor:\n' + b.doc
    else:
        docstring = a.doc or b.doc
    return Signature(merged_params, a.return_type | b.return_type, doc=docstring)


def sort_signatures(signatures: Sequence[Signature]) -> list[Signature]:
    """Return the signatures from the given sequence sorted so that
    a type-checker may choose the first matching one.
    """
    # `define_after` maps a signature index to a set of the indices
    #  of all signatures that should be defined after it.
    define_after: dict[int, set[int]] = {n: set() for n in range(len(signatures))}
    for (i, sig_1), (j, sig_2) in combinations(enumerate(signatures), 2):
        if not sig_1.has_arity_overlap(sig_2):
            continue
        if sig_1.return_type == sig_2.return_type:
            # Ambiguity doesn't matter if they return the same type.
            continue
        sig_1_first = sig_2_first = True
        for p, q in zip_longest(
            sig_1.parameters,
            sig_2.parameters,
            fillvalue=_absent_param,
        ):
            if not (sig_1_first or sig_2_first):
                # These signatures don't overlap.
                break
            sig_1_first &= p.type <= q.type
            sig_2_first &= q.type <= p.type
        if sig_1_first:
            define_after[i].add(j)
        elif sig_2_first:
            define_after[j].add(i)
    # Count how many "layers" of signatures each one needs to appear before.
    sig_depths = Counter[int](range(len(signatures)))
    for i, others in define_after.items():
        seen = {i} | others
        while others:
            sig_depths[i] += 1
            next_others = set[int]()
            for j in others:
                if j in seen:
                    continue
                batch = define_after[j] - seen
                seen |= batch
                next_others |= batch
            others = next_others
    return [signatures[i] for i, n in sig_depths.most_common()]


def expand_input(signatures: Sequence[Signature]) -> list[Signature]:
    """Expand the parameter types of a sequence of signatures
    without introducing ambiguity or redundancy.
    """
    # Store all possible parameter type expansions in a two-layer mapping.
    expanded_types: dict[int, dict[str, tc.Type]] = {
        i: {
            param.name: get_param_type_replacement(param.type)
            for param in signature.parameters
        }
        for i, signature in enumerate(signatures)
    }
    for (i, sig_1), (j, sig_2) in combinations(enumerate(signatures), 2):
        if not sig_1.has_arity_overlap(sig_2):
            continue
        r1, r2 = sig_1.return_type, sig_2.return_type
        new_types_1: dict[str, tc.Type] = {}
        new_types_2: dict[str, tc.Type] = {}
        for param_1, param_2 in zip(sig_1.parameters, sig_2.parameters):
            type_1 = expanded_types[i][param_1.name]
            type_2 = expanded_types[j][param_2.name]
            if not tc.types_intersect(type_1, type_2):
                break
            core_type_1 = param_1.type
            core_type_2 = param_2.type
            if not r1 >= r2 or type_1 < type_2 or core_type_1 < core_type_2:
                # If the return type is narrower or incompatible, or if
                # the parameter type is narrower, avoid any overlap in
                # the expanded parameter type.
                new_types_1[param_1.name] = core_type_1 | (type_1 - type_2)
            elif param_2.named:
                # Otherwise, just avoid some overlap between the parameter types.
                # Skip this if the other parameter isn't named, though,
                # as in practice it can usually be merged later on.
                new_types_1[param_1.name] = (
                    core_type_1 | tc.soft_difference(type_1, core_type_2)
                )
            if not r2 >= r1 or type_2 < type_1 or core_type_2 < core_type_1:
                new_types_2[param_2.name] = core_type_2 | (type_2 - type_1)
            elif param_1.named:
                new_types_2[param_2.name] = (
                    core_type_2 | tc.soft_difference(type_2, core_type_1)
                )
        # If the signatures intersect, apply the changes to their types.
        else:
            expanded_types[i] |= new_types_1
            expanded_types[j] |= new_types_2
    new_signatures: list[Signature] = []
    for i, signature in enumerate(signatures):
        new_parameters = [
            attrs.evolve(param, type=expanded_types[i][param.name])
            for param in signature.parameters
        ]
        new_signatures.append(attrs.evolve(signature, parameters=new_parameters))
    return new_signatures


def process_signatures(signatures: Sequence[Signature]) -> list[Signature]:
    """Sort and compress the given sequence of function signatures."""
    with_casts = expand_input(signatures)
    sorted_signatures = sort_signatures(with_casts)
    merged_signatures: list[Signature] = []
    for new in sorted_signatures:
        for i, old in enumerate(merged_signatures):
            if (merge_result := merge_signatures(old, new)) is not None:
                # The signatures were successfully merged
                merged_signatures[i] = merge_result
                break
        else:
            # The signature couldn't be merged with any already in merged_signatures
            merged_signatures.append(new.copy())
    return merged_signatures


def process_function(function: Function, *, class_name: str | None = None) -> None:
    function.signatures = process_signatures(function.signatures)
    match function:
        case Function('__eq__' | '__ne__', [Signature([_, other_param])]):
            other_param.type = 'object'
            other_param.named = False
        case Function(
            'assign', [Signature([_, copy_param])]
        ) if str(copy_param.type) == class_name:
            copy_param.type = 'Self'
        case Function('__deepcopy__', [Signature([_, Parameter(named=True) as memo])]):
            memo.named = False


def process_class(class_: Class) -> None:
    for item in class_.body.values():
        match item:
            case Class():
                process_class(item)
            case Function():
                process_function(item, class_name=class_.name)
    class_body = dict(class_.body)
    match class_body:
        case {
            '__len__': _,
            '__getitem__': Function(
                signatures=[Signature([_, Parameter(type=index_type)], item_type)]
            )
        } if str(index_type) == 'int':
            iter_return_type = f'Iterator[{item_type}]' if item_type else 'Iterator'
            class_body['__iter__'] = Function(
                '__iter__',
                [Signature([Parameter('self')], iter_return_type)],
                type_check_only=True,
            )
    class_.body = class_body
    if PTA_NAME_REGEX.match(class_.name):
        process_pointer_to_array_class(class_)
    elif VECTOR_NAME_REGEX.match(class_.name):
        process_vector_class(class_)
    elif 'RenderAttrib' in class_.bases:
        process_render_attrib_class(class_)


def process_files(files: Iterable[File]) -> None:
    classes: dict[str, Class] = {}
    for file in files:
        for item in file.nested:
            if isinstance(item, Class):
                process_class(item)
                classes[item.name] = item
            elif isinstance(item, Function):
                process_function(item)
    for cls in classes.values():
        remove_redefinitions(cls, classes)


def process_dependencies(file: File) -> None:
    current_dir = '.'.join(file.path.parts)
    seen = set[str]()
    for name in file.get_dependencies():
        if name in seen:
            continue
        seen.add(name)

        def alias_of(definition: str) -> None:
            alias = TypeAlias(name, definition)
            file.nested.append(alias)

        def as_type_var(parameters: Iterable[str]) -> None:
            type_var = TypeVariable(name, parameters)
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
            signatures=[Signature([_, Parameter('data', tc.MissingType()) as param])]
        ):
            param.type = 'bytes'
    match pta.body.get('get_data'):
        case Function(signatures=[Signature(return_type=tc.MissingType()) as sig]):
            sig.return_type = 'bytes'
    match pta.body.get('get_subdata'):
        case Function(signatures=[Signature(return_type=tc.MissingType()) as sig]):
            sig.return_type = 'bytes'
    match pta.body:
        case {
            '__getitem__': Function(signatures=[Signature(return_type=array_of)]),
            '__init__': Function(signatures=signatures),
        } if array_of:
            for sig in signatures:
                match sig:
                    case Signature([_, Parameter('source') as param]):
                        param.type = f'Sequence[{array_of}]'


def process_vector_class(vector: Class) -> None:
    """Process a representation of a Panda3D vector class whose name
    matches `VECTOR_NAME_REGEX`, applying various special cases.
    """
    name_match = VECTOR_NAME_REGEX.match(vector.name)
    assert name_match is not None
    kind, _, suffix = name_match[1], name_match[2], name_match[3]
    class_body = dict(vector.body)
    if kind.endswith('VecBase'):
        class_body.pop('get_data', None)
        class_body.pop('getData', None)
    if suffix == 'i' and not kind.startswith('Unaligned'):
        class_body.pop('__truediv__', None)
        class_body.pop('__itruediv__', None)
    for name in RETURN_SELF_IN_VECTORS & class_body.keys():
        match class_body[name]:
            case Function(signatures=[
                Signature(return_type=return_type) as sig
            ]) if not return_type or str(return_type) == vector.name:
                sig.return_type = 'Self'
    vector.body = class_body


def process_render_attrib_class(render_attrib: Class) -> None:
    """Process a subclass of `RenderAttrib`."""
    for name, function in render_attrib.body.items():
        if not isinstance(function, Function):
            continue
        if function.is_static_method:
            self_type = render_attrib.name
        else:
            self_type = 'Self'
        for signature in function.signatures:
            if str(signature.return_type) == 'RenderAttrib':
                signature.return_type = self_type


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
                    Function(signatures=sigs_1),
                    Function(signatures=sigs_2)
                ) if any(s1.doc and s1.doc != s2.doc for s1, s2 in zip(sigs_1, sigs_2)):
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
