__all__ = ['AnimControlInterval']

from typing import ClassVar

from panda3d.core import AnimControlCollection
from ..directnotify.Notifier import Notifier
from .Interval import Interval

class AnimControlInterval(Interval):
    notify: ClassVar[Notifier]
    animNum: ClassVar[int]
    controls: AnimControlCollection
    loopAnim: bool
    constrainedLoop: bool
    playRate: float
    frameRate: float
    startFrame: int
    endFrame: int
    reverse: bool
    numFrames: int
    implicitDuration: bool
    def __init__(
        self,
        controls,
        loop = 0,
        contstrainedLoop = 0,
        duration: float | None = None,
        startTime = None,
        endTime = None,
        startFrame: int | None = None,
        endFrame: int | None = None,
        playRate: float = 1,
        name: str | None = None
    ) -> None: ...
    def getCurrentFrame(self): ...
    def privStep(self, t: float) -> None: ...
    def privFinalize(self) -> None: ...
