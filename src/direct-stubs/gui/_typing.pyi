from collections.abc import Callable, Container, Iterable, Sequence
from typing import Any, Literal, TypedDict, TypeVar
from typing_extensions import TypeAlias

from panda3d._typing import Vec2Like, Vec3Like, Vec4Like
from panda3d.core import AudioSound, NodePath, PGButton, PGItem, Texture

PGItemT = TypeVar('PGItemT', bound=PGItem, default=PGItem)  # noqa: Y001
ReliefStyle: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 'flat', 'raised', 'sunken', 'groove', 'ridge', 'texture_border'] | None
_MaybeImage: TypeAlias = NodePath | Texture | tuple[str, str] | str | None
_MaybeGeom: TypeAlias = NodePath | str | None
MaybeImageOrSequence: TypeAlias = _MaybeImage | Sequence[_MaybeImage]
MaybeGeomOrSequence: TypeAlias = _MaybeGeom | Sequence[_MaybeGeom]

class GuiWidgetKeywords(TypedDict, total=False):
    numStates: int
    invertedFrames: Container[int]
    sortOrder: int
    state: Literal['normal', 'disabled'] | bool
    relief: ReliefStyle
    borderWidth: Vec2Like
    borderUvWidth: Vec2Like
    frameSize: Vec4Like | None
    frameColor: Vec4Like | Sequence[Vec4Like]
    frameTexture: Texture | str | Sequence[Texture | str] | None
    frameVisibleScale: Vec2Like
    pad: Vec2Like
    guiId: str | None
    pos: Vec3Like | None
    hpr: Vec3Like | None
    scale: Vec3Like | float | None
    color: Vec4Like | None
    suppressMouse: bool
    suppressKeys: bool
    enableEdit: bool

class FrameKeywords(GuiWidgetKeywords, total=False):
    image: MaybeImageOrSequence
    geom: MaybeGeomOrSequence
    text: str | Sequence[str] | None
    textMayChange: bool

class ButtonKeywords(FrameKeywords, total=False):
    pgFunc: Callable[[str], PGButton]
    command: Callable[..., object] | None
    extraArgs: Iterable[Any]
    commandButtons: Container[int]
    rolloverSound: AudioSound | None
    clickSound: AudioSound | None
    pressEffect: bool
