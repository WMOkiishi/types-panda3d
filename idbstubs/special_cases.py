import logging
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
    # The signatures for these don't change.
    '__repr__', '__str__',
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
    # 'operator --': 'decrement',
    'operator ^': '__xor__',
    # 'operator %': '__mod__',
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
    # 'operator --': 'decrement',
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
    '__await__': 'Iterator',
    '__bytes__': 'bytes',
    '__fspath__': 'str',
    '__iter__': 'Iterator',
})


# These methods almost certainly behave as if they return `self`
RETURN_SELF: Final = TrackingSet({
    '__iand__',
    '__ior__',
    '__ixor__',
    '__ilshift__',
    '__irshift__',
    '__iadd__',
    '__isub__',
    '__imul__',
    '__itruediv__',
    '__ifloordiv__',
    '__ipow__',
})


# Camel-case aliases are not generated for functions with these names.
NO_ALIAS: Final = TrackingSet({
    '_del',
    '__init__', '__call__', '__iter__', '__await__',
    '__getitem__', '__setitem__',
    '__eq__', '__ne__', '__lt__', '__le__', '__ge__', '__gt__',
    '__neg__', '__invert__',
    '__and__', '__or__', '__xor__', '__lshift__', '__rshift__',
    '__iand__', '__ior__', '__ixor__', '__ilshift__', '__irshift__',
    '__add__', '__sub__', '__mul__', '__truediv__', '__floordiv__',
    '__iadd__', '__isub__', '__imul__', '__itruediv__', '__ifloordiv__',
    '__ipow__', '__pow__',
    '__float__', '__int__', '__bool__', '__len__',
    '__copy__', '__deepcopy__', '__reduce_persist__',
})


# These types are effectively generic
GENERIC: Final = TrackingMap({
    'NodePath': '_N',
})


# Don't replace `size` with `__len__` for these
SIZE_NOT_LEN: Final = TrackingSet(('EggGroupNode', 'WindowProperties'))


# These types only exist under certain conditions
CONDITIONALS: Final = TrackingMap({
    'panda3d.core.WindowsRegistry': "sys.platform == 'win32'",
})


# These override type hints for various things
ATTR_TYPE_OVERRIDES: Final = TrackingMap({
    'BamReader::file_version': 'tuple[int, int]',
    'NodePath::python_tags': 'dict[Any, Any] | None',
    'NodePath::tags': 'MutableMapping[str, str] | None',
    'PandaNode::python_tags': 'dict[Any, Any]',
    'PythonCallbackObject::function': 'Callable',
    'StringStream::data': 'bytes',
    'TextEncoder::text': 'str',
    'EggGroupNode::children': 'list[EggNode]',
})
PARAM_TYPE_OVERRIDES: Final = TrackingMap[str, dict[tuple[int, int], str]]({
    'AsyncFuture::gather': {(0, 0): 'AsyncFuture'},
    'CallbackObject::make': {(0, 0): 'Callable'},
    'ConnectionReader::set_tcp_header_size': {(0, 1): 'Literal[0, 2, 4]'},
    'ConnectionWriter::set_tcp_header_size': {(0, 1): 'Literal[0, 2, 4]'},
    'Filename::Filename': {(2, 1): 'StrOrBytesPath'},
    'InternalName::make': {(0, 0): 'str'},
    'IStreamWrapper::IStreamWrapper': {(0, 1): 'core.istream'},
    'NodePath::NodePath': {
        (0, 0): 'NodePath[Never]',
        (1, 1): 'NodePath[_N]',
        (3, 1): '_N',
        (2, 2): '_N',
    },
    'NodePath::any_path': {(0, 0): '_M'},
    'NodePath::attach_new_node': {(0, 1): '_M'},
    'NodePath::clear_python_tag': {(0, 1): 'Any'},
    'NodePath::find_net_python_tag': {(0, 1): 'Any'},
    'NodePath::get_net_python_tag': {(0, 1): 'Any'},
    'NodePath::get_python_tag': {(0, 1): 'Any'},
    'NodePath::has_net_python_tag': {(0, 1): 'Any'},
    'NodePath::has_python_tag': {(0, 1): 'Any'},
    'NodePath::set_python_tag': {(0, 1): 'Any', (0, 2): 'Any'},
    'NodePathCollection::NodePathCollection': {(2, 1): 'Sequence[NodePath]'},
    'OStreamWrapper::OStreamWrapper': {(0, 1): 'core.ostream'},
    'PandaNode::clear_python_tag': {(0, 1): 'Any'},
    'PandaNode::get_python_tag': {(0, 1): 'Any'},
    'PandaNode::has_python_tag': {(0, 1): 'Any'},
    'PandaNode::set_python_tag': {(0, 1): 'Any', (0, 2): 'Any'},
    'PythonCallbackObject::PythonCallbackObject': {(0, 1): 'Callable'},
    'PythonCallbackObject::set_function': {(0, 1): 'Callable'},
    'PythonTask::PythonTask': {(0, 1): 'Callable'},
    'PythonTask::set_function': {(0, 1): 'Callable'},
    'PythonTask::set_upon_death': {(0, 1): 'Callable'},
    'SocketStream::set_tcp_header_size': {(0, 1): 'Literal[0, 2, 4]'},
    'SSReader::set_tcp_header_size': {(0, 1): 'Literal[0, 2, 4]'},
    'SSWriter::set_tcp_header_size': {(0, 1): 'Literal[0, 2, 4]'},
    'StreamReader::StreamReader': {(1, 1): 'core.istream'},
    'StreamWrapper::StreamWrapper': {(0, 1): 'core.iostream'},
    'StreamWriter::StreamWriter': {(1, 1): 'core.ostream'},
    'StringStream::set_data': {(0, 1): 'bytes'},
    'TextEncoder::append_text': {(0, 1): 'str'},
    'TextEncoder::decode_text': {(0, 1): 'bytes', (1, 1): 'bytes'},
    'TextEncoder::set_text': {(0, 1): 'str', (1, 1): 'bytes'},
    'TextureStage::set_alpha_scale': {(0, 1): 'Literal[1, 2, 4]'},
    'TextureStage::set_rgb_scale': {(0, 1): 'Literal[1, 2, 4]'},
    'TypedObject::is_exact_type': {(0, 1): 'TypeHandle | builtins.type'},
    'TypedObject::is_of_type': {(0, 1): 'TypeHandle | builtins.type'},
    'CConnectionRepository::set_tcp_header_size': {(0, 1): 'Literal[0, 2, 4]'},
    'DCClass::client_format_generate_CMU': {(0, 4): 'Sequence[str] | None'},
    'EggTexture::set_alpha_scale': {(0, 1): 'Literal[1, 2, 4]'},
    'EggTexture::set_rgb_scale': {(0, 1): 'Literal[1, 2, 4]'},
    'ARToolKit::make': {(0, 0): 'NodePath[Camera]'},
})
RETURN_TYPE_OVERRIDES: Final = TrackingMap[str, str | dict[int, str]]({
    'operator *': {
        16: 'LVecBase2d',
        17: 'LVecBase2f',
        19: 'LVecBase3d',
        21: 'LVecBase3f',
    },
    'AsyncFuture::gather': 'AsyncFuture',
    'BamReader::get_file_version': 'tuple[int, int]',
    'BoundingBox::get_num_planes': 'Literal[6]',
    'BoundingBox::get_num_points': 'Literal[8]',
    'BoundingHexahedron::get_num_planes': 'Literal[6]',
    'BoundingHexahedron::get_num_points': 'Literal[8]',
    'CallbackObject::make': 'PythonCallbackObject',
    'CollisionBox::get_num_planes': 'Literal[6]',
    'CollisionBox::get_num_points': 'Literal[8]',
    'Datagram::get_message': 'bytes',
    'EventQueue::is_queue_full': 'Literal[False]',
    'Filename::scan_directory': 'list[str]',
    'GlobPattern::match_files': 'list[str]',
    'GraphicsStateGuardian::get_prepared_textures': 'list[Any]',
    'IStreamWrapper::get_istream': 'core.istream',
    'LMatrix3f::size': 'Literal[3]',
    'LMatrix3f::Row::size': 'Literal[3]',
    'LMatrix3f::CRow::size': 'Literal[3]',
    'LMatrix3d::size': 'Literal[3]',
    'LMatrix3d::Row::size': 'Literal[3]',
    'LMatrix3d::CRow::size': 'Literal[3]',
    'LMatrix4f::size': 'Literal[4]',
    'LMatrix4f::Row::size': 'Literal[4]',
    'LMatrix4f::CRow::size': 'Literal[4]',
    'LMatrix4d::size': 'Literal[4]',
    'LMatrix4d::Row::size': 'Literal[4]',
    'LMatrix4d::CRow::size': 'Literal[4]',
    'NodePath::any_path': 'NodePath[_M]',
    'NodePath::attach_new_node': {0: 'NodePath[_M]'},
    'NodePath::flatten_light': 'Literal[0]',
    'NodePath::get_net_python_tag': 'Any | None',
    'NodePath::get_python_tag': 'Any | None',
    'NodePath::get_python_tag_keys': 'list[Any] | tuple[()]',
    'NodePath::get_python_tags': 'dict[Any, Any] | None',
    'NodePath::get_tag_keys': 'tuple[str, ...] | None',
    'NodePath::get_tags': 'MutableMapping[str, str] | None',
    'NodePath::get_tight_bounds': 'tuple[LPoint3f, LPoint3f] | None',
    'NodePath::node': '_N',
    'NodePathCollection::get_tight_bounds': 'tuple[LPoint3f, LPoint3f] | None',
    'OccluderNode::get_num_vertices': 'Literal[4]',
    'OStreamWrapper::get_ostream': 'core.ostream',
    'PandaNode::get_python_tag': 'Any | None',
    'PandaNode::get_python_tag_keys': 'list[Any] | tuple[()]',
    'PandaNode::get_python_tags': 'dict[Any, Any]',
    'PandaNode::get_tag_keys': 'tuple[str, ...]',
    'PNMImageHeader::PixelSpec::size': 'Literal[4]',
    'PythonCallbackObject::get_function': 'Callable',
    'PythonTask::get_args': 'tuple[Any, ...]',
    'PythonTask::get_function': 'Callable',
    'PythonTask::get_upon_death': 'Callable',
    'Ramfile::get_data': 'bytes',
    'Ramfile::read': 'bytes',
    'Ramfile::readline': 'bytes',
    'Ramfile::readlines': 'list[bytes]',
    'RenderState::get_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'RenderState::get_invert_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'RenderState::get_states': 'list[RenderState]',
    'RenderState::get_unused_states': 'list[RenderState]',
    'SparseArray::has_max_num_bits': 'Literal[False]',
    'StreamReader::extract_bytes': 'bytes',
    'StreamReader::get_istream': 'core.istream',
    'StreamReader::readline': 'bytes',
    'StreamReader::readlines': 'list[bytes]',
    'StreamWriter::get_ostream': 'core.ostream',
    'StreamWrapper::get_iostream': 'core.iostream',
    'StringStream::get_data': 'bytes',
    'TextEncoder::decode_text': 'str',
    'TextEncoder::encode_wchar': 'bytes',
    'TextEncoder::encode_wtext': 'bytes',
    'TextEncoder::get_text': {0: 'str', 1: 'bytes'},
    'TransformState::get_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'TransformState::get_invert_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'TransformState::get_states': 'list[TransformState]',
    'TransformState::get_unused_states': 'list[TransformState]',
    'VirtualFile::read_file': 'bytes',
    'pixel::size': 'Literal[3]',
    'EggGroupNode::get_children': 'list[EggNode]',
    'OdeBody::get_data': 'bytes',
    'OdeGeom::get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
    'OdeSpace::get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
})


NO_COERCION: Final = TrackingMap({
    'ConfigVariableBool': {'str'},
    'ConfigVariableColor': {'str'},
    'ConfigVariableDouble': {'str'},
    'ConfigVariableFilename': {'str'},
    'ConfigVariableInt': {'str'},
    'ConfigVariableInt64': {'str'},
    'ConfigVariableList': {'str'},
    'ConfigVariableString': {'str'},
    'LMatrix4d': {'LMatrix3d'},
    'LMatrix4f': {'LMatrix3f'},
    'LOrientationf': {'LMatrix3f', 'LMatrix4f'},
    'LOrientationd': {'LMatrix3d', 'LMatrix4d'},
    'LRotationf': {'LMatrix3f', 'LMatrix4f'},
    'LRotationd': {'LMatrix3d', 'LMatrix4d'},
    'LVecBase4d': {'LVecBase3d', 'LVector3d', 'LPoint3d'},
    'LVecBase4f': {'LVecBase3f', 'LVector3f', 'LPoint3f'},
    'LVecBase4i': {'LVecBase3i', 'LVector3i', 'LPoint3i'},
    'MovieVideo': {'str'},
    'OdeBody': {'OdeWorld'},
    'pixel': {'int'},
    'PNMImageHeader.PixelSpec': {'int'},
    'Shader': {'str'},
})
EXTRA_COERCION: Final = TrackingMap({
    'Filename': {'StrOrBytesPath'},
    'InternalName': {'str'},
    'CallbackObject': {'Callable'},
})


# This adds comments to ignore Mypy errors
IGNORE_ERRORS: Final = TrackingMap({
    'panda3d.core.Character.getBundle': 'assignment',
    'panda3d.core.DatagramBuffer': 'misc',
    'panda3d.core.DynamicTextFont': 'misc',
    'panda3d.core.GeomVertexRewriter': 'misc',
    'panda3d.core.GeomVertexRewriter.assign': 'override',
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
