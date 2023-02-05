__all__ = ['Installer', 'Standalone']

from _typeshed import StrOrBytesPath
from collections.abc import Generator, Mapping
from tarfile import TarInfo
from typing import AnyStr, ClassVar
from typing_extensions import Final, Literal

from direct.directnotify.Notifier import Notifier
from panda3d.core import Filename, HTTPClient, PNMImage

from .HostInfo import HostInfo
from .PackageInfo import PackageInfo

P3DEMBED_MAGIC: Final = 0xFF3D3D00

def archiveFilter(info): ...

class TarInfoRoot(TarInfo): ...
class TarInfoRootOSX(TarInfoRoot): ...

class Standalone:
    notify: ClassVar[Notifier]
    p3dfile: Filename
    basename: str
    tokens: Mapping[str, str]
    tempDir: Filename
    host: HostInfo
    http: HTTPClient
    def __init__(self, p3dfile: StrOrBytesPath, tokens: Mapping[str, str] = ...) -> None: ...
    def __del__(self) -> None: ...
    def buildAll(self, outputDir: str = '.') -> None: ...
    def build(self, output: Filename, platform: str | None = None, extraTokens: Mapping[str, str] = ...) -> None: ...
    def embed(self, output: Filename, p3dembed: Filename, extraTokens: Mapping[str, str] = ...) -> None: ...
    def getExtraFiles(self, platform: str | None) -> list[Filename]: ...

class PackageTree:
    platform: str
    hosts: dict[str, HostInfo]
    packages: dict[tuple[str, str | None], PackageInfo]
    hostUrl: str
    hostDir: Filename
    http: HTTPClient
    def __init__(self, platform: str, hostDir: StrOrBytesPath, hostUrl: str) -> None: ...
    def getHost(self, hostUrl) -> HostInfo: ...
    def installPackage(self, name: str, version: str | None, hostUrl=None): ...

class Icon:
    notify: ClassVar[Notifier]
    images: dict[int, PNMImage]
    def __init__(self) -> None: ...
    def addImage(self, image: PNMImage | Filename | str) -> bool: ...
    def generateMissingImages(self) -> None: ...
    def makeICO(self, fn: Filename | str) -> Literal[True]: ...
    def makeICNS(self, fn: Filename | str) -> Literal[True]: ...

class Installer:
    notify: ClassVar[Notifier]
    p3dFilename: Filename
    shortname: str
    fullname: str
    version: str
    includeRequires: bool
    offerRun: bool
    offerDesktopShortcut: bool
    licensename: str
    licensefile: Filename
    authorid: str
    authorname: str
    authoremail: str
    icon: Icon | None
    hostUrl: str | None
    requires: list[tuple[str, str, str]]
    extracts: list[str]
    tempDir: Filename
    standalone: Standalone
    def __init__(self, p3dfile: Filename, shortname: str, fullname: str, version: object, tokens=...) -> None: ...
    def __del__(self) -> None: ...
    def installPackagesInto(self, hostDir: StrOrBytesPath, platform: str) -> None: ...
    def buildAll(self, outputDir: str = '.') -> None: ...
    def build(self, output: StrOrBytesPath, platform: str | None = None) -> None: ...
    def buildDEB(self, output: StrOrBytesPath, platform: str) -> Filename: ...
    def buildArch(self, output: StrOrBytesPath, platform: str) -> Filename: ...
    def buildAPP(self, output: StrOrBytesPath, platform: str) -> Filename: ...
    def buildPKG(self, output: StrOrBytesPath, platform: str) -> Filename: ...
    def buildNSIS(self, output: StrOrBytesPath, platform: str) -> Filename: ...
    def os_walk(self, top: AnyStr) -> Generator[tuple[AnyStr, list[AnyStr], list[AnyStr]], None, None]: ...
