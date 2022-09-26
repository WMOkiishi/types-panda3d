__all__ = ['Transitions']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from direct.gui.DirectFrame import DirectFrame
from direct.interval import MetaInterval
from direct.interval.Interval import Interval
from direct.interval.LerpInterval import LerpColorInterval, LerpColorScaleInterval
from panda3d._typing import Vec4f
from panda3d.core import AsyncFuture, LVecBase3f, LVecBase4f, NodePath
from panda3d.direct import CInterval

_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']
_Interval: TypeAlias = Interval | CInterval

class Transitions:
    IrisModelName: ClassVar[str]
    FadeModelName: ClassVar[str]
    transitionIval: MetaInterval.Sequence | None
    letterboxIval: MetaInterval.Sequence | None
    iris: NodePath | None
    fade: DirectFrame | None
    letterbox: NodePath | None
    fadeModel: NodePath | None
    imagePos: LVecBase3f
    alphaOff: LVecBase4f
    alphaOn: LVecBase4f
    lerpFunc: type[LerpColorScaleInterval] | type[LerpColorInterval]
    irisTaskName: str
    fadeTaskName: str
    letterboxTaskName: str
    def __init__(self, loader: object, model: NodePath | None = None, scale: float = ..., pos: LVecBase3f = ...) -> None: ...
    def __del__(self) -> None: ...
    def setFadeModel(self, model: NodePath | None, scale: float = ...) -> None: ...
    def loadFade(self) -> None: ...
    def getFadeInIval(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> MetaInterval.Sequence: ...
    def getFadeOutIval(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> MetaInterval.Sequence: ...
    def fadeIn(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> AsyncFuture: ...
    def fadeOut(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> AsyncFuture: ...
    def fadeOutActive(self) -> bool: ...
    def fadeScreen(self, alpha: float = ...) -> None: ...
    def fadeScreenColor(self, color: Vec4f) -> None: ...
    def noFade(self) -> None: ...
    def setFadeColor(self, r: float, g: float, b: float) -> None: ...
    def loadIris(self) -> None: ...
    def irisIn(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> AsyncFuture: ...
    def irisOut(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> AsyncFuture: ...
    def noIris(self) -> None: ...
    def noTransitions(self) -> None: ...
    def loadLetterbox(self) -> None: ...
    def noLetterbox(self) -> None: ...
    def letterboxOn(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> AsyncFuture: ...
    def letterboxOff(
        self,
        t: float = ...,
        finishIval: _Interval | None = None,
        blendType: _BlendType = ...,
    ) -> AsyncFuture: ...
