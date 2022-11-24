from collections.abc import Callable, Mapping
from typing import Any, TypeVar, Union
from typing_extensions import TypeAlias

from direct.leveleditor.ObjectPaletteBase import ObjectGen
from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import LVecBase2f, NodePath

_NodePathT = TypeVar('_NodePathT', covariant=True, bound=NodePath)
_ObjectGenT = TypeVar('_ObjectGenT', covariant=True, bound=ObjectGen)

AnyReal = TypeVar('AnyReal', int, float)  # noqa: Y001

Incomplete: TypeAlias = Any
Obj: TypeAlias = tuple[str, _NodePathT, _ObjectGenT, Any, Any, Mapping[str, Any], Vec4OrTuple]
SimpleCallback: TypeAlias = Callable[[], object]
Unused: TypeAlias = object
Vec2OrTuple: TypeAlias = Union[LVecBase2f, tuple[float, float]]
Vec3OrTuple: TypeAlias = Union[Vec3Like, tuple[float, float, float]]
Vec4OrTuple: TypeAlias = Union[Vec4Like, tuple[float, float, float, float]]
