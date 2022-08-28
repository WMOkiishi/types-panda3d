from typing import ClassVar
from typing_extensions import Literal

from panda3d.core import DatagramIterator
from panda3d.direct import DCClass
from .ClientRepository import ClientRepository
from .DistributedObjectBase import DistributedObjectBase

class DistributedObjectAI(DistributedObjectBase):
    QuietZone: ClassVar[bool]
    DistributedObjectAI_initialized: Literal[1]
    accountName: str
    air: ClientRepository
    lastNonQuietZone = ...
    def __init__(self, air: ClientRepository) -> None: ...
    def getDeleteEvent(self) -> str | None: ...
    def sendDeleteEvent(self) -> None: ...
    def getCacheable(self) -> Literal[False]: ...
    def deleteOrDelay(self) -> None: ...
    def getDelayDeleteCount(self) -> Literal[0]: ...
    def delete(self) -> None: ...
    def isDeleted(self) -> bool: ...
    def isGenerated(self) -> bool: ...
    def getDoId(self) -> int: ...
    def preAllocateDoId(self) -> None: ...
    def announceGenerate(self) -> Literal[False, None]: ...
    def b_setLocation(self, parentId: int, zoneId: int) -> None: ...
    def d_setLocation(self, parentId: int, zoneId: int) -> None: ...
    def setLocation(self, parentId: int, zoneId: int) -> None: ...
    def getLocation(self) -> tuple[int | None, int | None] | None: ...
    def postGenerateMessage(self) -> None: ...
    def updateRequiredFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateAllRequiredFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateRequiredOtherFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def updateAllRequiredOtherFields(self, dclass: DCClass, di: DatagramIterator) -> None: ...
    def startMessageBundle(self, name) -> None: ...
    def sendMessageBundle(self) -> None: ...
    def getZoneChangeEvent(self) -> str: ...
    def getLogicalZoneChangeEvent(self) -> str: ...
    @staticmethod
    def staticGetZoneChangeEvent(doId: object) -> str: ...
    @staticmethod
    def staticGetLogicalZoneChangeEvent(doId: object) -> str: ...
    def handleLogicalZoneChange(self, newZoneId, oldZoneId) -> None: ...
    def getZoneData(self): ...
    def releaseZoneData(self) -> None: ...
    def getRender(self): ...
    def getNonCollidableParent(self): ...
    def getParentMgr(self): ...
    def getCollTrav(self, *args, **kArgs): ...
    def sendUpdate(self, fieldName, args=...) -> None: ...
    def GetPuppetConnectionChannel(self, doId: int) -> None: ...
    def GetAccountConnectionChannel(self, doId: int) -> None: ...
    def GetAccountIDFromChannelCode(self, channel: int) -> None: ...
    def GetAvatarIDFromChannelCode(self, channel: int) -> None: ...
    def sendUpdateToAvatarId(self, avId, fieldName, args) -> None: ...
    def sendUpdateToAccountId(self, accountId, fieldName, args) -> None: ...
    def sendUpdateToChannel(self, channelId, fieldName, args) -> None: ...
    def generateWithRequired(self, zoneId, optionalFields=...) -> None: ...
    def generateWithRequiredAndId(self, doId, parentId, zoneId, optionalFields=...) -> None: ...
    def generateOtpObject(self, parentId, zoneId, optionalFields=..., opId=None) -> None: ...
    def generate(self) -> None: ...
    def generateInit(self, repository=None) -> None: ...
    def generateTargetChannel(self, repository): ...
    def sendGenerateWithRequired(self, repository, parentId, zoneId, optionalFields=...) -> None: ...
    def initFromServerResponse(self, valDict) -> None: ...
    def requestDelete(self) -> None: ...
    def taskName(self, taskString): ...
    def uniqueName(self, idString): ...
    def validate(self, avId, bool, msg): ...
    def beginBarrier(self, name, avIds, timeout, callback): ...
    def getBarrierData(self) -> list[tuple]: ...
    def ignoreBarrier(self, context) -> None: ...
    def setBarrierReady(self, context) -> None: ...
    def isGridParent(self) -> bool: ...
    def execCommand(self, string, mwMgrId, avId, zoneId) -> None: ...
    def setAI(self, aiChannel) -> None: ...
