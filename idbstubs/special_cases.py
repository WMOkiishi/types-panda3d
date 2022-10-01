from collections.abc import Container
from typing import Final

# Don't write or check for stubs for anything with these names
NO_STUBS: Final = frozenset((
    # as per https://typing.readthedocs.io/en/latest/source/stubs.html#attribute-access
    '__getattribute__', '__delattr__',
    # TODO: These are used for vectors, but the typing is complex.
    '__getattr__', '__setattr__',
    # Pickle stuff
    '__getstate__', '__setstate__', '__reduce__', '__reduce_ex__',
    # Inherited from `object`; signature shouldn't change
    '__dict__', '__repr__', '__str__',
))


# These names are not exposed to Python, even though they may seem like they are
NOT_EXPOSED: Final = frozenset((
    'BitMaskNative',
    # These two haven't been removed yet, but will be soon.
    # (They're currently exposed as panda3d.core.__mul__ / __imul__.)
    # 'operator *',
    # 'operator *=',
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
))


# These almost certainly behave as if they return `self`
INPLACE_DUNDERS: Final = frozenset({
    '__iand__', '__ior__', '__ixor__', '__ilshift__', '__irshift__',
    '__iadd__', '__isub__', '__imul__', '__itruediv__', '__ifloordiv__',
    '__imod__', '__ipow__',
})


# Camel-case aliases are not generated for these names
NO_MANGLING: Final = INPLACE_DUNDERS | {
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
}


# These classes implement iteration via `__getitem__`
ITERABLE: Final = {
    'AsyncTaskCollection': 'AsyncTask',
    'LVecBase2f': 'float', 'LVecBase2d': 'float', 'LVecBase2i': 'int',
    'LVecBase3f': 'float', 'LVecBase3d': 'float', 'LVecBase3i': 'int',
    'LVecBase4f': 'float', 'LVecBase4d': 'float', 'LVecBase4i': 'int',
}

# These classes are effectively generic
GENERIC: Final = {
    'NodePath': '_N',
}


ATTRIBUTE_NAME_SHADOWS: Final[dict[str, Container[str]]] = {
    'panda3d.core.StreamReader': ('istream',),
    'panda3d.core.StreamWriter': ('ostream',),
    'panda3d.core.StreamWrapper': ('iostream',),
    'panda3d.core.IStreamWrapper': ('istream',),
    'panda3d.core.OStreamWrapper': ('ostream',),
}


ATTR_TYPE_OVERRIDES: Final = {
    'BamReader::file_version': 'tuple[int, int]',
    'EggGroupNode::children': 'list[EggNode]',
    'PythonCallbackObject::function': 'Callable',
    'StringStream::data': 'bytes',
    'TextEncoder::text': 'str',
}


CONDITIONALS: Final = {
    'panda3d.core.WindowsRegistry': "sys.platform == 'win32'",
}


PARAM_TYPE_OVERRIDES: dict[str, dict[tuple[int, int], str]] = {
    'panda3d.core.Filename.__init__': {(1, 1): 'StrOrBytesPath'},
    'panda3d.core.NodePath.__init__': {
        (1, 1): 'NodePath[_N]', (2, 1): '_N', (4, 2): '_N'
    },
    'panda3d.core.NodePath.any_path': {(0, 0): '_M'},
    'panda3d.core.NodePath.attach_new_node': {(0, 1): '_M'},
    'panda3d.core.PythonCallbackObject.__init__': {(0, 1): 'Callable'},
    'panda3d.core.PythonCallbackObject.set_function': {(0, 1): 'Callable'},
    'panda3d.core.PythonTask.__init__': {(0, 1): 'Callable'},
    'panda3d.core.PythonTask.set_function': {(0, 1): 'Callable'},
    'panda3d.core.PythonTask.set_upon_death': {(0, 1): 'Callable'},
    'panda3d.core.StringStream.set_data': {(0, 1): 'bytes'},
    'panda3d.core.TextEncoder.decode_text': {(0, 1): 'bytes', (1, 1): 'bytes'},
    'panda3d.core.TextEncoder.set_text': {(0, 1): 'str', (1, 1): 'bytes'},
}

RETURN_TYPE_OVERRIDES: dict[str, str | dict[int, str]] = {
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
    'panda3d.core.Filename.__fspath__': 'str',
    'panda3d.core.Filename.scan_directory': 'list[str]',
    'panda3d.core.GlobPattern.match_files': 'list[str]',
    'panda3d.core.GraphicsStateGuardian.get_prepared_textures': 'list[Any]',
    'panda3d.core.NodePath.any_path': 'NodePath[_M]',
    'panda3d.core.NodePath.attach_new_node': {0: 'NodePath[_M]'},
    'panda3d.core.NodePath.flatten_light': 'Literal[0]',
    'panda3d.core.NodePath.get_python_tags': 'dict[Any, Any] | None',
    'panda3d.core.NodePath.get_tag_keys': 'tuple[str, ...] | None',
    'panda3d.core.NodePath.get_tight_bounds': 'tuple[LPoint3f, LPoint3f] | None',
    'panda3d.core.NodePath.node': '_N',
    'panda3d.core.NodePathCollection.get_tight_bounds': 'tuple[LPoint3f, LPoint3f] | None',
    'panda3d.core.OccluderNode.get_num_vertices': 'Literal[4]',
    'panda3d.core.PandaNode.get_python_tags': 'dict[Any, Any]',
    'panda3d.core.PandaNode.get_tag_keys': 'tuple[str, ...]',
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
    'panda3d.core.VirtualFile.extract_bytes': 'bytes',
    'panda3d.core.VirtualFile.read_file': 'bytes',
    'panda3d.egg.EggGroupNode.get_children': 'list[EggNode]',
    'panda3d.ode.OdeGeom.get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
    'panda3d.ode.OdeSpace.get_AA_bounds': 'tuple[LPoint3f, LPoint3f]',
}

_fixed_lengths = [
    ('LMatrix3f', 3), ('LMatrix3f.Row', 3), ('LMatrix3f.CRow', 3),
    ('LMatrix3d', 3), ('LMatrix3d.Row', 3), ('LMatrix3d.CRow', 3),
    ('LMatrix4f', 4), ('LMatrix4f.Row', 4), ('LMatrix4f.CRow', 4),
    ('LMatrix4d', 4), ('LMatrix4d.Row', 4), ('LMatrix4d.CRow', 4),
    ('pixel', 3), ('PNMImageHeader.PixelSpec', 4),
]
for _name, _len in _fixed_lengths:
    RETURN_TYPE_OVERRIDES[f'panda3d.core.{_name}.__len__'] = f'Literal[{_len}]'


IGNORE_ERRORS: Final = {
    'panda3d.core.AsyncTaskSequence': 'misc',
    'panda3d.core.DatagramBuffer': 'misc',
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
    'panda3d.core.LQuaterniond.project': 'override',
    'panda3d.core.LQuaternionf.__imul__': 'misc, override',
    'panda3d.core.LQuaternionf.__mul__': 'override',
    'panda3d.core.LQuaternionf.project': 'override',
    'panda3d.core.LRotationd.__mul__': 'override',
    'panda3d.core.LRotationf.__mul__': 'override',
    'panda3d.core.LightNode': 'misc',
    'panda3d.core.LightLensNode': 'misc',
    'panda3d.core.MouseWatcher': 'misc',
    'panda3d.core.OSocketStream.flush': 'override',
    'panda3d.core.PGItem.get_state': 'override',
    'panda3d.core.PGItem.set_state': 'override',
    'panda3d.core.PGScrollFrame.setup': 'override',
    'panda3d.core.Socket_UDP.SendTo': 'override',
    'panda3d.core.SocketStream': 'misc',
    'panda3d.core.SocketStream.flush': 'override',
    'panda3d.core.StreamWrapper': 'misc',
    'panda3d.core.TextNode.get_transform': 'override',
    'panda3d.core.TextNode.set_transform': 'override',
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
}
