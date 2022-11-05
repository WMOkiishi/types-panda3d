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

from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import ConfigVariableColor, LQuaternionf, LVecBase2f, NodePath
from panda3d.direct import CLerpNodePathInterval

from .Interval import Interval

_T = TypeVar('_T')
_BlendType: TypeAlias = Literal['easeIn', 'easeOut', 'easeInOut', 'noBlend']
_EventType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]

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
    endPos: Vec3Like
    startPos: Vec3Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        startPos: Vec3Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpHprInterval(LerpNodePathInterval):
    paramSetup: bool
    endHpr: Vec3Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        hpr: Vec3Like,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpQuatInterval(LerpNodePathInterval):
    paramSetup: bool
    endQuat: Vec4Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        quat: LQuaternionf | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
        hpr: Vec3Like | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        scale: Vec3Like | float,
        startScale: Vec3Like | float | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpShearInterval(LerpNodePathInterval):
    paramSetup: bool
    endShear: Vec3Like
    startShear: Vec3Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        shear: Vec3Like,
        startShear: Vec3Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpPosHprInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: Vec3Like
    startPos: Vec3Like | None
    endHpr: Vec3Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        hpr: Vec3Like,
        startPos: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpPosQuatInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: Vec3Like
    startPos: Vec3Like | None
    endQuat: Vec4Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        quat: LQuaternionf | None = ...,
        startPos: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
        hpr: Vec3Like | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpHprScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endHpr: Vec3Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        hpr: Vec3Like,
        scale: Vec3Like | float,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        startScale: Vec3Like | float | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpQuatScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endQuat: Vec4Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        quat: LQuaternionf | None = ...,
        scale: Vec3Like | float | None = ...,
        hpr: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        startScale: Vec3Like | float | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpPosHprScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: Vec3Like
    startPos: Vec3Like | None
    endHpr: Vec3Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        hpr: Vec3Like,
        scale: Vec3Like | float,
        startPos: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        startScale: Vec3Like | float | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpPosQuatScaleInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: Vec3Like
    startPos: Vec3Like | None
    endQuat: Vec4Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        quat: LQuaternionf | None = ...,
        scale: Vec3Like | float | None = ...,
        startPos: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        startScale: Vec3Like | float | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
        hpr: Vec3Like | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpPosHprScaleShearInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: Vec3Like
    startPos: Vec3Like | None
    endHpr: Vec3Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    endShear: Vec3Like
    startShear: Vec3Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        hpr: Vec3Like,
        scale: Vec3Like | float,
        shear: Vec3Like,
        startPos: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        startScale: Vec3Like | float | None = ...,
        startShear: Vec3Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpPosQuatScaleShearInterval(LerpNodePathInterval):
    paramSetup: bool
    endPos: Vec3Like
    startPos: Vec3Like | None
    endQuat: Vec4Like
    startHpr: Vec3Like | None
    startQuat: Vec4Like | None
    endScale: Vec3Like | float
    startScale: Vec3Like | float | None
    endShear: Vec3Like
    startShear: Vec3Like | None
    inPython: bool
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        pos: Vec3Like,
        quat: LQuaternionf | None = ...,
        scale: Vec3Like | float | None = ...,
        shear: Vec3Like | None = ...,
        startPos: Vec3Like | None = ...,
        startHpr: Vec3Like | None = ...,
        startQuat: Vec4Like | None = ...,
        startScale: Vec3Like | float | None = ...,
        startShear: Vec3Like | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        fluid: bool = ...,
        name: str | None = ...,
        hpr: Vec3Like | None = ...,
    ) -> None: ...
    def privDoEvent(self, t: float, event: _EventType) -> None: ...  # type: ignore[override]

class LerpColorInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        color: Vec4Like | ConfigVariableColor,
        startColor: Vec4Like | ConfigVariableColor | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        name: str | None = ...,
        override: int | None = ...,
    ) -> None: ...

class LerpColorScaleInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        colorScale: Vec4Like | ConfigVariableColor,
        startColorScale: Vec4Like | ConfigVariableColor | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        bakeInStart: bool = ...,
        name: str | None = ...,
        override: int | None = ...,
    ) -> None: ...

class LerpTexOffsetInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        texOffset: LVecBase2f,
        startTexOffset: LVecBase2f | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        textureStage=...,
        bakeInStart: bool = ...,
        name: str | None = ...,
        override: int | None = ...,
    ) -> None: ...

class LerpTexRotateInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        texRotate: float,
        startTexRotate: float | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        textureStage=...,
        bakeInStart: bool = ...,
        name: str | None = ...,
        override: int | None = ...,
    ) -> None: ...

class LerpTexScaleInterval(LerpNodePathInterval):
    def __init__(
        self,
        nodePath: NodePath,
        duration: float,
        texScale: LVecBase2f,
        startTexScale: LVecBase2f | None = ...,
        other: NodePath | None = ...,
        blendType: _BlendType = ...,
        textureStage=...,
        bakeInStart: bool = ...,
        name: str | None = ...,
        override: int | None = ...,
    ) -> None: ...

class LerpFunctionNoStateInterval(Interval):
    lerpFunctionIntervalNum: ClassVar[int]
    function: Callable[..., object]
    fromData: float
    toData: float
    blendType: _BlendType
    extraArgs: list[Any]
    def __init__(
        self,
        function: Callable[..., object],
        duration: float = ...,
        fromData: float = ...,
        toData: float = ...,
        blendType: _BlendType = ...,
        extraArgs: list[Any] = ...,
        name: str | None = ...,
    ) -> None: ...

class LerpFuncNS(LerpFunctionNoStateInterval): ...

class LerpFunctionInterval(Interval):
    lerpFunctionIntervalNum: ClassVar[int]
    function: Callable[..., object]
    fromData: float
    toData: float
    blendType: _BlendType
    extraArgs: list[Any]
    def __init__(
        self,
        function: Callable[..., object],
        duration: float = ...,
        fromData: float = ...,
        toData: float = ...,
        blendType: _BlendType = ...,
        extraArgs: list[Any] = ...,
        name: str | None = ...,
    ) -> None: ...

class LerpFunc(LerpFunctionInterval): ...
