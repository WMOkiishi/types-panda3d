__all__ = ['Factory']

from typing import Any, ClassVar
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier

_Unused: TypeAlias = object

class Factory:
    notify: ClassVar[Notifier]
    def __init__(self) -> None: ...
    def create(self, type: type, *args: Any, **kwArgs: Any) -> Any: ...
    def nullCtor(self, *args: _Unused, **kwArgs: _Unused) -> None: ...
