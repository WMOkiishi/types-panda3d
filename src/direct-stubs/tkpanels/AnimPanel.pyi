__all__ = ['ActorControl', 'AnimPanel']

from collections.abc import Callable
from tkinter import Frame, IntVar, Label, Scale
from types import CodeType
from typing import Any, ClassVar, SupportsFloat
from typing_extensions import Final, Literal

from direct.tkwidgets.AppShell import AppShell

Pmw: Any

FRAMES: Final[Literal[0]]
SECONDS: Final[Literal[1]]

class AnimPanel(AppShell):
    index: ClassVar[int]
    session = ...
    playList: list
    actorControlIndex: int
    destroyCallBack: Callable[[], object] | None
    actorFrame: Frame | None
    lastT: float
    fToggleAll: bool
    def __init__(self, aList=..., parent=None, session=None, **kw) -> None: ...
    def createActorControls(self) -> None: ...
    def clearActorControls(self) -> None: ...
    def setActors(self) -> None: ...
    def loadAnim(self) -> None: ...
    def play(self, task) -> Literal[1]: ...
    def stopActorControls(self) -> None: ...
    def getActorControlAt(self, index): ...
    def toggleAllControls(self) -> None: ...
    def enableActorControls(self) -> None: ...
    def disableActorControls(self) -> None: ...
    def displayFrameCounts(self) -> None: ...
    def displaySeconds(self) -> None: ...
    def resetAllToZero(self) -> None: ...
    def resetAllToEnd(self) -> None: ...
    def nextFrame(self) -> None: ...
    def previousFrame(self) -> None: ...
    def setDestroyCallBack(self, callBack: Callable[[], object] | None) -> None: ...
    def destroy(self) -> None: ...

class ActorControl(Pmw.MegaWidget):
    fps: int
    offset: float
    maxSeconds: float
    currT: float
    fScaleCommand: bool
    fOneShot: bool
    unitsVar: IntVar
    animMenu: Pmw.ComboBox
    minLabel: Label
    frameControl: Scale
    maxLabel: Label
    frameActiveVar: IntVar
    playRate: float
    def __init__(self, parent=None, **kw) -> None: ...
    def updateDisplay(self) -> None: ...
    def selectAnimNamed(self, name: str) -> None: ...
    def setPlayRate(self, rate: str | bytes | CodeType) -> None: ...
    def setOffset(self) -> None: ...
    def enableControl(self) -> None: ...
    def disableControl(self) -> None: ...
    def displayFrameCounts(self) -> None: ...
    def displaySeconds(self) -> None: ...
    def play(self, deltaT: float, fLoop: bool) -> None: ...
    def goToF(self, f) -> None: ...
    def goToT(self, t) -> None: ...
    def goTo(self, t: SupportsFloat) -> None: ...
    def resetToZero(self) -> None: ...
    def resetToEnd(self) -> None: ...
    def nextFrame(self) -> None: ...
    def previousFrame(self) -> None: ...
