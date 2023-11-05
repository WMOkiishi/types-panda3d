__all__ = ['DirectLabel']

from collections.abc import Callable
from typing_extensions import Unpack

from panda3d.core import NodePath

from ._typing import FrameKeywords, PGItemT
from .DirectFrame import DirectFrame

class DirectLabel(DirectFrame[PGItemT]):
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], PGItemT],
        activeState: int = 0,
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def setActiveState(self) -> None: ...
