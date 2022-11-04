from collections.abc import Callable
from typing import Any
from typing_extensions import Final, Literal

import wx  # type: ignore[import]
from .LevelEditor import LevelEditor

CLOSE_STDIN: Final[str]

class StartupError(Exception): ...

class Process:
    process: wx.Process
    b: list[str]
    def __init__(self, parent, cmd, end_callback) -> None: ...
    def Poll(self, input: str = ...) -> list[str]: ...
    def CloseInp(self) -> None: ...
    def Kill(self, ks: str = ...) -> tuple[Literal[1], None] | tuple[Literal[0], tuple[Any, Any, Any]]: ...

FROM_MAYA_TO_EGG: Final[Literal[0]]
FROM_BAM_TO_MAYA: Final[Literal[1]]

class MayaConverter(wx.Dialog):
    editor: LevelEditor
    obj = ...
    isAnim: bool
    callBack: Callable[[list[str]], object] | None
    mayaFile = ...
    mainPanel: wx.Panel
    output: wx.TextCtrl
    timer: wx.Timer
    process: Process
    def __init__(
        self,
        parent,
        editor: LevelEditor,
        mayaFile,
        callBack: Callable[[list[str]], object] | None = ...,
        obj=...,
        isAnim: bool = ...,
        convertMode: Literal[0, 1] = ...,
    ) -> None: ...
    def convertFromMaya(self) -> None: ...
    def convertToMaya(self) -> None: ...
    def onEgg2MayaEnded(self, evt) -> None: ...
    def onBam2EggEnded(self, evt) -> None: ...
    def onPoll(self, evt) -> None: ...
    def onModelProcessEnded(self, evt): ...
    def onProcessEnded(self, evt) -> None: ...
