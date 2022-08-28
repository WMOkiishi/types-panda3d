from types import CodeType
from typing import Any
from typing_extensions import Literal

from .ClientRepository import ClientRepository
from .DistributedObjectUD import DistributedObjectUD

class DistributedObjectGlobalUD(DistributedObjectUD):
    doNotDeallocateChannel: bool
    isGlobalDistObj: bool
    ExecNamespace: dict[str, Any]
    def __init__(self, air: ClientRepository) -> None: ...
    def announceGenerate(self) -> Literal[False]: ...
    def delete(self) -> None: ...
    def execCommand(self, command: str | bytes | CodeType, mwMgrId: object, avId: object, zoneId: object) -> None: ...
