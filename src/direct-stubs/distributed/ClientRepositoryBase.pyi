from _typeshed import StrOrBytesPath
from collections.abc import Iterable
from typing import Any, TypeVar
from typing_extensions import Literal, TypeAlias

from direct._typing import Unused
from panda3d.core import Datagram, DatagramIterator, NodePath, RecorderController
from panda3d.direct import DCClass

from .ConnectionRepository import ConnectionRepository
from .CRCache import CRCache
from .CRDataCache import CRDataCache
from .DistributedObject import DistributedObject
from .ParentMgr import ParentMgr
from .RelatedObjectMgr import RelatedObjectMgr
from .TimeManager import TimeManager

_D = TypeVar('_D', bound=DistributedObject)
_DeferredInfo: TypeAlias = tuple[
    tuple[int, int | None, int, int, DatagramIterator],
    bool,
    Datagram,
    list[tuple[Datagram, DatagramIterator] | tuple[_MsgType, tuple[Datagram, DatagramIterator]]],
]
_MsgType: TypeAlias = Literal[1, 2, 3, 4]

class ClientRepositoryBase(ConnectionRepository):
    context: int
    deferredGenerates: list[tuple[_MsgType, Any]]
    deferredDoIds: dict[int, _DeferredInfo]
    lastGenerate: int
    noDefer: bool
    recorder: RecorderController
    cache: CRCache
    doDataCache: CRDataCache
    cacheOwner: CRCache
    serverDelta: float
    bootedIndex: int | None
    bootedText: str | None
    parentMgr: ParentMgr
    relatedObjectMgr: RelatedObjectMgr
    timeManager: TimeManager | None
    heartbeatInterval: float
    heartbeatStarted: bool
    lastHeartbeat: int
    specialNameNumber: int
    deferInterval: float
    def __init__(
        self,
        dcFileNames: str | Iterable[StrOrBytesPath] | None = None,
        dcSuffix: str = '',
        connectMethod: int | None = None,
        threadedNet: bool | None = None,
    ) -> None: ...
    def setDeferInterval(self, deferInterval: float) -> None: ...
    def specialName(self, label: object) -> str: ...
    def getTables(self, ownerView: bool) -> tuple[dict[int, DistributedObject], CRCache]: ...
    def allocateContext(self) -> int: ...
    def setServerDelta(self, delta: float) -> None: ...
    def getServerDelta(self) -> float: ...
    def getServerTimeOfDay(self) -> float: ...
    def doGenerate(self, parentId: int, zoneId: int | None, classId: int, doId: int, di: DatagramIterator) -> None: ...
    def flushGenerates(self) -> None: ...
    def replayDeferredGenerate(self, msgType: _MsgType, extra: int) -> None: ...
    def doDeferredGenerate(self, task: Unused) -> Literal[0, 2]: ...
    def generateWithRequiredFields(
        self, dclass: DCClass, doId: int, di: DatagramIterator, parentId: int | None, zoneId: int | None
    ) -> DistributedObject: ...
    def generateWithRequiredOtherFields(
        self, dclass: DCClass, doId: int, di: DatagramIterator, parentId: int | None = None, zoneId: int | None = None
    ) -> DistributedObject: ...
    def generateWithRequiredOtherFieldsOwner(self, dclass: DCClass, doId: int, di: DatagramIterator) -> DistributedObject: ...
    def disableDoId(self, doId: int, ownerView: bool = False) -> None: ...
    def handleDelete(self, di: DatagramIterator) -> None: ...
    def handleUpdateField(self, di: DatagramIterator) -> None: ...
    def handleGoGetLost(self, di: DatagramIterator) -> None: ...
    def handleServerHeartbeat(self, di: DatagramIterator) -> None: ...
    def handleSystemMessage(self, di: DatagramIterator) -> str: ...
    def handleSystemMessageAknowledge(self, di: DatagramIterator) -> str: ...
    def getObjectsOfClass(self, objClass: type[_D]) -> dict[int, _D]: ...
    def getObjectsOfExactClass(self, objClass: type[_D]) -> dict[int, _D]: ...
    def considerHeartbeat(self) -> None: ...
    def stopHeartbeat(self) -> None: ...
    def startHeartbeat(self) -> None: ...
    def sendHeartbeatTask(self, task: Unused) -> Literal[2]: ...
    def waitForNextHeartBeat(self) -> None: ...
    def replaceMethod(self, oldMethod: Unused, newFunction: Unused) -> int: ...
    def getWorld(self, doId: int) -> NodePath | None: ...
    def isLive(self) -> bool: ...
    def isLocalId(self, id: int) -> bool: ...
    def printDelayDeletes(self) -> None: ...
