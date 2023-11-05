__all__ = ['DirectRadioButton']

from _typeshed import SupportsGetItem
from collections.abc import Iterable
from typing import Any

from panda3d._typing import Vec4Like
from panda3d.core import NodePath

from .DirectButton import DirectButton
from .DirectLabel import DirectLabel

class DirectRadioButton(DirectButton):
    colors: SupportsGetItem[int, Vec4Like] | None
    indicator: DirectLabel
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def check(self) -> None: ...
    def setOthers(self, others: Iterable[DirectRadioButton]) -> None: ...
    def uncheck(self) -> None: ...
    def setIndicatorValue(self) -> None: ...
