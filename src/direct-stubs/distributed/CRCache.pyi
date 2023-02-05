from typing import ClassVar

from direct.directnotify.Notifier import Notifier

from .DistributedObject import DistributedObject

class CRCache:
    notify: ClassVar[Notifier]
    maxCacheItems: int
    storedCacheItems: int
    dict: dict[int, DistributedObject]
    fifo: list[DistributedObject]
    def __init__(self, maxCacheItems: int = 10) -> None: ...
    def isEmpty(self) -> int: ...
    def flush(self) -> None: ...
    def cache(self, distObj: DistributedObject) -> bool: ...
    def retrieve(self, doId: int) -> DistributedObject | None: ...
    def contains(self, doId: int) -> bool: ...
    def delete(self, doId: int) -> None: ...
    def checkCache(self) -> bool: ...
    def turnOff(self) -> None: ...
    def turnOn(self) -> None: ...
