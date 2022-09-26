__all__ = ['PackageInfo']

from collections.abc import Generator
from typing import ClassVar
from typing_extensions import Literal

from panda3d.core import Filename, HTTPClient, PStatCollector, TiXmlElement
from ..directnotify.Notifier import Notifier
from .AppRunner import AppRunner
from .FileSpec import FileSpec
from .HostInfo import HostInfo

class PackageInfo:
    class InstallStep:
        bytesNeeded: int
        bytesDone: int
        bytesFactor: int
        stepType: str
        pStatCol: PStatCollector
        def __init__(self, func, bytes: int, factor: int, stepType: str) -> None: ...
        def func(self): ...
        def getEffort(self) -> int: ...
        def getProgress(self) -> float: ...
    notify: ClassVar[Notifier]
    downloadFactor: int
    uncompressFactor: float
    unpackFactor: float
    patchFactor: float
    stepComplete: ClassVar[Literal[1]]
    stepFailed: ClassVar[Literal[2]]
    restartDownload: ClassVar[Literal[3]]
    stepContinue: ClassVar[Literal[4]]
    UsageBasename: ClassVar[str]
    host: HostInfo
    packageName: str
    packageVersion: str | None
    platform: str | None
    solo: bool
    asMirror: bool
    perPlatform: bool
    http: HTTPClient | None
    packageDir: Filename | None
    descFile = ...
    importDescFile = ...
    hasDescFile: bool
    patchVersion: int | None
    displayName: str | None
    guiApp: bool
    uncompressedArchive: FileSpec | None
    compressedArchive: FileSpec | None
    extracts: list
    requires: list
    installPlans: list[PackageInfo.InstallStep] | None
    downloadProgress: float
    hasPackage: bool
    installed: bool
    updated: bool
    diskSpace: int | None
    descFileDirname: str
    descFileBasename: str
    def __init__(
        self,
        host: HostInfo,
        packageName: str,
        packageVersion: str | None,
        platform: str | None = None,
        solo: bool = False,
        asMirror: bool = False,
        perPlatform: bool = False,
    ) -> None: ...
    def getPackageDir(self) -> Filename: ...
    def getDownloadEffort(self) -> int: ...
    def getPrevDownloadedEffort(self) -> int: ...
    def getFormattedName(self) -> str: ...
    def setupFilenames(self) -> None: ...
    def checkStatus(self) -> bool: ...
    def hasCurrentDescFile(self) -> bool: ...
    def downloadDescFile(self, http: HTTPClient) -> bool: ...
    def downloadDescFileGenerator(self, http: HTTPClient) -> Generator[Literal[1, 2, 4], None, None]: ...
    def downloadPackage(self, http: HTTPClient) -> bool: ...
    def downloadPackageGenerator(self, http: HTTPClient) -> Generator[Literal[1, 2, 4], None, None]: ...
    def installPackage(self, appRunner: AppRunner) -> bool: ...
    def markUsed(self) -> None: ...
    def getUsage(self) -> TiXmlElement | None: ...
