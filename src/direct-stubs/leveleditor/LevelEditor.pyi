from .AnimMgr import AnimMgr
from .LevelEditorBase import LevelEditorBase
from .LevelEditorUI import LevelEditorUI
from .ObjectHandler import ObjectHandler
from .ObjectMgr import ObjectMgr
from .ObjectPalette import ObjectPalette
from .ProtoPalette import ProtoPalette

class LevelEditor(LevelEditorBase):
    objectMgr: ObjectMgr
    animMgr: AnimMgr
    objectPalette: ObjectPalette
    objectHandler: ObjectHandler
    protoPalette: ProtoPalette
    ui: LevelEditorUI
