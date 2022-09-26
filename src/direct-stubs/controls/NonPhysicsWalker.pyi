from collections.abc import Callable
from typing import Any, ClassVar
from typing_extensions import Literal, TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import (
    BitMask_uint32_t_32,
    CollisionHandlerFloor,
    CollisionHandlerPusher,
    CollisionNode,
    CollisionRay,
    CollisionSphere,
    CollisionTraverser,
    ConfigVariableBool,
    LVector3f,
    NodePath,
)

_Unused: TypeAlias = object

class NonPhysicsWalker(DirectObject):
    notify: ClassVar[Notifier]
    wantDebugIndicator: ClassVar[ConfigVariableBool]
    slideName: ClassVar[str]
    worldVelocity: LVector3f
    collisionsActive: bool
    speed: float
    rotationSpeed: float
    slideSpeed: float
    vel: LVector3f
    stopThisFrame: bool
    avatarControlForwardSpeed: float
    avatarControlReverseSpeed: float
    avatarControlRotateSpeed: float
    avatar: Any
    avatarNodePath: NodePath
    getAirborneHeight: Callable[[], float]
    cTrav: CollisionTraverser
    cSphere: CollisionSphere
    cSphereNodePath: NodePath[CollisionNode]
    cSphereBitMask: BitMask_uint32_t_32
    cRay: CollisionRay
    cRayNodePath: NodePath[CollisionNode]
    cRayBitMask: BitMask_uint32_t_32
    pusher: CollisionHandlerPusher
    lifter: CollisionHandlerFloor
    def __init__(self) -> None: ...
    def setWalkSpeed(self, forward: float, jump: _Unused, reverse: float, rotate: float) -> None: ...
    def getSpeeds(self) -> tuple[float, float, float]: ...
    def setAvatar(self, avatar: Any) -> None: ...
    def setAirborneHeightFunc(self, getAirborneHeight: Callable[[], float]) -> None: ...
    def setWallBitMask(self, bitMask: BitMask_uint32_t_32) -> None: ...
    def setFloorBitMask(self, bitMask: BitMask_uint32_t_32) -> None: ...
    def swapFloorBitMask(self, oldMask: BitMask_uint32_t_32, newMask: BitMask_uint32_t_32) -> None: ...
    def initializeCollisions(
        self,
        collisionTraverser: CollisionTraverser,
        avatarNodePath: NodePath,
        avatarRadius: float = ...,
        floorOffset: float = ...,
        reach: float = ...,
    ) -> None: ...
    def deleteCollisions(self) -> None: ...
    def setTag(self, key: str, value: str) -> None: ...
    def setCollisionsActive(self, active: bool = True) -> None: ...
    def placeOnFloor(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def addBlastForce(self, vector: _Unused) -> None: ...
    def displayDebugInfo(self) -> None: ...
    def handleAvatarControls(self, task: _Unused) -> Literal[1]: ...
    def doDeltaPos(self) -> None: ...
    def reset(self) -> None: ...
    def getVelocity(self) -> LVector3f: ...
    def enableAvatarControls(self) -> None: ...
    def disableAvatarControls(self) -> None: ...
    def flushEventHandlers(self) -> None: ...
