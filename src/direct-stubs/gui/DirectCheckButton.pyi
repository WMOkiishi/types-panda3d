__all__ = ['DirectCheckButton']

from _typeshed import SupportsGetItem
from typing import Any

from panda3d._typing import Vec4Like
from panda3d.core import NodePath

from .DirectButton import DirectButton

class DirectCheckButton(DirectButton):
    colors: SupportsGetItem[int, Vec4Like] | None
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setIndicatorValue(self) -> None: ...
