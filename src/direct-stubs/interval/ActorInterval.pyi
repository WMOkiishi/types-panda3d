__all__ = ['ActorInterval', 'LerpAnimInterval']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import AnimControl
from panda3d.direct import CLerpAnimEffectInterval
from ..actor.Actor import Actor
from ..directnotify.Notifier import Notifier
from .Interval import Interval

_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']
_OldBool: TypeAlias = Literal[0, 1]

class ActorInterval(Interval):
    notify: ClassVar[Notifier]
    animNum: ClassVar[int]
    actor: Actor
    animName: str
    controls: list[AnimControl]
    loopAnim: bool | _OldBool
    constrainedLoop: bool | _OldBool
    forceUpdate: bool | _OldBool
    playRate: float
    frameRate: float
    startFrame: float
    endFrame: float
    reverse: bool
    numFrames: int
    implicitDuration: bool | _OldBool
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
    def privStep(self, t: float) -> None: ...
    def privFinalize(self) -> None: ...
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
