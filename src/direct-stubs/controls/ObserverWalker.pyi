from typing import ClassVar

from panda3d.core import CollisionTraverser
from ..directnotify.Notifier import Notifier
from .NonPhysicsWalker import NonPhysicsWalker

class ObserverWalker(NonPhysicsWalker):
    notify: ClassVar[Notifier]
    slideName: str
    def initializeCollisions(
        self,
        collisionTraverser: CollisionTraverser,
        avatarNodePath,
        avatarRadius: float = 1.4,
        floorOffset: float = 1,
        reach: float = 1,
    ) -> None: ...
    def deleteCollisions(self) -> None: ...
    def setCollisionsActive(self, active: bool = True) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def enableAvatarControls(self) -> None: ...
    def disableAvatarControls(self) -> None: ...
