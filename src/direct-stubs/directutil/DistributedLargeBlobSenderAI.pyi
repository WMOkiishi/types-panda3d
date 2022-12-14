from direct.distributed.ClientRepository import ClientRepository
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedLargeBlobSenderAI(DistributedObjectAI):
    targetAvId: int
    mode: int
    def __init__(self, air: ClientRepository, zoneId: int, targetAvId: int, data: object, useDisk: bool = ...) -> None: ...
    def getMode(self) -> int: ...
    def getTargetAvId(self) -> int: ...
    def setAck(self) -> None: ...
