import logging
from collections.abc import Container
from typing import Final

from .util import TrackingMap, TrackingSet

_logger: Final = logging.getLogger(__name__)


def log_unused() -> None:
    """Log warnings for any unused entries
    from the collections in this module.
    """
    for name, obj in globals().items():
        if isinstance(obj, TrackingSet):
            for i in obj.unused_items():
                _logger.warning(f'Unused item in {name}: {i!r}')
        elif isinstance(obj, TrackingMap):
            for k in obj.unused_keys():
                _logger.warning(f'Unused key in {name}: {k!r}')


# Don't write stubs for anything with these names
NO_STUBS: Final = TrackingSet({
    # Attribute access
    '__dict__', '__getattr__', '__setattr__', '__delattr__',
    # Pickle stuff
    '__getstate__', '__setstate__', '__reduce__',
})


# These names are not exposed to Python, even though they may seem like they are
NOT_EXPOSED: Final = TrackingSet({
    'TIXML_NO_ATTRIBUTE',
    'TIXML_SUCCESS',
    'TIXML_WRONG_TYPE',
    'LMatrix4f::begin',
    'LMatrix4f::end',
    'LMatrix4d::begin',
    'LMatrix4d::end',
    'PandaNode::__traverse__',
    'NodePath::__traverse__',
    'PythonTask::__traverse__',
    'PythonTask::__clear__',
    'GraphicsOutputBase::get_texture',
    'Notify::get_assert_handler',
    'Texture::get_ram_mipmap_pointer',
    'TiXmlBase::GetUserData',
    'LMatrix3f::get_data',
    'LMatrix3d::get_data',
    'LMatrix4f::get_data',
    'LMatrix4d::get_data',
    'UnalignedLMatrix4f::get_data',
    'UnalignedLMatrix4d::get_data',
    'Filename::operator /',
})


# Methods with these names are directly translated to particular Python names
# (mostly) from `methodRenameDictionary` in interfaceMakerPythonNative.cxx
METHOD_RENAMES: Final = TrackingMap({
    'operator ==': '__eq__',
    'operator !=': '__ne__',
    'operator <<': '__lshift__',
    'operator >>': '__rshift__',
    'operator <': '__lt__',
    'operator >': '__gt__',
    'operator <=': '__le__',
    'operator >=': '__ge__',
    'operator =': 'assign',
    'operator ()': '__call__',
    'operator []': '__getitem__',
    'operator [] =': '__setitem__',
    'operator ++': 'increment',
    'operator --': 'decrement',
    'operator ^': '__xor__',
    'operator %': '__mod__',
    'operator &': '__and__',
    'operator |': '__or__',
    'operator +': '__add__',
    'operator -': '__sub__',
    'operator *': '__mul__',
    'operator /': '__truediv__',
    'operator +=': '__iadd__',
    'operator -=': '__isub__',
    'operator *=': '__imul__',
    'operator /=': '__itruediv__',
    'operator |=': '__ior__',
    'operator &=': '__iand__',
    'operator ^=': '__ixor__',
    'operator <<=': '__ilshift__',
    'operator >>=': '__irshift__',
    'size': '__len__',
    '__nonzero__': '__bool__',
})
UNARY_METHOD_RENAMES: Final = TrackingMap({
    'operator ++': 'increment',
    'operator --': 'decrement',
    'operator ~': '__invert__',
    'operator -': '__neg__',
})


# These types from interrogate map directly to a Python type
TYPE_NAME_OVERRIDES: Final = TrackingMap({
    '_object': '',
    '_typeobject': 'type',
    'PN_stdfloat []': 'array[float]',
    'PN_stdfloat const []': 'array[float]',
    'basic_string< char >': 'str',
    'pvector< unsigned char >': 'bytes',
    # TODO: Do something more correct with this.
    'BitMaskNative': 'BitMask_uint32_t_32 | BitMask_uint64_t_64',
})


# If a function with one of these names returns "_object",
# we can assume a default return type
DEFAULT_RETURNS: Final = TrackingMap({
    '__repr__': 'str',
    '__int__': 'int',
    '__str__': 'str',
    '__bytes__': 'bytes',
    '__fspath__': 'str',
    'get_data': 'bytes',
    'get_subdata': 'bytes',
})


# These methods almost certainly behave as if they return `self`
INPLACE_DUNDERS: Final = TrackingSet({
    '__iand__', '__ior__', '__ixor__', '__ilshift__', '__irshift__',
    '__iadd__', '__isub__', '__imul__', '__itruediv__', '__ifloordiv__',
    '__imod__', '__ipow__',
})


# Camel-case aliases are not generated for these names
NO_MANGLING: Final = TrackingSet(INPLACE_DUNDERS | {
    '_del',
    '__init__', '__call__', '__iter__', '__await__',
    '__getattribute__', '__getattr__', '__setattr__', '__delattr__',
    '__getitem__', '__setitem__', '__delitem__',
    '__eq__', '__ne__', '__lt__', '__le__', '__ge__', '__gt__',
    '__neg__', '__pos__', '__invert__',
    '__and__', '__or__', '__xor__', '__lshift__', '__rshift__',
    '__rand__', '__ror__', '__rxor__', '__rlshift__', '__rrshift__',
    '__add__', '__sub__', '__mul__', '__truediv__', '__floordiv__',
    '__radd__', '__rsub__', '__rmul__', '__rtruediv__', '__rfloordiv__',
    '__mod__', '__rmod__', '__pow__', '__rpow__',
    '__repr__', '__str__', '__float__', '__int__', '__bool__', '__len__',
    '__copy__', '__deepcopy__', '__getstate__', '__setstate__',
    '__reduce__', '__reduce_ex__', '__reduce_persist__',
})


# These types are effectively generic
GENERIC: Final = TrackingMap({
    'NodePath': '_N',
})


# These types have attributes sharing names with other types
ATTRIBUTE_NAME_SHADOWS: Final = TrackingMap[str, Container[str]]({
    'panda3d.core.StreamReader': ('istream',),
    'panda3d.core.StreamWriter': ('ostream',),
    'panda3d.core.StreamWrapper': ('iostream',),
    'panda3d.core.IStreamWrapper': ('istream',),
    'panda3d.core.OStreamWrapper': ('ostream',),
})


# Don't replace `size` with `__len__` for these
SIZE_NOT_LEN: Final = TrackingSet(('EggGroupNode', 'WindowProperties'))


# These types only exist under certain conditions
CONDITIONALS: Final = TrackingMap({
    'panda3d.core.WindowsRegistry': "sys.platform == 'win32'",
})


# These override type hints for various things
ATTR_TYPE_OVERRIDES: Final = TrackingMap({
    'panda3d.core.BamReader.file_version': 'tuple[int, int]',
    'panda3d.core.NodePath.net_tags': 'Mapping[str, str]',
    'panda3d.core.NodePath.python_tags': 'dict[Any, Any] | None',
    'panda3d.core.NodePath.tags': 'MutableMapping[str, str] | None',
    'panda3d.core.PandaNode.python_tags': 'dict[Any, Any]',
    'panda3d.core.PandaNode.tags': 'MutableMapping[str, str]',
    'panda3d.core.PythonCallbackObject.function': 'Callable',
    'panda3d.core.StringStream.data': 'bytes',
    'panda3d.core.TextEncoder.text': 'str',
    'panda3d.egg.EggGroupNode.children': 'list[EggNode]',
})
PARAM_TYPE_OVERRIDES: Final = TrackingMap[str, dict[tuple[int, int], str]]({
    'panda3d.core.Filename.__init__': {(2, 1): 'StrOrBytesPath'},
    'panda3d.core.NodePath.__init__': {
        (1, 1): 'NodePath[_N]', (3, 1): '_N', (2, 2): '_N'
    },
    'panda3d.core.NodePath.any_path': {(0, 0): '_M'},
    'panda3d.core.NodePath.attach_new_node': {(0, 1): '_M'},
    'panda3d.core.NodePath.clear_python_tag': {(0, 1): 'Any'},
    'panda3d.core.NodePath.find_net_python_tag': {(0, 1): 'Any'},
    'panda3d.core.NodePath.get_net_python_tag': {(0, 1): 'Any'},
    'panda3d.core.NodePath.get_python_tag': {(0, 1): 'Any'},
    'panda3d.core.NodePath.has_net_python_tag': {(0, 1): 'Any'},
    'panda3d.core.NodePath.has_python_tag': {(0, 1): 'Any'},
    'panda3d.core.NodePath.set_python_tag': {(0, 1): 'Any', (0, 2): 'Any'},
    'panda3d.core.PandaNode.clear_python_tag': {(0, 1): 'Any'},
    'panda3d.core.PandaNode.get_python_tag': {(0, 1): 'Any'},
    'panda3d.core.PandaNode.has_python_tag': {(0, 1): 'Any'},
    'panda3d.core.PandaNode.set_python_tag': {(0, 1): 'Any', (0, 2): 'Any'},
    'panda3d.core.PythonCallbackObject.__init__': {(0, 1): 'Callable'},
    'panda3d.core.PythonCallbackObject.set_function': {(0, 1): 'Callable'},
    'panda3d.core.PythonTask.__init__': {(0, 1): 'Callable'},
    'panda3d.core.PythonTask.set_function': {(0, 1): 'Callable'},
    'panda3d.core.PythonTask.set_upon_death': {(0, 1): 'Callable'},
    'panda3d.core.StringStream.set_data': {(0, 1): 'bytes'},
    'panda3d.core.TextEncoder.decode_text': {(0, 1): 'bytes', (1, 1): 'bytes'},
    'panda3d.core.TextEncoder.set_text': {(0, 1): 'str', (1, 1): 'bytes'},
    'panda3d.vision.ARToolKit.make': {(0, 0): 'NodePath[Camera]'},
})
RETURN_TYPE_OVERRIDES: Final = TrackingMap[str, str | dict[int, str]]({
    'panda3d.core.AsyncFuture.__await__': 'Generator[Awaitable, None, None]',
    'panda3d.core.AsyncFuture.__iter__': 'Generator[Awaitable, None, None]',
    'panda3d.core.AsyncFuture.gather': 'AsyncFuture',
    'panda3d.core.BamReader.get_file_version': 'tuple[int, int]',
    'panda3d.core.BoundingBox.get_num_planes': 'Literal[6]',
    'panda3d.core.BoundingBox.get_num_points': 'Literal[8]',
    'panda3d.core.BoundingHexahedron.get_num_planes': 'Literal[6]',
    'panda3d.core.BoundingHexahedron.get_num_points': 'Literal[8]',
    'panda3d.core.CollisionBox.get_num_planes': 'Literal[6]',
    'panda3d.core.CollisionBox.get_num_points': 'Literal[8]',
    'panda3d.core.Datagram.get_message': 'bytes',
    'panda3d.core.EventQueue.is_queue_full': 'Literal[False]',
    'panda3d.core.Filename.scan_directory': 'list[str]',
    'panda3d.core.GlobPattern.match_files': 'list[str]',
    'panda3d.core.GraphicsStateGuardian.get_prepared_textures': 'list[Any]',
    'panda3d.core.LMatrix3f.__len__': 'Literal[3]',
    'panda3d.core.LMatrix3f.Row.__len__': 'Literal[3]',
    'panda3d.core.LMatrix3f.CRow.__len__': 'Literal[3]',
    'panda3d.core.LMatrix3d.__len__': 'Literal[3]',
    'panda3d.core.LMatrix3d.Row.__len__': 'Literal[3]',
    'panda3d.core.LMatrix3d.CRow.__len__': 'Literal[3]',
    'panda3d.core.LMatrix4f.__len__': 'Literal[4]',
    'panda3d.core.LMatrix4f.Row.__len__': 'Literal[4]',
    'panda3d.core.LMatrix4f.CRow.__len__': 'Literal[4]',
    'panda3d.core.LMatrix4d.__len__': 'Literal[4]',
    'panda3d.core.LMatrix4d.Row.__len__': 'Literal[4]',
    'panda3d.core.LMatrix4d.CRow.__len__': 'Literal[4]',
    'panda3d.core.NodePath.any_path': 'NodePath[_M]',
    'panda3d.core.NodePath.attach_new_node': {0: 'NodePath[_M]'},
    'panda3d.core.NodePath.flatten_light': 'Literal[0]',
    'panda3d.core.NodePath.get_net_python_tag': 'Any | None',
    'panda3d.core.NodePath.get_python_tag': 'Any | None',
    'panda3d.core.NodePath.get_python_tag_keys': 'list[Any] | tuple[()]',
    'panda3d.core.NodePath.get_python_tags': 'dict[Any, Any] | None',
    'panda3d.core.NodePath.get_tag_keys': 'tuple[str, ...] | None',
    'panda3d.core.NodePath.get_tags': 'MutableMapping[str, str] | None',
    'panda3d.core.NodePath.get_tight_bounds': 'tuple[LPoint3f, LPoint3f] | None',
    'panda3d.core.NodePath.node': '_N',
    'panda3d.core.NodePathCollection.get_tight_bounds': 'tuple[LPoint3f, LPoint3f] | None',
    'panda3d.core.OccluderNode.get_num_vertices': 'Literal[4]',
    'panda3d.core.PandaNode.get_python_tag': 'Any | None',
    'panda3d.core.PandaNode.get_python_tag_keys': 'list[Any] | tuple[()]',
    'panda3d.core.PandaNode.get_python_tags': 'dict[Any, Any]',
    'panda3d.core.PandaNode.get_tag_keys': 'tuple[str, ...]',
    'panda3d.core.PNMImageHeader.PixelSpec.__len__': 'Literal[4]',
    'panda3d.core.PythonCallbackObject.get_function': 'Callable',
    'panda3d.core.PythonTask.get_args': 'tuple[Any, ...]',
    'panda3d.core.PythonTask.get_function': 'Callable',
    'panda3d.core.PythonTask.get_upon_death': 'Callable',
    'panda3d.core.Ramfile.read': 'bytes',
    'panda3d.core.Ramfile.readline': 'bytes',
    'panda3d.core.Ramfile.readlines': 'list[bytes]',
    'panda3d.core.RenderState.get_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'panda3d.core.RenderState.get_invert_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'panda3d.core.RenderState.get_states': 'list[RenderState]',
    'panda3d.core.RenderState.get_unused_states': 'list[RenderState]',
    'panda3d.core.SparseArray.has_max_num_bits': 'Literal[False]',
    'panda3d.core.StreamReader.extract_bytes': 'bytes',
    'panda3d.core.StreamReader.readline': 'bytes',
    'panda3d.core.StreamReader.readlines': 'list[bytes]',
    'panda3d.core.TextEncoder.decode_text': 'str',
    'panda3d.core.TextEncoder.encode_wchar': 'bytes',
    'panda3d.core.TextEncoder.encode_wtext': 'bytes',
    'panda3d.core.TextEncoder.get_text': {0: 'str', 1: 'bytes'},
    'panda3d.core.TransformState.get_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'panda3d.core.TransformState.get_invert_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'panda3d.core.TransformState.get_states': 'list[TransformState]',
    'panda3d.core.TransformState.get_unused_states': 'list[TransformState]',
    'panda3d.core.VirtualFile.read_file': 'bytes',
    'panda3d.core.pixel.__len__': 'Literal[3]',
    'panda3d.egg.EggGroupNode.get_children': 'list[EggNode]',
    'panda3d.ode.OdeGeom.get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
    'panda3d.ode.OdeSpace.get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
})


# This adds comments to ignore Mypy errors
IGNORE_ERRORS: Final = TrackingMap({
    'panda3d.core.AsyncTaskSequence': 'misc',
    'panda3d.core.Character.getBundle': 'assignment',
    'panda3d.core.DatagramBuffer': 'misc',
    'panda3d.core.DynamicTextFont': 'misc',
    'panda3d.core.GeomVertexRewriter': 'misc',
    'panda3d.core.GeomVertexRewriter.setColumn': 'assignment',
    'panda3d.core.GeometricBoundingVolume.contains': 'override',
    'panda3d.core.GeometricBoundingVolume.extend_by': 'override',
    'panda3d.core.GeometricBoundingVolume.extendBy': 'assignment',
    'panda3d.core.HTTPDate.__isub__': 'misc',
    'panda3d.core.LOrientationd.__mul__': 'override',
    'panda3d.core.LOrientationf.__mul__': 'override',
    'panda3d.core.LPlaned.__imul__': 'misc, override',
    'panda3d.core.LPlaned.__mul__': 'override',
    'panda3d.core.LPlaned.project': 'override',
    'panda3d.core.LPlanef.__imul__': 'misc, override',
    'panda3d.core.LPlanef.__mul__': 'override',
    'panda3d.core.LPlanef.project': 'override',
    'panda3d.core.LQuaterniond.__imul__': 'misc, override',
    'panda3d.core.LQuaterniond.__mul__': 'override',
    'panda3d.core.LQuaternionf.__imul__': 'misc, override',
    'panda3d.core.LQuaternionf.__mul__': 'override',
    'panda3d.core.LRotationd.__mul__': 'override',
    'panda3d.core.LRotationf.__mul__': 'override',
    'panda3d.core.LightNode': 'misc',
    'panda3d.core.LightLensNode': 'misc',
    'panda3d.core.MouseWatcher': 'misc',
    'panda3d.core.OSocketStream.flush': 'override',
    'panda3d.core.PGItem.get_state': 'override',
    'panda3d.core.PGItem.getState': 'assignment',
    'panda3d.core.PGItem.set_state': 'override',
    'panda3d.core.PGItem.setState': 'assignment',
    'panda3d.core.PGScrollFrame.setup': 'override',
    'panda3d.core.Socket_UDP.SendTo': 'override',
    'panda3d.core.SocketStream': 'misc',
    'panda3d.core.SocketStream.flush': 'override',
    'panda3d.core.StreamWrapper': 'misc',
    'panda3d.core.TextNode.get_transform': 'override',
    'panda3d.core.TextNode.getTransform': 'assignment',
    'panda3d.core.TextNode.set_transform': 'override',
    'panda3d.core.TextNode.setTransform': 'assignment',
    'panda3d.core.TextNode.setShadow': 'assignment',
    'panda3d.core.TextNode.setShadowColor': 'assignment',
    'panda3d.core.TextNode.setTextColor': 'assignment',
    'panda3d.core.TextNode.transform': 'assignment',
    'panda3d.core.TrackerNode.get_transform': 'override',
    'panda3d.core.TrackerNode.getTransform': 'assignment',
    'panda3d.core.Triangulator3.add_vertex': 'override',
    'panda3d.core.Triangulator3.addVertex': 'assignment',
    'panda3d.core.Triangulator3.get_vertex': 'override',
    'panda3d.core.Triangulator3.getVertex': 'assignment',
    'panda3d.core.Triangulator3.get_vertices': 'override',
    'panda3d.core.Triangulator3.getVertices': 'assignment',
    'panda3d.core.Triangulator3.vertices': 'override',
    'panda3d.core.TypedReferenceCount': 'misc',
    'panda3d.core.VertexDataPage.alloc': 'override',
    'panda3d.core.VertexDataPage.write': 'override',
    'panda3d.core.iostream': 'misc',
    'panda3d.egg.EggData.recompute_polygon_normals': 'override',
    'panda3d.egg.EggData.recompute_vertex_normals': 'override',
    'panda3d.egg.EggData.recomputePolygonNormals': 'assignment',
    'panda3d.egg.EggData.recomputeVertexNormals': 'assignment',
    'panda3d.egg.EggGroup.write': 'override',
    'panda3d.egg.EggTexture.write': 'override',
    'panda3d.egg.EggVertex.compare_to': 'override',
    'panda3d.egg.EggVertex.compareTo': 'assignment',
    'panda3d.egg.EggVertex.sorts_less_than': 'override',
    'panda3d.egg.EggVertex.sortsLessThan': 'assignment',
})
