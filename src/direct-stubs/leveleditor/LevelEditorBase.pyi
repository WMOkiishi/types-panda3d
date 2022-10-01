from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable
from typing_extensions import Literal

from direct._typing import Unused
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from panda3d.core import BitMask_uint32_t_32, NodePath
from .ActionMgr import ActionMgr
from .CurveEditor import CurveEditor
from .FileMgr import FileMgr

class LevelEditorBase(DirectObject):
    currentFile: StrOrBytesPath | None
    fNeedToSave: bool
    actionEvents: list[tuple[str, Callable[..., None]]]
    curveEditor: CurveEditor
    fileMgr: FileMgr
    actionMgr: ActionMgr
    fMoveCamera: bool
    NPParent: NodePath
    settingsFile: StrOrBytesPath | None
    BASE_MODE: BitMask_uint32_t_32
    CREATE_CURVE_MODE: BitMask_uint32_t_32
    EDIT_CURVE_MODE: BitMask_uint32_t_32
    ANIM_MODE: BitMask_uint32_t_32
    GRAPH_EDITOR: bool
    mode: BitMask_uint32_t_32
    preMode = ...
    statusReadout: OnscreenText
    statusLines: list
    def __init__(self) -> None: ...
    def initialize(self) -> None: ...
    def setTitleWithFilename(self, filename: str | bytes = ...) -> None: ...
    def removeNodePathHook(self, nodePath: NodePath | None) -> None: ...
    def toggleWidget(self) -> None: ...
    def handleMouse1(self, modifiers: int) -> None: ...
    def handleMouse1Up(self) -> None: ...
    def handleMouse2(self, modifiers: int) -> None: ...
    def handleMouse2Up(self) -> None: ...
    def handleMouse3(self, modifiers: int) -> None: ...
    def handleMouse3Up(self) -> None: ...
    def handleDelete(self) -> None: ...
    def cleanUpManipulating(self, selectedNPs: Iterable[NodePath]) -> None: ...
    def select(
        self,
        nodePath: NodePath,
        fMultiSelect: bool = False,
        fSelectTag: bool = True,
        fResetAncestry: bool = True,
        fLEPane: bool = False,
        fUndo: int = True,
    ) -> None: ...
    def selectedNodePathHook(
        self,
        nodePath: NodePath,
        fMultiSelect: bool = False,
        fSelectTag: bool = True,
        fLEPane: bool = False,
    ) -> None: ...
    def deselectAll(self, np: Unused = None) -> None: ...
    def deselectAllCB(self, dnp: Unused = None) -> None: ...
    def reset(self) -> None: ...
    def resetOrthoCam(self, view) -> None: ...
    def save(self) -> None: ...
    def saveAs(self, fileName: StrOrBytesPath) -> None: ...
    def load(self, fileName: StrOrBytesPath) -> None: ...
    def saveSettings(self) -> None: ...
    def loadSettings(self) -> None: ...
    def convertMaya(self, modelname, callBack, obj=None, isAnim: bool = False) -> None: ...
    def convertFromMaya(self, modelname, callBack) -> None: ...
    def exportToMaya(self, mayaFileName: str) -> None: ...
    def exportToMayaCB(self, mayaFileName: str, exportRootNP) -> None: ...
    def updateStatusReadout(self, status, color=None) -> None: ...
    def updateStatusReadoutTimeouts(self, task=None) -> Literal[2]: ...
    def propMeetsReq(self, typeName: Unused, parentNP): ...
