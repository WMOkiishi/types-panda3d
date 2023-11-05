__all__ = ['DirectRadioButton']

from _typeshed import SupportsGetItem
from collections.abc import Iterable, MutableSequence, Sequence
from typing import Any, Generic, Literal, TypeVar
from typing_extensions import Unpack

from panda3d._typing import Vec4Like
from panda3d.core import NodePath

from ._typing import ButtonKeywords, MaybeGeomOrSequence, MaybeImageOrSequence, ReliefStyle
from .DirectButton import DirectButton
from .DirectLabel import DirectLabel

_T = TypeVar('_T', default=Any)

class DirectRadioButton(DirectButton, Generic[_T]):
    colors: SupportsGetItem[int, Vec4Like] | None
    indicator: DirectLabel
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        indicatorValue: int = 0,
        variable: MutableSequence[_T] = ...,
        value: Sequence[_T] = ...,
        others: Iterable[DirectRadioButton[_T]] = ...,
        boxBorder: float = 0,
        boxPlacement: Literal['left', 'below', 'right', 'above'] = 'left',
        boxGeom: MaybeGeomOrSequence = None,
        boxGeomColor: Vec4Like | None = None,
        boxGeomScale: float = 1.0,
        boxImage: MaybeImageOrSequence = None,
        boxImageScale: float = 1.0,
        boxImageColor: Vec4Like = ...,
        boxRelief: ReliefStyle = None,
        **kw: Unpack[ButtonKeywords],
    ) -> None: ...
    def check(self) -> None: ...
    def setOthers(self, others: Iterable[DirectRadioButton[_T]]) -> None: ...
    def uncheck(self) -> None: ...
    def setIndicatorValue(self) -> None: ...
