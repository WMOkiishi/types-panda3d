from collections.abc import Callable, Sequence
from typing_extensions import TypeAlias

from direct.interval import MetaInterval
from panda3d.core import LVecBase3f, NodePath

_Unused: TypeAlias = object

class AnimMgrBase:
    editor = ...
    graphEditorCounter: int
    keyFramesInfo: dict
    curveAnimation: dict
    lerpFuncs: dict[str, Callable[..., None]]
    curveLerpFuncs: dict[str, tuple[Callable[..., None], Callable[..., None]]]
    keyFrames: list
    points: list[LVecBase3f]
    hprs: list[LVecBase3f]
    curveSequence: MetaInterval.Sequence
    parallel: list
    def __init__(self, editor) -> None: ...
    def reset(self) -> None: ...
    def generateKeyFrames(self) -> None: ...
    def generateSlope(self, list: Sequence) -> None: ...
    def removeAnimInfo(self, uid) -> None: ...
    def singleCurveAnimation(self, nodePath, curve, time) -> MetaInterval.Sequence: ...
    def createParallel(self, startFrame: int, endFrame: int) -> list: ...
    def createCurveAnimation(self, parallel: list) -> None: ...
    def createActorAnimation(self, parallel: list, startFrame: int, endFrame: int) -> None: ...
    def createKeyFrameAnimation(self, parallel: list, startFrame: int, endFrame: int) -> None: ...
    def createCurveKeyFrameAnimation(self, parallel: list, startFrame: int, endFrame: int) -> None: ...
    def getPos(self, x: float, list: Sequence, i: int) -> float: ...
    def calculateT(self, a: float, b: float, c: float, d: float, x: _Unused) -> float: ...
    def lerpFuncX(self, pos: LVecBase3f, np: NodePath) -> None: ...
    def lerpFuncY(self, pos: LVecBase3f, np: NodePath) -> None: ...
    def lerpFuncZ(self, pos: LVecBase3f, np: NodePath) -> None: ...
    def lerpCurveFuncX(self, t: float, extraArgs) -> None: ...
    def lerpCurveFuncY(self, t: float, extraArgs) -> None: ...
    def lerpCurveFuncZ(self, t: float, extraArgs) -> None: ...
    def lerpFuncH(self, angle: float, np: NodePath) -> None: ...
    def lerpFuncP(self, angle: float, np: NodePath) -> None: ...
    def lerpFuncR(self, angle: float, np: NodePath) -> None: ...
    def lerpFuncSX(self, scale: float, np: NodePath) -> None: ...
    def lerpFuncSY(self, scale: float, np: NodePath) -> None: ...
    def lerpFuncSZ(self, scale: float, np: NodePath) -> None: ...
    def lerpFuncCR(self, R: float, np: NodePath) -> None: ...
    def lerpFuncCG(self, G: float, np: NodePath) -> None: ...
    def lerpFuncCB(self, B: float, np: NodePath) -> None: ...
    def lerpFuncCA(self, A: float, np: NodePath) -> None: ...
    def colorUpdate(self, r: float, g: float, b: float, a: float, np: NodePath) -> None: ...
