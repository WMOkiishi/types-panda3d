__all__ = ['DirectCheckButton']

from typing import Any

from panda3d.core import LVecBase4f, NodePath
from .DirectButton import DirectButton

class DirectCheckButton(DirectButton):
    colors: LVecBase4f | None
    def __init__(self, parent: NodePath | None, **kw: Any) -> None: ...
    def setIndicatorValue(self) -> None: ...
