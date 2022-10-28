__all__ = ['Placer', 'place']

import tkinter
from collections.abc import Callable, MutableMapping
from typing_extensions import Literal

import Pmw  # type: ignore[import]
from direct._typing import Unused
from direct.tkwidgets.AppShell import AppShell
from direct.tkwidgets.Dial import AngleDial
from direct.tkwidgets.Floater import Floater
from panda3d._typing import Vec3f
from panda3d.core import LVector3f, NodePath

class Placer(AppShell):
    tempCS: NodePath
    orbitFromCS: NodePath
    orbitToCS: NodePath
    refCS: NodePath
    nodePathDict: dict[str, NodePath]
    nodePathNames: list[str]
    refNodePathDict: dict[str, NodePath]
    refNodePathNames: list[str]
    initPos: LVector3f
    initHpr: LVector3f
    initScale: LVector3f
    deltaHpr: LVector3f
    posOffset: LVector3f
    undoEvents: list[tuple[str, Callable[..., None]]]
    movementMode: str
    nodePathMenu: Pmw.ComboBox
    nodePathMenuEntry: tkinter.Entry
    nodePathMenuBG: str
    refNodePathMenu: Pmw.ComboBox
    refNodePathMenuEntry: tkinter.Entry
    undoButton: tkinter.Button
    redoButton: tkinter.Button
    posX: Floater
    posY: Floater
    posZ: Floater
    hprH: AngleDial
    hprP: AngleDial
    hprR: AngleDial
    scalingMode: tkinter.StringVar
    scaleMenubutton: tkinter.Label
    scaleX: Floater
    scaleY: Floater
    scaleZ: Floater
    def __init__(self, parent: Unused = ..., **kw) -> None: ...
    def setMovementMode(self, movementMode: str) -> None: ...
    def setScalingMode(self) -> None: ...
    def selectNodePathNamed(self, name: str) -> None: ...
    def setActiveNodePath(self, nodePath: NodePath) -> None: ...
    def selectRefNodePathNamed(self, name: str) -> None: ...
    def setReferenceNodePath(self, nodePath: NodePath) -> None: ...
    def addNodePath(self, nodePath: NodePath) -> None: ...
    def addRefNodePath(self, nodePath: NodePath) -> None: ...
    def addNodePathToDict(self, nodePath: NodePath, names: list[str], menu, dict: MutableMapping[str, NodePath]) -> None: ...
    def updatePlacer(self) -> None: ...
    def updateAuxiliaryCoordinateSystems(self) -> None: ...
    def xform(self, value: float, axis: str) -> None: ...
    def xformStart(self, data: Unused) -> None: ...
    def xformStop(self, data: Unused) -> None: ...
    def xformRelative(self, value: float, axis: Literal['x', 'y', 'z', 'h', 'p', 'r']) -> None: ...
    def xformOrbit(self, value: float, axis: Literal['x', 'y', 'z', 'h', 'p', 'r']) -> None: ...
    def xformScale(self, value: float, axis: Literal['sx', 'sy', 'sz']) -> None: ...
    def updatePosWidgets(self, pos: Vec3f | tuple[float, float, float]) -> None: ...
    def updateHprWidgets(self, hpr: Vec3f | tuple[float, float, float]) -> None: ...
    def updateScaleWidgets(self, scale: Vec3f | tuple[float, float, float]) -> None: ...
    def zeroAll(self) -> None: ...
    def zeroPos(self) -> None: ...
    def zeroHpr(self) -> None: ...
    def unitScale(self) -> None: ...
    def updateResetValues(self, nodePath: NodePath) -> None: ...
    def resetAll(self) -> None: ...
    def resetPos(self) -> None: ...
    def resetHpr(self) -> None: ...
    def resetScale(self) -> None: ...
    def pushUndo(self, fResetRedo: bool = ...) -> None: ...
    def undoHook(self, nodePathList: Unused = ...) -> None: ...
    def pushUndoHook(self) -> None: ...
    def undoListEmptyHook(self) -> None: ...
    def pushRedo(self) -> None: ...
    def redoHook(self, nodePathList: Unused = ...) -> None: ...
    def pushRedoHook(self) -> None: ...
    def redoListEmptyHook(self) -> None: ...
    def printNodePathInfo(self) -> None: ...

def place(nodePath: NodePath) -> Placer: ...
