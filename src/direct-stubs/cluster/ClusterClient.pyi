from collections.abc import Container, Iterable, Sequence
from types import CodeType
from typing import Any, ClassVar, NoReturn
from typing_extensions import Literal, TypeAlias

from panda3d.core import (
    Connection,
    ConnectionWriter,
    DatagramIterator,
    LMatrix3f,
    LMatrix4f,
    LVecBase2f,
    LVecBase3f,
    LVecBase4f,
    LVector3f,
    NetDatagram,
    NodePath,
    QueuedConnectionManager,
    QueuedConnectionReader,
    UnalignedLVecBase4f,
)
from ..directnotify.Notifier import Notifier
from ..distributed.PyDatagramIterator import PyDatagramIterator
from ..showbase.DirectObject import DirectObject
from .ClusterMsgs import ClusterMsgHandler

_NamedMovement: TypeAlias = tuple[
    str,
    float, float, float,
    float, float, float,
    float, float, float,
    float, float, float, float,
    bool,
]
_Vec2f: TypeAlias = LVecBase2f | tuple[float, float]
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow | tuple[float, float, float]
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | tuple[float, float, float, float]

class ClusterClient(DirectObject):
    notify: ClassVar[Notifier]
    MGR_NUM: ClassVar[int]
    __name__: str
    daemon = ...
    qcm: QueuedConnectionManager
    serverList: list[DisplayConnection]
    serverQueues: list[list[tuple]]
    msgHandler: ClusterMsgHandler
    objectMappings: dict[str, NodePath]
    objectHasColor: dict[str, bool]
    controlMappings: dict[str, tuple[str, Sequence[int]]]
    controlOffsets: dict[str, LVector3f]
    taggedObjects: dict[str, dict[str, Any]]
    controlPriorities: dict[str, int]
    sortedControlMappings: list[tuple[int, str]]
    def __init__(self, configList: Iterable[ClusterConfigItem], clusterSyncFlag: int) -> None: ...
    def startReaderPollTask(self) -> None: ...
    def startControlObjectTask(self) -> None: ...
    def startSynchronizeTimeTask(self) -> None: ...
    def synchronizeTimeTask(self, task: object) -> Literal[1]: ...
    def startMoveCamTask(self) -> None: ...
    def controlObjectTask(self, task: object) -> Literal[1]: ...
    def sendNamedMovementDone(self, serverList: Sequence[int] | None = None) -> None: ...
    def redoSortedPriorities(self) -> None: ...
    def moveObject(
        self,
        nodePath: NodePath,
        object: str,
        serverList: Iterable[int],
        offset: _Vec3f,
        hasColor: bool = True,
    ) -> None: ...
    def moveCameraTask(self, task: object) -> Literal[1]: ...
    def moveCamera(self, xyz: _Vec3f, hpr: _Vec3f) -> None: ...
    def startMoveSelectedTask(self) -> None: ...
    def moveSelectedTask(self, state: object) -> Literal[1]: ...
    def addNamedObjectMapping(self, object: NodePath, name: str, hasColor: bool = True) -> None: ...
    def removeObjectMapping(self, name: str) -> None: ...
    def addControlMapping(
        self,
        objectName: str,
        controlledName: str,
        serverList: Sequence[int] | None = None,
        offset: LVector3f | None = None,
        priority: int = 0,
    ) -> None: ...
    def setControlMappingOffset(self, objectName: str, offset: LVector3f) -> None: ...
    def removeControlMapping(self, name: str, serverList: Container[int] | None = None) -> None: ...
    def getNodePathFindCmd(self, nodePath: NodePath) -> str: ...
    def getNodePathName(self, nodePath: NodePath) -> str: ...
    def addObjectTag(self, object, selectFunction, deselectFunction, selectArgs, deselectArgs) -> None: ...
    def removeObjectTag(self, object: str) -> None: ...
    def selectNodePath(self, nodePath: NodePath) -> None: ...
    def deselectNodePath(self, nodePath: NodePath) -> None: ...
    def sendCamFrustum(self, focalLength, filmSize, filmOffset, indexList: Iterable[int] = ...) -> None: ...
    def loadModel(self, nodePath: object) -> None: ...
    def __call__(self, commandString, fLocally: bool = True, serverList: Iterable[int] | None = ...) -> None: ...
    def handleDatagram(self, dgi: DatagramIterator, type: int, server: int) -> int: ...
    def handleMessageQueue(self, server: int) -> None: ...
    def handleNamedMovement(self, data: _NamedMovement) -> None: ...
    def exit(self) -> NoReturn: ...

class ClusterClientSync(ClusterClient):
    waitForSwap: bool
    ready: bool
    def startSwapCoordinatorTask(self) -> None: ...
    def swapCoordinator(self, task: object) -> Literal[1]: ...

class DisplayConnection:
    msgHandler: ClusterMsgHandler
    tcpConn: Connection
    qcr: QueuedConnectionReader
    cw: ConnectionWriter
    def __init__(self, qcm: QueuedConnectionManager, serverName: str, port: int, msgHandler: ClusterMsgHandler) -> None: ...
    def poll(self) -> list[tuple[NetDatagram, PyDatagramIterator, str]]: ...
    def sendCamOffset(self, xyz: _Vec3f, hpr: _Vec3f) -> None: ...
    def sendCamFrustum(self, focalLength: float, filmSize: _Vec2f, filmOffset: _Vec2f) -> None: ...
    def sendNamedMovementDone(self) -> None: ...
    def sendMoveNamedObject(self, xyz: _Vec3f, hpr: _Vec3f, scale: _Vec3f, color: _Vec4f, hidden: bool, name: str) -> None: ...
    def sendMoveCam(self, xyz: _Vec3f, hpr: _Vec3f) -> None: ...
    def sendMvoeSelected(self, xyz: _Vec3f, hpr: _Vec3f, scale: _Vec3f) -> None: ...
    def getSwapReady(self) -> None: ...
    def sendSwapNow(self) -> None: ...
    def sendCommandString(self, commandString: str) -> None: ...
    def sendExit(self) -> None: ...
    def sendTimeData(self, frameCount: int, frameTime: float, dt: float) -> None: ...

class ClusterConfigItem:
    serverConfigName: str
    serverName: str
    serverDaemonPort: int
    serverMsgPort: int
    xyz: LVector3f
    hpr: LVector3f
    fFrustum: bool
    focalLength: float
    filmSize: _Vec2f
    filmOffset: _Vec2f
    def __init__(self, serverConfigName: str, serverName: str, serverDaemonPort: int, serverMsgPort: int) -> None: ...
    def setCamOffset(self, xyz: LVector3f, hpr: LVector3f) -> None: ...
    def setCamFrustum(self, focalLength: float, filmSize: _Vec2f, filmOffset: _Vec2f) -> None: ...

def createClusterClient() -> ClusterClient | ClusterClientSync: ...

class DummyClusterClient(DirectObject):
    notify: ClassVar[Notifier]
    def __init__(self) -> None: ...
    def __call__(self, commandString: str | bytes | CodeType, fLocally: bool = True, serverList: object = None) -> None: ...
