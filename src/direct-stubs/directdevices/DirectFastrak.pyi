from collections.abc import Callable
from typing import ClassVar
from typing_extensions import Final, Literal

from panda3d.core import LVector3f
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject
from .DirectDeviceManager import DirectTracker

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
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def destroy(self) -> None: ...
    def updateTask(self, state: object) -> Literal[1]: ...
    def fastrakUpdate(self) -> None: ...