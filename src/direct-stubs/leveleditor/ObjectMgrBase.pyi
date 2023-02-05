from collections.abc import Iterable
from typing import SupportsInt, TypeVar

from direct._typing import Incomplete, Obj, Unused
from direct.actor import Actor
from panda3d._typing import Mat4Like, Vec3Like
from panda3d.core import LMatrix4f, NodePath, PandaNode

from .LevelEditor import LevelEditor

_N = TypeVar('_N', bound=PandaNode)

class PythonNodePath(NodePath[_N]):
    def __init__(self, node: _N) -> None: ...

class ObjectMgrBase:
    editor: LevelEditor
    objects: dict[str, Obj]
    npIndex: dict[NodePath, str]
    saveData: list[str]
    objectsLastXform: dict[str, LMatrix4f]
    lastUid: str
    lastUidMode: int
    currNodePath: NodePath | None
    currLiveNP: NodePath | None
    Actor: list[Obj[Actor.Actor, Incomplete]]
    Nodes: list[Obj[NodePath, Incomplete]]
    def __init__(self, editor: LevelEditor) -> None: ...
    def reset(self) -> None: ...
    def genUniqueId(self) -> str: ...
    def addNewCurveFromFile(
        self,
        curveInfo: Iterable[tuple[str, Vec3Like]],
        degree,
        uid: str | None = None,
        parent=None,
        fSelectObject: bool = True,
        nodePath: Unused = None,
    ) -> NodePath: ...
    def addNewCurve(
        self, curveInfo, degree, uid: str | None = None, parent=None, fSelectObject: bool = True, nodePath: NodePath | None = None
    ) -> NodePath: ...
    def addNewObject(
        self,
        typeName,
        uid: str | None = None,
        model=None,
        parent=None,
        anim=None,
        fSelectObject: bool = True,
        nodePath=None,
        nameStr: str | None = None,
    ) -> NodePath | None: ...
    def removeObjectById(self, uid: str) -> None: ...
    def removeObjectByNodePath(self, nodePath: NodePath) -> None: ...
    def findObjectById(self, uid: str): ...
    def findObjectByNodePath(self, nodePath: NodePath) -> Obj | None: ...
    def findObjectByNodePathBelow(self, nodePath: NodePath) -> Obj | None: ...
    def findObjectsByTypeName(self, typeName: str) -> list[Obj]: ...
    def deselectAll(self) -> None: ...
    def selectObject(self, nodePath: NodePath, fLEPane: bool = ...) -> None: ...
    def selectObjectCB(self, obj: Obj, fLEPane: bool) -> None: ...
    def updateObjectPropertyUI(self, obj: Obj) -> None: ...
    def onEnterObjectPropUI(self, event) -> None: ...
    def onLeaveObjectPropUI(self, event) -> None: ...
    def spawnUpdateObjectUITask(self) -> None: ...
    def updateObjectUITask(self, state): ...
    def updateObjectTransform(self, event) -> None: ...
    def setObjectTransform(self, uid: str, xformMat: Mat4Like) -> None: ...
    def updateObjectColor(self, r: float, g: float, b: float, a: float, np: NodePath | None = None) -> None: ...
    def updateObjectModel(self, model, obj: Obj, fSelectObject: bool = True) -> None: ...
    def updateObjectAnim(self, anim, obj: Obj, fSelectObject: bool = True) -> None: ...
    def updateObjectModelFromUI(self, event, obj: Obj) -> None: ...
    def updateObjectAnimFromUI(self, event, obj: Obj) -> None: ...
    def updateObjectProperty(self, event, obj: Obj, propName: str) -> None: ...
    def updateObjectPropValue(self, obj: Obj, propName, val, fSelectObject: bool = False, fUndo: bool = True) -> None: ...
    def updateCurve(self, val: SupportsInt, obj: Obj) -> None: ...
    def updateObjectProperties(self, nodePath: NodePath, propValues: Iterable[str]) -> None: ...
    def traverse(self, parent, parentId=None) -> None: ...
    def getSaveData(self) -> list: ...
    def getPreSaveData(self) -> None: ...
    def getPostSaveData(self) -> None: ...
    def duplicateObject(self, nodePath: NodePath, parent=None) -> NodePath: ...
    def duplicateChild(self, nodePath: NodePath, parent) -> None: ...
    def duplicateSelected(self) -> None: ...
    def makeSelectedLive(self) -> None: ...
    def replaceObjectWithTypeName(self, obj: Obj, typeName: str) -> None: ...
    def flatten(self, newobjModel, model, objDef, uid) -> None: ...
    def findActors(self, parent) -> None: ...
    def findNodes(self, parent) -> None: ...
