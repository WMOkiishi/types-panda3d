from collections.abc import Callable
from typing import Any, ClassVar, Literal
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import (
    GeomNode,
    GeomTriangles,
    GeomVertexData,
    GeomVertexFormat,
    GeomVertexWriter,
    LMatrix3f,
    LMatrix4f,
    LVecBase2f,
    LVector4f,
    NodePath,
    Texture,
)
from panda3d.direct import CMotionTrail

_VertexFunction: TypeAlias = Callable[[MotionTrailVertex, int, Any], LVector4f]

def remove_task() -> None: ...

class MotionTrailVertex:
    vertex_id: int
    vertex_function: _VertexFunction
    context: Any
    vertex: LVector4f
    start_color: LVector4f
    end_color: LVector4f
    v: float
    def __init__(self, vertex_id: int, vertex_function: _VertexFunction, context: Any) -> None: ...

class MotionTrailFrame:
    time: float
    transform: LMatrix4f
    def __init__(self, current_time: float, transform: LMatrix4f) -> None: ...

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
    previous_matrix: Any | None
    calculate_relative_matrix: bool
    playing: bool
    continuous_motion_trail: bool
    color_scale: float
    time_window: float
    sampling_time: float
    square_t: bool
    root_node_path: NodePath | None
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
    def motion_trail_task(self, task: Task) -> Literal[1]: ...
    def add_vertex(
        self, vertex_id: int, vertex_function: _VertexFunction | None = None, context: Any = None
    ) -> MotionTrailVertex: ...
    def set_vertex_color(self, vertex_id: int, start_color: LVector4f, end_color: LVector4f) -> None: ...
    def set_texture(self, texture: Texture | None) -> None: ...  # type: ignore[override]
    def update_vertices(self) -> None: ...
    def transferVertices(self) -> None: ...
    def register_motion_trail(self) -> None: ...
    def unregister_motion_trail(self) -> None: ...
    def begin_geometry(self) -> None: ...
    def add_geometry_quad(
        self,
        v0: Vec3Like,
        v1: Vec3Like,
        v2: Vec3Like,
        v3: Vec3Like,
        c0: Vec4Like,
        c1: Vec4Like,
        c2: Vec4Like,
        c3: Vec4Like,
        t0: LVecBase2f,
        t1: LVecBase2f,
        t2: LVecBase2f,
        t3: LVecBase2f,
    ) -> None: ...
    def end_geometry(self) -> None: ...
    def check_for_update(self, current_time: float) -> bool: ...
    def update_motion_trail(self, current_time: float, transform: LMatrix4f) -> None: ...
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
