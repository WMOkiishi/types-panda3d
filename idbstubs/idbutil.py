import logging
from collections.abc import Iterator
from functools import cache
from importlib.util import find_spec
from os import PathLike
from pathlib import Path
from typing import Final

import panda3d.interrogatedb as idb

from .idb_interface import (
    ElementIndex,
    FunctionIndex,
    FunctionWrapperIndex,
    IDBFunction,
    IDBType,
    TypeIndex,
)
from .special_cases import NOT_EXPOSED, TYPE_NAME_OVERRIDES

_logger: Final = logging.getLogger(__name__)


def type_is_unexposed_wrapper(t: TypeIndex, /) -> bool:
    """Return whether a type is a wrapper or non-global typedef."""
    return (
        idb.interrogate_type_is_wrapped(t)
        or (
            idb.interrogate_type_is_typedef(t)
            and not idb.interrogate_type_is_global(t)
        )
    )


def type_is_wrapped_or_typedef(t: TypeIndex, /) -> bool:
    """Return whether a type is a wrapper or typedef."""
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
    """Return whether the given type is an enumerated type
    exposed to Python simply as integer constants.
    """
    return bool(
        idb.interrogate_type_is_enum(t)
        and idb.interrogate_type_name(t)
        and not idb.interrogate_type_is_scoped_enum(t)
    )


def function_is_exposed(f: FunctionIndex, /) -> bool:
    """Return whether a function is exposed to Python."""
    if idb.interrogate_function_name(f) == 'operator new':
        return False
    if idb.interrogate_function_scoped_name(f) in NOT_EXPOSED:
        return False
    return any(wrapper_is_exposed(w) for w in get_python_wrappers(f))


def wrapper_is_exposed(w: FunctionWrapperIndex, /) -> bool:
    """Return whether a function wrapper is exposed to Python."""
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
    """Return whether an element is exposed to Python."""
    if not type_is_exposed(idb.interrogate_element_type(e)):
        return False
    if idb.interrogate_element_scoped_name(e) in NOT_EXPOSED:
        return False
    return True


@cache
def type_is_exposed(t: TypeIndex, /) -> bool:
    """Return whether a type is exposed to Python."""
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


def get_global_types() -> Iterator[TypeIndex]:
    """Yield the indices of all top-level types known to interrogate."""
    for n in range(idb.interrogate_number_of_global_types()):
        t = idb.interrogate_get_global_type(n)
        if not idb.interrogate_type_is_nested(t):
            yield t


def get_global_functions() -> Iterator[FunctionIndex]:
    """Yield the indices of all top-level functions known to interrogate."""
    for n in range(idb.interrogate_number_of_global_functions()):
        yield idb.interrogate_get_global_function(n)
    for n in range(idb.interrogate_number_of_globals()):
        g = idb.interrogate_get_global(n)
        yield idb.interrogate_element_getter(g)


def get_python_wrappers(f: FunctionIndex, /) -> Iterator[FunctionWrapperIndex]:
    """Yield the indices of a function's Python wrappers."""
    for n in range(idb.interrogate_function_number_of_python_wrappers(f)):
        yield idb.interrogate_function_python_wrapper(f, n)


def get_constructors(t: TypeIndex, /) -> Iterator[FunctionIndex]:
    """Yield the indices of a type's constructors."""
    for n in range(idb.interrogate_type_number_of_constructors(t)):
        yield idb.interrogate_type_get_constructor(t, n)


def get_all_methods(idb_type: IDBType) -> Iterator[IDBFunction]:
    """Yield all of a type's methods."""
    yield from idb_type.constructors
    yield from idb_type.casts
    yield from idb_type.up_down_casts
    yield from idb_type.methods


def get_derivations(t: TypeIndex, /) -> Iterator[TypeIndex]:
    """Yield the indices of a type's direct base classes."""
    for n in range(idb.interrogate_type_number_of_derivations(t)):
        yield idb.interrogate_type_get_derivation(t, n)
