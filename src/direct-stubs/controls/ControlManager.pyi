from typing import ClassVar
from typing_extensions import Literal

from panda3d.core import ConfigVariableBool
from ..directnotify.Notifier import Notifier

CollisionHandlerRayStart: float

class ControlManager:
    notify: ClassVar[Notifier]
    wantWASD: ClassVar[ConfigVariableBool]
    passMessagesThrough: bool
    inputStateTokens: list
    WASDTurnTokens: list
    controls: dict
    currentControls = ...
    currentControlsName: str | None
    isEnabled: bool
    forceAvJumpToken = ...
    def __init__(self, enable: bool = True, passMessagesThrough: bool = False) -> None: ...
    def __str__(self) -> str: ...
    def add(self, controls, name: str = 'basic') -> None: ...
    def get(self, name: str): ...
    def remove(self, name: str) -> None: ...
    def use(self, name: str, avatar) -> None: ...
    def setSpeeds(self): ...
    def getIsAirborne(self) -> bool: ...
    def setTag(self, key, value) -> None: ...
    def deleteCollisions(self) -> None: ...
    def collisionsOn(self) -> None: ...
    def collisionsOff(self) -> None: ...
    def placeOnFloor(self) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def stop(self) -> None: ...
    def disableAvatarJump(self) -> None: ...
    def enableAvatarJump(self) -> None: ...
    def monitor(self, foo: object) -> Literal[1]: ...
    def setWASDTurn(self, turn: bool) -> None: ...
