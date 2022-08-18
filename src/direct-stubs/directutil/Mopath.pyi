from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from panda3d.core import GeomNode, LPoint3f, LVector3f, NodePath, ParametricCurve
from ..showbase.DirectObject import DirectObject

_OldBool: TypeAlias = Literal[0, 1]

class Mopath(DirectObject):
    nameIndex: ClassVar[int]
    name: str
    fluid: bool | _OldBool
    tPoint: LPoint3f
    tPoint: LPoint3f
    posPoint: LPoint3f
    hprPoint: LPoint3f
    tangentVec: LVector3f
    fFaceForward: bool | _OldBool
    faceForwardDelta: float | None
    faceForwardNode: NodePath | None
    timeScale: float
    upVectorNodePath: NodePath | None
    reverseUpVector: bool
    maxT: float
    loop: bool | _OldBool
    xyzNurbsCurve: ParametricCurve | None
    hprNurbsCurve: ParametricCurve | None
    tNurbsCurve: list
    node = ...
    def __init__(
        self,
        name: str | None = None,
        fluid: bool = True,
        objectToLoad: NodePath | str | None = None,
        upVectorNodePath: NodePath | None = None,
        reverseUpVector: bool = False
    ) -> None: ...
    def getMaxT(self) -> float: ...
    def loadFile(self, filename: str, fReset: bool = True) -> None: ...
    def loadNodePath(self, nodePath: NodePath, fReset: bool = True) -> None: ...
    def reset(self) -> None: ...
    def calcTime(self, tIn: float) -> float: ...
    def getFinalState(self) -> tuple[LPoint3f, LPoint3f]: ...
    def goTo(self, node: NodePath, time: float) -> None: ...
    def play(self, node: NodePath, time: float = 0, loop: bool = False) -> None: ...
    def stop(self) -> None: ...
    def draw(self, subdiv: int = 1000) -> NodePath[GeomNode]: ...
