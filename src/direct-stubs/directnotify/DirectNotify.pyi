from tkinter import Toplevel
from typing import Any, ClassVar
from typing_extensions import Protocol

from .Logger import Logger
from .Notifier import Notifier

class _SupportsNotify(Protocol):
    __name__: ClassVar[str]
    notify: ClassVar[Notifier]

class DirectNotify:
    logger: Logger
    streamWriter: Any
    def __init__(self) -> None: ...
    def getCategories(self) -> list[str]: ...
    def getCategory(self, categoryName: str) -> Notifier | None: ...
    def newCategory(self, categoryName: str, logger: Logger | None = None) -> Notifier: ...
    def setDconfigLevel(self, categoryName: str) -> None: ...
    def setDconfigLevels(self) -> None: ...
    def setVerbose(self) -> None: ...
    def popupControls(self, tl: Toplevel | None = None) -> None: ...
    def giveNotify(self, cls: type[_SupportsNotify]) -> None: ...
