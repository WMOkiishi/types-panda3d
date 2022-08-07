from itertools import product
from typing import Final

# Don't write or check for stubs for anything with these names
NO_STUBS: Final = frozenset((
    # as per https://typing.readthedocs.io/en/latest/source/stubs.html#attribute-access
    '__getattribute__', '__delattr__',
    # TODO: These are used for vectors, but the typing is complex.
    '__getattr__', '__setattr__',
    # Pickle stuff
    '__getstate__', '__setstate__',
    '__reduce__', '__reduce_ex__', '__reduce_persist__',
    # Inherited from `object`; signature shouldn't change
    '__dict__', '__repr__',
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
    'LVecBase2i::operator /',
    'LVecBase2i::operator /=',
    'LVecBase3i::operator /',
    'LVecBase3i::operator /=',
    'LVecBase4i::operator /',
    'LVecBase4i::operator /=',
    'LVector2i::operator /',
    'LVector2i::operator /=',
    'LVector3i::operator /',
    'LVector3i::operator /=',
    'LVector4i::operator /',
    'LVector4i::operator /=',
    'LPoint2i::operator /',
    'LPoint2i::operator /=',
    'LPoint3i::operator /',
    'LPoint3i::operator /=',
    'LPoint4i::operator /',
    'LPoint4i::operator /=',
    'LVecBase2f::get_data',
    'LVecBase2d::get_data',
    'LVecBase2i::get_data',
    'LVecBase3f::get_data',
    'LVecBase3d::get_data',
    'LVecBase3i::get_data',
    'LVecBase4f::get_data',
    'LVecBase4d::get_data',
    'LVecBase4i::get_data',
    'UnalignedLVecBase4f::get_data',
    'UnalignedLVecBase4d::get_data',
    'UnalignedLVecBase4i::get_data',
    'LMatrix3f::get_data',
    'LMatrix3d::get_data',
    'LMatrix4f::get_data',
    'LMatrix4d::get_data',
    'UnalignedLMatrix4f::get_data',
    'UnalignedLMatrix4d::get_data',
))


# Camel-case aliases are not generated for these names
NO_MANGLING: Final = frozenset((
    '_del',
    '__init__', '__call__', '__iter__', '__await__',
    '__getattribute__', '__getattr__', '__setattr__', '__delattr__',
    '__getitem__', '__setitem__', '__delitem__',
    '__eq__', '__ne__', '__lt__', '__le__', '__ge__', '__gt__',
    '__neg__', '__pos__', '__invert__',
    '__and__', '__or__', '__xor__', '__lshift__', '__rshift__',
    '__iand__', '__ior__', '__ixor__', '__ilshift__', '__irshift__',
    '__rand__', '__ror__', '__rxor__', '__rlshift__', '__rrshift__',
    '__add__', '__sub__', '__mul__', '__truediv__', '__floordiv__',
    '__iadd__', '__isub__', '__imul__', '__itruediv__', '__ifloordiv__',
    '__radd__', '__rsub__', '__rmul__', '__rtruediv__', '__rfloordiv__',
    '__mod__', '__imod__', '__rmod__', '__pow__', '__ipow__', '__rpow__',
    '__repr__', '__str__', '__float__', '__int__', '__bool__', '__len__',
    '__copy__', '__deepcopy__', '__getstate__', '__setstate__',
    '__reduce__', '__reduce_ex__', '__reduce_persist__',
))


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


PARAM_TYPE_OVERRIDES: dict[str, dict[tuple[int, int], str]] = {
    'panda3d.core.Filename.__init__': {(1, 1): 'str | bytes | PathLike'},
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
    'panda3d.core.TextEncoder.decode_text': {(0, 1): 'bytes'},
}

RETURN_TYPE_OVERRIDES: dict[str, str | dict[int, str]] = {
    'panda3d.core.AsyncFuture.__await__': 'Generator[Awaitable, None, None]',
    'panda3d.core.AsyncFuture.__iter__': 'Generator[Awaitable, None, None]',
    'panda3d.core.Datagram.get_message': 'bytes',
    'panda3d.core.Filename.__fspath__': 'str',
    'panda3d.core.Filename.scan_directory': 'list[str]',
    'panda3d.core.GlobPattern.match_files': 'list[str]',
    'panda3d.core.GraphicsStateGuardian.get_prepared_textures': 'list[Any]',
    'panda3d.core.NodePath.any_path': 'NodePath[_M]',
    'panda3d.core.NodePath.attach_new_node': {0: 'NodePath[_M]'},
    'panda3d.core.NodePath.get_python_tags': 'dict[Any, Any] | None',
    'panda3d.core.NodePath.node': '_N',
    'panda3d.core.PandaNode.get_python_tags': 'dict[Any, Any]',
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
    'panda3d.core.TextEncoder.decode_text': 'str',
    'panda3d.core.TextEncoder.encode_wchar': 'bytes',
    'panda3d.core.TextEncoder.encode_wtext': 'bytes',
    'panda3d.core.TransformState.get_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'panda3d.core.TransformState.get_invert_composition_cache': 'list[tuple[Any, Any] | tuple[None, None]]',
    'panda3d.core.TransformState.get_states': 'list[TransformState]',
    'panda3d.core.TransformState.get_unused_states': 'list[TransformState]',
    'panda3d.core.VirtualFile.read_file': 'bytes',
}
_returns_self = product(
    ('LVecBase2f', 'LVecBase2d', 'LVecBase2i',
     'LVecBase3f', 'LVecBase3d', 'LVecBase3i',
     'LVecBase4f', 'LVecBase4d', 'LVecBase4i'),
    ('__floordiv__', '__ifloordiv__', '__pow__', '__ipow__',
     '__iadd__', '__isub__', '__imul__', '__itruediv__',
     '__round__', '__floor__', '__ceil__')
)
for _name, _func in _returns_self:
    _func_name = '.'.join(('panda3d.core', _name, _func))
    RETURN_TYPE_OVERRIDES[_func_name] = 'Self'
    PARAM_TYPE_OVERRIDES.setdefault(_func_name, {})[(0, 0)] = 'Self'
