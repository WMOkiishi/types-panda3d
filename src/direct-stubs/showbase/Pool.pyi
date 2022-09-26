__all__ = ['Pool']

from collections.abc import Callable
from typing import Any, ClassVar, Generic, TypeVar

from direct.directnotify.Notifier import Notifier

_T = TypeVar('_T')

class Pool(Generic[_T]):
    notify: ClassVar[Notifier]
    def __init__(self, free: list[_T] | None = None) -> None: ...
    def add(self, item: _T) -> None: ...
    def remove(self, item: _T) -> None: ...
    def checkout(self) -> _T: ...
    def checkin(self, item: _T) -> None: ...
    def reset(self) -> None: ...
    def hasFree(self) -> bool: ...
    def isFree(self, item: object) -> bool: ...
    def isUsed(self, item: object) -> bool: ...
    def getNumItems(self) -> tuple[int, int]: ...
    def cleanup(self, cleanupFunc: Callable[[Any], object] | None = None) -> None: ...
