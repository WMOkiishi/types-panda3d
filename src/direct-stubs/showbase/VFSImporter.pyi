__all__ = ['register', 'reloadSharedPackage', 'reloadSharedPackages', 'sharedPackages']

from collections.abc import Iterable
from types import ModuleType
from typing import Any
from typing_extensions import Final, Literal

from direct._typing import Unused
from panda3d._typing import Filepath
from panda3d.core import Filename, VirtualFile, VirtualFileSystem

sharedPackages: dict[str, Literal[True]]
vfs: Final[VirtualFileSystem]
compiledExtensions: list[str]

class VFSImporter:
    dir_path: Filename
    def __init__(self, path: Filename | str) -> None: ...
    def find_module(self, fullname: str, path: Filename | None = ...) -> VFSLoader | None: ...

class VFSLoader:
    dir_path: Filename
    timestamp: int | None
    filename: Filename
    desc: bytes
    packagePath: Filename | None
    def __init__(
        self, dir_path: Filename, vfile: VirtualFile | None, filename: Filename, desc: bytes, packagePath: Filename | None = ...
    ) -> None: ...
    def load_module(self, fullname: str, loadingShared: bool = ...) -> ModuleType: ...
    def getdata(self, path: Filepath) -> bytes: ...
    def is_package(self, fullname: Unused) -> bool: ...
    def get_code(self, fullname: Unused) -> Any | None: ...
    def get_source(self, fullname: Unused) -> str | None: ...
    def get_filename(self, fullname: Unused) -> str: ...

class VFSSharedImporter:
    def __init__(self) -> None: ...
    def find_module(self, fullname: str, path: Iterable[str] | None = ..., reload: bool = ...) -> VFSSharedImporter | None: ...
    def getLoadedDirname(self, mod: ModuleType) -> str | None: ...

class VFSSharedLoader:
    loaders: Iterable[VFSLoader]
    reload: bool
    def __init__(self, loaders: Iterable[VFSLoader], reload: bool) -> None: ...
    def load_module(self, fullname: str) -> ModuleType | None: ...

def register() -> None: ...
def reloadSharedPackage(mod: ModuleType) -> None: ...
def reloadSharedPackages() -> None: ...
