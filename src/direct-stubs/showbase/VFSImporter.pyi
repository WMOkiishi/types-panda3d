__all__ = ['register', 'reloadSharedPackage', 'reloadSharedPackages', 'sharedPackages']

from collections.abc import Iterable
from os import PathLike
from types import ModuleType
from typing_extensions import Final, Literal, TypeAlias

from panda3d.core import ConfigVariableFilename, Filename, VirtualFile, VirtualFileSystem

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike

sharedPackages: dict[str, Literal[True]]
vfs: Final[VirtualFileSystem]
compiledExtensions: list[str]

class VFSImporter:
    dir_path: Filename
    def __init__(self, path: Filename | str) -> None: ...
    def find_module(self, fullname: str, path: Filename | None) -> VFSLoader | None: ...

class VFSLoader:
    dir_path: Filename
    timestamp: int | None
    filename: Filename
    desc: bytes
    packagePath: Filename | None
    def __init__(
        self,
        dir_path: Filename,
        vfile: VirtualFile | None,
        filename: Filename,
        desc: bytes,
        packagePath: Filename | None = None,
    ) -> None: ...
    def load_module(self, fullname: str, loadingShared: bool = False) -> ModuleType: ...
    def getdata(self, path: _Filename) -> bytes: ...
    def is_package(self, fullname: object) -> bool: ...
    def get_code(self, fullname: object): ...
    def get_source(self, fullname: object) -> str | None: ...

class VFSSharedImporter:
    def __init__(self) -> None: ...
    def find_module(self, fullname: str, path: Iterable[str] | None = None, reload: bool = False) -> VFSSharedImporter | None: ...
    def getLoadedDirname(self, mod: ModuleType) -> str | None: ...

class VFSSharedLoader:
    loaders: Iterable[VFSLoader]
    reload: bool
    def __init__(self, loaders: Iterable[VFSLoader], reload: bool) -> None: ...
    def load_module(self, fullname: str) -> ModuleType | None: ...

def register() -> None: ...
def reloadSharedPackage(mod: ModuleType) -> None: ...
def reloadSharedPackages() -> None: ...
