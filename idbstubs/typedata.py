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
from sys import stdlib_module_names
from typing import Final

from . import typecmp as tc
from .idb_interface import IDBType, get_all_types
from .idbutil import type_is_exposed
from .special_cases import EXTRA_COERCION, NO_COERCION, TYPE_NAME_OVERRIDES
from .translation import ATOMIC_TYPES, make_class_name
from .util import unpack_union

_logger: Final = logging.getLogger(__name__)

_modules: dict[str, str] = {}
_param_type_replacements: dict[str, str] = {}
_enum_definitions: dict[str, str] = {}

BUILTIN_NAMES: Final = frozenset(dir(builtins))
KNOWN_IMPORTS: Final = {
    'array': 'array',
    'Callable': 'collections.abc',
    'Coroutine': 'collections.abc',
    'Generator': 'collections.abc',
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
    'Self': 'typing_extensions',  # Introduced in 3.11
    'TypeAlias': 'typing_extensions',  # Introduced in 3.10
    'TypeVar': 'typing',
    'StrOrBytesPath': '_typeshed',
    'core': 'panda3d',
}

# These exist entirely for readability and brevity
TYPE_ALIASES: Final = {
    'Vec2Like': 'LVecBase2f | tuple[float, float]',
    'DoubleVec2Like': 'LVecBase2d | tuple[float, float]',
    'IntVec2Like': 'LVecBase2i | tuple[int, int]',
    'Vec3Like': 'LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow | tuple[float, float, float]',
    'DoubleVec3Like': 'LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow | tuple[float, float, float]',
    'IntVec3Like': 'LVecBase3i | tuple[int, int, int]',
    'Vec4Like': 'LVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | tuple[float, float, float, float] | ConfigVariableColor',
    'DoubleVec4Like': 'LVecBase4d | LMatrix4d.Row | LMatrix4d.CRow | tuple[float, float, float, float]',
    'IntVec4Like': 'LVecBase4i | tuple[int, int, int, int]',
    'Mat4Like': 'LMatrix3f | LMatrix4f | UnalignedLMatrix4f',
    'DoubleMat4Like': 'LMatrix3d | LMatrix4d | UnalignedLMatrix4d',
    'URL': 'URLSpec | str',
    'SearchPathLike': 'ConfigVariableFilename | ConfigVariableSearchPath | DSearchPath | Filename | str',
    'TaskCoroutine': 'Coroutine[Any, None, _T_co] | Generator[Any, None, _T_co]',
    'TaskFunction': 'Callable[..., int | TaskCoroutine[int | None] | None]',
}
for _alias_name in TYPE_ALIASES:
    KNOWN_IMPORTS[_alias_name] = 'panda3d._typing'

TYPE_VARIABLES: Final[dict[str, tuple[tuple[str, ...], str]]] = {
    '_N': (('PandaNode',), 'covariant'),
    '_M': (('PandaNode',), 'invariant'),
    '_T_co': ((), 'covariant'),
}


@cache
def get_type_name(idb_type: IDBType) -> str:
    """Return the Python name for a type. If the type is a non-scoped enum,
    the name returned is an alias name, prefixed by an underscore.
    """
    if idb_type.is_wrapped or (idb_type.is_typedef and not idb_type.is_global):
        # Wrapped types and local typedefs aren't exposed to Python.
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


@cache
def make_type(idb_type: IDBType) -> tc.Type:
    type_name = get_type_name(idb_type)
    if idb_type.is_typedef:
        typ = tc.AliasType(
            type_name, make_type(idb_type.wrapped_type),
        )
    else:
        bases: list[tc.ClassType] = []
        for derivation in idb_type.derivations:
            base = make_type(derivation)
            assert isinstance(base, tc.ClassType)
            bases.append(base)
        typ = tc.ClassType(type_name, bases)
    return typ


def load_data() -> None:
    coercions = defaultdict[str, set[str]](set)
    typecasts = defaultdict[str, set[str]](set)
    for idb_type in get_all_types():
        type_name = get_type_name(idb_type)
        if idb_type.is_wrapped:
            continue
        if idb_type.is_enum and not idb_type.is_scoped_enum:
            if 0 < len(idb_type.enum_values) < 25:
                values = sorted(e.value for e in idb_type.enum_values)
                values_str = ', '.join(str(v) for v in values)
                definition = f'Literal[{values_str}]'
            else:
                definition = 'int'
            _enum_definitions[type_name] = definition
            continue
        if idb_type.is_global and not idb_type.is_nested:
            tc.register(make_type(idb_type))
            mod_name = idb_type.module_name
            lib_name = idb_type.library_name.removeprefix('libp3')
            _modules[type_name] = mod_name + '._' + lib_name
        for cast_to in explicit_cast_to(idb_type):
            typecasts[get_type_name(cast_to)].add(type_name)
        coercions[type_name].update(
            get_type_name(t) for t in implicit_cast_from(idb_type)
        )
    for k, v in TYPE_ALIASES.items():
        alias = tc.AliasType(k, tc.get(v))
        tc.register(alias)
    tc.register(
        tc.ProtocolType(
            'StrOrBytesPath', frozenset((
                tc.get('str'),
                tc.get('Filename'),
                tc.get('ConfigVariableFilename'),
            ))
        )
    )
    union_aliases = [(k, frozenset(unpack_union(v))) for k, v in TYPE_ALIASES.items()]
    for cast_to_name in tuple(coercions.keys() | typecasts.keys()):  # freeze keys
        cast_from_name = combine_types(
            get_all_coercible(
                cast_to_name,
                coercion_map=coercions,
                typecast_map=typecasts,
                union_aliases=union_aliases,
            )
        )
        if cast_from_name and cast_to_name != cast_from_name:
            _param_type_replacements[cast_to_name] = cast_from_name


def recursive_superclasses(idb_type: IDBType) -> frozenset[IDBType]:
    derivations = set[IDBType]()
    for derivation in idb_type.unwrap().derivations:
        derivations.add(derivation)
        derivations |= recursive_superclasses(derivation)
    return frozenset(derivations)


def explicit_cast_to(idb_type: IDBType) -> Iterator[IDBType]:
    for cast in idb_type.casts:
        for wrapper in cast.wrappers:
            cast_to = wrapper.return_type.unwrap()
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
            cast_from = wrapper.parameters[0].type.unwrap()
            if cast_from.name == '_object':
                continue
            if idb_type in recursive_superclasses(cast_from):
                continue
            if type_is_exposed(cast_from):
                yield cast_from


def get_all_coercible(
        cast_to: str,
        *, coercion_map: Mapping[str, Set[str]],
        typecast_map: Mapping[str, Set[str]],
        union_aliases: Iterable[tuple[str, Set[str]]] = ()) -> set[str]:
    """Based on `coercion_map`, return a set of the names of the types
    that can be automatically coerced to the type with the given name.
    """
    cast_from = {cast_to} | coercion_map[cast_to]
    if (remove := NO_COERCION.get(cast_to)) is not None:
        cast_from -= remove
    for name in tuple(cast_from):  # freeze entries
        cast_from |= typecast_map[name]
    if (add := EXTRA_COERCION.get(cast_to)) is not None:
        cast_from |= add
    for alias, alias_of in union_aliases:
        if cast_from >= alias_of:
            cast_from -= alias_of
            cast_from.add(alias)
    return cast_from


def get_param_type_replacement(type_name: str) -> tc.Type:
    """Return a type expressing all types that can be
    automatically coerced to the given type.
    """
    typ = tc.get(type_name)
    while isinstance(typ, tc.AliasType):
        typ = typ.alias_of
    alias_of = str(typ)
    replacement = _param_type_replacements.get(alias_of)
    if replacement is None:
        return tc.get(type_name)
    replacement_types = set(unpack_union(replacement))
    if alias_of not in replacement_types:
        return tc.get(replacement)
    replacement_types.discard(alias_of)
    replacement_types.add(type_name)
    return tc.unify_types(tc.get(t) for t in replacement_types)


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
    typ = tc.get(name)
    if not isinstance(typ, tc.ClassType):
        return [name]
    bases = [typ]
    linear_bases: list[str] = []
    while bases:
        for next_base in bases:
            other_bases = [b for b in bases if b != next_base]
            if any(other_base <= next_base for other_base in other_bases):
                continue
            # This base works as the next one.
            linear_bases.append(str(next_base))
            bases = [*next_base.bases, *other_bases]
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


def combine_types(types: Iterable[str]) -> str:
    """Return a string representing a type equivalent to the union
    of the types represented by the given strings.
    """
    return str(tc.unify_types(tc.get(t) for t in types))
