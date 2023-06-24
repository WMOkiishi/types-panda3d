__all__ = ['AnimControlInterval']

from typing import ClassVar

from panda3d.core import AnimControl, AnimControlCollection

from .Interval import Interval

class AnimControlInterval(Interval):
    animNum: ClassVar[int]
    controls: AnimControlCollection
    loopAnim: bool
    constrainedLoop: bool
    playRate: float
    frameRate: float
    startFrame: float
    endFrame: float
    reverse: bool
    numFrames: int
    implicitDuration: bool
    currT: float
    def __init__(
        self,
        controls: AnimControl | AnimControlCollection,
        loop: bool = ...,
        constrainedLoop: bool = ...,
        duration: float | None = None,
        startTime: float | None = None,
        endTime: float | None = None,
        startFrame: float | None = None,
        endFrame: float | None = None,
        playRate: float = 1.0,
        name: str | None = None,
    ) -> None: ...
    def getCurrentFrame(self) -> float | None: ...
