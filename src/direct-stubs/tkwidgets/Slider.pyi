__all__ = ['Slider', 'SliderWidget', 'rgbPanel']

import Pmw  # type: ignore[import]
from .Valuator import Valuator, rgbPanel as rgbPanel

class Slider(Valuator):
    def setMin(self) -> None: ...
    def setMax(self) -> None: ...

class SliderWidget(Pmw.MegaWidget):
    value: float
    formatString: str
    increment: float
    xPad: int
    left: float
    right: float
    def __init__(self, parent=None, **kw) -> None: ...
    def destroy(self) -> None: ...
    def set(self, value: float, fCommand: bool = True) -> None: ...
    def get(self) -> float: ...
    def updateIndicator(self, value: float) -> None: ...
    def setMin(self) -> None: ...
    def setMax(self) -> None: ...
    def setNumDigits(self) -> None: ...
    def setRelief(self) -> None: ...
    def setBorderwidth(self) -> None: ...
    def setBackground(self) -> None: ...
    def highlightWidget(self, event) -> None: ...
    def restoreWidget(self, event) -> None: ...
