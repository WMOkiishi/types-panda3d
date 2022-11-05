__all__ = ['setupMirror', 'showFrustum']

from panda3d._typing import Vec4Like
from panda3d.core import NodePath

def setupMirror(
    name: str,
    width: float,
    height: float,
    rootCamera: NodePath | None = ...,
    bufferSize: int = ...,
    clearColor: Vec4Like | None = ...,
) -> NodePath: ...
def showFrustum(np: NodePath) -> None: ...
