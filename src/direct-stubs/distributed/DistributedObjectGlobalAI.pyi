from typing_extensions import Literal

from .DistributedObjectAI import DistributedObjectAI

class DistributedObjectGlobalAI(DistributedObjectAI):
    doNotDeallocateChannel: bool
    isGlobalDistObj: bool
    def announceGenerate(self) -> Literal[False]: ...
