__all__ = ['MopathRecorder']

import tkinter
from collections.abc import Callable, MutableMapping
from typing import Any, ClassVar, SupportsFloat, SupportsInt
from typing_extensions import Final, Literal, TypeAlias

import Pmw  # type: ignore[import]
from direct._typing import AnyReal, Unused
from direct.directtools.DirectGeometry import LineNodePath
from direct.directtools.DirectSelection import SelectionRay
from direct.showbase.DirectObject import DirectObject
from direct.tkwidgets.AppShell import AppShell
from direct.tkwidgets.Dial import AngleDial
from direct.tkwidgets.EntryScale import EntryScale
from direct.tkwidgets.Floater import Floater
from direct.tkwidgets.Slider import Slider
from direct.tkwidgets.VectorWidgets import ColorEntry, Vector2Entry, Vector3Entry
from panda3d._typing import Vec3f
from panda3d.core import CurveFitter, GeomNode, LPoint3f, LRGBColor, NodePath, ParametricCurveCollection

_TkFill: TypeAlias = Literal['none', 'x', 'y', 'both']
_TkRelief: TypeAlias = Literal['raised', 'sunken', 'flat', 'ridge', 'solid', 'groove']
_TkSide: TypeAlias = Literal['left', 'right', 'top', 'bottom']

PRF_UTILITIES: Final[list[str]]

class MopathRecorder(AppShell, DirectObject):
    count: ClassVar[int]
    name: str
    nodePath: NodePath | None
    playbackNodePath: NodePath | None
    nodePathParent: NodePath
    recorderNodePath: NodePath
    tempCS: NodePath
    playbackMarker: NodePath
    playbackMarkerIds: list[int]
    tangentGroup: NodePath
    tangentMarker: NodePath
    tangentMarkerIds: list[int]
    tangentLines: LineNodePath
    nodePathDict: dict[str, NodePath]
    nodePathNames: list[str]
    manipulandumId: int | None
    trace: LineNodePath
    oldPlaybackNodePath: NodePath | None
    pointSet: list[tuple[float, Vec3f, Vec3f]]
    prePoints: list[tuple[float, Vec3f, Vec3f]]
    postPoints: list[tuple[float, Vec3f, Vec3f]]
    pointSetDict: dict[str, list[tuple[float, Vec3f, Vec3f]]]
    pointSetCount: int
    pointSetName: str
    samplingMode: str
    preRecordFunc: Callable[[], object] | None
    startStopHook: str
    keyframeHook: str
    lastPos: LPoint3f
    curveFitter: CurveFitter
    numTicks: int
    numSegs: int
    curveCollection: ParametricCurveCollection | None
    nurbsCurveDrawer = ...
    curveNodePath: NodePath[GeomNode]
    maxT: float
    playbackTime: float
    loopPlayback: bool
    playbackSF: float
    desampleFrequency: float
    numSamples: int
    recordStart: float
    deltaTime: float
    controlStart: float
    controlStop: float
    recordStop: float
    cropFrom: float
    cropTo: float
    fAdjustingValues: bool
    iRayCS: NodePath
    iRay: SelectionRay
    actionEvents: list[tuple[str, Callable[..., None]]]
    undoButton: tkinter.Button
    redoButton: tkinter.Button
    nodePathMenu: Pmw.ComboBox
    nodePathMenuEntry: tkinter.Entry
    nodePathMenuBG: str
    recordingType: tkinter.StringVar
    speedScale: tkinter.Scale
    speedVar: tkinter.StringVar
    speedEntry: tkinter.Entry
    mainNotebook: Pmw.NoteBook
    resamplePage: tkinter.Frame
    refinePage: tkinter.Frame
    extendPage: tkinter.Frame
    cropPage: tkinter.Frame
    drawPage: tkinter.Frame
    optionsPage: tkinter.Frame
    sf: Pmw.ScrolledFrame
    def __init__(self, parent: Unused = ..., **kw) -> None: ...
    def pushUndo(self, fResetRedo: bool = ...) -> None: ...
    def undoHook(self, nodePathList: Unused = ...) -> None: ...
    def pushUndoHook(self) -> None: ...
    def undoListEmptyHook(self) -> None: ...
    def pushRedo(self) -> None: ...
    def redoHook(self, nodePathList: Unused = ...) -> None: ...
    def pushRedoHook(self) -> None: ...
    def redoListEmptyHook(self) -> None: ...
    def selectedNodePathHook(self, nodePath: NodePath) -> None: ...
    def getChildIds(self, nodePath: NodePath) -> list[int]: ...
    def deselectedNodePathHook(self, nodePath: NodePath) -> None: ...
    def curveEditTask(self, state: Unused) -> Literal[1]: ...
    def manipulateObjectStartHook(self) -> None: ...
    def manipulateObjectCleanupHook(self, nodePathList: Unused = ...) -> None: ...
    def createNewPointSet(self) -> None: ...
    def extractPointSetFromCurveFitter(self) -> None: ...
    def extractPointSetFromCurveCollection(self) -> None: ...
    def selectPointSetNamed(self, name: str) -> None: ...
    def setPathVis(self) -> None: ...
    def setKnotVis(self) -> None: ...
    def setCvVis(self) -> None: ...
    def setHullVis(self) -> None: ...
    def setTraceVis(self) -> None: ...
    def setMarkerVis(self) -> None: ...
    def setNumSegs(self, value: SupportsInt) -> None: ...
    def setNumTicks(self, value: SupportsFloat) -> None: ...
    def setTickScale(self, value: SupportsFloat) -> None: ...
    def setPathColor(self, color: LRGBColor | tuple[float, float, float]) -> None: ...
    def setKnotColor(self, color: LRGBColor | tuple[float, float, float]) -> None: ...
    def setCvColor(self, color: LRGBColor | tuple[float, float, float]) -> None: ...
    def setTickColor(self, color: LRGBColor | tuple[float, float, float]) -> None: ...
    def setHullColor(self, color: LRGBColor | tuple[float, float, float]) -> None: ...
    def setStartStopHook(self, event=...) -> None: ...
    def setKeyframeHook(self, event=...) -> None: ...
    def reset(self) -> None: ...
    def setSamplingMode(self, mode: str) -> None: ...
    def disableKeyframeButton(self) -> None: ...
    def enableKeyframeButton(self) -> None: ...
    def setRecordingType(self, type: str) -> None: ...
    def setNewCurveMode(self) -> None: ...
    def setRefineMode(self) -> None: ...
    def setExtendMode(self) -> None: ...
    def toggleRecordVar(self) -> None: ...
    def toggleRecord(self) -> None: ...
    def recordTask(self, state) -> Literal[1]: ...
    def addKeyframe(self, fToggleRecord: bool = ...) -> None: ...
    def easeInOut(self, t: AnyReal) -> AnyReal: ...
    def setPreRecordFunc(self, func) -> None: ...
    def recordPoint(self, time: float) -> None: ...
    def computeCurves(self) -> None: ...
    def initTrace(self) -> None: ...
    def updateWidgets(self) -> None: ...
    def selectNodePathNamed(self, name: str) -> None: ...
    def setNodePath(self, nodePath: NodePath) -> None: ...
    def setPlaybackNodePath(self, nodePath: NodePath) -> None: ...
    def addNodePath(self, nodePath: NodePath) -> None: ...
    def addNodePathToDict(self, nodePath: NodePath, names: list[str], menu, dict: MutableMapping[str, NodePath]) -> None: ...
    def setLoopPlayback(self) -> None: ...
    def playbackGoTo(self, time: float) -> None: ...
    def startPlayback(self) -> None: ...
    def setSpeedScale(self, value: SupportsFloat) -> None: ...
    def setPlaybackSF(self, value: SupportsFloat) -> None: ...
    def playbackTask(self, state) -> Literal[0, 1]: ...
    def stopPlayback(self) -> None: ...
    def jumpToStartOfPlayback(self) -> None: ...
    def jumpToEndOfPlayback(self) -> None: ...
    def startStopPlayback(self) -> None: ...
    def setDesampleFrequency(self, frequency: float) -> None: ...
    def desampleCurve(self) -> None: ...
    def setNumSamples(self, numSamples: SupportsInt) -> None: ...
    def sampleCurve(self, fCompute: bool = ...) -> None: ...
    def makeEven(self) -> None: ...
    def faceForward(self) -> None: ...
    def setPathDuration(self, event) -> None: ...
    def setPathDurationTo(self, newMaxT: float) -> None: ...
    def setRecordStart(self, value: float) -> None: ...
    def getPrePoints(self, type: str = ...) -> None: ...
    def setControlStart(self, value: float) -> None: ...
    def setControlStop(self, value: float) -> None: ...
    def setRefineStop(self, value: float) -> None: ...
    def getPostPoints(self) -> None: ...
    def mergePoints(self) -> None: ...
    def setCropFrom(self, value: float) -> None: ...
    def setCropTo(self, value: float) -> None: ...
    def cropCurve(self) -> None: ...
    def loadCurveFromFile(self) -> None: ...
    def saveCurveToFile(self) -> None: ...
    def followTerrain(self, height: float = ...) -> None: ...
    def addWidget(self, widget, category: str, text: str) -> None: ...  # type: ignore[override]
    def getWidget(self, category: str, text: str) -> Any: ...
    def getVariable(self, category: str, text: str) -> Any: ...
    def createLabeledEntry(
        self,
        parent: tkinter.Misc | None,
        category: str,
        text: str,
        balloonHelp,
        value: str = ...,
        command=...,
        relief: _TkRelief = ...,
        side: _TkSide = ...,
        expand: int = ...,
        width: int = ...,
    ) -> tuple[tkinter.Frame, tkinter.Label, tkinter.Entry]: ...
    def createButton(
        self,
        parent: tkinter.Misc | None,
        category: str,
        text: str,
        balloonHelp,
        command,
        side: _TkSide = ...,
        expand: int = ...,
        fill: _TkFill = ...,
    ) -> tkinter.Button: ...
    def createCheckbutton(
        self,
        parent: tkinter.Misc | None,
        category: str,
        text: str,
        balloonHelp,
        command,
        initialState,
        side: str = ...,
        fill: _TkFill = ...,
        expand: int = ...,
    ) -> tkinter.Checkbutton: ...
    def createRadiobutton(
        self,
        parent,
        side: _TkSide,
        category: str,
        text: str,
        balloonHelp,
        variable: tkinter.Variable | Literal[''],
        value,
        command=...,
        fill: _TkFill = ...,
        expand: int = ...,
    ) -> tkinter.Radiobutton: ...
    def createFloater(
        self,
        parent,
        category: str,
        text: str,
        balloonHelp,
        command=...,
        min: float = ...,
        resolution: float | None = ...,
        maxVelocity: float = ...,
        **kw,
    ) -> Floater: ...
    def createAngleDial(self, parent, category: str, text: str, balloonHelp, command=..., **kw) -> AngleDial: ...
    def createSlider(
        self,
        parent,
        category: str,
        text: str,
        balloonHelp,
        command=...,
        min: float = ...,
        max: float = ...,
        resolution: float | None = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw,
    ) -> Slider: ...
    def createEntryScale(
        self,
        parent,
        category: str,
        text: str,
        balloonHelp,
        command=...,
        min: float = ...,
        max: float = ...,
        resolution: float | None = ...,
        side: _TkSide = ...,
        fill: _TkFill = ...,
        expand: int = ...,
        **kw,
    ) -> EntryScale: ...
    def createVector2Entry(self, parent, category: str, text: str, balloonHelp, command=..., **kw) -> Vector2Entry: ...
    def createVector3Entry(self, parent, category: str, text: str, balloonHelp, command=..., **kw) -> Vector3Entry: ...
    def createColorEntry(self, parent, category: str, text: str, balloonHelp, command=..., **kw) -> ColorEntry: ...
    def createOptionMenu(self, parent, category: str, text: str, balloonHelp, items, command) -> tkinter.StringVar: ...
    def createComboBox(
        self,
        parent,
        category: str,
        text: str,
        balloonHelp,
        items,
        command,
        history: int = ...,
        side: _TkSide = ...,
        expand: int = ...,
        fill: _TkFill = ...,
    ) -> Pmw.ComboBox: ...
    def makeCameraWindow(self) -> None: ...
