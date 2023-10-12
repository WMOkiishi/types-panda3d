__all__ = ['ActorControl', 'AnimPanel']

import tkinter
from collections.abc import Callable
from types import CodeType
from typing import ClassVar, SupportsFloat
from typing_extensions import Final, Literal

import Pmw  # type: ignore[import-untyped]
from direct.directtools.DirectSession import DirectSession
from direct.tkwidgets.AppShell import AppShell

FRAMES: Final = 0
SECONDS: Final = 1

class AnimPanel(AppShell):
    index: ClassVar[int]
    session: DirectSession | None
    playList: list[ActorControl]
    actorControlIndex: int
    destroyCallBack: Callable[[], object] | None
    actorFrame: tkinter.Frame | None
    lastT: float
    fToggleAll: bool
    actorControlList: list[ActorControl]
    def __init__(self, aList=[], parent=None, session=None, **kw) -> None: ...
    def createActorControls(self) -> None: ...
    def clearActorControls(self) -> None: ...
    def setActors(self) -> None: ...
    def loadAnim(self) -> None: ...
    def playActorControls(self) -> None: ...
    def play(self, task) -> Literal[1]: ...
    def stopActorControls(self) -> None: ...
    def getActorControlAt(self, index: int) -> ActorControl: ...
    def enableActorControlAt(self, index: int) -> None: ...
    def toggleAllControls(self) -> None: ...
    def enableActorControls(self) -> None: ...
    def disableActorControls(self) -> None: ...
    def disableActorControlAt(self, index) -> None: ...
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
    unitsVar: tkinter.IntVar
    animMenu: Pmw.ComboBox
    minLabel: tkinter.Label
    frameControl: tkinter.Scale
    maxLabel: tkinter.Label
    frameActiveVar: tkinter.IntVar
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
