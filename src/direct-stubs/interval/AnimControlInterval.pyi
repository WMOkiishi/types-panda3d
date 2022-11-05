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
    startFrame: int
    endFrame: int
    reverse: bool
    numFrames: int
    implicitDuration: bool
    currT: float
    def __init__(
        self,
        controls: AnimControl | AnimControlCollection,
        loop: bool = ...,
        constrainedLoop: bool = ...,
        duration: float | None = ...,
        startTime: int | None = ...,
        endTime: int | None = ...,
        startFrame: int | None = ...,
        endFrame: int | None = ...,
        playRate: float = ...,
        name: str | None = ...,
    ) -> None: ...
    def getCurrentFrame(self) -> float | None: ...
