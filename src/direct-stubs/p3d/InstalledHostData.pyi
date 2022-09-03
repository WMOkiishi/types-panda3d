__all__ = ['InstalledHostData']

from panda3d.core import Filename
from .HostInfo import HostInfo
from .InstalledPackageData import InstalledPackageData
from .ScanDirectoryNode import ScanDirectoryNode

class InstalledHostData:
    host: HostInfo | None
    pathname: Filename
    totalSize: int
    packages: list[InstalledPackageData]
    hostUrl: str
    descriptiveName: str
    def __init__(self, host: HostInfo | None, dirnode: ScanDirectoryNode) -> None: ...
