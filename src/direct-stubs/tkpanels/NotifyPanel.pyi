__all__ = ['NotifyPanel']

import tkinter

import Pmw  # type: ignore[import]
from direct._typing import Unused
from direct.directnotify.DirectNotify import DirectNotify
from direct.directnotify.Notifier import Notifier
from panda3d.core import NotifyCategory

class NotifyPanel:
    activeCategory: Notifier | None
    categoryList: Pmw.ScrolledListBox
    severity: tkinter.IntVar
    fatalSeverity: tkinter.Radiobutton
    errorSeverity: tkinter.Radiobutton
    warningSeverity: tkinter.Radiobutton
    infoSeverity: tkinter.Radiobutton
    debugSeverity: tkinter.Radiobutton
    spamSeverity: tkinter.Radiobutton
    def __init__(self, directNotify: DirectNotify, tl: tkinter.Toplevel | None = ...) -> None: ...
    def getPandaCategories(self) -> list[NotifyCategory | list[NotifyCategory]]: ...
    def getPandaCategoriesAsList(self) -> list[NotifyCategory]: ...
    def setActivePandaCategory(self, event: Unused = ...) -> None: ...
    def setActiveSeverity(self) -> None: ...
