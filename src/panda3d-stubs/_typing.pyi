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

Vec3Like: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
DoubleVec3Like: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
Vec4Like: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
DoubleVec4Like: TypeAlias = LVecBase4d | UnalignedLVecBase4d | LMatrix4d.Row | LMatrix4d.CRow
IntVec4Like: TypeAlias = LVecBase4i | UnalignedLVecBase4i
Mat4Like: TypeAlias = LMatrix4f | UnalignedLMatrix4f
DoubleMat4Like: TypeAlias = LMatrix4d | UnalignedLMatrix4d
URL: TypeAlias = URLSpec | str
