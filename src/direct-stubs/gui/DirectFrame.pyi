__all__ = ['DirectFrame']

from collections.abc import Sequence
from typing import Any, ClassVar, Union
from typing_extensions import Literal, TypeAlias

from panda3d.core import NodePath, Texture
from .DirectGuiBase import DirectGuiWidget

_MaybeGeom: TypeAlias = NodePath | str | None
_MaybeImage: TypeAlias = Union[NodePath, Texture, tuple[str, str], str, None]

class DirectFrame(DirectGuiWidget):
    DefDynGroups: ClassVar[tuple[Literal['text'], Literal['geom'], Literal['image']]]
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def clearText(self) -> None: ...
    def setText(self, text: str | Sequence[str] | None = None) -> None: ...
    def clearGeom(self) -> None: ...
    def setGeom(self, geom: _MaybeGeom | Sequence[_MaybeGeom] = None) -> None: ...
    def clearImage(self) -> None: ...
    def setImage(self, image: _MaybeImage | Sequence[_MaybeImage] = None) -> None: ...
