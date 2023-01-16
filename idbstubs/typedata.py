import builtins
import itertools
import logging
from collections import defaultdict
from collections.abc import (
    Callable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
    Set,
)
from functools import cache
from itertools import combinations, product
from sys import stdlib_module_names
from typing import Final

from .idb_interface import IDBType, get_all_types
from .idbutil import (
    type_is_exposed,
    type_is_unexposed_wrapper,
    type_is_unscoped_enum,
    unwrap_type,
)
from .special_cases import EXTRA_COERCION, NO_COERCION, TYPE_NAME_OVERRIDES
from .translation import ATOMIC_TYPES, make_class_name
from .util import unpack_union

_logger: Final = logging.getLogger(__name__)

_modules: dict[str, str] = {}
_inheritance: dict[str, set[str]] = {}
_direct_inheritance: dict[str, tuple[str, ...]] = {}
_aliases: dict[str, str] = {}
_param_type_replacements: dict[str, str] = {}
_enum_definitions: dict[str, str] = {}

BUILTIN_NAMES: Final = frozenset(dir(builtins))
KNOWN_IMPORTS: Final = {
    'array': 'array',
    'Callable': 'collections.abc',
    'Iterable': 'collections.abc',
    'Iterator': 'collections.abc',
    'Mapping': 'collections.abc',
    'MutableMapping': 'collections.abc',
    'MutableSequence': 'collections.abc',
    'Sequence': 'collections.abc',
    'Enum': 'enum',
    'Any': 'typing',
    'ClassVar': 'typing',
    'Final': 'typing_extensions',  # Introduced in 3.8
    'final': 'typing_extensions',  # Introduced in 3.8
    'Generic': 'typing',
    'Literal': 'typing_extensions',  # Introduced in 3.8
    'Never': 'typing_extensions',  # Introduced in 3.11
    'NoReturn': 'typing',
    'overload': 'typing',
    'TypeAlias': 'typing_extensions',  # Introduced in 3.10
    'TypeVar': 'typing',
    'Self': '_typeshed',
    'StrOrBytesPath': '_typeshed',
    'core': 'panda3d',
}

# These exist entirely for readability and brevity
TYPE_ALIASES: Final = {
    'Vec3Like': 'LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow',
    'DoubleVec3Like': 'LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow',
    'Vec4Like': 'LVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor',
    'DoubleVec4Like': 'LVecBase4d | LMatrix4d.Row | LMatrix4d.CRow',
    'Mat4Like': 'LMatrix4f | UnalignedLMatrix4f',
    'DoubleMat4Like': 'LMatrix4d | UnalignedLMatrix4d',
    'URL': 'URLSpec | str',
    'SearchPathLike': 'ConfigVariableFilename | ConfigVariableSearchPath | DSearchPath | Filename | str'
}
_type_alias_data = [
    (k, frozenset(v.split(' | ')))
    for k, v in TYPE_ALIASES.items()
]
for _alias_name in TYPE_ALIASES:
    KNOWN_IMPORTS[_alias_name] = 'panda3d._typing'

TYPE_VARIABLES: Final[dict[str, tuple[tuple[str, ...], str]]] = {
    '_N': (('PandaNode',), 'covariant'),
    '_M': (('PandaNode',), 'invariant'),
}


@cache
def get_type_name(idb_type: IDBType) -> str:
    """Return the Python name for a type. If the type is a non-scoped enum,
    the name returned is an alias name, prefixed by an underscore.
    """
    if type_is_unexposed_wrapper(idb_type):
        return get_type_name(idb_type.wrapped_type)
    if idb_type.is_atomic:
        return ATOMIC_TYPES[idb_type.atomic_token]
    # We can't use `str.removeprefix` because of `ParamValue< std::string >`
    name = idb_type.scoped_name.replace('std::', '')
    if (override := TYPE_NAME_OVERRIDES.get(name)) is not None:
        return override
    if not idb_type.is_fully_defined:
        if name.startswith('PointerTo< '):
            name = name[11:-2]
        elif name.startswith('ConstPointerTo< '):
            name = name[16:-2]
    name_iter = (make_class_name(s) for s in name.split('::'))
    if idb_type.is_enum and not idb_type.is_scoped_enum:
        return '_' + '_'.join(name_iter)
    return '.'.join(name_iter)


def load_data() -> None:
    coercions = defaultdict[str, set[str]](set)
    typecasts = defaultdict[str, set[str]](set)
    for idb_type in get_all_types():
        type_name = get_type_name(idb_type)
        if idb_type.is_wrapped:
            continue
        if type_is_unscoped_enum(idb_type):
            values = sorted(e.value for e in idb_type.enum_values)
            values_str = ', '.join(str(v) for v in values)
            _enum_definitions[type_name] = f'Literal[{values_str}]' if values else 'int'
            continue
        if idb_type.is_global and not idb_type.is_nested:
            mod_name = idb_type.module_name
            lib_name = idb_type.library_name.removeprefix('libp3')
            _modules[type_name] = mod_name + '._' + lib_name
        if idb_type.is_typedef:
            if idb_type.is_global:
                _aliases[type_name] = get_type_name(unwrap_type(idb_type))
            # Don't record coercion or inheritance information for typedefs
            continue
        for cast_to in explicit_cast_to(idb_type):
            typecasts[get_type_name(cast_to)].add(type_name)
        coercions[type_name].update(
            get_type_name(t) for t in implicit_cast_from(idb_type)
        )
        if base_classes := recursive_superclasses(idb_type):
            _inheritance[type_name] = {
                get_type_name(s) for s in base_classes
            }
            _direct_inheritance[type_name] = tuple(
                get_type_name(s) for s in idb_type.derivations
            )
    for cast_to_name in tuple(coercions.keys() | typecasts.keys()):  # freeze keys
        cast_from_name = combine_types(
            get_all_coercible(
                cast_to_name,
                coercion_map=coercions,
                typecast_map=typecasts,
            )
        )
        if cast_from_name and cast_to_name != cast_from_name:
            _param_type_replacements[cast_to_name] = cast_from_name


def recursive_superclasses(idb_type: IDBType) -> frozenset[IDBType]:
    derivations = set[IDBType]()
    for derivation in unwrap_type(idb_type).derivations:
        derivations.add(derivation)
        derivations |= recursive_superclasses(derivation)
    return frozenset(derivations)


def explicit_cast_to(idb_type: IDBType) -> Iterator[IDBType]:
    for cast in idb_type.casts:
        for wrapper in cast.wrappers:
            cast_to = unwrap_type(wrapper.return_type)
            if type_is_exposed(cast_to) and not cast_to.is_atomic:
                yield cast_to


def implicit_cast_from(idb_type: IDBType) -> Iterator[IDBType]:
    """Yield the types that can be implicitly cast
    to the type with the given index.
    """
    for function in itertools.chain(idb_type.constructors, idb_type.methods):
        for wrapper in function.wrappers:
            if not wrapper.is_coerce_constructor:
                continue
            max_arity = len(wrapper.parameters)
            min_arity = sum(not p.is_optional for p in wrapper.parameters)
            if min_arity > 1 or max_arity < 1:
                continue
            if wrapper.parameters[0].name in ('fill_value', 'type_handle'):
                continue
            cast_from = unwrap_type(wrapper.parameters[0].type)
            if cast_from.name == '_object':
                continue
            if idb_type in recursive_superclasses(cast_from):
                continue
            if type_is_exposed(cast_from):
                yield cast_from


def get_all_coercible(
        cast_to: str,
        *, coercion_map: Mapping[str, Set[str]],
        typecast_map: Mapping[str, Set[str]]) -> set[str]:
    """Based on `coercion_map`, return a set of the names of the types
    that can be automatically coerced to the type with the given name.
    """
    cast_from = {cast_to} | coercion_map[cast_to]
    for name in tuple(cast_from):  # freeze entries
        cast_from |= typecast_map[name]
    if (remove := NO_COERCION.get(cast_to)) is not None:
        cast_from -= remove
    if (add := EXTRA_COERCION.get(cast_to)) is not None:
        cast_from |= add
    return cast_from


def get_param_type_replacement(type_name: str) -> str:
    """Return a type expressing all types that can be
    automatically coerced to the given type.
    """
    alias_of = _aliases.get(type_name)
    if alias_of is None:
        replacement = _param_type_replacements.get(type_name)
    else:
        replacement = _param_type_replacements.get(alias_of)
        if replacement is not None:
            replacement_types = set(unpack_union(replacement))
            if alias_of in replacement_types:
                replacement_types.discard(alias_of)
                replacement_types.add(type_name)
                replacement = combine_types(replacement_types)
    return type_name if replacement is None else replacement


def get_module(name: str) -> str | None:
    if (module := KNOWN_IMPORTS.get(name)) is not None:
        return module
    elif (module := _modules.get(name)) is not None:
        return module
    elif name in stdlib_module_names:
        return ''
    else:
        return None


def get_mro(name: str, /) -> list[str]:
    """Return a list of the names of the classes in the MRO of a class."""
    name = _aliases.get(name, name)
    bases = [name]
    linear_bases: list[str] = []
    while bases:
        for next_base in bases:
            other_bases = [b for b in bases if b != next_base]
            if any(inherits_from(other_base, next_base) for other_base in other_bases):
                continue
            # This base works as the next one.
            linear_bases.append(next_base)
            bases = list(_direct_inheritance.get(next_base, ())) + other_bases
            break
        else:
            # Each base inherits from one of the others.
            _logger.error(f'Could not construct MRO for {name}')
            return []
    return linear_bases


def process_dependency(
        name: str,
        *, if_alias: Callable[[str], object],
        if_import: Callable[[str], object],
        if_type_var: Callable[[Sequence[str], str], object]) -> bool:
    if name in BUILTIN_NAMES:
        pass
    elif (alias_def := _enum_definitions.get(name)) is not None:
        if_alias(alias_def)
    elif (type_var_params := TYPE_VARIABLES.get(name)) is not None:
        if_type_var(*type_var_params)
    elif (module := get_module(name)) is not None:
        if_import(module)
    else:
        return False
    return True


def inherits_from(a: str, b: str, /) -> bool:
    """Return whether `a` is narrower than `b`.
    Does not work with union types; use `subtype_relationship` instead.
    """
    a, b = _aliases.get(a, a), _aliases.get(b, b)
    if 'Any' in (a, b):
        return False
    if a == b:
        return True
    if b == 'object' or a in ('Never', 'NoReturn'):
        return True
    if (a, b) in (('bool', 'int'), ('int', 'float')):
        return True
    if a in ('Filename', 'ConfigVariableFilename', 'str') and b == 'StrOrBytesPath':
        return True
    return b in _inheritance.get(a, set())


def expand_type(s: str, /) -> set[str]:
    """Return a set of type names whose union is equivalent
    to the type represented by the given string.
    """
    if not s:
        return set()
    parts, new_parts = set[str](), {s}
    while parts != new_parts:
        parts, new_parts = new_parts, set[str]()
        for part in parts:
            part = TYPE_ALIASES.get(part, part)
            new_parts.update(unpack_union(part))
    return parts


def subtype_relationship(a: str, b: str, /) -> tuple[bool, bool]:
    """Return a tuple of two Boolean values, representing whether
    `a` is a subtype of `b` and vice versa, respectively.
    """
    expanded_a = expand_type(a)
    expanded_b = expand_type(b)
    found_broader_in_b = dict.fromkeys(expanded_a, False)
    found_broader_in_a = dict.fromkeys(expanded_b, False)
    for i, j in product(expanded_a, expanded_b):
        if not found_broader_in_b[i] and inherits_from(i, j):
            found_broader_in_b[i] = True
        if not found_broader_in_a[j] and inherits_from(j, i):
            found_broader_in_a[j] = True
    return (all(found_broader_in_b.values()),
            all(found_broader_in_a.values()))


def type_difference(a: str, b: str, /) -> str:
    """Return a string representing the difference between
    the types represented by the given strings.
    """
    expanded_a = expand_type(a)
    expanded_b = expand_type(b)
    result = set(expanded_a)
    for t in expanded_a:
        for u in expanded_b:
            if inherits_from(t, u):
                result.remove(t)
                break
    if not result:
        result.add('Never')
    return combine_types(result)


def types_intersect(a: str, b: str, /) -> bool:
    """Return whether the types represented by
    the given strings have an intersection.
    """
    if not a or not b:
        return True
    return any(
        inherits_from(t, u) or inherits_from(u, t)
        for t, u in product(expand_type(a), expand_type(b))
    )


def combine_types(types: Iterable[str]) -> str:
    """Return a string representing a type equivalent to the union
    of the types represented by the given strings.
    """
    combined = set[str]()
    for t in types:
        combined |= expand_type(t)
    for a, b in combinations(combined, 2):
        a_subtypes_b, b_subtypes_a = subtype_relationship(a, b)
        if a_subtypes_b:
            combined.discard(a)
        elif b_subtypes_a:
            combined.discard(b)
    for alias, alias_of in _type_alias_data:
        if combined >= alias_of:
            combined -= alias_of
            combined.add(alias)
    return ' | '.join(sorted(combined, key=lambda s: (s == 'None', s)))
