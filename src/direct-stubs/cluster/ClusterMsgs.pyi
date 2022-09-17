from typing import Union
from typing_extensions import Final, Literal, TypeAlias

from panda3d.core import (
    Datagram,
    DatagramIterator,
    LMatrix3f,
    LMatrix4f,
    LVecBase2f,
    LVecBase3f,
    LVecBase4f,
    NetDatagram,
    QueuedConnectionReader,
    UnalignedLVecBase4f,
)
from ..directnotify.Notifier import Notifier
from ..distributed.PyDatagram import PyDatagram
from ..distributed.PyDatagramIterator import PyDatagramIterator

_NamedMovement: TypeAlias = tuple[
    str,
    float, float, float,
    float, float, float,
    float, float, float,
    float, float, float, float,
    bool,
]
_Vec2f: TypeAlias = Union[LVecBase2f, tuple[float, float]]
_Vec3f: TypeAlias = Union[LVecBase3f, LMatrix3f.Row, LMatrix3f.CRow, tuple[float, float, float]]
_Vec4f: TypeAlias = Union[LVecBase4f, UnalignedLVecBase4f, LMatrix4f.Row, LMatrix4f.CRow, tuple[float, float, float, float]]

CLUSTER_NONE: Final[Literal[0]]
CLUSTER_CAM_OFFSET: Final[Literal[1]]
CLUSTER_CAM_FRUSTUM: Final[Literal[2]]
CLUSTER_CAM_MOVEMENT: Final[Literal[3]]
CLUSTER_SWAP_READY: Final[Literal[4]]
CLUSTER_SWAP_NOW: Final[Literal[5]]
CLUSTER_COMMAND_STRING: Final[Literal[6]]
CLUSTER_SELECTED_MOVEMENT: Final[Literal[7]]
CLUSTER_TIME_DATA: Final[Literal[8]]
CLUSTER_NAMED_OBJECT_MOVEMENT: Final[Literal[9]]
CLUSTER_NAMED_MOVEMENT_DONE: Final[Literal[10]]
CLUSTER_EXIT: Final[Literal[100]]
CLUSTER_DAEMON_PORT: int
CLUSTER_SERVER_PORT: int
SERVER_STARTUP_STRING: str

class ClusterMsgHandler:
    packetNumber: int
    notify: Notifier
    def __init__(self, packetStart: int, notify: Notifier) -> None: ...
    def nonBlockingRead(
        self,
        qcr: QueuedConnectionReader,
    ) -> tuple[NetDatagram, PyDatagramIterator, str] | tuple[NetDatagram | None, None, Literal[0]]: ...
    def blockingRead(
        self,
        qcr: QueuedConnectionReader,
    ) -> tuple[NetDatagram, PyDatagramIterator, str] | tuple[NetDatagram, None, Literal[0]]: ...
    def readHeader(self, datagram: Datagram | DatagramIterator) -> tuple[PyDatagramIterator, str]: ...
    def makeCamOffsetDatagram(self, xyz: _Vec3f, hpr: _Vec3f) -> PyDatagram: ...
    def parseCamOffsetDatagram(self, dgi: DatagramIterator) -> tuple[float, float, float, float, float, float]: ...
    def makeCamFrustumDatagram(self, focalLength: float, filmSize: _Vec2f, filmOffset: _Vec2f) -> PyDatagram: ...
    def parseCamFrustumDatagram(self, dgi: DatagramIterator) -> tuple[float, tuple[float, float], tuple[float, float]]: ...
    def makeCamMovementDatagram(self, xyz: _Vec3f, hpr: _Vec3f) -> PyDatagram: ...
    def makeNamedMovementDone(self) -> PyDatagram: ...
    def makeNamedObjectMovementDatagram(
        self,
        xyz: _Vec3f,
        hpr: _Vec3f,
        scale: _Vec3f,
        color: _Vec4f,
        hidden: bool,
        name: str,
    ) -> PyDatagram: ...
    def parseCamMovementDatagram(self, dgi: DatagramIterator) -> tuple[float, float, float, float, float, float]: ...
    def parseNamedMovementDatagram(self, dgi: DatagramIterator) -> _NamedMovement: ...
    def makeSelectedMovementDatagram(self, xyz: _Vec3f, hpr: _Vec3f, scale: _Vec3f) -> PyDatagram: ...
    def parseSelectedMovementDatagram(
        self,
        dgi: DatagramIterator,
    ) -> tuple[float, float, float, float, float, float, float, float, float]: ...
    def makeCommandStringDatagram(self, commandString: str) -> PyDatagram: ...
    def parseCommandStringDatagram(self, dgi: DatagramIterator) -> str: ...
    def makeSwapNowDatagram(self) -> PyDatagram: ...
    def makeSwapReadyDatagram(self) -> PyDatagram: ...
    def makeExitDatagram(self) -> PyDatagram: ...
    def makeTimeDataDatagram(self, frameCount: int, frameTime: float, dt: float) -> PyDatagram: ...
    def parseTimeDataDatagram(self, dgi: DatagramIterator): ...
