from typing import ClassVar
from typing_extensions import Final, Literal

from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject
from .DirectDeviceManager import DirectAnalogs

RAD_PAN: Final[Literal[0]]
RAD_TILT: Final[Literal[1]]
RAD_ZOOM: Final[Literal[2]]
RAD_FOCUS: Final[Literal[3]]

class DirectRadamec(DirectObject):
    radamecCount: ClassVar[int]
    notify: ClassVar[Notifier]
    name: str
    devie: str
    analogs: DirectAnalogs
    numAnalogs: int
    aList: list[float]
    minRange: list[float]
    maxRange: list[float]
    def __init__(self, devie: str = 'Analog0', nodePath: object = None) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def updateTask(self, task: object) -> Literal[1]: ...
    def radamecDebug(self) -> None: ...
    def normalizeChannel(self, chan: int, minVal: float = -1, maxVal: float = 1) -> float: ...
