from collections.abc import Callable
from typing import ClassVar
from typing_extensions import Final, Literal, TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import LVector3f
from .DirectDeviceManager import DirectTracker

_Unused: TypeAlias = object
_TaskCont: TypeAlias = Literal[1]

NULL_AXIS: Final[Literal[-1]]
FAST_X: Final[Literal[0]]
FAST_Y: Final[Literal[1]]
FAST_Z: Final[Literal[2]]

class DirectFastrak(DirectObject):
    fastrakCount: ClassVar[int]
    notify: ClassVar[Notifier]
    name: str
    deviceNo: int
    device: str
    tracker: DirectTracker
    trackerPos: LVector3f | None
    updateFunc: Callable[[], object]
    def __init__(self, device: str = ..., nodePath: _Unused = ...): ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def updateTask(self, state: _Unused) -> _TaskCont: ...
    def fastrakUpdate(self) -> None: ...
