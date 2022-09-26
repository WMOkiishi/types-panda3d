__all__ = ['ShadowPlacer']

from typing import ClassVar

from panda3d.core import BitMask_uint32_t_32, CollisionHandlerFloor, CollisionNode, CollisionRay, CollisionTraverser, NodePath
from ..directnotify.Notifier import Notifier
from .DirectObject import DirectObject

class ShadowPlacer(DirectObject):
    notify: ClassVar[Notifier]
    isActive: bool
    cTrav: CollisionTraverser
    shadowNodePath: NodePath
    cRay: CollisionRay
    cRayNodePath: NodePath[CollisionNode]
    cRayBitMask: BitMask_uint32_t_32
    lifter: CollisionHandlerFloor
    def __init__(
        self,
        cTrav: CollisionTraverser,
        shadowNodePath: NodePath,
        wallCollideMask: object,
        floorCollideMask: BitMask_uint32_t_32,
    ) -> None: ...
    def setup(
        self,
        cTrav: CollisionTraverser,
        shadowNodePath: NodePath,
        wallCollideMask: object,
        floorCollideMask: BitMask_uint32_t_32,
    ) -> None: ...
    def delete(self) -> None: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def resetToOrigin(self) -> None: ...
