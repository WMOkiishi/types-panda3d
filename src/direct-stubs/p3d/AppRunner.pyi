__all__ = ['AppRunner', 'ArgumentError', 'dummyAppRunner']

from collections.abc import Callable
from typing import ClassVar
from typing_extensions import Final, Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import ConfigPage, Filename, HTTPClient, URLSpec, WindowHandle, WindowProperties
from .FileSpec import FileSpec
from .HostInfo import HostInfo
from .InstalledHostData import InstalledHostData
from .JavaScript import ConcreteStruct, UndefinedObject
from .PackageInfo import PackageInfo

class ArgumentError(AttributeError): ...
class ScriptAttributes: ...

class AppRunner(DirectObject):
    notify: ClassVar[Notifier]
    ConfigBasename: ClassVar[str]
    maxDiskUsage: ClassVar[int]
    P3DVCNone: Final[Literal[0]]
    P3DVCNormal: Final[Literal[1]]
    P3DVCForce: Final[Literal[2]]
    P3DVCNever: Final[Literal[3]]
    P3D_CONTENTS_DEFAULT_MAX_AGE: Final[Literal[5]]
    dummy: bool
    allowPythonDev: bool
    guiApp: bool
    interactiveConsole: bool
    initialAppImport: bool
    trueFileIO: bool
    respectPerPlatform: bool
    verifyContents: Literal[0, 1, 2, 3]
    sessionId: int
    packedAppEnvironmentInitialized: bool
    gotWindow: bool
    gotP3DFilename: bool
    p3dFilename: Filename | None
    p3dUrl: URLSpec | None
    started: bool
    windowOpened: bool
    windowPrc: ConfigPage | None
    http: HTTPClient | None
    Undefined: UndefinedObject
    ConcreteStruct: type[ConcreteStruct]
    nextScriptId: int
    instanceId = ...
    rootDir: Filename | None
    logDirectory: Filename | None
    superMirrorUrl = ...
    installedPackages: list
    downloadingPackages: list
    hosts: dict[str, HostInfo]
    altHost = ...
    altHostMap: dict
    pandaHostUrl: str
    exceptionHandler: Callable[[], object] | None
    downloadTask: None
    multifileRoot: str
    main: ScriptAttributes
    dom = ...
    deferredEvals: list
    requestFunc = ...
    windowProperties: WindowProperties | None
    tokens = ...
    argv = ...
    tokenDict: dict[str, str]
    def __init__(self) -> None: ...
    def getToken(self, tokenName: str) -> str | None: ...
    def getTokenInt(self, tokenName: str) -> int | None: ...
    def getTokenFloat(self, tokenName: str) -> float | None: ...
    def getTokenBool(self, tokenName: str) -> bool | None: ...
    def installPackage(self, packageName: str, version: str | None = None, hostUrl: str | None = None) -> bool: ...
    def getHostWithAlt(self, hostUrl: str | None) -> HostInfo: ...
    def getHost(self, hostUrl: str, hostDir: str | None = None) -> HostInfo: ...
    def getHostWithDir(self, hostDir: Filename | str | None) -> HostInfo: ...
    def deletePackages(self, packages: list[PackageInfo]) -> list[PackageInfo]: ...
    def freshenFile(self, host: HostInfo, fileSpec: FileSpec, localPathname: Filename) -> bool: ...
    def scanInstalledPackages(self) -> list[InstalledHostData]: ...
    def readConfigXml(self) -> None: ...
    def writeConfigXml(self) -> None: ...
    def checkDiskUsage(self) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...
    def rmtree(self, filename: Filename) -> None: ...
    def setSessionId(self, sessionId: int) -> None: ...
    def initPackedAppEnvironment(self) -> None: ...
    def getPandaScriptObject(self) -> ScriptAttributes: ...
    def setBrowserScriptObject(self, dom) -> None: ...
    def setInstanceInfo(
        self,
        rootDir: str,
        logDirectory: str | None,
        superMirrorUrl,
        verifyContents: Literal[0, 1, 2, 3],
        main: ScriptAttributes | None,
        respectPerPlatform: bool,
    ) -> None: ...
    def addPackageInfo(
        self,
        name: str,
        platform: str | None,
        version: str | None,
        hostUrl: str,
        hostDir: str | None = None,
        recurse: bool = False,
    ) -> None: ...
    def setP3DFilename(
        self,
        p3dFilename: str,
        tokens,
        argv,
        instanceId,
        interactiveConsole: bool,
        p3dOffset: int = ...,
        p3dUrl: URLSpec | str | None = None,
    ) -> None: ...
    def loadMultifilePrcFiles(self, mf, root) -> None: ...
    def setupWindow(
        self,
        windowType: Literal['embedded', 'hidden', 'fullscreen'],
        x: int,
        y: int,
        width: int,
        height: int,
        parent: WindowHandle | int,
    ) -> None: ...
    def setRequestFunc(self, func) -> None: ...
    def sendRequest(self, request, *args): ...
    def notifyRequest(self, message: str) -> None: ...
    def evalScript(self, expression, needsResponse: bool = False) -> None: ...
    def scriptRequest(
        self,
        operation,
        object,
        propertyName: str = ...,
        value=None,
        needsResponse: bool = True,
    ): ...
    def dropObject(self, objectId) -> None: ...

def dummyAppRunner(tokens=..., argv=None) -> AppRunner: ...
