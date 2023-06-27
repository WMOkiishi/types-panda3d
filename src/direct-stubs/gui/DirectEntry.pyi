__all__ = ['DirectEntry']

from typing import Any, ClassVar, Final

from direct._typing import Unused
from panda3d.core import ConfigVariableBool, NodePath, TextFont

from .DirectFrame import DirectFrame
from .OnscreenText import OnscreenText

ENTRY_FOCUS_STATE: Final = 0
ENTRY_NO_FOCUS_STATE: Final = 1
ENTRY_INACTIVE_STATE: Final = 2

class DirectEntry(DirectFrame):
    directWtext: ClassVar[ConfigVariableBool]
    AllowCapNamePrefixes: ClassVar[tuple[str, ...]]
    ForceCapNamePrefixes: ClassVar[tuple[str, ...]]
    onscreenText: OnscreenText
    unicodeText: bool
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def setup(self) -> None: ...
    def updateWidth(self) -> None: ...
    def updateNumLines(self) -> None: ...
    def setFocus(self) -> None: ...
    def setCursorKeysActive(self) -> None: ...
    def setOverflowMode(self) -> None: ...
    def setObscureMode(self) -> None: ...
    def setBackgroundFocus(self) -> None: ...
    def setRolloverSound(self) -> None: ...
    def setClickSound(self) -> None: ...
    def commandFunc(self, event: Unused) -> None: ...
    def failedCommandFunc(self, event: Unused) -> None: ...
    def autoCapitalizeFunc(self) -> None: ...
    def focusInCommandFunc(self) -> None: ...
    def focusOutCommandFunc(self) -> None: ...
    def set(self, text: str) -> None: ...
    def get(self, plain: bool = False) -> str: ...
    def getCursorPosition(self) -> int: ...
    def setCursorPosition(self, pos: int) -> None: ...
    def getNumCharacters(self) -> int: ...
    def enterText(self, text: str) -> None: ...
    def getFont(self) -> TextFont: ...
    def getBounds(self, state: Unused = 0) -> tuple[float, float, float, float]: ...  # type: ignore[override]
