__all__ = ['BlackOnWhite', 'NameConfirm', 'OnscreenText', 'Plain', 'ScreenPrompt', 'ScreenTitle']

from typing import Any, overload
from typing_extensions import Literal, TypeAlias

from panda3d.core import LVecBase4f, NodePath, TextFont, TextNode

_Alignment: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_Color: TypeAlias = LVecBase4f | tuple[float, float, float, float]
_OldBool: TypeAlias = Literal[0, 1]
_OrderedPair: TypeAlias = tuple[float, float]

Plain: Literal[1]
ScreenTitle: Literal[2]
ScreenPrompt: Literal[3]
NameConfirm: Literal[4]
BlackOnWhite: Literal[5]

class OnscreenText(NodePath[TextNode]):
    textNode: TextNode
    mayChange: bool | _OldBool
    isClean: bool | _OldBool
    decal: bool
    font: TextFont
    text: str
    text_pos: _OrderedPair
    text_r: float
    roll: float
    text_scale: _OrderedPair
    scale: _OrderedPair
    wordwrap: float
    fg: LVecBase4f
    bg: LVecBase4f
    shadow: LVecBase4f
    frame: LVecBase4f
    align: _Alignment
    unicodeText: Literal[True]
    def __init__(
        self,
        text: str = '',
        style: int = 1,
        pos: _OrderedPair = (0, 0),
        roll: float = 0,
        scale: float | _OrderedPair | None = None,
        fg: _Color | None = None,
        bg: _Color | None = None,
        shadow: _Color | None = None,
        shadowOffset: _OrderedPair = (0.04, 0.04),
        frame: _Color | None = None,
        align: _Alignment | None = None,
        wordwrap: float | None = None,
        drawOrder: int | None = None,
        decal: bool = False,
        font: TextFont | None = None,
        parent: NodePath | None = None,
        sort: int = 0,
        mayChange: bool = True,
        direction: Literal['LTR', 'RTL', 'ltr', 'rtl', None] = None,
    ) -> None: ...
    def cleanup(self) -> None: ...
    def destroy(self) -> None: ...
    def freeze(self) -> None: ...
    def thaw(self) -> None: ...
    def setDecal(self, decal: bool) -> None: ...
    def getDecal(self) -> bool: ...
    def setFont(self, font: TextFont) -> None: ...
    def getFont(self) -> TextFont: ...
    def clearText(self) -> None: ...
    def setText(self, text: str) -> None: ...
    def appendText(self, text: str) -> None: ...
    def getText(self) -> str: ...
    def setTextX(self, x: float) -> None: ...
    def setX(self, x: float) -> None: ...
    def setTextY(self, x: float) -> None: ...
    def setY(self, x: float) -> None: ...
    @overload
    def setTextPos(self, x: float, y: float) -> None: ...
    @overload
    def setTextPos(self, x: _OrderedPair, y: None = None) -> None: ...
    def getTextPos(self) -> _OrderedPair: ...
    def setPos(self, x: float, y: float) -> None: ...
    def getPos(self) -> _OrderedPair: ...
    @property
    def pos(self) -> _OrderedPair: ...
    def setTextR(self, r: float) -> None: ...
    def getTextR(self) -> float: ...
    def setRoll(self, roll: float) -> None: ...
    def getRoll(self) -> float: ...
    @overload
    def setTextScale(self, sx: float | _OrderedPair, sy: None = None) -> None: ...
    @overload
    def setTextScale(self, sx: float, sy: float) -> None: ...
    def getTextScale(self) -> _OrderedPair: ...
    @overload
    def setScale(self, sx: float | _OrderedPair, sy: None = None) -> None: ...
    @overload
    def setScale(self, sx: float, sy: float) -> None: ...
    def getScale(self) -> _OrderedPair: ...
    def updateTransformMat(self) -> None: ...
    def setWordwrap(self, wordwrap: float) -> None: ...
    def getWordwrap(self) -> float: ...
    def setFg(self, fg: _Color) -> None: ...
    def setBg(self, bg: _Color) -> None: ...
    def setShadow(self, shadow: _Color) -> None: ...
    def setFrame(self, frame: _Color) -> None: ...
    def configure(self, option: object = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    cget = __getitem__
    def setALign(self, align: float) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
