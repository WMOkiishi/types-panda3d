from direct.showbase.DirectObject import DirectObject
from panda3d.core import NodePath, Texture

class TexViewer(DirectObject):
    tex: Texture
    cleanedUp: bool
    root: NodePath
    cards: NodePath
    t2: Texture
    def __init__(self, tex: Texture) -> None: ...
    def cleanup(self) -> None: ...
