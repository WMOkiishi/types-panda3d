from typing import Union
from typing_extensions import TypeAlias

from panda3d.core._downloader import URLSpec
from panda3d.core._dtoolutil import DSearchPath, Filename
from panda3d.core._linmath import (
    ConfigVariableColor,
    LMatrix3d,
    LMatrix3f,
    LMatrix4d,
    LMatrix4f,
    LVecBase2d,
    LVecBase2f,
    LVecBase2i,
    LVecBase3d,
    LVecBase3f,
    LVecBase3i,
    LVecBase4d,
    LVecBase4f,
    LVecBase4i,
    UnalignedLMatrix4d,
    UnalignedLMatrix4f,
)
from panda3d.core._prc import ConfigVariableFilename, ConfigVariableSearchPath

Vec2Like: TypeAlias = Union[LVecBase2f, tuple[float, float]]
DoubleVec2Like: TypeAlias = Union[LVecBase2d, tuple[float, float]]
IntVec2Like: TypeAlias = Union[LVecBase2i, tuple[int, int]]
Vec3Like: TypeAlias = Union[LVecBase3f, LMatrix3f.Row, LMatrix3f.CRow, tuple[float, float, float]]
DoubleVec3Like: TypeAlias = Union[LVecBase3d, LMatrix3d.Row, LMatrix3d.CRow, tuple[float, float, float]]
IntVec3Like: TypeAlias = Union[LVecBase3i, tuple[int, int, int]]
Vec4Like: TypeAlias = Union[LVecBase4f, LMatrix4f.Row, LMatrix4f.CRow, tuple[float, float, float, float], ConfigVariableColor]
DoubleVec4Like: TypeAlias = Union[LVecBase4d, LMatrix4d.Row, LMatrix4d.CRow, tuple[float, float, float, float]]
IntVec4Like: TypeAlias = Union[LVecBase4i, tuple[int, int, int, int]]
Mat4Like: TypeAlias = LMatrix4f | UnalignedLMatrix4f
DoubleMat4Like: TypeAlias = LMatrix4d | UnalignedLMatrix4d
URL: TypeAlias = URLSpec | str
SearchPathLike: TypeAlias = ConfigVariableFilename | ConfigVariableSearchPath | DSearchPath | Filename | str
