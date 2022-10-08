from typing import ClassVar
from typing_extensions import Final, Literal, TypeAlias

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from .DirectDeviceManager import DirectAnalogs

_TaskCont: TypeAlias = Literal[1]

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
    def __init__(self, device: str = ..., nodePath: Unused = ...) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def updateTask(self, state: Unused) -> _TaskCont: ...
    def radamecDebug(self) -> None: ...
    def normalizeChannel(self, chan: int, minVal: float = ..., maxVal: float = ...) -> float: ...
