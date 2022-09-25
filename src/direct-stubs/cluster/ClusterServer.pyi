from typing import Any, ClassVar, Union
from typing_extensions import Literal, TypeAlias

from panda3d.core import (
    Camera,
    Connection,
    ConnectionWriter,
    DatagramIterator,
    LMatrix3f,
    LVecBase3f,
    LVector3f,
    Lens,
    NodePath,
    QueuedConnectionManager,
    QueuedConnectionListener,
    QueuedConnectionReader,
)
from ..directnotify.Notifier import Notifier
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
_TaskCont: TypeAlias = Literal[1]
_Unused: TypeAlias = object
_Vec3f: TypeAlias = Union[LVecBase3f, LMatrix3f.Row, LMatrix3f.CRow, tuple[float, float, float]]

class ClusterServer(DirectObject):
    notify: ClassVar[Notifier]
    MSG_NUM: ClassVar[int]
    cameraJig: NodePath
    camera: NodePath[Camera]
    lens: Lens
    lastConnection: Connection | None
    fPosReceived: bool
    qcm: QueuedConnectionManager
    qcl: QueuedConnectionListener
    qcr: QueuedConnectionReader
    cw: ConnectionWriter
    tcpRendezvous: Connection
    msgHandler: ClusterMsgHandler
    daemon: Any
    objectMappings: dict[str, NodePath]
    objectHasColor: dict[str, bool]
    controlMappings: dict[str, str]
    controlPriorities: dict[str, int]
    controlOffsets: dict[str, LVector3f]
    messageQueue: list[_NamedMovement]
    sortedControlMappings: list[tuple[int, str]]
    def __init__(self, cameraJig: NodePath, camera: NodePath[Camera]) -> None: ...
    def startListenerPollTask(self) -> None: ...
    def listenerPollTask(self, task: _Unused) -> _TaskCont: ...
    def addNamedObjectMapping(self, object: NodePath, name: str, hasColor: bool = True, priority: _Unused = 0) -> None: ...
    def removeObjectMapping(self, name: str) -> None: ...
    def redoSortedPriorities(self) -> None: ...
    def addControlMapping(
        self,
        objectName: str,
        controlledName: str,
        offset: LVector3f | None = None,
        priority: int = 0,
    ) -> None: ...
    def setControlMappingOffset(self, objectName: str, offset: LVector3f) -> None: ...
    def removeControlMapping(self, name: str) -> None: ...
    def startControlObjectTask(self) -> None: ...
    def controlObjectTask(self, task: _Unused) -> _TaskCont: ...
    def sendNamedMovementDone(self) -> None: ...
    def moveObject(self, nodePath: NodePath, object: str, offset: _Vec3f, hasColor: bool) -> None: ...
    def startReaderPollTask(self) -> None: ...
    def startSwapCoordinator(self) -> None: ...
    def swapCoordinatorTask(self, task: _Unused) -> _TaskCont: ...
    def sendSwapReady(self) -> None: ...
    def handleDatagram(self, dgi: DatagramIterator, type: int) -> int: ...
    def handleCamOffset(self, dgi: DatagramIterator) -> None: ...
    def handleCamFrustum(self, dgi: DatagramIterator) -> None: ...
    def handleNamedMovement(self, data: _NamedMovement) -> None: ...
    def handleMessageQueue(self) -> None: ...
    def handleCamMovement(self, dgi: DatagramIterator) -> None: ...
    def handleSelectedMovement(self, dgi: DatagramIterator) -> None: ...
    def handleTimeData(self, dgi: DatagramIterator) -> None: ...
    def handleCommandString(self, dgi: DatagramIterator) -> None: ...
