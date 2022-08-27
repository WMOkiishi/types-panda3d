from collections.abc import Iterable
from os import PathLike
from typing import ClassVar

from panda3d.core import DatagramIterator, UniqueIdAllocator
from ..directnotify.Notifier import Notifier
from .ClientRepositoryBase import ClientRepositoryBase
from .DistributedObject import DistributedObject

class ClientRepository(ClientRepositoryBase):
    notify: ClassVar[Notifier]
    GameGlobalsId: int
    doNotDeallocateChannel: bool
    doIdAllocator: UniqueIdAllocator | None
    doIdBase: int
    doIdLast: int
    currentSenderId: int | None
    interestZones: list
    ourChannel: int
    def __init__(
        self,
        dcFileNames: str | Iterable[str | bytes | PathLike] | None = None,
        dcSuffix: str = '',
        connectMethod: int | None = None,
        threadedNet: bool | None = None,
    ) -> None: ...
    def handleSetDoIdrange(self, di: DatagramIterator) -> None: ...
    def createReady(self) -> None: ...
    def handleRequestGenerates(self, di: DatagramIterator) -> None: ...
    def resendGenerate(self, obj) -> None: ...
    def handleGenerate(self, di: DatagramIterator) -> None: ...
    def allocateDoId(self) -> int: ...
    def reserveDoId(self, doId: int) -> int: ...
    def freeDoId(self, doId: int) -> None: ...
    def storeObjectLocation(self, object: DistributedObject, parentId: int, zoneId: int) -> None: ...
    def createDistributedObject(
        self,
        className=None,
        distObj=None,
        zoneId: int = 0,
        optionalFields=None,
        doId=None,
        reserveDoId: bool = False,
    ): ...
    def formatGenerate(self, distObj, extraFields): ...
    def sendDeleteMsg(self, doId) -> None: ...
    def sendDisconnect(self) -> None: ...
    def setInterestZones(self, interestZoneIds) -> None: ...
    def setObjectZone(self, distObj, zoneId: int) -> None: ...
    def sendSetLocation(self, doId: int, parentId: int, zoneId: int) -> None: ...
    def sendHeartbeat(self) -> None: ...
    def isLocalId(self, id: int) -> bool: ...
    def haveCreateAuthority(self) -> bool: ...
    def getAvatarIdFromSender(self) -> int | None: ...
    def handleDatagram(self, di: DatagramIterator) -> None: ...
    def handleMessageType(self, msgType, di: DatagramIterator) -> None: ...
    def handleUpdateField(self, di: DatagramIterator) -> None: ...
    def handleDisable(self, di: DatagramIterator) -> None: ...
    def handleDelete(self, di: DatagramIterator) -> None: ...
    def deleteObject(self, doId: int) -> None: ...
    def stopTrackRequestDeletedDO(self, *args: object) -> None: ...
    def sendUpdate(self, distObj, fieldName, args) -> None: ...
    def sendUpdateToChannel(self, distObj, channelId, fieldName, args) -> None: ...
