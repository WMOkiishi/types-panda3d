__all__ = ['DirectCheckButton']

from typing import Any

from panda3d.core import LColor, NodePath

from .DirectButton import DirectButton

class DirectCheckButton(DirectButton):
    colors: LColor | None
    def __init__(self, parent: NodePath | None = ..., **kw: Any) -> None: ...
    def setIndicatorValue(self) -> None: ...
