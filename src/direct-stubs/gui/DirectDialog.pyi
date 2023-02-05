__all__ = [
    'DirectDialog',
    'OkCancelDialog',
    'OkDialog',
    'RetryCancelDialog',
    'YesNoCancelDialog',
    'YesNoDialog',
    'cleanupDialog',
    'findDialog',
]

from typing import Any, ClassVar

from direct._typing import Unused
from panda3d.core import NodePath

from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

def findDialog(uniqueName: str) -> DirectDialog: ...
def cleanupDialog(uniqueName: str) -> None: ...

class DirectDialog(DirectFrame):
    AllDialogs: ClassVar[dict[str, DirectDialog]]
    PanelIndex: ClassVar[int]
    numButtons: int
    buttonList: list[DirectButton]
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def configureDialog(self) -> None: ...
    def show(self) -> None: ...  # type: ignore[override]
    def hide(self) -> None: ...  # type: ignore[override]
    def buttonCommand(self, value: Any, event: Unused = None) -> None: ...
    def setMessage(self, message: str) -> None: ...
    def cleanup(self) -> None: ...

class OkDialog(DirectDialog): ...
class OkCancelDialog(DirectDialog): ...
class YesNoDialog(DirectDialog): ...
class YesNoCancelDialog(DirectDialog): ...
class RetryCancelDialog(DirectDialog): ...
