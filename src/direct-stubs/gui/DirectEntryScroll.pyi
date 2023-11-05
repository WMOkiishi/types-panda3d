__all__ = ['DirectEntryScroll']

from _typeshed import Unused
from collections.abc import Callable
from typing import TypeVar
from typing_extensions import Unpack

from panda3d._typing import Vec4Like
from panda3d.core import NodePath, PGVirtualFrame

from ._typing import FrameKeywords
from .DirectFrame import DirectFrame

_PGVirtualFrameT = TypeVar('_PGVirtualFrameT', bound=PGVirtualFrame, default=PGVirtualFrame)

class DirectEntryScroll(DirectFrame[_PGVirtualFrameT]):
    canvas: NodePath
    visXMin: float
    visXMax: float
    clipXMin: float
    clipXMax: float
    entry: NodePath | None
    def __init__(
        self,
        entry: NodePath | None,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], _PGVirtualFrameT] = ...,
        clipSize: Vec4Like = (-1, 1, -1, 1),
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def setEntry(self, entry: NodePath) -> None: ...
    def clearEntry(self) -> None: ...
    def cursorMove(self, cursorX: Unused, cursorY: Unused) -> None: ...
    def moveToCenterCursor(self) -> None: ...
    def getCanvas(self) -> NodePath: ...
    def setClipSize(self) -> None: ...
    def resetCanvas(self) -> None: ...
