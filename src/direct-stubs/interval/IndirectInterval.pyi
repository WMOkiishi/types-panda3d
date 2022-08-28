__all__ = ['IndirectInterval']

from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.direct import LerpBlendType
from .Interval import Interval

_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']

class IndirectInterval(Interval):
    indirectIntervalNum: ClassVar[int]
    interval: Interval
    startAtSTart: bool
    endAtEnd: bool
    startT: float
    endT: float
    deltaT: float
    blendType: LerpBlendType
    def __init__(
        self,
        interval: Interval,
        startT: float = 0,
        endT: float | None = None,
        playRate: float = 1,
        duration: float | None = None,
        blendType: _BlendType = 'noBlend',
        name: str | None = None,
    ) -> None: ...
    def privInitialize(self, t: float) -> None: ...
    def privInstant(self) -> None: ...
    def privFinalize(self) -> None: ...
    def privReverseInitialize(self, t: float) -> None: ...
    def privReverseInstant(self) -> None: ...
    def privReverseFinalize(self) -> None: ...
    def privInterrupt(self) -> None: ...
