__all__ = ['setupMirror', 'showFrustum']

from typing_extensions import TypeAlias

from panda3d.core import ConfigVariableColor, LMatrix4f, LVecBase4f, NodePath, UnalignedLVecBase4f

_Vec4f: TypeAlias = LVecBase4f | UnalignedLVecBase4f | LMatrix4f.Row | LMatrix4f.CRow | ConfigVariableColor

def setupMirror(
    name: str,
    width: float,
    height: float,
    rootCamera: NodePath | None = None,
    bufferSize: int = 256,
    clearColor: _Vec4f | None = None,
) -> NodePath: ...
def showFrustum(np: NodePath) -> None: ...
