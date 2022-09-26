__all__ = ['BulletinBoardWatcher']

from collections.abc import Callable
from typing import ClassVar

from ..directnotify.Notifier import Notifier
from .DirectObject import DirectObject

class BulletinBoardWatcher(DirectObject):
    notify: ClassVar[Notifier]
    name: str
    postNames: list[str]
    removeNames: list[str]
    callback: Callable[[], object]
    waitingOn: set[str]
    def __init__(
        self,
        name: str,
        postNames: str | list[str] | tuple[str, ...],
        callback: Callable[[], object],
        removeNames: str | list[str] | tuple[str, ...] | None = None,
    ) -> None: ...
    def destroy(self) -> None: ...
    def isDone(self) -> bool: ...
