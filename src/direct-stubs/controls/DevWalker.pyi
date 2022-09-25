from typing import Any, ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import CollisionTraverser, ConfigVariableBool, ConfigVariableDouble, LVector3f, NodePath, PythonTask
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

_Unused: TypeAlias = object

class DevWalker(DirectObject):
    notify: ClassVar[Notifier]
    wantDebugIndicator: ClassVar[ConfigVariableBool]
    runMultiplier: ClassVar[ConfigVariableDouble]
    slideName: ClassVar[str]
    speed: float
    rotationSpeed: float
    slideSpeed: float
    vel: LVector3f
    task: PythonTask | None
    avatarControlForwardSpeed: float
    avatarControlReverseSpeed: float
    avatarControlRotateSpeed: float
    avatar: Any
    cTrav: CollisionTraverser
    avatarNodePath: NodePath
    liftSpeed: float
    def __init__(self) -> None: ...
    def setWalkSpeed(self, forward: float, jump: _Unused, reverse: float, rotate: float) -> None: ...
    def getSpeeds(self) -> tuple[float, float, float]: ...
    def setAvatar(self, avatar: Any) -> None: ...
    def setWallBitMask(self, bitMask: _Unused) -> None: ...
    def setFloorBitMask(self, bitMask: _Unused) -> None: ...
    def initializeCollisions(
        self,
        collisionTraverser: CollisionTraverser,
        avatarNodePath: NodePath,
        wallCollideMask: _Unused,
        floorCollideMask: _Unused,
        avatarRadius: _Unused = ...,
        floorOffset: _Unused = ...,
        reach: _Unused = ...,
    ) -> None: ...
    def setAirborneHeightFunc(self, getAirborneHeight: _Unused) -> None: ...
    def deleteCollisions(self) -> None: ...
    def setTag(self, key: _Unused, value: _Unused) -> None: ...
    def setCollisionsActive(self, active: _Unused = ...) -> None: ...
    def placeOnFloor(self) -> None: ...
    def oneTimeCollide(self) -> None: ...
    def addBlastForce(self, vector: _Unused) -> None: ...
    def displayDebugInfo(self) -> None: ...
    def handleAvatarControls(self, task: _Unused) -> Literal[1]: ...
    def enableAvatarControls(self) -> None: ...
    def disableAvatarControls(self) -> None: ...
    def flushEventHandlers(self) -> None: ...
