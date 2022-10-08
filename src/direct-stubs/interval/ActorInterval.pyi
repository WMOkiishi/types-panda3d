__all__ = ['ActorInterval', 'LerpAnimInterval']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from direct.actor.Actor import Actor
from panda3d.core import AnimControl
from panda3d.direct import CLerpAnimEffectInterval
from .Interval import Interval

_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']

class ActorInterval(Interval):
    animNum: ClassVar[int]
    actor: Actor
    animName: str
    controls: list[AnimControl]
    loopAnim: bool
    constrainedLoop: bool
    forceUpdate: bool
    playRate: float
    frameRate: float
    startFrame: float
    endFrame: float
    reverse: bool
    numFrames: int
    implicitDuration: bool
    def __init__(
        self,
        actor: Actor,
        animName: str,
        loop: bool = ...,
        constrainedLoop: bool = ...,
        duration: float | None = ...,
        startTime: float | None = ...,
        endTime: float | None = ...,
        startFrame: float | None = ...,
        endFrame: float | None = ...,
        playRate: float = ...,
        name: str | None = ...,
        forceUpdate: bool = ...,
        partName: str | None = ...,
        lodName: str | None = ...,
    ) -> None: ...
    def getCurrentFrame(self) -> float | None: ...
    def resetControls(self, partName: str | None, lodName: str | None = ...) -> None: ...

class LerpAnimInterval(CLerpAnimEffectInterval):
    lerpAnimNum: ClassVar[int]
    def __init__(
        self,
        actor: Actor,
        duration: float,
        startAnim: str | None,
        endAnim: str | None,
        startWeight: float = ...,
        endWeight: float = ...,
        blendType: _BlendType = ...,
        name: str | None = ...,
        partName: str | None = ...,
        lodName: str | None = ...,
    ) -> None: ...
