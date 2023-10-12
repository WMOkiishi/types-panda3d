import wx.siplib as sip  # type: ignore[import-untyped]

from .LevelEditorUIBase import LevelEditorUIBase

class LevelEditorUI(LevelEditorUIBase, metaclass=sip.wrapper): ...
