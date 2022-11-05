from _typeshed import StrOrBytesPath
from typing_extensions import TypeAlias

from panda3d.core._downloader import URLSpec
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
    LVecBase4i,
    UnalignedLMatrix4d,
    UnalignedLMatrix4f,
    UnalignedLVecBase4d,
    UnalignedLVecBase4f,
    UnalignedLVecBase4i,
)
from panda3d.core._prc import ConfigVariableFilename

DoubleVec3Like: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
Vec3Like: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
DoubleVec4Like: TypeAlias = LVecBase4d | UnalignedLVecBase4d | LMatrix4d.Row | LMatrix4d.CRow
Vec4Like: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
IntVec4Like: TypeAlias = LVecBase4i | UnalignedLVecBase4i
DoubleMat4Like: TypeAlias = LMatrix4d | UnalignedLMatrix4d
Mat4Like: TypeAlias = LMatrix4f | UnalignedLMatrix4f
Filepath: TypeAlias = StrOrBytesPath | ConfigVariableFilename
URL: TypeAlias = URLSpec | str
