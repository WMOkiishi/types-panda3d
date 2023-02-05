__all__ = ['DirectLabel']

from typing import Any

from panda3d.core import NodePath

from .DirectFrame import DirectFrame

class DirectLabel(DirectFrame):
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setActiveState(self) -> None: ...
