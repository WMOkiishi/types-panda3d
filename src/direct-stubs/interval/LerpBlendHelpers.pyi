__all__ = ['getBlend']

from typing import overload
from typing_extensions import Literal

from panda3d.direct import EaseInBlendType, EaseInOutBlendType, EaseOutBlendType, NoBlendType

easeIn: EaseInBlendType
easeOut: EaseOutBlendType
easeInOut: EaseInOutBlendType
noBlend: NoBlendType

@overload
def getBlend(blendType: Literal['easeIn']) -> EaseInBlendType: ...
@overload
def getBlend(blendType: Literal['easeOut']) -> EaseOutBlendType: ...
@overload
def getBlend(blendType: Literal['easeInOut']) -> EaseInOutBlendType: ...
@overload
def getBlend(blendType: Literal['noBlend']) -> NoBlendType: ...
