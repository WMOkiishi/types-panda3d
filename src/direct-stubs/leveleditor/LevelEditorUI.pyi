import wx.siplib as sip  # type: ignore

from .LevelEditorUIBase import LevelEditorUIBase

class LevelEditorUI(LevelEditorUIBase, metaclass=sip.wrapper): ...
