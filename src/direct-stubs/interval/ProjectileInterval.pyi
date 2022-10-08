__all__ = ['ProjectileInterval']

from typing import Any, ClassVar

from panda3d._typing import Vec3f
from panda3d.core import CollisionNode, LParabolaf, NodePath
from .Interval import Interval

class ProjectileInterval(Interval):
    projectileIntervalNum: ClassVar[int]
    gravity: ClassVar[float]
    node: NodePath
    collNode: CollisionNode | None
    implicitStartPos: bool
    trajectoryArgs: tuple[Any, ...]
    startPos: Vec3f
    zAcc: float
    endPos: Vec3f | None
    startVel: Vec3f
    parabola: LParabolaf
    def __init__(
        self,
        node: NodePath,
        startPos: Vec3f | None = ...,
        endPos: Vec3f | None = ...,
        duration: float | None = ...,
        startVel: Vec3f | None = ...,
        endZ: float | None = ...,
        wayPoint: Vec3f | None = ...,
        timeToWayPoint: float | None = ...,
        gravityMult: float | None = ...,
        name: str | None = ...,
        collNode: CollisionNode | NodePath[CollisionNode] | None = ...,
    ) -> None: ...
    def testTrajectory(self) -> bool: ...
