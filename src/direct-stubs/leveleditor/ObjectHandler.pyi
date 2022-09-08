from typing_extensions import SupportsIndex

from panda3d.core import NodePath
from ..actor.Actor import Actor

class ObjectHandler:
    editor = ...
    def __init__(self, editor) -> None: ...
    def createDoubleSmiley(self, horizontal: bool = True) -> NodePath: ...
    def updateDoubleSmiley(self, val: float, obj) -> None: ...
    def updateSmiley(self, val: SupportsIndex, obj) -> None: ...
    def createPanda(self) -> PandaActor: ...
    def createGrass(self) -> NodePath: ...

class PandaActor(Actor):
    def __init__(self) -> None: ...
