from collections.abc import Sequence
from typing import Any, ClassVar
from typing_extensions import Final, Literal, TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.interval.MetaInterval import MetaInterval
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d.core import AsyncTask, CollisionEntry, LPoint3f, LVector3f, NodePath, PandaNode

CAM_MOVE_DURATION: Final[float]
COA_MARKER_SF: Final[float]
Y_AXIS: Final[LVector3f]

_TaskCont: TypeAlias = Literal[1]
_Unused: TypeAlias = object

class DirectCameraControl(DirectObject):
    notify: ClassVar[Notifier]
    startT: float
    startF: int
    orthoViewRoll: float
    lastView: int
    coa: LPoint3f
    coaMarker: NodePath
    coaMarkerPos: LPoint3f
    coaMarkerColorIval: MetaInterval | None
    fLockCOA: bool
    nullHitPointCount: int
    cqEntries: list
    coaMarkerRef: NodePath[PandaNode]
    camManipRef: NodePath[PandaNode]
    switchDirBelowZero: bool
    manipulateCameraTask: AsyncTask | None
    manipulateCameraInterval: MetaInterval | None
    actionEvents: list[list[Any]]
    keyEvents: list[list[Any]]
    lockRoll: bool
    useMayaCamControls: bool
    altDown: bool
    perspCollPlane: NodePath | None
    perspCOllPlane2: NodePath | None
    def __init__(self) -> None: ...
    def toggleMarkerVis(self) -> None: ...
    def mouseRotateStart(self, modifiers: int) -> None: ...
    def mouseDollyStart(self, modifiers: int) -> None: ...
    def mouseDollyStop(self) -> None: ...
    def mouseFlyStart(self, modifiers: int) -> None: ...
    def mouseFlyStop(self) -> None: ...
    def mouseFlyStartTopWin(self) -> None: ...
    def mouseFlyStopTopWin(self) -> None: ...
    def spawnXZTranslateOrHPanYZoom(self) -> None: ...
    def spawnXZTranslateOrHPPan(self) -> None: ...
    def spawnXZTranslate(self) -> None: ...
    def spawnOrthoTranslate(self) -> None: ...
    def spawnHPanYZoom(self) -> None: ...
    def spawnOrthoZoom(self) -> None: ...
    def spawnHPPan(self) -> None: ...
    def XZTranslateOrHPanYZoomTask(self, state: Task) -> _TaskCont: ...
    def XZTranslateOrHPPanTask(self, state: _Unused) -> _TaskCont: ...
    def XZTranslateTask(self, state: _Unused) -> _TaskCont: ...
    def OrthoTranslateTask(self, state: Task) -> _TaskCont: ...
    def HPanYZoomTask(self, state: Task) -> _TaskCont | None: ...
    def OrthoZoomTask(self, state: _Unused) -> _TaskCont: ...
    def HPPanTask(self, state: _Unused) -> _TaskCont: ...
    def spawnMouseRotateTask(self) -> None: ...
    def mouseRotateTask(self, state: Task) -> _TaskCont: ...
    def spawnMouseRollTask(self) -> None: ...
    def mouseRollTask(self, state: Task) -> _TaskCont: ...
    def lockCOA(self) -> None: ...
    def unlockCOA(self) -> None: ...
    def toggleCOALock(self) -> None: ...
    def pickNextCOA(self) -> None: ...
    def computeCOA(self, entry: CollisionEntry) -> None: ...
    def updateCoa(self, ref2point: Sequence[float], coaDist: float | None = None, ref: NodePath | None = None) -> None: ...
    def updateCoaMarkerSizeOnDeath(self) -> None: ...
    def updateCoaMarkerSize(self, coaDist: float | None = None) -> None: ...
    def homeCam(self) -> None: ...
    def uprightCam(self) -> None: ...
    def orbitUprightCam(self) -> None: ...
    def centerCam(self) -> None: ...
    def centerCamNow(self) -> None: ...
    def centerCamIn(self, t: _Unused) -> None: ...
    def zoomCam(self, zoomFactor: float, t: _Unused) -> None: ...
    def spawnMoveToView(self, view: int) -> None: ...
    def swingCamAboutWidget(self, degrees: float, t: _Unused) -> None: ...
    def reparentCam(self, parent: NodePath) -> None: ...
    def fitOnWidget(self, nodePath: _Unused = ...) -> None: ...
    def moveToFit(self) -> None: ...
    def stickToWidgetTask(self, state: _Unused) -> _TaskCont: ...
    def enableMouseFly(self, fKeyEvents: bool = True) -> None: ...
    def disableMouseFly(self) -> None: ...
    def removeManipulateCameraTask(self) -> None: ...
