__all__ = ['DirectScrolledList', 'DirectScrolledListItem']

from typing import Any, ClassVar

from panda3d.core import NodePath
from ..directnotify.Notifier import Notifier
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

class DirectScrolledListItem(DirectButton):
    notify: ClassVar[Notifier]
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def select(self) -> None: ...

class DirectScrolledList(DirectFrame):
    notify: ClassVar[Notifier]
    index: int
    nextItemID: int
    incButton: DirectButton
    decButton: DirectButton
    itemFrame: DirectFrame
    currentSelected: DirectScrolledListItem
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setForceHeight(self) -> None: ...
    def recordMaxHeight(self) -> None: ...
    def setScrollSpeed(self) -> None: ...
    def setNumItemsVisible(self) -> None: ...
    def destroy(self) -> None: ...
    def selectListItem(self, item: DirectScrolledListItem) -> None: ...
    def scrollBy(self, delta: int) -> None: ...
    def getItemIndexForItemID(self, itemID: int) -> int: ...
    def scrollToItemID(self, itemID: int, centered: bool = False) -> None: ...
    def scrollTo(self, index: int, centered: bool = False) -> bool: ...
    def makeAllItems(self) -> None: ...
    def addItem(self, item: DirectScrolledListItem | str, refresh: bool = True): ...
    def removeItem(self, item: DirectScrolledListItem | str, refresh: bool = True) -> bool: ...
    def removeAndDestroyItem(self, item: DirectScrolledListItem, refresh: bool = True) -> bool: ...
    def removeAllItems(self, refresh: bool = True) -> bool: ...
    def removeAndDestroyAllItems(self, refresh: bool = True) -> bool: ...
    def refresh(self) -> None: ...
    def getSelectedIndex(self) -> int: ...
    def getSelectedText(self) -> str: ...
    def setIncButtonCallback(self) -> None: ...
    def setDecButtonCallback(self) -> None: ...
