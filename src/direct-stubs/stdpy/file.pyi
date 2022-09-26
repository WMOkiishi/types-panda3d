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

from _typeshed import ReadableBuffer, StrOrBytesPath
from collections.abc import Generator, Iterable, Mapping
from io import IOBase
from posixpath import join as join
from typing import Any, TypeVar
from typing_extensions import TypeAlias

from panda3d.core import ConfigVariableFilename, VirtualFile, istream, ostream

_Filename: TypeAlias = StrOrBytesPath | ConfigVariableFilename
_Unused: TypeAlias = object
_F = TypeVar('_F', bound=_Filename)

def open(
    file: _Filename | VirtualFile | istream | ostream,
    mode: str = ...,
    buffering: int = ...,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,
) -> Any: ...

class StreamIOWrapper(IOBase):
    def __init__(self, stream: istream | ostream, needsVfsClose: bool = False) -> None: ...
    def read(self, size: int | None = ...) -> bytes: ...
    read1 = read
    def readline(self, size: _Unused = ...) -> bytes: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...  # type: ignore[override]
    def write(self, b: bytes) -> int: ...
    def writelines(self, lines: Iterable[ReadableBuffer]) -> None: ...

def listdir(path: str) -> list[str]: ...
def walk(
    top: _F,
    topdown: bool = True,
    onerror: _Unused = None,
    followlinks: bool = True,
) -> Generator[tuple[_F, list[str], list[str]], None, None]: ...
def isfile(path: str) -> bool: ...
def isdir(path: str) -> bool: ...
def exists(path: str) -> bool: ...
def lexists(path: str) -> bool: ...
def getmtime(path: str) -> int: ...
def getsize(path: str) -> int: ...
def execfile(path: str, globals: dict[str, Any] | None = None, locals: Mapping[str, Any] | None = None) -> None: ...
