from typing_extensions import Literal

from .ClientRepository import ClientRepository
from .DistributedObjectAI import DistributedObjectAI

class DistributedObjectGlobalAI(DistributedObjectAI):
    doNotDeallocateChannel: bool
    isGlobalDistObj: bool
    def __init__(self, air: ClientRepository) -> None: ...
    def announceGenerate(self) -> Literal[False]: ...
    def delete(self) -> None: ...
