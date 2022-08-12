__all__ = [
    'PickleError', 'PicklingError', 'UnpicklingError', 'Pickler',
    'Unpickler', 'dump', 'dumps', 'load', 'loads', 'HIGHEST_PROTOCOL',
]

from pickle import (
    HIGHEST_PROTOCOL as HIGHEST_PROTOCOL,
    PickleError as PickleError,
    PicklingError as PicklingError,
    UnpicklingError as UnpicklingError,
    DEFAULT_PROTOCOL as DEFAULT_PROTOCOL,
    Pickler as BasePickler,
    Unpickler as BaseUnpickler,
)
from typing import Any

class Pickler(BasePickler):
    def clear_memo(self) -> None: ...
    def save(self, obj, save_persistent_id: bool = True) -> None: ...

class Unpickler(BaseUnpickler):
    def load_reduce(self) -> None: ...

def dump(obj: Any, file, protocol: int | None = None) -> None: ...
def dumps(obj: Any, protocol: int | None = None): ...
def load(file) -> Any: ...
def loads(str: bytes) -> Any: ...
