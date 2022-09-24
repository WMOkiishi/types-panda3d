from collections.abc import Sequence
from typing_extensions import TypeAlias

from panda3d.core import LMatrix3f, LVecBase2f, LVecBase3f, NodePath, PerspectiveLens, RenderState
from ..fsm.FSM import FSM
from ..interval import MetaInterval
from .DistributedObject import DistributedObject

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow

class Fixture(NodePath, FSM):
    id: int
    lens: PerspectiveLens
    scaleIval: MetaInterval.Sequence | None
    recordingInProgress: bool
    dirty: bool
    def __init__(self, id: int, parent: NodePath, pos: _Vec3f, hpr: _Vec3f, fov: LVecBase2f | float) -> None: ...
    def pack(self) -> str: ...
    def setId(self, id: int) -> None: ...
    def setFov(self, fov: LVecBase2f | float) -> None: ...
    def adjustFov(self, x: float, y: float) -> None: ...
    def getFov(self) -> LVecBase2f: ...
    def setupFrustum(self) -> None: ...
    def setRecordingInProgress(self, inProgress: bool) -> None: ...
    def getScaleIval(self) -> MetaInterval.Sequence: ...
    def setState(self, state: RenderState) -> None: ...
    def exitOff(self) -> None: ...
    def enterOff(self) -> None: ...
    def enterStandby(self) -> None: ...
    def enterBlinking(self) -> None: ...
    def exitBlinking(self) -> None: ...
    def enterRecording(self) -> None: ...
    def exitRecording(self) -> None: ...
    def enterUsing(self, args: Sequence[object] | None = ...) -> None: ...
    def exitUsing(self) -> None: ...

class DistributedCamera(DistributedObject):
    parent: NodePath | None
    fixtures: dict[int, Fixture]
    cameraId: int
    def __getitem__(self, index: int) -> Fixture: ...
    def pack(self) -> str: ...
    def getOv(self) -> DistributedObject | None: ...
    def setCamParent(self, doId: int) -> None: ...
    def getCamParent(self) -> NodePath | None: ...
    def setFixtures(self, fixtures: Sequence[Fixture]) -> None: ...
    def textFixture(self, index: int) -> None: ...
    def stopTesting(self, index: int) -> None: ...