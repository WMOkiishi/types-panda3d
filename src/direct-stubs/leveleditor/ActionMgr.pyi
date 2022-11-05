from collections.abc import Callable
from typing import Any, TypeVar

from direct._typing import Obj
from direct.showbase.PythonUtil import Functor
from panda3d.core import LMatrix4f
from .LevelEditor import LevelEditor

_T = TypeVar('_T')

class ActionMgr:
    undoList: list[ActionBase]
    redoList: list[ActionBase]
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def push(self, action: ActionBase) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ActionBase(Functor[_T]):
    function: Callable[..., _T]
    result: _T | None
    def redo(self) -> _T | None: ...
    def saveStatus(self) -> None: ...
    def postCall(self) -> None: ...
    def undo(self) -> None: ...

class ActionAddNewObj(ActionBase):
    editor: LevelEditor
    uid: str
    def __init__(self, editor: LevelEditor, *args: Any, **kargs: Any) -> None: ...

class ActionDeleteObj(ActionBase):
    editor: LevelEditor
    selectedUIDs: list
    hierarchy: dict
    objInfos: dict
    objTransforms: dict
    def __init__(self, editor: LevelEditor, *args: Any, **kargs: Any) -> None: ...

class ActionDeleteObjById(ActionBase):
    editor: LevelEditor
    uid: str
    hierarchy: dict
    objInfos: dict
    objTransforms: dict
    def __init__(self, editor: LevelEditor, uid: str) -> None: ...

class ActionChangeHierarchy(ActionBase):
    editor: LevelEditor
    oldGrandParentId = ...
    oldParentId = ...
    newParentId = ...
    childName: str
    def __init__(self, editor: LevelEditor, oldGrandParentId, oldParentId, newParentId, childName, *args, **kargs) -> None: ...

class ActionSelectObj(ActionBase):
    editor: LevelEditor
    selectedUIDs: list
    def __init__(self, editor: LevelEditor, *args: Any, **kargs: Any) -> None: ...

class ActionTransformObj(ActionBase):
    editor: LevelEditor
    uid: str
    origMat: LMatrix4f | None
    def __init__(self, editor: LevelEditor, *args, **kargs: Any) -> None: ...

class ActionDeselectAll(ActionBase):
    editor: LevelEditor
    selectedUIDs: list[str]
    def __init__(self, editor: LevelEditor, *args: Any, **kargs: Any) -> None: ...

class ActionUpdateObjectProp(ActionBase[_T]):
    editor: LevelEditor
    fSelectObject: bool
    obj: Obj
    propName: str
    newVal = ...
    oldVal = ...
    undoFunc: Callable[[], object]
    def __init__(
        self,
        editor: LevelEditor,
        fSelectObject: bool,
        obj: Obj,
        propName: str,
        val,
        oldVal,
        function: Callable[..., _T],
        undoFunc: Callable[[], object],
        *args: Any,
        **kargs: Any,
    ) -> None: ...
    def redo(self) -> _T: ...
