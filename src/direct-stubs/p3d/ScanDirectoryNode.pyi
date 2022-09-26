__all__ = ['ScanDirectoryNode']

from typing_extensions import Final

from panda3d.core import Filename, VirtualFileSystem

vfs: Final[VirtualFileSystem]

class ScanDirectoryNode:
    pathname: Filename
    filenames: list[Filename]
    fileSize: int
    nested: list[ScanDirectoryNode]
    nextedSize: int
    def __init__(self, pathname: Filename, ignoreUsageXml: bool = False) -> None: ...
    def getTotalSize(self) -> int: ...
    def extractSubdir(self, pathname: Filename) -> ScanDirectoryNode: ...
