from _typeshed import Unused
from types import CodeType
from typing import Any, Literal

from .DistributedObjectUD import DistributedObjectUD

class DistributedObjectGlobalUD(DistributedObjectUD):
    doNotDeallocateChannel: bool
    isGlobalDistObj: bool
    ExecNamespace: dict[str, Any]
    def announceGenerate(self) -> Literal[False]: ...
    def execCommand(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, command: str | bytes | CodeType, mwMgrId: Unused, avId: Unused, zoneId: Unused
    ) -> None: ...
