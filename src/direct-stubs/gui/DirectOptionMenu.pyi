__all__ = ['DirectOptionMenu']

from typing import Any, overload
from typing_extensions import TypeAlias

from panda3d.core import NodePath
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

_Unused: TypeAlias = object

class DirectOptionMenu(DirectButton):
    initFrameSize: tuple[float, float, float, float] | None
    popupMarker: DirectFrame
    initPopupMarkerPos: tuple[float, float, float] | None
    popupMenu: DirectFrame | None
    selectedIndex: int | None
    highlightedIndex: int | None
    cancelFrame: DirectFrame
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setItems(self) -> None: ...
    def showPopupMenu(self, event: _Unused = None) -> None: ...
    def hidePopupMenu(self, event: _Unused = None) -> None: ...
    def selectHighlightedIndex(self, event: _Unused = None) -> None: ...
    @overload
    def index(self, index: int) -> int: ...
    @overload
    def index(self, index: object) -> int | None: ...
    def set(self, index: int, fCommand: bool = True) -> None: ...
    def get(self) -> Any: ...
