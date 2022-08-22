from typing import ClassVar
from typing_extensions import Literal

from panda3d.core import ConfigVariableBool
from ..directnotify.Notifier import Notifier
from .GravityWalker import GravityWalker

class TwoDWalker(GravityWalker):
    notify: ClassVar[Notifier]
    wantDebugIndicator: ClassVar[ConfigVariableBool]
    wantFloorSphere: ClassVar[ConfigVariableBool]
    earlyEventSphere: ClassVar[ConfigVariableBool]
    def __init__(
        self,
        gravity: float = -32.1740,
        standableGround: float = 0.707,
        hardLandingForce: float = 16.0,
    ) -> None: ...
    def handleAvatarControls(self, task: object) -> Literal[1]: ...
    def jumpPressed(self) -> None: ...
