from collections.abc import Mapping
from types import CodeType
from typing import Any, ClassVar
from typing_extensions import Literal

from direct._typing import Unused
from panda3d.core import Datagram, DatagramIterator
from panda3d.direct import DCClass

from .ClientRepository import ClientRepository
from .DistributedObjectBase import DistributedObjectBase

class DistributedObjectUD(DistributedObjectBase):
    QuietZone: ClassVar[int]
    DistributedObjectUD_initialized: Literal[1]
    accountName: str
    air: ClientRepository
    lastNonQuietZone: int | None
    def __init__(self, air: ClientRepository) -> None: ...
    def getDeleteEvent(self) -> str | None: ...
    def sendDeleteEvent(self) -> None: ...
    def isDeleted(self) -> bool: ...
    def isGenerated(self) -> bool: ...
    def getDoId(self) -> int: ...
    def preAllocateDoId(self) -> None: ...
    def announceGenerate(self) -> Literal[False, None]: ...
    def postGenerateMessage(self) -> None: ...
    def addInterest(self, zoneId, note: str = '', event: str | None = None) -> None: ...
    def b_setLocation(self, parentId: int, zoneId: int) -> None: ...
    def d_setLocation(self, parentId: int, zoneId: int) -> None: ...
    def setLocation(self, parentId: int | None, zoneId: int | None) -> None: ...
    def updateRequiredFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateAllRequiredFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateRequiredOtherFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateAllRequiredOtherFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def sendSetZone(self, zoneId) -> None: ...
    def getZoneChangeEvent(self): ...
    def getLogicalZoneChangeEvent(self): ...
    def handleLogicalZoneChange(self, newZoneId: int, oldZoneId: int) -> None: ...
    def getRender(self): ...
    def getNonCollidableParent(self): ...
    def getParentMgr(self): ...
    def getCollTrav(self, *args, **kArgs): ...
    def sendUpdate(self, fieldName: str, args=...) -> None: ...
    def GetPuppetConnectionChannel(self, doId: int) -> int: ...
    def GetAccountConnectionChannel(self, doId: int) -> int: ...
    def GetAccountIDFromChannelCode(self, channel: int) -> int: ...
    def GetAvatarIDFromChannelCode(self, channel: int) -> int: ...
    def sendUpdateToAvatarId(self, avId: int, fieldName: str, args) -> None: ...
    def sendUpdateToAccountId(self, accountId: int, fieldName: str, args) -> None: ...
    def sendUpdateToChannel(self, channelId: int, fieldName: str, args) -> None: ...
    def generateWithRequired(self, zoneId: int, optionalFields=...): ...
    def generateWithRequiredAndId(self, doId: int, parentId: int, zoneId: int, optionalFields=...) -> None: ...
    def generateOtpObject(self, parentId: int, zoneId: int, optionalFields=..., doId: Any | None = None) -> None: ...
    def generate(self) -> None: ...
    def generateInit(self, repository: Unused = None) -> None: ...
    def generateTargetChannel(self, repository): ...
    def sendGenerateWithRequired(self, repository, parentId: int, zoneId: int, optionalFields=...) -> None: ...
    def initFromServerResponse(self, valDict: Mapping[str, Datagram | bytes]) -> None: ...
    def requestDelete(self) -> None: ...
    def taskName(self, taskString: object) -> str: ...
    def uniqueName(self, idString: object) -> str: ...
    def validate(self, avId, bool: bool, msg) -> bool: ...
    def beginBarrier(self, name, avIds, timeout, callback): ...
    def ignoreBarrier(self, context) -> None: ...
    def setBarrierReady(self, context) -> None: ...
    def isGridParent(self) -> Literal[False]: ...
    def execCommand(self, string: str | bytes | CodeType, mwMgrId: Unused, avId: Unused, zoneId: Unused) -> None: ...
