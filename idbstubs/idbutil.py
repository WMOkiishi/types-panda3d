import logging
from functools import cache
from importlib.util import find_spec
from os import PathLike
from pathlib import Path
from typing import Final

import panda3d.interrogatedb as idb

from .idb_interface import IDBElement, IDBFunction, IDBFunctionWrapper, IDBType
from .special_cases import NOT_EXPOSED, TYPE_NAME_OVERRIDES

_logger: Final = logging.getLogger(__name__)


def type_is_unexposed_wrapper(idb_type: IDBType) -> bool:
    """Return whether a type is a wrapper or non-global typedef."""
    return (
        idb_type.is_wrapped
        or (idb_type.is_typedef and not idb_type.is_global)
    )


def unwrap_type(idb_type: IDBType) -> IDBType:
    """Traverse wrapped types and return the first type
    that is neither a wrapper nor a typedef.
    """
    while idb_type.is_wrapped or idb_type.is_typedef:
        idb_type = idb_type.wrapped_type
    return idb_type


def type_is_unscoped_enum(idb_type: IDBType) -> bool:
    """Return whether the given type is an enumerated type
    exposed to Python simply as integer constants.
    """
    return bool(
        idb_type.is_enum and idb_type.name
        and not idb_type.is_scoped_enum
    )


def type_has_copy_constructor(idb_type: IDBType) -> bool:
    """Return whether the given type has a "copy constructor",
    meaning it has a `__copy__` method.
    """
    for function in idb_type.constructors:
        for wrapper in function.wrappers:
            if wrapper.is_copy_constructor:
                return True
    for function in idb_type.methods:
        if function.name == 'make_copy':
            return True
    return False


def function_is_exposed(function: IDBFunction) -> bool:
    """Return whether a function is exposed to Python."""
    if function.name == 'operator new':
        return False
    if function.scoped_name in NOT_EXPOSED:
        return False
    return any(wrapper_is_exposed(w) for w in function.wrappers)


def wrapper_is_exposed(wrapper: IDBFunctionWrapper) -> bool:
    """Return whether a function wrapper is exposed to Python."""
    if not type_is_exposed(wrapper.return_type):
        return False
    for parameter in wrapper.parameters:
        if parameter.is_this:
            continue
        if not type_is_exposed(parameter.type):
            return False
    return True


def element_is_exposed(element: IDBElement) -> bool:
    """Return whether an element is exposed to Python."""
    if not type_is_exposed(element.type):
        return False
    if element.scoped_name in NOT_EXPOSED:
        return False
    return True


@cache
def type_is_exposed(idb_type: IDBType) -> bool:
    """Return whether a type is exposed to Python."""
    if idb_type.is_wrapped or idb_type.is_typedef:
        return type_is_exposed(idb_type.wrapped_type)
    if idb_type.is_atomic or idb_type.name in TYPE_NAME_OVERRIDES:
        return True
    if idb_type.is_array:
        # TODO: What's going on with compose_matrix and decompose_matrix?
        return False
    if idb_type.name.startswith(('PointerTo< ', 'ConstPointerTo< ')):
        return True
    if idb_type.is_unpublished:
        _logger.debug(f'Type {idb_type} is unpublished')
        return False
    if idb_type.is_nested:
        if not idb_type.is_fully_defined:
            _logger.info(f'Nested type {idb_type} is not fully defined')
            return False
    elif not idb_type.is_global:
        _logger.info(f'Type {idb_type} is neither global nor nested')
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
