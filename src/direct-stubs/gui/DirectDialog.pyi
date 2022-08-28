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

from panda3d.core import NodePath
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

def findDialog(uniqueName: str) -> DirectDialog: ...
def cleanupDialog(uniqueName: str) -> None: ...

class DirectDialog(DirectFrame):
    AllDialogs: ClassVar[dict]
    PanelIndex: ClassVar[int]
    numButtons: int
    buttonList: list[DirectButton]
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def configureDialog(self) -> None: ...
    def buttonCommand(self, value, event: object = None) -> None: ...
    def setMessage(self, message: str) -> None: ...
    def cleanup(self) -> None: ...

class OkDialog(DirectDialog):
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...

class OkCancelDialog(DirectDialog):
    def __init__(self, parent: NodePath | None, **kw: Any) -> None: ...

class YesNoDialog(DirectDialog):
    def __init__(self, parent: NodePath | None, **kw: Any) -> None: ...

class YesNoCancelDialog(DirectDialog):
    def __init__(self, parent: NodePath | None, **kw: Any) -> None: ...

class RetryCancelDialog(DirectDialog):
    def __init__(self, parent: NodePath | None, **kw: Any) -> None: ...
