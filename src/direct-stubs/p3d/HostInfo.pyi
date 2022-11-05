__all__ = ['HostInfo']

from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from panda3d.core import Filename, HashVal, HTTPClient, TiXmlHandle

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
        appRunner: AppRunner | None = ...,
        hostDir: Filename | str | None = ...,
        rootDir: Filename | None = ...,
        asMirror: bool = ...,
        perPlatform: bool | None = ...,
    ) -> None: ...
    def freshenFile(self, http: HTTPClient, fileSpec: FileSpec, localPathname: Filename) -> bool: ...
    def downloadContentsFile(self, http: HTTPClient | None, redownload: bool = ..., hashVal: HashVal | None = ...) -> bool: ...
    def redownloadContentsFile(self, http: HTTPClient | None) -> bool: ...
    def hasCurrentContentsFile(self) -> bool: ...
    def readContentsFile(self, tempFilename: Filename | None = ..., freshDownload: bool = ...) -> bool: ...
    def readHostXml(self, xhost: TiXmlHandle) -> None: ...
    def getPackage(self, name: str, version: str | None, platform: str | None = ...) -> PackageInfo | None: ...
    def getPackages(self, name: str | None = ..., platform: str | None = ...) -> list[PackageInfo]: ...
    def getAllPackages(self, includeAllPlatforms: bool = ...) -> list[PackageInfo]: ...
    def deletePackages(self, packages: list[PackageInfo]) -> list[PackageInfo]: ...
