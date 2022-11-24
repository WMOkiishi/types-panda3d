from collections.abc import Iterable, Sequence
from typing import Any
from typing_extensions import Literal

from direct._typing import Unused
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d._typing import Vec3Like
from panda3d.core import LPoint3f, LVecBase3f, LVector3f, NodePath

from .DirectGeometry import LineNodePath

class DirectManipulationControl(DirectObject):
    objectHandles: ObjectHandles
    hitPt: LPoint3f
    prevHit: LVector3f
    hitPtScale: LPoint3f
    prevHitScale: LVector3f
    rotatingCenter: LPoint3f
    initScaleMag: float
    constraint: str | None
    rotateAxis: Literal['x', 'y', 'z']
    lastCrankAngle: float
    fSetCoa: bool
    fHitInit: bool
    fScaleInit: bool
    fScaleInit1: bool
    fWidgetTop: bool
    fFreeManip: bool
    fScaling3D: bool
    fScaling1D: bool
    fMovable: bool
    mode: Literal['select', 'camera', 'move', None]
    worldSpaceManip: bool
    useSeparateScaleHandles: bool
    actionEvents: list[Sequence[Any]]
    defaultSkipFlags: int
    optionalSkipFlags: int
    unmovableTagList: list[str]
    fAllowSelectionOnly: bool
    fAllowMarquee: bool
    marquee: LineNodePath | None
    gMultiView: bool
    fGridSnap: bool
    def __init__(self) -> None: ...
    def scaleWidget(self, factor: float) -> None: ...
    def supportMultiView(self) -> None: ...
    def manipulationStart(self, modifiers: int) -> None: ...
    def switchToWorldSpaceMode(self) -> None: ...
    def switchToLocalSpaceMode(self) -> None: ...
    def switchToMoveMode(self, state: Unused) -> Literal[0]: ...
    def watchMouseTask(self, state: Task) -> Literal[0, 1]: ...
    def watchMarqueeTask(self, state: Task) -> Literal[1]: ...
    def drawMarquee(self, startX: float, startY: float) -> None: ...
    def manipulationStop(self) -> None: ...
    def manipulateObjectCleanup(self) -> None: ...
    def spawnFollowSelectedNodePathTask(self) -> None: ...
    def followSelectedNodePathTask(self, state) -> None: ...
    def enableManipulation(self) -> None: ...
    def disableManipulation(self, allowSelectionOnly: bool = ...) -> None: ...
    def toggleObjectHandlesMode(self) -> None: ...
    def removeManipulateObjectTask(self) -> None: ...
    def enableWidgetMove(self) -> None: ...
    def disableWidgetMove(self) -> None: ...
    def getEditTypes(self, objects: Iterable[Any]) -> int: ...
    def manipulateObject(self) -> None: ...
    def spawnManipulateObjectTask(self) -> None: ...
    def manipulateObjectTask(self, state: Task) -> Literal[0, 1]: ...
    def addTag(self, tag: str) -> None: ...
    def removeTag(self, tag: str) -> None: ...
    def gridSnapping(self, nodePath: NodePath, offset: float) -> LPoint3f: ...
    def xlate1D(self, state: Unused) -> None: ...
    def xlate2D(self, state: Unused) -> None: ...
    def rotate1D(self, state: Unused) -> None: ...
    def widgetCheck(self, type: str) -> bool | None: ...
    def xlateCamXZ(self, state: Unused) -> None: ...
    def xlateCamXY(self, state: Unused) -> None: ...
    def rotate2D(self, state: Task) -> None: ...
    def rotateAboutViewVector(self, state: Task) -> None: ...
    def scale1D(self, state: Unused) -> None: ...
    def scale3D(self, state: Unused) -> None: ...
    def plantSelectedNodePath(self) -> None: ...

class ObjectHandles(NodePath, DirectObject):
    scalingNode: NodePath
    ohScalingFactor: int
    directScalingFactor: int
    hitPt: LVector3f
    xHandles: NodePath
    xPostGroup: NodePath
    xPostCollision: NodePath
    xRingGroup: NodePath
    xRingCollision: NodePath
    xDiscGroup: NodePath
    xDisc: NodePath
    xDiscCollision: NodePath
    xScaleGroup: NodePath
    xScaleCollision: NodePath
    yHandles: NodePath
    yPostGroup: NodePath
    yPostCollision: NodePath
    yRingGroup: NodePath
    yRingCollision: NodePath
    yDiscGroup: NodePath
    yDisc: NodePath
    yDiscCollision: NodePath
    yScaleGroup: NodePath
    yScaleCollision: NodePath
    zHandles: NodePath
    zPostGroup: NodePath
    zPostCollision: NodePath
    zRingGroup: NodePath
    zRingCollision: NodePath
    zDiscGroup: NodePath
    zDisc: NodePath
    zDiscCollision: NodePath
    zScaleGroup: NodePath
    zScaleCollision: NodePath
    fActive: bool
    guideLines: NodePath
    def __init__(self, name: str = ...): ...
    def coaModeColor(self) -> None: ...
    def disabledModeColor(self) -> None: ...
    def manipModeColor(self) -> None: ...
    def toggleWidget(self) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def showWidgetIfActive(self) -> None: ...
    def showWidget(self) -> None: ...
    def hideWidget(self) -> None: ...
    def enableHandles(self, handles: str | list[str]) -> None: ...
    def enableHandle(self, handle: str) -> None: ...
    def disableHandles(self, handles: str | list[str]) -> None: ...
    def disableHandle(self, handle: str) -> None: ...
    def showAllHandles(self) -> None: ...
    def hideAllHandles(self) -> None: ...
    def showHandle(self, handle: str) -> None: ...
    def showGuides(self) -> None: ...
    def hideGuides(self) -> None: ...
    def setDirectScalingFactor(self, factor: float) -> None: ...
    def setScalingFactor(self, scaleFactor: float) -> None: ...
    def getScalingFactor(self) -> LVecBase3f: ...
    def transferObjectHandlesScale(self) -> None: ...
    def multiplyScalingFactorBy(self, factor: float) -> None: ...
    def growToFit(self) -> None: ...
    def createObjectHandleLines(self) -> None: ...
    def createGuideLines(self) -> None: ...
    def getAxisIntersectPt(self, axis: Literal['x', 'y', 'z']) -> LVector3f: ...
    def getMouseIntersectPt(self) -> LPoint3f: ...
    def getWidgetIntersectPt(self, nodePath: NodePath, plane: Literal['x', 'y', 'z']) -> LVector3f: ...

def drawBox(lines: LineNodePath, center: Vec3Like, sideLength: float) -> None: ...
