import builtins
import logging
from collections import defaultdict
from collections.abc import Callable, Iterator, Sequence
from functools import cache
from itertools import combinations, product
from typing import Final

import panda3d.interrogatedb as idb

from .idbutil import (
    TYPE_NAME_OVERRIDES, TypeIndex, get_constructors, get_derivations,
    get_python_wrappers, type_is_exposed, type_is_unscoped_enum,
    type_is_wrapped_or_typedef, unwrap_type
)
from .translation import ATOMIC_TYPES, class_name_from_cpp_name
from .util import flatten, unpack_union

_logger: Final = logging.getLogger(__name__)

_modules: dict[str, str] = {}
_inheritance: dict[str, set[str]] = {}
_linear_inheritance: dict[str, tuple[str, ...]] = {}
_coercions = defaultdict[TypeIndex, set[TypeIndex]](set)
_param_type_replacements: dict[str, str] = {}
_enum_definitions: dict[str, str] = {}
_implicit_cast_param_names = frozenset(
    ('param0', 'copy', 'other', 'value', 'from')
)

BUILTIN_NAMES: Final = frozenset(dir(builtins))
STDLIB_IMPORTS: Final = {
    'array': 'array',
    'Awaitable': 'collections.abc',
    'Callable': 'collections.abc',
    'Generator': 'collections.abc',
    'Iterable': 'collections.abc',
    'Iterator': 'collections.abc',
    'Mapping': 'collections.abc',
    'Sequence': 'collections.abc',
    'Enum': 'enum',
    'Any': 'typing',
    'ClassVar': 'typing',
    'Final': 'typing_extensions',  # Introduced in 3.8
    'final': 'typing_extensions',  # Introduced in 3.8
    'Generic': 'typing',
    'Literal': 'typing_extensions',  # Introduced in 3.8
    'NoReturn': 'typing',
    'overload': 'typing',
    'TypeAlias': 'typing_extensions',  # Introduced in 3.10
    'TypeVar': 'typing',
    'StrOrBytesPath': '_typeshed',
    'core': 'panda3d',
}

# These exist entirely for readability and brevity
TYPE_ALIASES: Final = {
    '_Vec3d': 'LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow',
    '_Vec3f': 'LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow',
    '_Vec4d': 'LVecBase4d | UnalignedLVecBase4d | LMatrix4d.Row | LMatrix4d.CRow',
    '_Vec4f': 'LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor',
    '_Vec4i': 'LVecBase4i | UnalignedLVecBase4i',
    '_Mat4d': 'LMatrix4d | UnalignedLMatrix4d',
    '_Mat4f': 'LMatrix4f | UnalignedLMatrix4f',
    '_Filename': 'Filename | ConfigVariableFilename | StrOrBytesPath',
}
_type_alias_data = [
    (k, frozenset(v.split(' | ')))
    for k, v in TYPE_ALIASES.items()
]

TYPE_VARIABLES: Final = {
    '_N': ('PandaNode',),
    '_M': ('PandaNode',),
    '_Self': (),
}


@cache
def get_direct_type_name(t: TypeIndex, /) -> str:
    name = idb.interrogate_type_name(t)
    return class_name_from_cpp_name(name)


@cache
def get_type_name(t: TypeIndex, /) -> str:
    """Return the Python name for a type. If the type is a non-scoped enum,
    the name returned is an alias name, prefixed by an underscore.
    """
    if type_is_wrapped_or_typedef(t):
        return get_type_name(idb.interrogate_type_wrapped_type(t))
    if idb.interrogate_type_is_atomic(t):
        atomic_token = idb.interrogate_type_atomic_token(t)
        return ATOMIC_TYPES[atomic_token]
    # We can't use `str.removeprefix` because of `ParamValue< std::string >`
    name = idb.interrogate_type_scoped_name(t).replace('std::', '')
    if (override := TYPE_NAME_OVERRIDES.get(name)) is not None:
        return override
    if not idb.interrogate_type_is_fully_defined(t):
        if name.startswith('PointerTo< '):
            name = name[11:-2]
        elif name.startswith('ConstPointerTo< '):
            name = name[16:-2]
    name_iter = (class_name_from_cpp_name(s) for s in name.split('::'))
    if idb.interrogate_type_is_enum(t):
        if not idb.interrogate_type_is_scoped_enum(t):
            return '_' + '_'.join(name_iter)
    return '.'.join(name_iter)


def load_data() -> None:
    for n in range(idb.interrogate_number_of_types()):
        t = idb.interrogate_get_type(n)
        if type_is_wrapped_or_typedef(t):
            continue
        if type_is_unscoped_enum(t):
            value_count = idb.interrogate_type_number_of_enum_values(t)
            values = sorted(idb.interrogate_type_enum_value(t, n) for n in range(value_count))
            values_str = ', '.join(str(v) for v in values)
            _enum_definitions[get_type_name(t)] = f'Literal[{values_str}]' if values else 'int'
            continue
        if idb.interrogate_type_is_global(t) and not idb.interrogate_type_is_nested(t):
            mod_name = idb.interrogate_type_module_name(t)
            lib_name = idb.interrogate_type_library_name(t).removeprefix('libp3')
            _modules[get_type_name(t)] = mod_name + '._' + lib_name
        for cast_to in explicit_cast_to(t):
            _coercions[cast_to].add(t)
        if cast_from := set(implicit_cast_from(t)):
            _coercions[t].update(cast_from)
        if base_classes := recursive_superclasses(t):
            _inheritance[get_type_name(t)] = {
                get_type_name(s) for s in base_classes
            }
            _linear_inheritance[get_type_name(t)] = tuple(
                get_type_name(s) for s in linear_superclasses(t)
            )
    for cast_to in tuple(_coercions):  # freeze keys
        cast_to_name = get_type_name(cast_to)
        cast_from_name = make_param_type_replacement(cast_to)
        if cast_to_name != cast_from_name:
            _param_type_replacements[cast_to_name] = cast_from_name


@cache
def recursive_superclasses(t: TypeIndex, /) -> frozenset[TypeIndex]:
    t = unwrap_type(t)
    derivations = set[TypeIndex]()
    for d in get_derivations(t):
        derivations.add(d)
        derivations |= recursive_superclasses(d)
    return frozenset(derivations)


@cache
def linear_superclasses(t: TypeIndex, /) -> tuple[TypeIndex, ...]:
    """Return a tuple of the indices of the (recursive) superclasses for a
    type, stopping either at the top of the hierarchy or at the first class
    that inherits directly from multiple classes, whichever comes first.
    """
    bases = tuple(get_derivations(t))
    if len(bases) != 1:
        return ()
    else:
        return bases + linear_superclasses(bases[0])


def explicit_cast_to(t: TypeIndex, /) -> Iterator[TypeIndex]:
    for i in range(idb.interrogate_type_number_of_casts(t)):
        f = idb.interrogate_type_get_cast(t, i)
        for j in range(idb.interrogate_function_number_of_python_wrappers(f)):
            w = idb.interrogate_function_python_wrapper(f, j)
            cast_to = unwrap_type(idb.interrogate_wrapper_return_type(w))
            if idb.interrogate_type_is_atomic(cast_to):
                continue
            if type_is_exposed(cast_to):
                yield cast_to


def implicit_cast_from(t: TypeIndex, /) -> Iterator[TypeIndex]:
    for w in flatten(map(get_python_wrappers, get_constructors(t))):
        if idb.interrogate_wrapper_number_of_parameters(w) != 1:
            continue
        if (idb.interrogate_wrapper_parameter_name(w, 0)
                not in _implicit_cast_param_names):
            continue
        cast_from = unwrap_type(idb.interrogate_wrapper_parameter_type(w, 0))
        if t in recursive_superclasses(cast_from):
            continue
        if type_is_exposed(cast_from):
            yield cast_from


def make_param_type_replacement(cast_to: TypeIndex) -> str:
    """Return a type expressing all types that can be
    automatically coerced to the given type.
    """
    cast_from, next_layer = {cast_to}, _coercions[cast_to]
    while cast_layer := next_layer - cast_from:
        cast_from |= cast_layer
        next_layer = frozenset(flatten(
            _coercions[i]
            for i in cast_layer
        ))
    for a, b in combinations(tuple(cast_from), 2):
        if b in recursive_superclasses(a):
            cast_from.discard(a)
        elif a in recursive_superclasses(b):
            cast_from.discard(b)
    cast_from_names = {get_type_name(i) for i in cast_from}
    if idb.interrogate_type_name(cast_to) == 'Filename':
        cast_from_names.add('StrOrBytesPath')
    for alias, alias_of in _type_alias_data:
        if cast_from_names >= alias_of:
            cast_from_names -= alias_of
            cast_from_names.add(alias)
    cast_from_name = ' | '.join(
        sorted(cast_from_names, key=lambda s: (s == 'None', s))
    )
    return cast_from_name


@cache
def get_param_type_replacement(type_name: str) -> str | None:
    """Return a type expressing all types that can be
    automatically coerced to the given type.
    """
    replacement = _param_type_replacements.get(type_name)
    if replacement is not None:
        _logger.debug(f'Replaced parameter type {type_name!r}'
                      f' with {replacement!r}')
    return replacement


@cache
def get_alias_def(name: str) -> str | None:
    return _enum_definitions.get(name) or TYPE_ALIASES.get(name)


@cache
def get_module(name: str) -> str | None:
    return STDLIB_IMPORTS.get(name) or _modules.get(name)


def get_linear_superclasses(name: str, /) -> tuple[str, ...]:
    """Return a tuple of the names of the (recursive) superclasses for a type,
    stopping either at the top of the hierarchy or at the first class that
    inherits directly from multiple classes, whichever comes first.
    """
    return _linear_inheritance.get(name, ())


def process_dependency(
        name: str,
        *, if_alias: Callable[[str], object],
        if_import: Callable[[str], object],
        if_type_var: Callable[[Sequence], object]) -> bool:
    if name in BUILTIN_NAMES:
        pass
    elif (alias_def := get_alias_def(name)) is not None:
        if_alias(alias_def)
    elif (type_var_bounds := TYPE_VARIABLES.get(name)) is not None:
        if_type_var(type_var_bounds)
    elif (module := get_module(name)) is not None:
        if_import(module)
    else:
        return False
    return True


def inherits_from(a: str, b: str, /) -> bool:
    """Return whether `a` is narrower than `b`."""
    if 'Any' in (a, b):
        return False
    if a == b:
        return True
    if b == 'object' or a in ('Never', 'NoReturn'):
        return True
    if (a, b) in (('bool', 'int'), ('int', 'float')):
        return True
    return b in _inheritance.get(a, set())


def subtype_relationship(a: str, b: str, /) -> tuple[bool, bool]:
    """Return a tuple of two Boolean values, representing whether
    `a` is a subtype of `b` and vice versa, respectively.
    """
    a, b = TYPE_ALIASES.get(a, a), TYPE_ALIASES.get(b, b)
    l1, l2 = unpack_union(a), unpack_union(b)
    found_broader_in_b = dict.fromkeys(l1, False)
    found_broader_in_a = dict.fromkeys(l2, False)
    for i, j in product(l1, l2):
        if not found_broader_in_b[i] and inherits_from(i, j):
            found_broader_in_b[i] = True
        if not found_broader_in_a[j] and inherits_from(j, i):
            found_broader_in_a[j] = True
    return (all(found_broader_in_b.values()),
            all(found_broader_in_a.values()))


def combine_types(*types: str) -> str:
    combined = set(flatten(unpack_union(t) for t in types))
    for i in tuple(combined):
        if any(inherits_from(i, j) for j in combined if i != j):
            combined.remove(i)
    return ' | '.join(sorted(combined, key=lambda s: (s == 'None', s)))
