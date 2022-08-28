from typing import ClassVar
from typing_extensions import Literal

from ..directnotify.Notifier import Notifier
from .ClientRepository import ClientRepository
from .DistributedObjectAI import DistributedObjectAI

class DistributedObjectGlobalAI(DistributedObjectAI):
    notify: ClassVar[Notifier]
    doNotDeallocateChannel: bool
    isGlobalDistObj: bool
    def __init__(self, air: ClientRepository) -> None: ...
    def announceGenerate(self) -> Literal[False]: ...
    def delete(self) -> None: ...
