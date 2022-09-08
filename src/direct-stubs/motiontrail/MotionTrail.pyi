from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import (
    ConfigVariableColor,
    GeomNode,
    GeomTriangles,
    GeomVertexData,
    GeomVertexFormat,
    GeomVertexWriter,
    LMatrix3f,
    LMatrix4f,
    LVecBase2f,
    LVecBase3f,
    LVecBase4f,
    LVector4f,
    NodePath,
    Texture,
    UnalignedLVecBase4f,
)
from panda3d.direct import CMotionTrail
from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject

_Vec3f: TypeAlias = LVecBase3f | LMatrix3f.Row | LMatrix3f.CRow
_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

def remove_task() -> None: ...

class MotionTrailVertex:
    vertex_id = ...
    vertex_function = ...
    context = ...
    vertex: LVector4f
    start_color: LVector4f
    end_color: LVector4f
    v: float
    def __init__(self, vertex_id, vertex_function, context) -> None: ...

class MotionTrailFrame:
    time: float
    transform = ...
    def __init__(self, current_time: float, transform) -> None: ...

class MotionTrail(NodePath, DirectObject):
    notify: ClassVar[Notifier]
    task_added: ClassVar[bool]
    motion_trail_list: ClassVar[list[MotionTrail]]
    motion_trail_task_name: ClassVar[str]
    global_enable: ClassVar[bool]
    active: bool
    enable: bool
    pause: bool
    pause_time: float
    fade: bool
    fade_end: bool
    fade_start_time: float
    fade_color_scale: float
    total_vertices: int
    last_update_time: float
    texture: Texture | None
    vertex_list: list[MotionTrailVertex]
    frame_list: list[MotionTrailFrame]
    parent_node_path: NodePath
    previous_matrix = ...
    calculate_relative_matrix: bool
    playing: bool
    continuous_motion_trail: bool
    color_scale: float
    time_window: float
    sampling_time: float
    square_t: bool
    root_node_path = ...
    geom_node: GeomNode
    geom_node_path: NodePath[GeomNode]
    relative_to_render: bool
    use_nurbs: bool
    resolution_distance: float
    cmotion_trail: CMotionTrail
    modified_vertices: bool
    use_python_version: bool
    vertex_index: int
    format: GeomVertexFormat
    vertex_data: GeomVertexData
    vertex_writer: GeomVertexWriter
    triangles: GeomTriangles
    @classmethod
    def setGlobalEnable(cls, enable: bool) -> None: ...
    def __init__(self, name: str, parent_node_path: NodePath) -> None: ...
    def delete(self) -> None: ...
    def print_matrix(self, matrix: LMatrix3f) -> None: ...
    def motion_trail_task(self, task) -> Literal[1]: ...
    def add_vertex(self, vertex_id, vertex_function, context) -> MotionTrailVertex: ...
    def set_vertex_color(self, vertex_id: int, start_color: LVector4f, end_color: LVector4f) -> None: ...
    def set_texture(self, texture: Texture | None) -> None: ...
    def update_vertices(self) -> None: ...
    def transferVertices(self) -> None: ...
    def register_motion_trail(self) -> None: ...
    def unregister_motion_trail(self) -> None: ...
    def begin_geometry(self) -> None: ...
    def add_geometry_quad(
        self,
        v0: _Vec3f,
        v1: _Vec3f,
        v2: _Vec3f,
        v3: _Vec3f,
        c0: _Vec4f,
        c1: _Vec4f,
        c2: _Vec4f,
        c3: _Vec4f,
        t0: LVecBase2f,
        t1: LVecBase2f,
        t2: LVecBase2f,
        t3: LVecBase2f,
    ) -> None: ...
    def end_geometry(self) -> None: ...
    def check_for_update(self, curent_time: float) -> bool: ...
    def update_motion_trail(self, current_time: float, transform) -> None: ...
    def enable_motion_trail(self, enable: bool) -> None: ...
    def reset_motion_trail(self) -> None: ...
    def reset_motion_trail_geometry(self) -> None: ...
    def attach_motion_trail(self) -> None: ...
    def begin_motion_trail(self) -> None: ...
    def end_motion_trail(self) -> None: ...
    def set_fade(self, time: float, current_time: float) -> None: ...
    def pause_motion_trail(self, current_time: float) -> None: ...
    def resume_motion_trail(self, current_time: float) -> None: ...
    def toggle_pause_motion_trail(self, current_time: float) -> None: ...