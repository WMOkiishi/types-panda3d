__all__ = ['DirectWaitBar']

from collections.abc import Callable
from typing import Literal
from typing_extensions import TypeAlias, Unpack

from panda3d._typing import Vec2Like, Vec4Like
from panda3d.core import NodePath, PGFrameStyle, PGWaitBar, Texture

from ._typing import FrameKeywords
from .DirectFrame import DirectFrame

_PGFrameStyle_Type: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]

class DirectWaitBar(DirectFrame[PGWaitBar]):
    barStyle: PGFrameStyle
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], PGWaitBar] = ...,
        range: float = 100,
        value: float = 0,
        barBorderWidth: Vec2Like = (0, 0),
        barColor: Vec4Like = (1, 0, 0, 1),
        barTexture: Texture | str | None = None,
        barRelief: _PGFrameStyle_Type = ...,
        text_pos: Vec2Like = (0, -0.025),
        text_scale: float = 0.1,
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def setRange(self) -> None: ...
    def setValue(self) -> None: ...
    def getPercent(self) -> float: ...
    def updateBarStyle(self) -> None: ...
    def setBarRelief(self) -> None: ...
    def setBarBorderWidth(self) -> None: ...
    def setBarColor(self) -> None: ...
    def setBarTexture(self) -> None: ...
    def update(self, value: float) -> None: ...
    def finish(self, N: float = 10) -> None: ...
