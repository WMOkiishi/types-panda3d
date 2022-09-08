from typing import TypeVar
from typing_extensions import Protocol

_T_contra = TypeVar('_T_contra', contravariant=True)

class _SupportsWrite(Protocol[_T_contra]):
    def write(self, s: _T_contra, /) -> object: ...

class ProtoObjs:
    dirname: str
    name: str
    filename: str
    data: dict
    def __init__(self, name: str) -> None: ...
    def populate(self) -> None: ...
    def saveProtoData(self, f: _SupportsWrite[str] | None) -> None: ...
    def saveToFile(self) -> None: ...
