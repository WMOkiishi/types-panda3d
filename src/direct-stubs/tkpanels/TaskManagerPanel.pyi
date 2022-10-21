from tkinter import Button, Checkbutton, IntVar, Misc, Toplevel
from typing import Any
from typing_extensions import Literal

import Pmw  # type: ignore[import]
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task, TaskManager
from direct.tkwidgets.AppShell import AppShell

class TaskManagerPanel(AppShell):
    taskMgr: TaskManager
    taskMgrWidget: Any
    def __init__(self, taskMgr: TaskManager, parent: Toplevel | None = ..., **kw) -> None: ...

class TaskManagerWidget(DirectObject):
    parent: Misc | None
    taskMgr: TaskManager
    currentTask: Task | None
    taskListBox: Pmw.ScrolledListBox
    removeButton: Button
    removeMatchingButton: Button
    taskMgrVerbose: IntVar
    update: Button
    dynamicUpdate: Checkbutton
    def __init__(self, parent: Misc | None, taskMgr: TaskManager) -> None: ...
    def popupMenu(self, event) -> Literal['break']: ...
    def setCurrentTask(self, event=...) -> None: ...
    def updateTaskListBox(self) -> None: ...
    def toggleTaskMgrVerbose(self) -> None: ...
    def spawnTaskHook(self, task) -> None: ...
    def removeTaskHook(self, task) -> None: ...
    def removeCurrentTask(self) -> None: ...
    def removeMatchingTasks(self) -> None: ...
    def onDestroy(self) -> None: ...
