__all__ = ['ShadowPlacer']

from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from panda3d.core import CollideMask, CollisionHandlerFloor, CollisionNode, CollisionRay, CollisionTraverser, NodePath
from .DirectObject import DirectObject

class ShadowPlacer(DirectObject):
    notify: ClassVar[Notifier]
    isActive: bool
    cTrav: CollisionTraverser
    shadowNodePath: NodePath
    cRay: CollisionRay
    cRayNodePath: NodePath[CollisionNode]
    cRayBitMask: CollideMask
    lifter: CollisionHandlerFloor
    def __init__(
        self,
        cTrav: CollisionTraverser,
        shadowNodePath: NodePath,
        wallCollideMask: object,
        floorCollideMask: CollideMask,
    ) -> None: ...
    def setup(
        self,
        cTrav: CollisionTraverser,
        shadowNodePath: NodePath,
        wallCollideMask: object,
        floorCollideMask: CollideMask,
    ) -> None: ...
    def delete(self) -> None: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def resetToOrigin(self) -> None: ...
