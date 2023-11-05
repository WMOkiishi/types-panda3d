__all__ = ['DirectSlider']

from collections.abc import Callable, Iterable
from typing import Any, Literal
from typing_extensions import Unpack

from panda3d.core import NodePath, PGSliderBar

from ._typing import FrameKeywords
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

class DirectSlider(DirectFrame[PGSliderBar]):
    thumb: DirectButton
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], PGSliderBar] = ...,
        range: tuple[float, float] = (0, 1),
        value: float = 0,
        scrollSize: float = 0.01,
        pageSize: float = 0.1,
        orientation: Literal['horizontal', 'vertical', 'vertical_inverted'] = 'horizontal',
        command: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def setRange(self) -> None: ...
    def setValue(self, value: float) -> None: ...
    def getValue(self) -> float: ...
    def getRatio(self) -> float: ...
    def setScrollSize(self) -> None: ...
    def setPageSize(self) -> None: ...
    def setOrientation(self) -> None: ...
    def commandFunc(self) -> None: ...
