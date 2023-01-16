from typing_extensions import TypeAlias

from panda3d.core._downloader import URLSpec
from panda3d.core._dtoolutil import DSearchPath, Filename
from panda3d.core._linmath import (
    ConfigVariableColor,
    LMatrix3d,
    LMatrix3f,
    LMatrix4d,
    LMatrix4f,
    LVecBase3d,
    LVecBase3f,
    LVecBase4d,
    LVecBase4f,
    UnalignedLMatrix4d,
    UnalignedLMatrix4f,
)
from panda3d.core._prc import ConfigVariableFilename, ConfigVariableSearchPath

Vec3Like: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
DoubleVec3Like: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
Vec4Like: TypeAlias = LVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
DoubleVec4Like: TypeAlias = LVecBase4d | LMatrix4d.Row | LMatrix4d.CRow
Mat4Like: TypeAlias = LMatrix4f | UnalignedLMatrix4f
DoubleMat4Like: TypeAlias = LMatrix4d | UnalignedLMatrix4d
URL: TypeAlias = URLSpec | str
SearchPathLike: TypeAlias = ConfigVariableFilename | ConfigVariableSearchPath | DSearchPath | Filename | str
