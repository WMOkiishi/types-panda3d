__all__ = [
    'execfile',
    'exists',
    'getmtime',
    'getsize',
    'isdir',
    'isfile',
    'join',
    'lexists',
    'listdir',
    'open',
    'walk',
]

from collections.abc import Mapping
from io import IOBase
from posixpath import join as join
from typing import Any

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd: bool = True): ...

class StreamIOWrapper(IOBase):
    def __init__(self, stream, needsVfsClose: bool = False) -> None: ...
    def read(self, size: int | None = -1) -> bytes: ...
    read1 = read
    def readline(self, size: object = -1) -> bytes: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...
    def write(self, b) -> int: ...
    def writelines(self, lines) -> None: ...

def listdir(path) -> list[str]: ...
def walk(top, topdown: bool = True, onerror=None, followlinks: bool = True): ...
def isfile(path) -> bool: ...
def isdir(path) -> bool: ...
def exists(path) -> bool: ...
def lexists(path) -> bool: ...
def getmtime(path) -> int: ...
def getsize(path) -> int: ...
def execfile(path, globals: dict[str, Any] | None = None, locals: Mapping[str, Any] | None = None) -> None: ...