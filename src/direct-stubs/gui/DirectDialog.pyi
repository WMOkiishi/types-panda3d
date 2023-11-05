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

from _typeshed import Unused
from collections.abc import Callable, Iterable, Sequence
from typing import Any, ClassVar, Literal
from typing_extensions import TypeAlias, Unpack

from panda3d._typing import Vec4Like
from panda3d.core import NodePath

from ._typing import FrameKeywords, PGItemT, ReliefStyle
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

_TextProperties_Alignment: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

def findDialog(uniqueName: str) -> DirectDialog: ...
def cleanupDialog(uniqueName: str) -> None: ...

class DirectDialog(DirectFrame[PGItemT]):
    AllDialogs: ClassVar[dict[str, DirectDialog]]
    PanelIndex: ClassVar[int]
    numButtons: int
    buttonList: list[DirectButton]
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], PGItemT] = ...,
        dialogName: str = ...,
        text_align: _TextProperties_Alignment = 0,
        text_scale: float = 0.06,
        buttonTextList: Sequence[str | None] = ...,
        buttonGeomList=...,
        buttonImageList=...,
        buttonValueList=...,
        buttonHotKeyList=...,
        button_borderWidth: tuple[float, float] = (0.01, 0.01),
        button_pad: tuple[float, float] = (0.01, 0.01),
        button_relief: ReliefStyle = 2,
        button_text_scale: float = 0.06,
        buttonSize: Vec4Like | None = None,
        topPad: float = 0.06,
        midPad: float = 0.12,
        sidePad: float = 0.0,
        buttonPadSF: float = 1.1,
        fadeScreen: bool = False,
        command: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def configureDialog(self) -> None: ...
    def show(self) -> None: ...  # type: ignore[override]
    def hide(self) -> None: ...  # type: ignore[override]
    def buttonCommand(self, value: Any, event: Unused = None) -> None: ...
    def setMessage(self, message: str | Sequence[str] | None) -> None: ...
    def cleanup(self) -> None: ...

class OkDialog(DirectDialog): ...
class OkCancelDialog(DirectDialog): ...
class YesNoDialog(DirectDialog): ...
class YesNoCancelDialog(DirectDialog): ...
class RetryCancelDialog(DirectDialog): ...
