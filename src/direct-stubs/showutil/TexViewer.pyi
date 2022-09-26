from panda3d.core import NodePath, Texture
from ..showbase.DirectObject import DirectObject

class TexViewer(DirectObject):
    tex: Texture
    cleanedUp: bool
    root: NodePath
    cards: NodePath
    t2: Texture
    def __init__(self, tex: Texture) -> None: ...
    def cleanup(self) -> None: ...
