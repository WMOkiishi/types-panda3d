from typing import Any
from typing_extensions import Literal

from .DistributedObjectUD import DistributedObjectUD

class DistributedObjectGlobalUD(DistributedObjectUD):
    doNotDeallocateChannel: bool
    isGlobalDistObj: bool
    ExecNamespace: dict[str, Any]
    def announceGenerate(self) -> Literal[False]: ...
