__all__ = ['OnScreenDebug']

from typing import Any, ClassVar, Literal

from direct.gui.OnscreenText import OnscreenText
from panda3d.core import ConfigVariableBool

class OnScreenDebug:
    enabled: ClassVar[ConfigVariableBool]
    onScreenText: OnscreenText | None
    frame: int
    text: str
    data: dict[str, tuple[int, Any]]
    def __init__(self) -> None: ...
    def load(self) -> None: ...
    def render(self) -> None: ...
    def clear(self) -> None: ...
    def add(self, key: str, value: Any) -> Literal[1]: ...
    def has(self, key: str) -> bool: ...
    def remove(self, key: str) -> None: ...
    def removeAllWithPrefix(self, prefix: str) -> None: ...
    def append(self, text: str) -> None: ...
