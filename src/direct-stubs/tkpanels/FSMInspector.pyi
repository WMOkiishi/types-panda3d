__all__ = ['FSMInspector', 'StateInspector']

import tkinter
from typing_extensions import TypeAlias

import Pmw  # type: ignore[import-untyped]
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from direct.tkwidgets.AppShell import AppShell

_CanvasItemId: TypeAlias = int

class FSMInspector(AppShell):
    fsm: ClassicFSM
    states: list[str]
    stateInspectorDict: dict[str, StateInspector]
    name: str
    def __init__(self, fsm: ClassicFSM, **kw) -> None: ...
    def scrolledCanvas(self) -> Pmw.ScrolledCanvas: ...
    def canvas(self) -> tkinter.Canvas: ...
    def setFontSize(self, size) -> None: ...
    def setMarkerSize(self, size) -> None: ...
    def drawConnections(self, event=None) -> None: ...
    def connectStates(self, fromState: StateInspector, toState: StateInspector) -> None: ...
    def computeEndpoints(self, fromState: StateInspector, toState: StateInspector) -> list[float]: ...
    def computePoint(self, radius: float, angle: float) -> tuple[float, float]: ...
    def findAngle(self, fromPoint: tuple[float, float], toPoint: tuple[float, float]) -> float: ...
    def mouse2Down(self, event) -> None: ...
    def mouse2Motion(self, event) -> None: ...
    def createStateInspectors(self) -> None: ...
    def getStateInspector(self, name: str) -> StateInspector | None: ...
    def addState(self, state: State) -> StateInspector: ...
    def enteredState(self, stateName: str) -> None: ...
    def exitedState(self, stateName: str) -> None: ...
    def setGridSize(self, size) -> None: ...
    def popupGridDialog(self) -> None: ...
    def toggleGridSnap(self) -> None: ...
    def printLayout(self) -> None: ...

class StateInspector(Pmw.MegaArchetype):
    inspector: FSMInspector
    state: State
    tag: str
    fsm: ClassicFSM
    scrolledCanvas: Pmw.ScrolledCanvas
    x: float
    y: float
    marker: _CanvasItemId
    text: _CanvasItemId
    rect: _CanvasItemId
    radius: float
    gridSize: float
    fGridSnap: bool
    def __init__(self, inspector: FSMInspector, state: State, **kw) -> None: ...
    def setRadius(self, size) -> None: ...
    def setGridSize(self, size) -> None: ...
    def setText(self, text=None) -> None: ...
    def setPos(self, x: float, y: float, snapToGrid: bool = ...) -> None: ...
    def center(self) -> tuple[float, float]: ...
    def getName(self) -> str: ...
    def mouseEnter(self, event) -> None: ...
    def mouseLeave(self, event) -> None: ...
    def mouseDown(self, event) -> None: ...
    def mouseMotion(self, event) -> None: ...
    def mouseRelease(self, event) -> None: ...
    def popupStateMenu(self, event) -> None: ...
    def transitionTo(self) -> None: ...
    def inspectSubMachine(self) -> None: ...
    def enteredState(self) -> None: ...
    def exitedState(self) -> None: ...
