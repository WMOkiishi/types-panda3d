from typing import ClassVar

from direct.showbase.DirectObject import DirectObject
from panda3d.core import GeomNode, LPoint3f, LVector3f, NodePath, PandaNode, ParametricCurve

class Mopath(DirectObject):
    nameIndex: ClassVar[int]
    name: str
    fluid: bool
    tPoint: LPoint3f
    posPoint: LPoint3f
    hprPoint: LPoint3f
    tangentVec: LVector3f
    fFaceForward: bool
    faceForwardDelta: float | None
    faceForwardNode: NodePath | None
    timeScale: float
    upVectorNodePath: NodePath | None
    reverseUpVector: bool
    maxT: float
    loop: bool
    xyzNurbsCurve: ParametricCurve | None
    hprNurbsCurve: ParametricCurve | None
    tNurbsCurve: list[ParametricCurve]
    node: PandaNode
    def __init__(
        self,
        name: str | None = None,
        fluid: bool = ...,
        objectToLoad: NodePath | str | None = None,
        upVectorNodePath: NodePath | None = None,
        reverseUpVector: bool = False,
    ) -> None: ...
    def getMaxT(self) -> float: ...
    def loadFile(self, filename: str, fReset: bool = ...) -> None: ...
    def loadNodePath(self, nodePath: NodePath, fReset: bool = ...) -> None: ...
    def reset(self) -> None: ...
    def calcTime(self, tIn: float) -> float: ...
    def getFinalState(self) -> tuple[LPoint3f, LPoint3f]: ...
    def goTo(self, node: NodePath, time: float) -> None: ...
    def play(self, node: NodePath, time: float = 0.0, loop: bool = ...) -> None: ...
    def stop(self) -> None: ...
    def draw(self, subdiv: int = 1000) -> NodePath[GeomNode]: ...
