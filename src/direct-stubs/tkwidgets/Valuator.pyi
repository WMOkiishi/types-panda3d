__all__ = ['Valuator', 'ValuatorGroup', 'ValuatorGroupPanel']

from typing import Any, ClassVar
from typing_extensions import Final, Literal

import Pmw  # type: ignore[import]

VALUATOR_MINI: Final[Literal['mini']]
VALUATOR_FULL: Final[Literal['full']]

class Valuator(Pmw.MegaWidget):
    sfBase: ClassVar[float]
    sfDist: ClassVar[int]
    deadband: ClassVar[int]
    adjustedValue = ...
    propertyList: list[str]
    fInit: bool
    entryFormat: str
    def __init__(self, parent=None, **kw: Any) -> None: ...
    def set(self, value, fCommand: bool = True) -> None: ...
    def get(self): ...
    def setEntry(self, value, fCommand: bool = True) -> None: ...
    def setEntryFormat(self) -> None: ...
    def validateEntryInput(self, event) -> None: ...
    def setState(self) -> None: ...
    def setLabel(self) -> None: ...
    def zero(self) -> None: ...
    def reset(self) -> None: ...
    def mouseReset(self, event) -> None: ...
    def addPropertyToDialog(self, property, pDict) -> None: ...
    def createValuator(self) -> None: ...
    def packValuator(self) -> None: ...
    def addValuatorMenuEntries(self) -> None: ...
    def addValuatorPropertiesToDialog(self) -> None: ...

FLOATER: Final[Literal['floater']]
DIAL: Final[Literal['dial']]
ANGLEDIAL: Final[Literal['angledial']]
SLIDER: Final[Literal['slider']]

class ValuatorGroup(Pmw.MegaWidget):
    def __init__(self, parent=None, **kw) -> None: ...
    def set(self, value, fCommand: bool = True) -> None: ...
    def setAt(self, index: int, value) -> None: ...
    def get(self): ...
    def getAt(self, index: int): ...
    def __len__(self) -> int: ...

class ValuatorGroupPanel(Pmw.MegaToplevel):
    def __init__(self, parent=None, **kw) -> None: ...
    def toggleBalloon(self) -> None: ...
    def reset(self) -> None: ...
    def set(this, value, fCommand: bool = True) -> None: ...
    def setAt(this, index: int, value) -> None: ...
    def get(this): ...
    def getAt(this, index: int): ...
    def grid_configure(this, *args, **kw): ...
    def grid_forget(this, *args, **kw): ...
    def grid_info(this, *args, **kw): ...
    def grid_remove(this, *args, **kw): ...
    def info(this, *args, **kw): ...
    def location(this, *args, **kw): ...
    def pack(this, *args, **kw): ...
    def pack_configure(this, *args, **kw): ...
    def pack_forget(this, *args, **kw): ...
    def pack_info(this, *args, **kw): ...
    def place(this, *args, **kw): ...
    def place_configure(this, *args, **kw): ...
    def place_forget(this, *args, **kw): ...
    def place_info(this, *args, **kw): ...

def rgbPanel(nodePath, callback=None, style: Literal['mini', 'full'] = ...) -> ValuatorGroupPanel: ...
def lightRGBPanel(light, style: Literal['mini', 'full'] = ...) -> ValuatorGroupPanel: ...
