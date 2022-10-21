__all__ = ['DirectRadioButton']

from collections.abc import Iterable
from typing import Any

from panda3d.core import LColor, NodePath
from .DirectButton import DirectButton
from .DirectLabel import DirectLabel

class DirectRadioButton(DirectButton):
    colors: list[LColor] | None
    indicator: DirectLabel
    def __init__(self, parent: NodePath | None = ..., **kw: Any) -> None: ...
    def check(self) -> None: ...
    def setOthers(self, others: Iterable[DirectRadioButton]) -> None: ...
    def uncheck(self) -> None: ...
    def setIndicatorValue(self) -> None: ...
