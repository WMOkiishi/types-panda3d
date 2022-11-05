__all__ = ['InstalledPackageData']

from panda3d.core import Filename

from .PackageInfo import PackageInfo
from .ScanDirectoryNode import ScanDirectoryNode

class InstalledPackageData:
    package: PackageInfo | None
    pathname: Filename
    totalSize: int
    lastUse: int | None
    displayName: str
    def __init__(self, package: PackageInfo | None, dirnode: ScanDirectoryNode) -> None: ...
