from collections.abc import Sequence

from direct._typing import Unused
from panda3d.core import Datagram, DatagramIterator, UniqueIdAllocator

from .ClientRepositoryBase import ClientRepositoryBase
from .DistributedObjectBase import DistributedObjectBase

class ClientRepository(ClientRepositoryBase):
    doNotDeallocateChannel: bool
    doIdAllocator: UniqueIdAllocator | None
    doIdBase: int
    doIdLast: int
    currentSenderId: int | None
    interestZones: list[int]
    ourChannel: int
    def handleSetDoIdrange(self, di: DatagramIterator) -> None: ...
    def createReady(self) -> None: ...
    def handleRequestGenerates(self, di: DatagramIterator) -> None: ...
    def resendGenerate(self, obj: DistributedObjectBase) -> None: ...
    def handleGenerate(self, di: DatagramIterator) -> None: ...
    def allocateDoId(self) -> int: ...
    def reserveDoId(self, doId: int) -> int: ...
    def freeDoId(self, doId: int) -> None: ...
    def storeObjectLocation(self, object: DistributedObjectBase, parentId: int, zoneId: int) -> None: ...  # type: ignore[override]
    def createDistributedObject(
        self,
        className: str | None = ...,
        distObj: DistributedObjectBase | None = ...,
        zoneId: int = ...,
        optionalFields: Sequence[str] | None = ...,
        doId: int | None = ...,
        reserveDoId: bool = ...,
    ) -> DistributedObjectBase: ...
    def formatGenerate(self, distObj: DistributedObjectBase, extraFields: Sequence[str] | None) -> Datagram: ...
    def sendDeleteMsg(self, doId: int) -> None: ...
    def sendDisconnect(self) -> None: ...
    def setInterestZones(self, interestZoneIds: list[int]) -> None: ...
    def setObjectZone(self, distObj: DistributedObjectBase, zoneId: int) -> None: ...
    def sendSetLocation(self, doId: int, parentId: int, zoneId: int) -> None: ...
    def sendHeartbeat(self) -> None: ...
    def isLocalId(self, doId: int) -> bool: ...
    def haveCreateAuthority(self) -> bool: ...
    def getAvatarIdFromSender(self) -> int | None: ...
    def handleMessageType(self, msgType: object, di: DatagramIterator) -> None: ...
    def handleDisable(self, di: DatagramIterator) -> None: ...
    def deleteObject(self, doId: int) -> None: ...
    def stopTrackRequestDeletedDO(self, *args: Unused) -> None: ...
    def sendUpdate(self, distObj: DistributedObjectBase, fieldName: str, args) -> None: ...
    def sendUpdateToChannel(self, distObj: DistributedObjectBase, channelId: int, fieldName: str, args) -> None: ...
