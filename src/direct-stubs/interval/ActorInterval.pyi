__all__ = ['ActorInterval', 'LerpAnimInterval']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import AnimControl
from panda3d.direct import CLerpAnimEffectInterval
from ..actor.Actor import Actor
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
        loop: bool = False,
        constrainedLoop: bool = False,
        duration: float | None = None,
        startTime = None,
        endTime = None,
        startFrame = None,
        endFrame = None,
        playRate: float = 1,
        name: str | None = None,
        forceUpdate: bool = False,
        partName = None,
        lodName = None,
    ) -> None: ...
    def getCurrentFrame(self) -> float | None: ...
    def resetControls(self, partName: str | None, lodName: str | None = None) -> None: ...

class LerpAnimInterval(CLerpAnimEffectInterval):
    lerpAnimNum: ClassVar[int]
    def __init__(
        self,
        actor,
        duration: float,
        startAnim: str | None,
        endAnim: str | None,
        startWeight: float = 0,
        endWeight: float = 1,
        blendType: _BlendType = 'noBlend',
        name: str | None = None,
        partName: str | None = None,
        lodName: str | None = None,
    ) -> None: ...
