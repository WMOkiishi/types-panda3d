from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .ClientRepository import ClientRepository
from .DistributedObjectAI import DistributedObjectAI

class TimeManagerAI(DistributedObjectAI):
    notify: ClassVar[Notifier]
    def __init__(self, air: ClientRepository) -> None: ...
    def requestServerTime(self, context: int) -> None: ...
