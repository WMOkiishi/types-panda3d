__all__ = ['DirectOptionMenu']

from _typeshed import Unused
from collections.abc import Sequence
from typing import Literal, overload
from typing_extensions import TypeAlias, Unpack

from panda3d._typing import Vec2Like, Vec3Like, Vec4Like
from panda3d.core import NodePath

from ._typing import ButtonKeywords
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

_TextProperties_Alignment: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class DirectOptionMenu(DirectButton):
    initFrameSize: tuple[float, float, float, float] | None
    popupMarker: DirectFrame
    initPopupMarkerPos: tuple[float, float, float] | None
    popupMenu: DirectFrame | None
    selectedIndex: int | None
    highlightedIndex: int | None
    cancelFrame: DirectFrame
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        items: Sequence[str] = ...,
        initialitem: int | None = None,
        popupMarkerBorder: Vec2Like = (0.1, 0.1),
        popupMarker_pos: Vec3Like | None = None,
        highlightColor: Vec4Like = (0.5, 0.5, 0.5, 1),
        highlightScale: Vec2Like = (1, 1),
        text_align: _TextProperties_Alignment = 0,
        **kw: Unpack[ButtonKeywords],
    ) -> None: ...
    def setItems(self) -> None: ...
    def showPopupMenu(self, event: Unused = None) -> None: ...
    def hidePopupMenu(self, event: Unused = None) -> None: ...
    def selectHighlightedIndex(self, event: Unused = None) -> None: ...
    @overload
    def index(self, index: int) -> int: ...
    @overload
    def index(self, index: object) -> int | None: ...
    def set(self, index: int, fCommand: bool = ...) -> None: ...
    def get(self) -> str: ...
