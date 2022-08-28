__all__ = [
    'LerpColorInterval',
    'LerpColorScaleInterval',
    'LerpFunc',
    'LerpFuncNS',
    'LerpFunctionInterval',
    'LerpFunctionNoStateInterval',
    'LerpHprInterval',
    'LerpHprScaleInterval',
    'LerpPosHprScaleInterval',
    'LerpPosHprScaleShearInterval',
    'LerpPosQuatScaleInterval',
    'LerpPosQuatScaleShearInterval',
    'LerpNodePathInterval',
    'LerpPosHprInterval',
    'LerpPosInterval',
    'LerpPosQuatInterval',
    'LerpQuatInterval',
    'LerpQuatScaleInterval',
    'LerpScaleInterval',
    'LerpShearInterval',
    'LerpTexOffsetInterval',
    'LerpTexRotateInterval',
    'LerpTexScaleInterval',
]

from collections.abc import Callable
from typing import Any, ClassVar, TypeVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import (
    ConfigVariableColor,
    LMatrix3f,
    LMatrix4f,
    LVecBase2f,
    LVecBase3f,
    LVecBase4f,
    NodePath,
    UnalignedLVecBase4f,
)
from panda3d.direct import CLerpNodePathInterval
from .Interval import Interval

_T = TypeVar('_T')
_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']
_EventType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow

class LerpNodePathInterval(CLerpNodePathInterval):
    lerpNodePathNum: ClassVar[int]
    def __init__(
        self,
        name: str | None,
        duration: float,
        blendType: _BlendType,
        bakeInStart: bool,
        fluid: bool,
        nodePath: NodePath,
        other: NodePath | None,
    ) -> None: ...
    def anyCallable(self, *params: object) -> bool: ...
    def setupParam(self, func: Callable[[_T], object], param: _T | Callable[[], _T]) -> None: ...

class LerpPosInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        startPos: _Vec3f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpHprInterval(LerpNodePathInterval):
    paramSetup: bool
    endHpr: _Vec3f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        hpr: _Vec3f,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpQuatInterval(LerpNodePathInterval):
    paramSetup: bool
    endQuat: _Vec4f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        quat = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
        hpr: _Vec3f | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        scale: _Vec3f | float,
        startScale: _Vec3f | float | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpShearInterval(LerpNodePathInterval):
    paramSetup: bool
    endShear: _Vec3f
    startShear: _Vec3f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        shear: _Vec3f,
        startShear: _Vec3f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpPosHprInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    endHpr: _Vec3f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        hpr: _Vec3f,
        startPos: _Vec3f | None = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpPosQuatInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    endQuat: _Vec4f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        quat = None,
        startPos: _Vec3f | None = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpHprScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endHpr: _Vec3f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        scale: _Vec3f | float,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        startScale: _Vec3f | float | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpQuatScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endQuat: _Vec4f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        quat: _Vec4f | None = None,
        scale=None,
        hpr=None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        startScale: _Vec3f | float | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpPosHprScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    endHpr: _Vec3f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        hpr: _Vec3f,
        scale: _Vec3f | float,
        startPos: _Vec3f | None = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        startScale: _Vec3f | float | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpPosQuatScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    endQuat: _Vec4f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        quat: _Vec4f | None = None,
        scale=None,
        startPos: _Vec3f | None = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        startScale: _Vec3f | float | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpPosHprScaleShearInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    endHpr: _Vec3f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    endShear: _Vec3f
    startShear: _Vec3f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        hpr: _Vec3f,
        scale: _Vec3f | float,
        shear: _Vec3f,
        startPos: _Vec3f | None = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        startScale: _Vec3f | float | None = None,
        startShear: _Vec3f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpPosQuatScaleShearInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: _Vec3f
    startPos: _Vec3f | None
    endQuat: _Vec4f
    startHpr: _Vec3f | None
    startQuat: _Vec4f | None
    endScale: _Vec3f | float
    startScale: _Vec3f | float | None
    endShear: _Vec3f
    startShear: _Vec3f | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: _Vec3f,
        quat: _Vec4f | None = None,
        scale=None,
        shear=None,
        startPos: _Vec3f | None = None,
        startHpr: _Vec3f | None = None,
        startQuat: _Vec4f | None = None,
        startScale: _Vec3f | float | None = None,
        startShear: _Vec3f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...

class LerpColorInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        color: _Vec4f | ConfigVariableColor,
        startColor: _Vec4f | ConfigVariableColor | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...

class LerpColorScaleInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        colorScale: _Vec4f | ConfigVariableColor,
        startColorScale: _Vec4f | ConfigVariableColor | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...

class LerpTexOffsetInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        texOffset: LVecBase2f,
        startTexOffset: LVecBase2f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...

class LerpTexRotateInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        texRotate: float,
        startTexRotate: float | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...

class LerpTexScaleInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        texScale: LVecBase2f,
        startTexScale: LVecBase2f | None = None,
        other: NodePath | None = None,
        blendType: _BlendType = 'noBlend',
        bakeInStart: bool = True,
        fluid: bool = False,
        name: str | None = None,
    ) -> None: ...

class LerpFunctionNoStateInterval(Interval):
    lerpFunctionIntervalNum: ClassVar[int]
    function: Callable[..., object]
    fromData: float
    toData: float
    blendType: _BlendType
    extraArgs = ...
    def __init__(
        self,
        function: Callable[..., object],
        duration: float = 0,
        fromData: float = 0,
        toData: float = 1,
        blendType: _BlendType = 'noBlend',
        extraArgs: list[Any] = ...,
        name: str | None = None,
    ) -> None: ...
    def privStep(self, t: float) -> None: ...

class LerpFuncNS(LerpFunctionNoStateInterval): ...

class LerpFunctionInterval(Interval):
    lerpFunctionIntervalNum: ClassVar[int]
    function: Callable[..., object]
    fromData: float
    toData: float
    blendType: _BlendType
    extraArgs = ...
    def __init__(
        self,
        function: Callable[..., object],
        duration: float = 0,
        fromData: float = 0,
        toData: float = 1,
        blendType: _BlendType = 'noBlend',
        extraArgs: list[Any] = ...,
        name: str | None = None,
    ) -> None: ...
    def privStep(self, t: float) -> None: ...

class LerpFunc(LerpFunctionInterval): ...
