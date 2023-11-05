__all__ = ['DirectCheckButton']

from _typeshed import SupportsGetItem
from typing import Literal
from typing_extensions import Unpack

from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import NodePath

from ._typing import ButtonKeywords, MaybeImageOrSequence, ReliefStyle
from .DirectButton import DirectButton

class DirectCheckButton(DirectButton):
    colors: SupportsGetItem[int, Vec4Like] | None
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        indicatorValue: int = 0,
        boxBorder: float = 0,
        boxPlacement: Literal['left', 'below', 'right', 'above'] = 'left',
        boxImage: MaybeImageOrSequence = None,
        boxImageScale: Vec3Like | float | None = 1,
        boxImageColor: Vec4Like | None = None,
        boxRelief: ReliefStyle = 'sunken',
        **kw: Unpack[ButtonKeywords],
    ) -> None: ...
    def setIndicatorValue(self) -> None: ...
