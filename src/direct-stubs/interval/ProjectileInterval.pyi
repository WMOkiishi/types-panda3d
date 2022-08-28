__all__ = ['ProjectileInterval']

from typing import Any, ClassVar
from typing_extensions import TypeAlias

from panda3d.core import CollisionNode, LMatrix3f, LParabolaf, LVecBase3f, NodePath
from .Interval import Interval

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow

class ProjectileInterval(Interval):
    projectileIntervalNum: ClassVar[int]
    gravity: ClassVar[float]
    node: NodePath
    collNode: CollisionNode | None
    implicitStartPos: bool
    trajectoryArgs = tuple[Any, ...]
    startPos: _Vec3f
    zAcc: float
    endPos: _Vec3f | None
    startVel: _Vec3f
    parabola: LParabolaf
    def __init__(
        self,
        node: NodePath,
        startPos: _Vec3f | None = None,
        endPos: _Vec3f | None = None,
        duration: float | None = None,
        startVel: _Vec3f | None = None,
        endZ: float | None = None,
        wayPoint: _Vec3f | None = None,
        timeToWayPoint: float | None = None,
        gravityMult: float | None = None,
        name: str | None = None,
        collNode: CollisionNode | NodePath[CollisionNode] | None = None,
    ) -> None: ...
    def testTrajectory(self) -> bool: ...
    def privInitialize(self, t: float) -> None: ...
    def privInstant(self) -> None: ...
    def privStep(self, t: float) -> None: ...
