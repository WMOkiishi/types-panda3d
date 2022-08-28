__all__ = [
    'AcceptInterval',
    'EventInterval',
    'Func',
    'FunctionInterval',
    'HprInterval',
    'HprScaleInterval',
    'IgnoreInterval',
    'ParentInterval',
    'PosHprInterval',
    'PosInterval',
    'PosHprScaleInterval',
    'ScaleInterval',
    'Wait',
    'WrtParentInterval',
]

from collections.abc import Callable, Iterable
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from panda3d.core import LMatrix3f, LVecBase3f, NodePath
from panda3d.direct import WaitInterval
from ..showbase.DirectObject import DirectObject
from .Interval import Interval

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow

class FunctionInterval(Interval):
    functionIntervalNum: ClassVar[int]
    function: Callable[..., object]
    extraArgs: Iterable[Any]
    kw: Any
    def __init__(
        self,
        function: Callable[..., object],
        *,
        name: str | None = None,
        openEnded: bool = True,
        extraArgs = ...,
        **kw: Any,
    ) -> None: ...
    @staticmethod
    def makeUniqueName(func, suffix: str = '') -> str: ...
    def privInstant(self) -> None: ...

class EventInterval(FunctionInterval):
    def __init__(self, event: str, sentArgs: list[Any] = ...) -> None: ...

class AcceptInterval(FunctionInterval):
    def __init__(self, dirObj: DirectObject, event: str, function: Callable[..., object], name: str | None = None) -> None: ...

class IgnoreInterval(FunctionInterval):
    def __init__(self, dirObj: DirectObject, event: str, name: str | None) -> None: ...

class ParentInterval(FunctionInterval):
    parentIntervalNum: ClassVar[int]
    def __init__(self, nodePath: NodePath, parent: NodePath, name: str | None = None) -> None: ...

class WrtParentInterval(FunctionInterval):
    wrtParentIntervalNum: ClassVar[int]
    def __init__(self, nodePath: NodePath, parent: NodePath, name: str | None = None) -> None: ...

class PosInterval(FunctionInterval):
    posIntervalNum: ClassVar[int]
    def __init__(
            self, nodePath: NodePath, pos: _Vec3f, duration: float = 0, name: str | None = None, other: NodePath | None = None) -> None: ...

class HprInterval(FunctionInterval):
    hprIntervalNum: ClassVar[int]
    def __init__(
        self,
        nodePath: NodePath,
        hpr: _Vec3f,
        duration: float = 0,
        name: str | None = None,
        other: NodePath | None = None,
    ) -> None: ...

class ScaleInterval(FunctionInterval):
    scaleIntervalNum: ClassVar[int]
    def __init__(
        self,
        nodePath: NodePath,
        scale: _Vec3f | float,
        duration: float = 0,
        name: str | None = None,
        other: NodePath | None = None,
    ) -> None: ...

class PosHprInterval(FunctionInterval):
    posHprIntervalNum: ClassVar[int]
    def __init__(
        self,
        nodePath: NodePath,
        pos: _Vec3f,
        hpr: _Vec3f,
        duration: float = 0,
        name: str | None = None,
        other: NodePath | None = None,
    ) -> None: ...

class HprScaleInterval(FunctionInterval):
    hprScaleIntervalNum: ClassVar[int]
    def __init__(
        self,
        nodePath: NodePath,
        hpr: _Vec3f,
        scale: _Vec3f | float,
        duration: float = 0,
        name: str | None = None,
        other: NodePath | None = None,
    ) -> None: ...

class PosHprScaleInterval(FunctionInterval):
    posHprScaleIntervalNum: ClassVar[int]
    def __init__(
        self,
        nodePath: NodePath,
        pos: _Vec3f,
        hpr: _Vec3f,
        scale: _Vec3f | float,
        duration: float = 0,
        name: str | None = None,
        other: NodePath | None = None,
    ) -> None: ...

class Func(FunctionInterval):
    def __init__(
        self,
        function: Callable[..., object],
        *extraArgs: Any,
        name: str | None = None,
        openEnded: bool = True,
        **kw: Any,
    ) -> None: ...

class Wait(WaitInterval):
    def __init__(self, duration: float) -> None: ...
