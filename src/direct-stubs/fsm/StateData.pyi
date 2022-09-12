__all__ = ['StateData']

from typing import Any, ClassVar

from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import  DirectObject

class StateData(DirectObject):
    notify: ClassVar[Notifier]
    doneEvent: Any
    doneStatus: Any
    isLoaded: bool
    isEntered: bool
    def __init__(self, doneEvent: Any) -> None: ...
    def enter(self) -> bool: ...
    def exit(self) -> bool: ...
    def load(self) -> bool: ...
    def unload(self) -> bool: ...
    def getDoneStatus(self) -> Any: ...
