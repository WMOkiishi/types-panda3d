from collections.abc import Callable
from typing import Any
from typing_extensions import Final, Literal

import wx  # type: ignore[import]
import wx.siplib as sip  # type: ignore[import]
from direct._typing import Obj, Unused

from .LevelEditor import LevelEditor

CLOSE_STDIN: Final[str]
FROM_MAYA_TO_EGG: Final[Literal[0]]
FROM_BAM_TO_MAYA: Final[Literal[1]]

class StartupError(Exception): ...

class Process:
    process: wx.Process
    b: list[str]
    def __init__(self, parent, cmd, end_callback) -> None: ...
    def Poll(self, input: str = ...) -> list[str]: ...
    def CloseInp(self) -> None: ...
    def Kill(self, ks: str = ...) -> tuple[Literal[1], None] | tuple[Literal[0], tuple[Any, Any, Any]]: ...

class MayaConverter(wx.Dialog, metaclass=sip.wrapper):
    editor: LevelEditor
    obj: Obj
    isAnim: bool
    callBack: Callable[[list[str]], object] | None
    mayaFile: str
    mainPanel: wx.Panel
    output: wx.TextCtrl
    timer: wx.Timer
    process: Process
    def __init__(
        self,
        parent: Any,
        editor: LevelEditor,
        mayaFile: str,
        callBack: Callable[[list[str]], object] | None = ...,
        obj: Obj | None = ...,
        isAnim: bool = ...,
        convertMode: Literal[0, 1] = ...,
    ) -> None: ...
    def convertFromMaya(self) -> None: ...
    def convertToMaya(self) -> None: ...
    def onEgg2MayaEnded(self, evt: Unused) -> None: ...
    def onBam2EggEnded(self, evt: Unused) -> None: ...
    def onPoll(self, evt: Unused) -> None: ...
    def onModelProcessEnded(self, evt: Unused): ...
    def onProcessEnded(self, evt: Unused) -> None: ...
