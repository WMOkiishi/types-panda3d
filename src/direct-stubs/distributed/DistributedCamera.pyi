from collections.abc import Sequence

from direct._typing import Unused
from direct.fsm.FSM import FSM
from direct.interval import MetaInterval
from panda3d._typing import Vec3Like
from panda3d.core import LVecBase2f, NodePath, PerspectiveLens, RenderState

from .DistributedObject import DistributedObject

class Fixture(NodePath, FSM):
    id: int
    lens: PerspectiveLens
    scaleIval: MetaInterval.Sequence | None
    recordingInProgress: bool
    dirty: bool
    def __init__(self, id: int, parent: NodePath, pos: Vec3Like, hpr: Vec3Like, fov: LVecBase2f | float) -> None: ...
    def pack(self) -> str: ...
    def setId(self, id: int) -> None: ...
    def setFov(self, fov: LVecBase2f | float) -> None: ...
    def adjustFov(self, x: float, y: float) -> None: ...
    def getFov(self) -> LVecBase2f: ...
    def setupFrustum(self) -> None: ...
    def setRecordingInProgress(self, inProgress: bool) -> None: ...
    def show(self) -> None: ...  # type: ignore[override]
    def getScaleIval(self) -> MetaInterval.Sequence: ...
    def setState(self, state: RenderState) -> None: ...  # type: ignore[override]
    def exitOff(self) -> None: ...
    def enterOff(self) -> None: ...
    def enterStandby(self) -> None: ...
    def enterBlinking(self) -> None: ...
    def exitBlinking(self) -> None: ...
    def enterRecording(self) -> None: ...
    def exitRecording(self) -> None: ...
    def enterUsing(self, args: Sequence[Unused] = ...) -> None: ...
    def exitUsing(self) -> None: ...

class DistributedCamera(DistributedObject):
    parent: NodePath | None
    fixtures: dict[int, Fixture]
    cameraId: int
    def __getitem__(self, index: int) -> Fixture: ...
    def pack(self) -> str: ...
    def getOV(self) -> DistributedObject | None: ...
    def setCamParent(self, doId: int) -> None: ...
    def getCamParent(self) -> NodePath | None: ...
    def setFixtures(self, fixtures: Sequence[Fixture]) -> None: ...
    def testFixture(self, index: int) -> None: ...
    def stopTesting(self, index: int) -> None: ...
