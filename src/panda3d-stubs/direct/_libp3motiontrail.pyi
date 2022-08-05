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
    """The method used in creating the motion trail is based on taking samples of
    time and transformations (the position and orientation matrix) in real-
    time.  The method also requires a number of vertices (positions) that
    determines "shape" of the motion trail (i.e.  the edge of a blade).  A
    start color and end color is also required for each vertex.  The color is
    interpolated as function of time.  The colors are typically used to fade
    the motion trail so the end color is typically black.
    
    The vertices are submitted via the "add_vertex" function.  For each frame,
    a sample is submited via the "update_motion_trail" function.  During the
    "update_motion_trail" function, the motion trail geometry is created
    dynamically from the sample history and the vertices.
    
    The user must specifiy a GeomNode via "set_geom_node".
    
    The duration of the sample history is specified by a time window.  A larger
    time window creates longer motion trails (given constant speed).  Samples
    that are no longer within the time window are automatically discarded.
    
    The nurbs option can be used to create smooth interpolated curves from the
    samples.  The nurbs option is useful for animations that lack sampling to
    begin with, animations that move very quickly, or low frame rates.
    
    The texture option be used to create variation to the motion trail.  The u
    coordinate of the texture corresponds to time and the v coordinate
    corresponds to the "shape" of the motion trail.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None:
        """Constructor"""
        ...
    @overload
    def __init__(self, __param0: CMotionTrail) -> None: ...
    def reset(self) -> None:
        """Reset the frame sample history."""
        ...
    def reset_vertex_list(self) -> None:
        """Reset the vertex list."""
        ...
    def enable(self, enable: bool) -> None:
        """Enable/disable the motion trail."""
        ...
    def set_geom_node(self, geom_node: GeomNode) -> None:
        """Set the GeomNode."""
        ...
    def add_vertex(self, vertex: _Vec4f, start_color: _Vec4f, end_color: _Vec4f, v: float) -> None:
        """Add a vertex."""
        ...
    def set_parameters(self, sampling_time: float, time_window: float, use_texture: bool, calculate_relative_matrix: bool, use_nurbs: bool, resolution_distance: float) -> None:
        """Set motion trail parameters.
        
        sampling_time = Can be used to specify a lower sampling rate than the frame
        rate.  Use 0.0 with nurbs.
        
        time_window = a component for the "length" of the motion trail.  The motion
        trail length = time_window * velocity of the object.
        
        use_texture = texture option on/off.
        
        calculate_relative_matrix = calculate relative matrix on/off.
        
        use_nurbs = nurbs option on/off
        
        resolution_distance = the distance used to determine the number of geometry
        samples.  samples = motion trail length / resolution_distance.  Applicable
        only if nurbs is on.
        """
        ...
    def check_for_update(self, current_time: float) -> int:
        """Check if a sample can be submitted."""
        ...
    def update_motion_trail(self, current_time: float, transform: _Mat4f) -> None:
        """See class header comments."""
        ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    resetVertexList = reset_vertex_list
    setGeomNode = set_geom_node
    addVertex = add_vertex
    setParameters = set_parameters
    checkForUpdate = check_for_update
    updateMotionTrail = update_motion_trail
    getClassType = get_class_type
