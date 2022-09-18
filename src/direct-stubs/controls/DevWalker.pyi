from typing import ClassVar
from typing_extensions import Literal

from panda3d.core import CollisionTraverser, ConfigVariableBool, LVector3f, PythonTask
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

class DevWalker(DirectObject):
    notify: ClassVar[Notifier]
    wantDebugIndicator: ClassVar[ConfigVariableBool]
    runMultiplier: ClassVar[ConfigVariableBool]
    slideName: ClassVar[str]
    speed: float
    rotationSpeed: float
    slideSpeed: float
    vel: LVector3f
    task: PythonTask | None
    avatarControlForwardSpeed: float
    avatarControlReverseSpeed: float
    avatarControlRotateSpeed: float
    avatar = ...
    cTrav: CollisionTraverser
    avatarNodePath = ...
    liftSpeed: float
    def __init__(self) -> None: ...
    def setWalkSpeed(self, forward: float, jump: object, reverse: float, rotate: float) -> None: ...
    def getSpeeds(self) -> tuple[float, float, float]: ...
    def setAvatar(self, avatar) -> None: ...
    def setWallBitMask(self, bitMask: object) -> None: ...
    def setFloorBitMask(self, bitMask: object) -> None: ...
    def initializeCollisions(
        self,
        collisionTraverser: CollisionTraverser,
        avatarNodePath,
        avatarRadius: float = 1.4,
        floorOffset: float = 1,
        reach: float = 1,
    ) -> None: ...
    def setAirborneHeightFunc(self, getAirborneHeight: object) -> None: ...
    def deleteCollisions(self) -> None: ...
    def setTag(self, key: object, value: object) -> None: ...
    def setCollisionsActive(self, active: object = 1) -> None: ...
    def placeOnFloor(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def addBlastForce(self, vector: object) -> None: ...
    def displayDebugInfo(self) -> None: ...
    def handleAvatarControls(self, task: object) -> Literal[1]: ...
    def enableAvatarControls(self) -> None: ...
    def disableAvatarControls(self) -> None: ...
    def flushEventHandlers(self) -> None: ...