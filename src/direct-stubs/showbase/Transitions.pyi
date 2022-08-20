__all__ = ['Transitions']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import AsyncFuture, ConfigVariableColor, LMatrix4f, LVecBase3f, LVecBase4f, NodePath, UnalignedLVecBase4f
from panda3d.direct import CInterval
from ..gui.DirectFrame import DirectFrame
from ..interval import MetaInterval
from ..interval.Interval import Interval
from ..interval.LerpInterval import LerpColorInterval, LerpColorScaleInterval

_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']
_Interval: TypeAlias = Interval | CInterval
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor


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
    def __init__(self, loader: object, model: NodePath | None = None, scale: float = 3, pos: LVecBase3f = ...) -> None: ...
    def __del__(self) -> None: ...
    def setFadeModel(self, model: NodePath | None, scale: float = 1) -> None: ...
    def loadFade(self) -> None: ...
    def getFadeInIval(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> MetaInterval.Sequence: ...
    def getFadeOutIval(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> MetaInterval.Sequence: ...
    def fadeIn(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> AsyncFuture: ...
    def fadeOut(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> AsyncFuture: ...
    def fadeOutActive(self): ...
    def fadeScreen(self, alpha: float = 0.5) -> None: ...
    def fadeScreenColor(self, color: _Vec4f) -> None: ...
    def noFade(self) -> None: ...
    def setFadeColor(self, r: float, g: float, b: float) -> None: ...
    def loadIris(self) -> None: ...
    def irisIn(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> AsyncFuture: ...
    def irisOut(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> AsyncFuture: ...
    def noIris(self) -> None: ...
    def noTransitions(self) -> None: ...
    def loadLetterbox(self) -> None: ...
    def noLetterbox(self) -> None: ...
    def letterboxOn(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> AsyncFuture: ...
    def letterboxOff(
        self,
        t: float = 0.5,
        finishIval: _Interval | None = None,
        blendType: _BlendType = 'noBlend',
    ) -> AsyncFuture: ...
