from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Sequence
from typing import Any
from typing_extensions import Final, Literal, Never, TypeAlias

from direct._typing import Unused
from direct.distributed.CachedDOData import CachedDOData
from panda3d.core import DatagramIterator
from panda3d.direct import DCClass

from .DistributedObjectBase import DistributedObjectBase
from .DoInterestManager import InterestHandle

_State: TypeAlias = Literal[1, 2, 3, 4, 5, 6]

ESNew: Final = 1
ESDeleted: Final = 2
ESDisabling: Final = 3
ESDisabled: Final = 4
ESGenerating: Final = 5
ESGenerated: Final = 6
ESNum2Str: Final[dict[_State, str]]

class DistributedObject(DistributedObjectBase):
    neverDisable: bool
    DistributedObject_initialized: Literal[1]
    activeState: _State
    cacheable: bool
    def getAutoInterests(self) -> list[int]: ...
    def setNeverDisable(self, bool: bool) -> None: ...
    def getNeverDisable(self) -> bool: ...
    def setCachedData(self, name: str, data: CachedDOData) -> None: ...
    def hasCachedData(self, name: str) -> bool: ...
    def getCachedData(self, name: str): ...
    def flushCachedData(self, name: str) -> None: ...
    def setCacheable(self, bool: bool) -> None: ...
    def getCacheable(self) -> bool: ...
    def deleteOrDelay(self) -> None: ...
    def disableAnnounceAndDelete(self) -> None: ...
    def getDelayDeleteCount(self) -> int: ...
    def getDelayDeleteEvent(self) -> str: ...
    def getDisableEvent(self) -> str: ...
    def disableAndAnnounce(self) -> None: ...
    def announceGenerate(self) -> None: ...
    def disable(self) -> None: ...
    def isDisabled(self) -> bool: ...
    def isGenerated(self) -> bool: ...
    def generate(self) -> None: ...
    def generateInit(self) -> None: ...
    def getDoId(self) -> int: ...
    def postGenerateMessage(self) -> None: ...
    def updateRequiredFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateAllRequiredFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateRequiredOtherFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def sendUpdate(self, fieldName: str, args=[], sendToId: int | None = None) -> None: ...
    def sendDisableMsg(self) -> None: ...
    def sendDeleteMsg(self) -> None: ...
    def taskName(self, taskString: object) -> str: ...
    def uniqueName(self, idString: object) -> str: ...
    def getCallbackContext(self, callback: Callable[..., object], extraArgs: Sequence[Any] = []) -> int: ...
    def getCurrentContexts(self) -> list[int]: ...
    def getCallback(self, context: int) -> Callable[..., object]: ...
    def getCallbackArgs(self, context: int) -> Sequence[Any]: ...
    def doCallbackContext(self, context: int, args: Sequence[Any]) -> None: ...
    def setBarrierData(self, data: Iterable[tuple[Incomplete, Incomplete, Incomplete]]) -> None: ...
    def getBarrierData(self) -> tuple[tuple[int, str, list[Never]]]: ...
    def doneBarrier(self, name: str | None = None) -> None: ...
    def addInterest(self, zoneId: int, note: str = '', event: str | None = None) -> InterestHandle | None: ...
    def removeInterest(self, handle: InterestHandle, event: str | None = None) -> bool: ...
    def b_setLocation(self, parentId: int, zoneId: int) -> None: ...
    def d_setLocation(self, parentId: int, zoneId: int) -> None: ...
    def setLocation(self, parentId: int | None, zoneId: int | None) -> None: ...
    def isLocal(self) -> bool: ...
    def isGridParent(self) -> bool: ...
    def execCommand(self, string: Unused, mwMgrId: Unused, avId: Unused, zoneId: Unused) -> None: ...
