from typing_extensions import Final, Literal

from panda3d.core import DatagramIterator
from panda3d.direct import DCClass

from .DistributedObjectBase import DistributedObjectBase

ESNew: Final = 1
ESDeleted: Final = 2
ESDisabling: Final = 3
ESDisabled: Final = 4
ESGenerating: Final = 5
ESGenerated: Final = 6

class DistributedObjectOV(DistributedObjectBase):
    DistributedObjectOV_initialized: Literal[1]
    DistributedObjectOV_deleted: Literal[1]
    activeState: Literal[1, 2, 3, 4, 5, 6]
    def getDelayDeleteCount(self) -> Literal[0]: ...
    def deleteOrDelay(self) -> None: ...
    def disableAnnounceAndDelete(self) -> None: ...
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
    def getCacheable(self) -> Literal[False]: ...
    def sendUpdate(self, fieldName: str, args=[], sendToId: int | None = None) -> None: ...
    def uniqueName(self, idString: object) -> str: ...
    def taskName(self, taskString: object) -> str: ...
