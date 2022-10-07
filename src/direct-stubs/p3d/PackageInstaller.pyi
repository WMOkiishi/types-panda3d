__all__ = ['PackageInstaller']

from typing import ClassVar
from typing_extensions import Final, Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from direct.stdpy.threading import Lock, RLock
from panda3d.core import PythonTask
from .AppRunner import AppRunner
from .HostInfo import HostInfo
from .PackageInfo import PackageInfo

class PackageInstaller(DirectObject):
    class PendingPackage:
        notify: ClassVar[Notifier]
        packageName: str
        version: str | None
        host: HostInfo
        package: PackageInfo
        done: bool
        success: bool
        notified: bool
        calledPackageStarted: bool
        calledPackageFinished: bool
        downloadEffort: int
        prevDownloadEffort: int
        def __init__(self, packageName: str, version: str | None, host: HostInfo) -> None: ...
        def __cmp__(self, pp): ...
        def getProgress(self) -> float: ...
        def checkDescFile(self) -> bool: ...
        def getDescFile(self, http) -> bool: ...

    notify: ClassVar[Notifier]
    globalLock: ClassVar[Lock]
    nextUniqueId: ClassVar[int]
    S_initial: Final[Literal[0]]
    S_ready: Final[Literal[1]]
    S_started: Final[Literal[2]]
    S_done: Final[Literal[3]]
    uniqueId: int
    appRunner: AppRunner
    taskChain: str
    callbackLock: Lock
    calldedDownloadStarted: bool
    calledDownloadFinished: bool
    packageLock: RLock
    packages: list[PackageInstaller.PendingPackage]
    state: Literal[0, 1, 2, 3]
    needsDescFile: list
    descFileTask: PythonTask | None
    needsDownload: list
    downloadTask: PythonTask | None
    earlyDone: list[PackageInstaller.PendingPackage]
    done: list[PackageInstaller.PendingPackage]
    failed: list[PackageInstaller.PendingPackage]
    progressTask: PythonTask | None
    def __init__(self, appRunner: AppRunner, taskChain: str = ...) -> None: ...
    def destroy(self) -> None: ...
    def cleanup(self) -> None: ...
    def addPackage(self, packageName: str, version: str | None = None, hostUrl: str | None = None) -> None: ...
    def donePackages(self) -> None: ...
    def downloadStarted(self) -> None: ...
    def packageStarted(self, package: PackageInfo) -> None: ...
    def packageProgress(self, package: PackageInfo, progress: float) -> None: ...
    def downloadProgress(self, overallProgress: float) -> None: ...
    def packageFinished(self, package: PackageInfo, success: bool) -> None: ...
    def downloadFinished(self, success: bool) -> None: ...
