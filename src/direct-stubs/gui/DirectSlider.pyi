__all__ = ['DirectSlider']

from typing import Any

from panda3d.core import NodePath

from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

class DirectSlider(DirectFrame):
    thumb: DirectButton
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setRange(self) -> None: ...
    def setValue(self, value: float) -> None: ...
    def getValue(self) -> float: ...
    def getRatio(self) -> float: ...
    def setScrollSize(self) -> None: ...
    def setPageSize(self) -> None: ...
    def setOrientation(self) -> None: ...
    def commandFunc(self) -> None: ...
