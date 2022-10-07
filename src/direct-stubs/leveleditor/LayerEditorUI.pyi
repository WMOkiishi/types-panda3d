import wx  # type: ignore[import]

class LayerEditorUI(wx.Panel):
    editor = ...
    editorTxt: str
    saveData: list[str]
    layersDataDict: dict[int, list]
    layersDataDictNextKey: int
    systemLayerKeys: list
    llist: wx.ListCtrl
    opAdd: str
    opDelete: str
    opRename: str
    opAddObj: str
    opRemoveObj: str
    opShowObj: str
    opHideObj: str
    menuItemsGen: list[str]
    menuItemsObj: list[str]
    popupmenu: wx.Menu
    def __init__(self, parent, editor) -> None: ...
    def menuAppendGenItems(self) -> None: ...
    def menuAppendObjItems(self, hitItem) -> None: ...
    def onShowPopup(self, event) -> None: ...
    def onPopupItemSelected(self, event) -> None: ...
    def reset(self) -> None: ...
    def findLabel(self, text) -> bool: ...
    def addLayerData(self, idx: int, objUID) -> None: ...
    def addLayerEntry(self, name, idx: int) -> None: ...
    def addLayer(self) -> None: ...
    def deleteLayer(self) -> None: ...
    def renameLayer(self) -> None: ...
    def removeObjData(self, objUID) -> None: ...
    def removeObj(self) -> None: ...
    def addObj(self) -> None: ...
    def onShowMembers(self, event) -> None: ...
    def HideObj(self, hide: bool) -> None: ...
    def traverse(self) -> None: ...
    def getSaveData(self) -> list[str]: ...
