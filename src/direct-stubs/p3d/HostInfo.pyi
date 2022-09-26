__all__ = ['HostInfo']

from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from panda3d.core import Filename, HTTPClient, HashVal, TiXmlHandle
from .AppRunner import AppRunner
from .FileSpec import FileSpec
from .PackageInfo import PackageInfo

class HostInfo:
    notify: ClassVar[Notifier]
    hostUrl: str
    hostUrlPrefix: str | None
    downloadUrlPrefix: str | None
    appRunner: AppRunner | None
    rootDir: Filename | None
    hostDir: Filename | None
    asMirror: bool
    perPlatform: bool
    hasContentsFile: bool
    contentsExpiration: int
    contentSpec: FileSpec
    descriptiveName: str | None
    mirrors: list[str]
    altHosts: dict[str, str]
    packages: dict[tuple[str, str], dict[str, PackageInfo]]
    def __init__(
        self,
        hostUrl: str,
        appRunner: AppRunner | None = None,
        hostDir: Filename | str | None = None,
        rootDir: Filename | None = None,
        asMirror: bool = False,
        perPlatform: bool | None = None,
    ) -> None: ...
    def freshenFile(self, http: HTTPClient, fileSpec: FileSpec, localPathname: Filename) -> bool: ...
    def downloadContentsFile(self, http: HTTPClient | None, redownload: bool = False, hashVal: HashVal | None = None) -> bool: ...
    def redownloadContentsFile(self, http: HTTPClient | None) -> bool: ...
    def hasCurrentContentsFile(self) -> bool: ...
    def readContentsFile(self, tempFilename: Filename | None = None, freshDownload: bool = False) -> bool: ...
    def readHostXml(self, xhost: TiXmlHandle) -> None: ...
    def getPackage(self, name: str, version: str | None, platform: str | None = None) -> PackageInfo | None: ...
    def getPackages(self, name: str | None = None, platform: str | None = None) -> list: ...
    def getAllPackages(self, includeAllPlatforms: bool = False) -> list[PackageInfo]: ...
    def deletePackages(self, packages: list[PackageInfo]) -> list[PackageInfo]: ...
