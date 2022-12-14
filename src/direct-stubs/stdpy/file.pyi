__all__ = ['execfile', 'exists', 'getmtime', 'getsize', 'isdir', 'isfile', 'join', 'lexists', 'listdir', 'open', 'walk']

from _typeshed import ReadableBuffer, StrOrBytesPath
from collections.abc import Generator, Iterable, Mapping
from io import IOBase
from posixpath import join as join
from typing import Any, TypeVar

from direct._typing import Unused
from panda3d.core import VirtualFile, istream, ostream

_StrOrBytesPathT = TypeVar('_StrOrBytesPathT', bound=StrOrBytesPath)

def open(
    file: StrOrBytesPath | VirtualFile | istream | ostream,
    mode: str = ...,
    buffering: int = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    newline: str | None = ...,
    closefd: bool = ...,
) -> Any: ...

class StreamIOWrapper(IOBase):
    def __init__(self, stream: istream | ostream, needsVfsClose: bool = ...) -> None: ...
    def read(self, size: int | None = ...) -> bytes: ...
    read1 = read
    def readline(self, size: Unused = ...) -> bytes: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...  # type: ignore[override]
    def write(self, b: bytes) -> int: ...
    def writelines(self, lines: Iterable[ReadableBuffer]) -> None: ...

def listdir(path: str) -> list[str]: ...
def walk(
    top: _StrOrBytesPathT, topdown: bool = ..., onerror: object = ..., followlinks: bool = ...
) -> Generator[tuple[_StrOrBytesPathT, list[str], list[str]], None, None]: ...
def isfile(path: str) -> bool: ...
def isdir(path: str) -> bool: ...
def exists(path: str) -> bool: ...
def lexists(path: str) -> bool: ...
def getmtime(path: str) -> int: ...
def getsize(path: str) -> int: ...
def execfile(path: str, globals: dict[str, Any] | None = ..., locals: Mapping[str, Any] | None = ...) -> None: ...
