__all__ = ['AngleDial', 'Dial', 'DialWidget']

from typing_extensions import Final, Literal

import Pmw  # type: ignore[import-untyped]

from .Valuator import Valuator

TWO_PI: Final[float]
ONEPOINTFIVE_PI: Final[float]
POINTFIVE_PI: Final[float]
INNER_SF: Final = 0.2
DIAL_FULL_SIZE: Final = 45
DIAL_MINI_SIZE: Final = 30

class Dial(Valuator):
    def setBase(self) -> None: ...
    def setDelta(self) -> None: ...
    def setSnap(self) -> None: ...
    def setRollover(self) -> None: ...

class AngleDial(Dial): ...

class DialWidget(Pmw.MegaWidget):
    value: float
    def __init__(self, parent=None, **kw) -> None: ...
    def set(self, value: float, fCommand: bool = ...) -> None: ...
    def get(self) -> float: ...
    def mouseDown(self, event) -> None: ...
    def mouseUp(self, event) -> None: ...
    def shiftMouseMotion(self, event) -> None: ...
    def mouseMotion(self, event, fShift: bool = ...) -> None: ...
    def computeDialAngle(self, event, fShift: bool = ...) -> float: ...
    def computeValueFromAngle(self, dialAngle: float) -> None: ...
    def updateIndicator(self, value: float) -> None: ...
    def updateIndicatorDegrees(self, degAngle: float) -> None: ...
    def updateIndicatorRadians(self, dialAngle: float) -> None: ...
    def knobMouseDown(self, event) -> None: ...
    def updateDialTask(self, state) -> Literal[1]: ...
    def updateDialSF(self, event) -> Literal[0] | None: ...
    def knobMouseUp(self, event) -> None: ...
    def setNumDigits(self) -> None: ...
    def setRelief(self) -> None: ...
    def setBorderwidth(self) -> None: ...
    def setBackground(self) -> None: ...
    def setNumSegments(self) -> None: ...
    def highlightKnob(self, event) -> None: ...
    def restoreKnob(self, event) -> None: ...
