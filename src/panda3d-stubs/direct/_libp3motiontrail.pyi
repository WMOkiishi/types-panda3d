from typing import Any, ClassVar, TypeAlias, overload
from panda3d.core import (
    ConfigVariableColor,
    GeomNode,
    LMatrix4f,
    LVecBase4f,
    TypeHandle,
    TypedReferenceCount,
    UnalignedLMatrix4f,
    UnalignedLVecBase4f,
)

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor
_Mat4f: TypeAlias = LMatrix4f | UnalignedLMatrix4f

class CMotionTrail(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: CMotionTrail) -> None: ...
    def reset(self) -> None: ...
    def reset_vertex_list(self) -> None: ...
    def enable(self, enable: bool) -> None: ...
    def set_geom_node(self, geom_node: GeomNode) -> None: ...
    def add_vertex(self, vertex: _Vec4f, start_color: _Vec4f, end_color: _Vec4f, v: float) -> None: ...
    def set_parameters(self, sampling_time: float, time_window: float, use_texture: bool, calculate_relative_matrix: bool, use_nurbs: bool, resolution_distance: float) -> None: ...
    def check_for_update(self, current_time: float) -> int: ...
    def update_motion_trail(self, current_time: float, transform: _Mat4f) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    resetVertexList = reset_vertex_list
    setGeomNode = set_geom_node
    addVertex = add_vertex
    setParameters = set_parameters
    checkForUpdate = check_for_update
    updateMotionTrail = update_motion_trail
    getClassType = get_class_type
