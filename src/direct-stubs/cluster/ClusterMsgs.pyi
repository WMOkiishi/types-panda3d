from typing import Final, Literal
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import Datagram, DatagramIterator, LVecBase2f, NetDatagram, QueuedConnectionReader

_NamedMovement: TypeAlias = tuple[
    str, float, float, float, float, float, float, float, float, float, float, float, float, float, bool
]

CLUSTER_NONE: Final = 0
CLUSTER_CAM_OFFSET: Final = 1
CLUSTER_CAM_FRUSTUM: Final = 2
CLUSTER_CAM_MOVEMENT: Final = 3
CLUSTER_SWAP_READY: Final = 4
CLUSTER_SWAP_NOW: Final = 5
CLUSTER_COMMAND_STRING: Final = 6
CLUSTER_SELECTED_MOVEMENT: Final = 7
CLUSTER_TIME_DATA: Final = 8
CLUSTER_NAMED_OBJECT_MOVEMENT: Final = 9
CLUSTER_NAMED_MOVEMENT_DONE: Final = 10
CLUSTER_EXIT: Final = 100
CLUSTER_DAEMON_PORT: int
CLUSTER_SERVER_PORT: int
SERVER_STARTUP_STRING: str

class ClusterMsgHandler:
    packetNumber: int
    notify: Notifier
    def __init__(self, packetStart: int, notify: Notifier) -> None: ...
    def nonBlockingRead(
        self, qcr: QueuedConnectionReader
    ) -> tuple[NetDatagram, PyDatagramIterator, str] | tuple[NetDatagram | None, None, Literal[0]]: ...
    def blockingRead(
        self, qcr: QueuedConnectionReader
    ) -> tuple[NetDatagram, PyDatagramIterator, str] | tuple[NetDatagram, None, Literal[0]]: ...
    def readHeader(self, datagram: Datagram | DatagramIterator) -> tuple[PyDatagramIterator, str]: ...
    def makeCamOffsetDatagram(self, xyz: Vec3Like, hpr: Vec3Like) -> PyDatagram: ...
    def parseCamOffsetDatagram(self, dgi: DatagramIterator) -> tuple[float, float, float, float, float, float]: ...
    def makeCamFrustumDatagram(self, focalLength: float, filmSize: LVecBase2f, filmOffset: LVecBase2f) -> PyDatagram: ...
    def parseCamFrustumDatagram(self, dgi: DatagramIterator) -> tuple[float, tuple[float, float], tuple[float, float]]: ...
    def makeCamMovementDatagram(self, xyz: Vec3Like, hpr: Vec3Like) -> PyDatagram: ...
    def makeNamedMovementDone(self) -> PyDatagram: ...
    def makeNamedObjectMovementDatagram(
        self, xyz: Vec3Like, hpr: Vec3Like, scale: Vec3Like, color: Vec4Like, hidden: bool, name: str
    ) -> PyDatagram: ...
    def parseCamMovementDatagram(self, dgi: DatagramIterator) -> tuple[float, float, float, float, float, float]: ...
    def parseNamedMovementDatagram(self, dgi: DatagramIterator) -> _NamedMovement: ...
    def makeSelectedMovementDatagram(self, xyz: Vec3Like, hpr: Vec3Like, scale: Vec3Like) -> PyDatagram: ...
    def parseSelectedMovementDatagram(
        self, dgi: DatagramIterator
    ) -> tuple[float, float, float, float, float, float, float, float, float]: ...
    def makeCommandStringDatagram(self, commandString: str) -> PyDatagram: ...
    def parseCommandStringDatagram(self, dgi: DatagramIterator) -> str: ...
    def makeSwapNowDatagram(self) -> PyDatagram: ...
    def makeSwapReadyDatagram(self) -> PyDatagram: ...
    def makeExitDatagram(self) -> PyDatagram: ...
    def makeTimeDataDatagram(self, frameCount: int, frameTime: float, dt: float) -> PyDatagram: ...
    def parseTimeDataDatagram(self, dgi: DatagramIterator) -> tuple[int, float, float]: ...
