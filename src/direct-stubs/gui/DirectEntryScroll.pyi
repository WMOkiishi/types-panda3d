__all__ = ['DirectEntryScroll']

from typing import Any

from panda3d.core import NodePath
from .DirectFrame import DirectFrame

class DirectEntryScroll(DirectFrame):
    canvas: NodePath
    visXMin: float
    visXMax: float
    clipXMin: float
    clipXMax: float
    entry: NodePath | None
    def __init__(self, entry: NodePath | None, parent: NodePath | None, **kw: Any) -> None: ...
    def setEntry(self, entry: NodePath) -> None: ...
    def clearEntry(self) -> None: ...
    def cursorMove(self, cursorX: object, cursorY: object) -> None: ...
    def moveToCenterCursor(self) -> None: ...
    def destroy(self) -> None: ...
    def getCanvas(self) -> NodePath: ...
    def setClipSize(self) -> None: ...
    def resetCanvas(self) -> None: ...
