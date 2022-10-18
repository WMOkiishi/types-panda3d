import logging
from collections.abc import Iterator
from functools import cache
from importlib.util import find_spec
from os import PathLike
from pathlib import Path
from typing import Final, TypeAlias

import panda3d.interrogatedb as idb

from .special_cases import NOT_EXPOSED, TYPE_NAME_OVERRIDES

_logger: Final = logging.getLogger(__name__)

TypeIndex: TypeAlias = int
ElementIndex: TypeAlias = int
FunctionIndex: TypeAlias = int
FunctionWrapperIndex: TypeAlias = int
MakeSeqIndex: TypeAlias = int
ManifestIndex: TypeAlias = int


def type_is_unexposed_wrapper(t: TypeIndex, /) -> bool:
    """Return whether the type is a wrapper or a non-global typedef."""
    return (
        idb.interrogate_type_is_wrapped(t)
        or (
            idb.interrogate_type_is_typedef(t)
            and not idb.interrogate_type_is_global(t)
        )
    )


def type_is_wrapped_or_typedef(t: TypeIndex, /) -> bool:
    """Return whether the type is a wrapper or typedef."""
    return (
        idb.interrogate_type_is_wrapped(t)
        or idb.interrogate_type_is_typedef(t)
    )


def unwrap_type(t: TypeIndex, /) -> TypeIndex:
    """Traverse wrapped types and return the index of the first type
    that is neither a wrapper nor a typedef.
    """
    while type_is_wrapped_or_typedef(t):
        t = idb.interrogate_type_wrapped_type(t)
    return t


def type_is_unscoped_enum(t: TypeIndex, /) -> bool:
    return bool(
        idb.interrogate_type_is_enum(t)
        and idb.interrogate_type_name(t)
        and not idb.interrogate_type_is_scoped_enum(t)
    )


def function_is_exposed(f: FunctionIndex, /) -> bool:
    if idb.interrogate_function_name(f) == 'operator new':
        return False
    if idb.interrogate_function_scoped_name(f) in NOT_EXPOSED:
        return False
    wrapper_count = idb.interrogate_function_number_of_python_wrappers(f)
    if not wrapper_count:
        return False
    for n in range(wrapper_count):
        wrapper = idb.interrogate_function_python_wrapper(f, n)
        if wrapper_is_exposed(wrapper):
            return True
    return False


def wrapper_is_exposed(w: FunctionWrapperIndex, /) -> bool:
    return_type = idb.interrogate_wrapper_return_type(w)
    if not type_is_exposed(return_type):
        return False
    for n in range(idb.interrogate_wrapper_number_of_parameters(w)):
        if idb.interrogate_wrapper_parameter_is_this(w, n):
            continue
        param_type = idb.interrogate_wrapper_parameter_type(w, n)
        if not type_is_exposed(param_type):
            return False
    return True


def element_is_exposed(e: ElementIndex, /) -> bool:
    if not type_is_exposed(idb.interrogate_element_type(e)):
        return False
    if idb.interrogate_element_scoped_name(e) in NOT_EXPOSED:
        return False
    return True


@cache
def type_is_exposed(t: TypeIndex, /) -> bool:
    """Return True if a type is exposed to Python; return False otherwise."""
    if type_is_wrapped_or_typedef(t):
        return type_is_exposed(idb.interrogate_type_wrapped_type(t))
    name = idb.interrogate_type_name(t)
    if idb.interrogate_type_is_atomic(t) or name in TYPE_NAME_OVERRIDES:
        return True
    if idb.interrogate_type_is_array(t):
        # TODO: What's going on with compose_matrix and decompose_matrix?
        return False
    if name.startswith(('PointerTo< ', 'ConstPointerTo< ')):
        return True
    if idb.interrogate_type_is_unpublished(t):
        _logger.debug(f'Type {name!r} ({t}) is unpublished')
        return False
    if idb.interrogate_type_is_nested(t):
        if not idb.interrogate_type_is_fully_defined(t):
            _logger.info(f'Nested type {name!r} ({t}) is not fully defined')
            return False
    elif not idb.interrogate_type_is_global(t):
        _logger.info(f'Type {name!r} ({t}) is neither global nor nested')
        return False
    return True


def load_interrogate_database(
        directory: str | PathLike[str] | None = None) -> None:
    """Request all ".in" files contained within the given directory.
    If `directory` is `None`, use the pandac module's "input" directory.
    """
    if directory is None:
        pandac = find_spec('pandac')
        if not (pandac and pandac.origin):
            raise ImportError('Could not find "pandac" module')
        directory = Path(pandac.origin).parent.joinpath('input')
    else:
        directory = Path(directory)
    _logger.info(f'Requesting all database files from {directory}')
    idb.interrogate_add_search_directory(str(directory))
    for db in directory.glob('*.in'):
        idb.interrogate_request_database(db.name)
    # Trigger a load of the database
    # idb.interrogate_type_comment(0)


def get_all_methods(t: TypeIndex, /) -> Iterator[FunctionIndex]:
    # constructors
    for n in range(idb.interrogate_type_number_of_constructors(t)):
        yield idb.interrogate_type_get_constructor(t, n)
    # type casts
    for n in range(idb.interrogate_type_number_of_casts(t)):
        yield idb.interrogate_type_get_cast(t, n)
    # upcasts and downcasts
    for n in range(idb.interrogate_type_number_of_derivations(t)):
        if idb.interrogate_type_derivation_has_upcast(t, n):
            yield idb.interrogate_type_get_upcast(t, n)
        if idb.interrogate_type_derivation_has_downcast(t, n):
            yield idb.interrogate_type_get_downcast(t, n)
    # regular methods
    for n in range(idb.interrogate_type_number_of_methods(t)):
        yield idb.interrogate_type_get_method(t, n)


def get_global_getters() -> Iterator[FunctionIndex]:
    for n in range(idb.interrogate_number_of_globals()):
        g = idb.interrogate_get_global(n)
        yield idb.interrogate_element_getter(g)


def get_global_functions() -> Iterator[FunctionIndex]:
    for n in range(idb.interrogate_number_of_global_functions()):
        yield idb.interrogate_get_global_function(n)


def get_python_wrappers(i: FunctionIndex) -> Iterator[FunctionWrapperIndex]:
    for n in range(idb.interrogate_function_number_of_python_wrappers(i)):
        yield idb.interrogate_function_python_wrapper(i, n)


def get_constructors(i: TypeIndex) -> Iterator[FunctionIndex]:
    for n in range(idb.interrogate_type_number_of_constructors(i)):
        yield idb.interrogate_type_get_constructor(i, n)


def get_derivations(i: TypeIndex) -> Iterator[TypeIndex]:
    for n in range(idb.interrogate_type_number_of_derivations(i)):
        yield idb.interrogate_type_get_derivation(i, n)
