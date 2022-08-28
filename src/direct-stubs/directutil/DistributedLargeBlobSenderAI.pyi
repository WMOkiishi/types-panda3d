from typing import ClassVar

from ..directnotify.Notifier import Notifier
from ..distributed.ClientRepository import ClientRepository
from ..distributed.DistributedObjectAI import DistributedObjectAI

class DistributedLargeBlobSenderAI(DistributedObjectAI):
    notify: ClassVar[Notifier]
    targetAvId: int
    mode: int
    def __init__(self, air: ClientRepository, zoneId: int, targetAvId: int, data: object, useDisk: bool = False) -> None: ...
    def getMode(self) -> int: ...
    def getTargetAvId(self) -> int: ...
    def setAck(self) -> None: ...
