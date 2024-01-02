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
    '__await__': 'Generator[Any, None, Any]',
    '__bytes__': 'bytes',
    '__fspath__': 'str',
    '__iter__': 'Iterator',
})


# These methods almost certainly behave as if they return `self`
RETURN_SELF: Final = TrackingSet({
    'operator =',
    'operator &=',
    'operator |=',
    'operator ^=',
    'operator <<=',
    'operator >>=',
    'operator +=',
    'operator -=',
    'operator *=',
    'operator /=',
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


# Pretend these classes don't have these bases
SKIP_INHERITANCE: Final = TrackingMap({
    'Triangulator3': {'Triangulator'},
})


# These types only exist under certain conditions
CONDITIONALS: Final = TrackingMap({
    'WindowsRegistry': "sys.platform == 'win32'",
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
    'AsyncFuture::add_done_callback': {(0, 1): 'Callable[[AsyncFuture], object]'},
    'AsyncFuture::gather': {(0, 0): 'AsyncFuture'},
    'BoundingVolume::contains': {(0, 1): 'Self'},
    'BoundingVolume::extend_by': {(0, 1): 'Self'},
    'CallbackObject::make': {(0, 0): 'Callable'},
    'EggAttributes::compare_to': {(0, 1): 'Self'},
    'EggAttributes::sorts_less_than': {(0, 1): 'Self'},
    'EggVertex::compare_to': {(0, 1): 'Self'},
    'EggVertex::sorts_less_than': {(0, 1): 'Self'},
    'Filename::Filename': {(2, 1): 'StrOrBytesPath'},
    'GeometricBoundingVolume::contains': {(0, 1): 'Self'},
    'GeometricBoundingVolume::extend_by': {(0, 1): 'Self'},
    'InternalName::make': {(0, 0): 'str'},
    'IStreamWrapper::IStreamWrapper': {(0, 1): 'core.istream'},
    'NodePath::NodePath': {
        (0, 0): 'NodePath[Never]',
        (1, 1): 'NodePath[_N]',
        (3, 1): '_N',
        (4, 0): 'NodePath[PandaNode]',
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
    'PythonTask::PythonTask': {(0, 1): 'TaskFunction | TaskCoroutine[Any] | None'},
    'PythonTask::set_args': {(0, 1): 'Sequence[Any] | None'},
    'PythonTask::set_function': {(0, 1): 'TaskFunction | None'},
    'PythonTask::set_upon_death': {(0, 1): 'Callable[[], object] | None'},
    'StreamReader::StreamReader': {(1, 1): 'core.istream'},
    'StreamWrapper::StreamWrapper': {(0, 1): 'core.iostream'},
    'StreamWriter::StreamWriter': {(1, 1): 'core.ostream'},
    'StringStream::set_data': {(0, 1): 'bytes'},
    'TextEncoder::append_text': {(0, 1): 'str'},
    'TextEncoder::decode_text': {(0, 1): 'bytes', (1, 1): 'bytes'},
    'TextEncoder::set_text': {(0, 1): 'str', (1, 1): 'bytes'},
    'TypedObject::is_exact_type': {(0, 1): 'TypeHandle | builtins.type'},
    'TypedObject::is_of_type': {(0, 1): 'TypeHandle | builtins.type'},
    'DCClass::client_format_generate_CMU': {(0, 4): 'Sequence[str] | None'},
    'ARToolKit::make': {(0, 0): 'NodePath[Camera]'},
})
RETURN_TYPE_OVERRIDES: Final = TrackingMap[str, str | dict[int, str]]({
    'operator *': {
        16: 'LVecBase2d',
        17: 'LVecBase2f',
        19: 'LVecBase3d',
        21: 'LVecBase3f',
    },
    'AsyncFuture::add_done_callback': 'None',
    'AsyncFuture::gather': 'AsyncFuture',
    'BamReader::get_file_version': 'tuple[int, int]',
    'CallbackObject::make': 'PythonCallbackObject',
    'Datagram::get_message': 'bytes',
    'EventQueue::is_queue_full': 'Literal[False]',
    'Filename::scan_directory': 'list[str]',
    'GlobPattern::match_files': 'list[str]',
    'GraphicsStateGuardian::get_prepared_textures': 'list[Any]',
    'IStreamWrapper::get_istream': 'core.istream',
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
    'OStreamWrapper::get_ostream': 'core.ostream',
    'PandaNode::get_off_clip_planes': 'ClipPlaneAttrib',
    'PandaNode::get_python_tag': 'Any | None',
    'PandaNode::get_python_tag_keys': 'list[Any] | tuple[()]',
    'PandaNode::get_python_tags': 'dict[Any, Any]',
    'PandaNode::get_tag_keys': 'tuple[str, ...]',
    'PythonCallbackObject::get_function': 'Callable',
    'PythonTask::get_args': 'tuple[Any, ...]',
    'PythonTask::get_function': 'TaskFunction | None',
    'PythonTask::get_upon_death': 'Callable[[], object] | None',
    'Ramfile::get_data': 'bytes',
    'Ramfile::read': 'bytes',
    'Ramfile::readline': 'bytes',
    'Ramfile::readlines': 'list[bytes]',
    'RenderAttrib::get_unique': 'Self',
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
    'EggGroupNode::get_children': 'list[EggNode]',
    'OdeBody::get_data': 'bytes',
    'OdeGeom::get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
    'OdeSpace::get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
})


NO_COERCION: Final = TrackingMap({
    'ButtonHandle': {'int'},
    'ColorInterpolationManager': {'LVecBase4f'},
    'ConfigVariableBool': {'str'},
    'ConfigVariableColor': {'str'},
    'ConfigVariableDouble': {'str'},
    'ConfigVariableFilename': {'str'},
    'ConfigVariableInt': {'str'},
    'ConfigVariableInt64': {'str'},
    'ConfigVariableList': {'str'},
    'ConfigVariableString': {'str'},
    'LoaderOptions': {'int'},
    'LOrientationf': {'LMatrix3f', 'LMatrix4f'},
    'LOrientationd': {'LMatrix3d', 'LMatrix4d'},
    'LRotationf': {'LMatrix3f', 'LMatrix4f'},
    'LRotationd': {'LMatrix3d', 'LMatrix4d'},
    # We ignore coercion from unaligned vectors because it introduces
    # too much noise. They're not useful from Python anyway.
    'LVecBase4d': {'LVector3d', 'LPoint3d', 'UnalignedLVecBase4d'},
    'LVecBase4f': {'LVector3f', 'LPoint3f', 'UnalignedLVecBase4f'},
    'LVecBase4i': {'LVector3i', 'LPoint3i', 'UnalignedLVecBase4i'},
    'MovieVideo': {'str'},
    'OdeBody': {'OdeWorld'},
    'pixel': {'int'},
    'PNMImageHeader.PixelSpec': {'int'},
    'RenderState': {'RenderAttrib'},
    'Shader': {'str'},
})
EXTRA_COERCION: Final = TrackingMap({
    'Filename': {'StrOrBytesPath'},
    'InternalName': {'str'},
    'CallbackObject': {'Callable'},
    'LVecBase2f': {'tuple[float, float]'},
    'LVector2f': {'tuple[float, float]'},
    'LPoint2f': {'tuple[float, float]'},
    'LVecBase2d': {'tuple[float, float]'},
    'LVector2d': {'tuple[float, float]'},
    'LPoint2d': {'tuple[float, float]'},
    'LVecBase2i': {'tuple[int, int]'},
    'LVector2i': {'tuple[int, int]'},
    'LPoint2i': {'tuple[int, int]'},
    'LVecBase3f': {'tuple[float, float, float]'},
    'LVector3f': {'tuple[float, float, float]'},
    'LPoint3f': {'tuple[float, float, float]'},
    'LVecBase3d': {'tuple[float, float, float]'},
    'LVector3d': {'tuple[float, float, float]'},
    'LPoint3d': {'tuple[float, float, float]'},
    'LVecBase3i': {'tuple[int, int, int]'},
    'LVector3i': {'tuple[int, int, int]'},
    'LPoint3i': {'tuple[int, int, int]'},
    'LVecBase4f': {'tuple[float, float, float, float]'},
    'UnalignedLVecBase4f': {'tuple[float, float, float, float]'},
    'LVector4f': {'tuple[float, float, float, float]'},
    'LPoint4f': {'tuple[float, float, float, float]'},
    'LQuaternionf': {'tuple[float, float, float, float]'},
    'LRotationf': {'tuple[float, float, float, float]'},
    'LPlanef': {'tuple[float, float, float, float]'},
    'LVecBase4d': {'tuple[float, float, float, float]'},
    'LVector4d': {'tuple[float, float, float, float]'},
    'LPoint4d': {'tuple[float, float, float, float]'},
    'LQuaterniond': {'tuple[float, float, float, float]'},
    'LRotationd': {'tuple[float, float, float, float]'},
    'LPlaned': {'tuple[float, float, float, float]'},
    'UnalignedLVecBase4d': {'tuple[float, float, float, float]'},
    'LVecBase4i': {'tuple[int, int, int, int]'},
    'LVector4i': {'tuple[int, int, int, int]'},
    'LPoint4i': {'tuple[int, int, int, int]'},
    'UnalignedLVecBase4i': {'tuple[int, int, int, int]'},
})


# This adds comments to ignore Mypy errors
IGNORED_MYPY_ERRORS: Final = TrackingMap({
    'AsyncTask': 'misc',
    'AsyncTaskSequence': 'misc',
    'DatagramBuffer': 'misc',
    'DynamicTextFont': 'misc',
    'GeomVertexArrayData': 'misc',
    'GeomVertexRewriter': 'misc',
    'GeomVertexRewriter::operator =': 'override',
    'HTTPDate::operator -=': 'misc',
    'LOrientationd::operator *': 'override',
    'LOrientationf::operator *': 'override',
    'LPlaned::operator *=': 'override',
    'LPlaned::operator *': 'override',
    'LPlaned::project': 'override',
    'LPlanef::operator *=': 'override',
    'LPlanef::operator *': 'override',
    'LPlanef::project': 'override',
    'LQuaterniond::operator *=': 'misc, override',
    'LQuaterniond::operator *': 'override',
    'LQuaternionf::operator *=': 'misc, override',
    'LQuaternionf::operator *': 'override',
    'LRotationd::operator *': 'override',
    'LRotationf::operator *': 'override',
    'LightNode': 'misc',
    'LightLensNode': 'misc',
    'MouseWatcher': 'misc',
    'OSocketStream::flush': 'override',
    'PGItem::get_state': 'override',
    'PGItem::set_state': 'override',
    'PGScrollFrame::setup': 'override',
    'ShaderBuffer': 'misc',
    'Socket_UDP::SendTo': 'override',
    'SocketStream': 'misc',
    'SocketStream::flush': 'override',
    'StreamWrapper': 'misc',
    'TextNode': 'misc',
    'TextNode::get_transform': 'override',
    'TextNode::set_transform': 'override',
    'TextNode::transform': 'assignment',
    'TrackerNode::get_transform': 'override',
    'TypedReferenceCount': 'misc',
    'VertexDataPage::alloc': 'override',
    'VertexDataPage::write': 'override',
    'std::iostream': 'misc',
    'EggData::recompute_polygon_normals': 'override',
    'EggData::recompute_vertex_normals': 'override',
    'EggGroup': 'misc',
    'EggGroup::write': 'override',
    'EggNamedObject': 'misc',
    'EggPrimitive': 'misc',
    'EggTexture': 'misc',
    'EggTexture::write': 'override',
    'EggVertex': 'misc',
})

# This adds comments to ignore Pyright errors
IGNORED_PYRIGHT_ERRORS: Final = TrackingMap({
    'Character::get_bundle': 'reportIncompatibleMethodOverride',
    'LQuaterniond::output': 'reportIncompatibleMethodOverride',
    'LQuaternionf::output': 'reportIncompatibleMethodOverride',
    'SequenceNode::frame_rate': 'reportIncompatibleMethodOverride',
})
