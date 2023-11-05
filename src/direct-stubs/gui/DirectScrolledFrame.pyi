__all__ = ['DirectScrolledFrame']

from collections.abc import Callable
from typing_extensions import Unpack

from panda3d._typing import Vec4Like
from panda3d.core import NodePath, PGScrollFrame

from ._typing import FrameKeywords
from .DirectFrame import DirectFrame
from .DirectScrollBar import DirectScrollBar

class DirectScrolledFrame(DirectFrame[PGScrollFrame]):
    verticalScroll: DirectScrollBar
    horizontalScroll: DirectScrollBar
    canvas: NodePath
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], PGScrollFrame] = ...,
        canvasSize: Vec4Like = (-1, 1, -1, 1),
        manageScrollBars: bool = True,
        autoHideScrollBars: bool = True,
        scrollBarWidth: float = 0.08,
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def setScrollBarWidth(self) -> None: ...
    def setCanvasSize(self) -> None: ...
    def getCanvas(self) -> NodePath: ...
    def setManageScrollBars(self) -> None: ...
    def setAutoHideScrollBars(self) -> None: ...
    def commandFunc(self) -> None: ...
