from collections.abc import Callable
from typing import Any, ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import (
    BitMask_uint32_t_32,
    CollisionHandlerFloor,
    CollisionHandlerQueue,
    CollisionNode,
    CollisionRay,
    CollisionSphere,
    CollisionTraverser,
    ConfigVariableBool,
    LVector3f,
    NodePath,
)
from panda3d.physics import ActorNode, PhysicsCollisionHandler, PhysicsManager
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

_Unused: TypeAlias = object

class PhysicsWalker(DirectObject):
    notify: ClassVar[Notifier]
    wantDebugIndicator: ClassVar[ConfigVariableBool]
    useLifter: ClassVar[bool]
    useHeightRay: ClassVar[bool]
    needToDeltaPos: bool
    physVelocityIndicator: NodePath
    avatarControlForwardSpeed: float
    avatarControlJumpForce: float
    avatarControlReverseSpeed: float
    avatarControlRotateSpeed: float
    getAirborneHeight: Callable[[], float] | None
    collisionsActive: bool
    isAirborne: bool
    highMark: float
    cRay: CollisionRay
    cRayNodePath: NodePath[CollisionNode]
    cRayBitMask: BitMask_uint32_t_32
    lifter: CollisionHandlerFloor
    cRayQueue: CollisionHandlerQueue
    avatarRadius: float
    cSphere: CollisionSphere
    cSphereNodePath: NodePath[CollisionNode]
    cSphereBitMask: BitMask_uint32_t_32
    pusher: PhysicsCollisionHandler
    actorNode: ActorNode
    phys: PhysicsManager
    cTrav: CollisionTraverser
    floorOffset: float
    avatarNodePath: NodePath[ActorNode]
    physContactIndicator: NodePath
    def __init__(self, gravity: float = ..., standableGround: float = ..., hardLandingForce: float = ...) -> None: ...
    def setWalkSpeed(self, forward: float, jump: float, reverse: float, rotate: float) -> None: ...
    def getSpeeds(self) -> tuple[float, float]: ...
    def setAvatar(self, avatar: Any) -> None: ...
    def setupRay(self, floorBitmask: BitMask_uint32_t_32, floorOffset: float) -> None: ...
    def determineHeight(self) -> float: ...
    def setupSphere(self, bitmask: BitMask_uint32_t_32, avatarRadius: float) -> None: ...
    def setupPhysics(self, avatarNodePath: NodePath[ActorNode]) -> NodePath[ActorNode]: ...
    def initializeCollisions(
        self,
        collisionTraverser: CollisionTraverser,
        avatarNodePath: NodePath[ActorNode],
        avatarRadius: float = ...,
        floorOffset: float = ...,
        reach: float = ...,
    ) -> None: ...
    def setAirborneHeightFunc(self, getAirborneHeight: Callable[[], float]) -> None: ...
    def setAvatarPhysicsIndicator(self, indicator: NodePath) -> None: ...
    def avatarPhysicsIndicator(self, task: _Unused) -> Literal[1]: ...
    def deleteCollisions(self) -> None: ...
    def setCollisionsActive(self, active: bool = True) -> None: ...
    def getCollisionsActive(self) -> bool: ...
    def placeOnFloor(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def addBlastForce(self, vector: _Unused) -> None: ...
    def displayDebugInfo(self) -> None: ...
    def handleAvatarControls(self, task: _Unused) -> Literal[1]: ...
    def doDeltaPos(self) -> None: ...
    def setPriorParentVector(self) -> None: ...
    def reset(self) -> None: ...
    def getVelocity(self) -> LVector3f: ...
    def enableAvatarControls(self) -> None: ...
    def disableAvatarControls(self) -> None: ...
    def flushEventHandlers(self) -> None: ...
