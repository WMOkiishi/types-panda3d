__all__ = ['Factory']

from typing import Any, ClassVar

from ..directnotify.Notifier import Notifier

class Factory:
    notify: ClassVar[Notifier]
    def __init__(self) -> None: ...
    def create(self, type, *args: Any, **kwArgs: Any): ...
    def nullCtor(self, *args: object, **kwArgs: object) -> None: ...
