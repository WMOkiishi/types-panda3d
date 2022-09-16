__all__ = ['DirectOptionMenu']

from typing import Any, overload

from panda3d.core import NodePath
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

class DirectOptionMenu(DirectButton):
    initFrameSize = ...
    popupMarker: DirectFrame
    initPopupMarkerPos = ...
    popupMenu: DirectFrame | None
    selectedIndex: int | None
    highlightedIndex: int | None
    cancelFrame: DirectFrame
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setItems(self) -> None: ...
    def showPopupMenu(self, event: object = None) -> None: ...
    def hidePopupMenu(self, event: object = None) -> None: ...
    def selectHighlightedIndex(self, event: object = None) -> None: ...
    @overload
    def index(self, index: int) -> int: ...
    @overload
    def index(self, index: object) -> int | None: ...
    def set(self, index, fCommand: bool = True) -> None: ...
    def get(self): ...