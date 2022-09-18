__all__ = ['BulletinBoard']

from typing import Any, ClassVar, TypeVar, overload

from ..directnotify.Notifier import Notifier

_T = TypeVar('_T')

class BulletinBoard:
    notify: ClassVar[Notifier]
    def __init__(self) -> None: ...
    @overload
    def get(self, postName: str) -> Any | None: ...
    @overload
    def get(self, postName: str, default: _T) -> Any | _T: ...
    def has(self, postName: str) -> bool: ...
    def getEvent(self, postName: str) -> str: ...
    def getRemoveEvent(self, postName: str) -> str: ...
    def post(self, postName: str, value: Any = None) -> None: ...
    def update(self, postName: str, value: Any) -> None: ...
    def remove(self, postName: str) -> None: ...
    def removeIfEqual(self, postName: str, value: Any) -> None: ...