__all__ = [
    'HIGHEST_PROTOCOL',
    'PickleError',
    'Pickler',
    'PicklingError',
    'Unpickler',
    'UnpicklingError',
    'dump',
    'dumps',
    'load',
    'loads',
]

from _typeshed import SupportsRead, SupportsReadline, SupportsWrite
from pickle import (
    DEFAULT_PROTOCOL as DEFAULT_PROTOCOL,
    HIGHEST_PROTOCOL as HIGHEST_PROTOCOL,
    PickleError as PickleError,
    Pickler as BasePickler,
    PicklingError as PicklingError,
    Unpickler as BaseUnpickler,
    UnpicklingError as UnpicklingError,
)
from typing import Any, TypeVar
from typing_extensions import Protocol

_T_co = TypeVar('_T_co', covariant=True)

class _SupportsReadAndReadline(SupportsRead[_T_co], SupportsReadline[_T_co], Protocol[_T_co]): ...

class Pickler(BasePickler):
    def save(self, obj: Any, save_persistent_id: bool = True) -> None: ...

class Unpickler(BaseUnpickler):
    def load_reduce(self) -> None: ...

def dump(obj: Any, file: SupportsWrite[bytes], protocol: int | None = None) -> None: ...
def dumps(obj: Any, protocol: int | None = None) -> bytes: ...
def load(file: _SupportsReadAndReadline[bytes]) -> Any: ...
def loads(str: bytes) -> Any: ...
