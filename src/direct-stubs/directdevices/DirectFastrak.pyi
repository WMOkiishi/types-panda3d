from collections.abc import Callable
from typing import ClassVar, Final, Literal
from typing_extensions import TypeAlias

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import LVector3f

from .DirectDeviceManager import DirectTracker

_TaskCont: TypeAlias = Literal[1]

NULL_AXIS: Final = -1
FAST_X: Final = 0
FAST_Y: Final = 1
FAST_Z: Final = 2

class DirectFastrak(DirectObject):
    fastrakCount: ClassVar[int]
    notify: ClassVar[Notifier]
    name: str
    deviceNo: int
    device: str
    tracker: DirectTracker
    trackerPos: LVector3f | None
    updateFunc: Callable[[], object]
    def __init__(self, device: str = 'Tracker0', nodePath: Unused = None): ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def updateTask(self, state: Unused) -> _TaskCont: ...
    def fastrakUpdate(self) -> None: ...
