__all__ = ['NotifyPanel']

from tkinter import IntVar, Radiobutton, Toplevel
from typing import Any

from direct.directnotify.DirectNotify import DirectNotify
from direct.directnotify.Notifier import Notifier

Pmw: Any

class NotifyPanel:
    activeCategory: Notifier | None
    categoryList: Pmw.ScrolledListBox
    severity: IntVar
    fatalSeverity: Radiobutton
    errorSeverity: Radiobutton
    warningSeverity: Radiobutton
    infoSeverity: Radiobutton
    debugSeverity: Radiobutton
    spamSeverity: Radiobutton
    def __init__(self, directNotify: DirectNotify, tl: Toplevel | None = None) -> None: ...
    def getPandaCategories(self): ...
    def getPandaCategoriesAsList(self): ...
    def setActivePandaCategory(self, event=None) -> None: ...
    def setActiveSeverity(self) -> None: ...
