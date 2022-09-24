__all__ = ['DirectEntryScroll']

from typing import Any
from typing_extensions import TypeAlias

from panda3d.core import NodePath
from .DirectFrame import DirectFrame

_Unused: TypeAlias = object

class DirectEntryScroll(DirectFrame):
    canvas: NodePath
    visXMin: float
    visXMax: float
    clipXMin: float
    clipXMax: float
    entry: NodePath | None
    def __init__(self, entry: NodePath | None, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setEntry(self, entry: NodePath) -> None: ...
    def clearEntry(self) -> None: ...
    def cursorMove(self, cursorX: _Unused, cursorY: _Unused) -> None: ...
    def moveToCenterCursor(self) -> None: ...
    def getCanvas(self) -> NodePath: ...
    def setClipSize(self) -> None: ...
    def resetCanvas(self) -> None: ...
