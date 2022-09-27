from _typeshed import StrOrBytesPath
from typing_extensions import TypeAlias

from panda3d.core import (
    ConfigVariableColor,
    ConfigVariableFilename,
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

Vec3d: TypeAlias = LVecBase3d | LMatrix3d.Row | LMatrix3d.CRow
Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
Vec4d: TypeAlias = LVecBase4d | UnalignedLVecBase4d | LMatrix4d.Row | LMatrix4d.CRow
Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
Vec4i: TypeAlias = LVecBase4i | UnalignedLVecBase4i
Mat4d: TypeAlias = LMatrix4d | UnalignedLMatrix4d
Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f
Filepath: TypeAlias = StrOrBytesPath | ConfigVariableFilename
