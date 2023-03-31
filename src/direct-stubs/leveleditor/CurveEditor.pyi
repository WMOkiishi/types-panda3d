from collections.abc import Sequence
from typing_extensions import Literal, TypeAlias

from direct.directtools.DirectSelection import DirectNodePath
from direct.showbase.DirectObject import DirectObject
from direct.showutil.Rope import Rope
from direct.task.Task import Task
from panda3d._typing import Vec3Like, Vec4Like
from panda3d.core import NodePath, NurbsCurveEvaluator

from .LevelEditor import LevelEditor

_Vert: TypeAlias = Vec3Like | Vec4Like

class CurveEditor(DirectObject):
    editor: LevelEditor
    i: int
    ropeNum: int
    curve: list[_Vert]
    curveControl: list[tuple[int, NodePath]]
    currentRope: Rope | None
    degree: int
    selected: DirectNodePath
    currentCurve: NurbsCurveEvaluator
    def __init__(self, editor: LevelEditor) -> None: ...
    def createCurve(self) -> None: ...
    def editCurve(self, task: Task) -> Literal[1] | None: ...
    def onControlerDelete(self) -> None: ...
    def ropeUpdate(self, curve: Sequence[_Vert]) -> None: ...
    def onBaseMode(self) -> None: ...
    def updateScene(self) -> None: ...
    def doneEdit(self) -> None: ...
    def createControler(self, x: float, y: float) -> None: ...
