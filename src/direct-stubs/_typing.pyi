from collections.abc import Mapping
from typing import Any, TypeVar
from typing_extensions import TypeAlias

from direct.leveleditor.ObjectPaletteBase import ObjectGen
from panda3d._typing import Vec4Like
from panda3d.core import NodePath

_NodePathT = TypeVar('_NodePathT', covariant=True, bound=NodePath)
_ObjectGenT = TypeVar('_ObjectGenT', covariant=True, bound=ObjectGen)

AnyReal = TypeVar('AnyReal', int, float)  # noqa: Y001

Obj: TypeAlias = tuple[str, _NodePathT, _ObjectGenT, Any, Any, Mapping[str, Any], Vec4Like]
Unused: TypeAlias = object
