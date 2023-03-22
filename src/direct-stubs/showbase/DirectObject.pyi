__all__ = ['DirectObject']

from collections.abc import Callable, Sequence
from typing import Any, overload
from typing_extensions import TypeAlias

from panda3d._typing import TaskCoroutine
from panda3d.core import AsyncTask, PythonTask

# Ideally, this should just be Sequence[Any], but the code here and in Messenger
# means that it has to be one of these.
_Args: TypeAlias = tuple[Any, ...] | list[Any]

class DirectObject:
    def __init__(self) -> None: ...
    def accept(self, event: str, method: Callable[..., Any], extraArgs: _Args = []) -> None: ...
    def accept_once(self, event: str, method: Callable[..., Any], extraArgs: _Args = []) -> None: ...
    def ignore(self, event: str) -> None: ...
    def ignore_all(self) -> None: ...
    def is_accepting(self, event: str) -> bool: ...
    def get_all_accepting(self) -> list[tuple[str, int]]: ...
    def is_ignoring(self, event: str) -> bool: ...
    @overload
    def add_task(
        self,
        funcOrTask: PythonTask | Callable[..., int | TaskCoroutine[int | None] | None] | TaskCoroutine[Any],
        name: str | None = None,
        sort: int | None = None,
        extraArgs: Sequence[Any] | None = None,
        priority: int | None = None,
        appendTask: bool = False,
        uponDeath: Callable[..., object] | None = None,
        taskChain: str | None = None,
        *,
        delay: float | None = None,
    ) -> PythonTask: ...
    @overload
    def add_task(
        self,
        funcOrTask: AsyncTask,
        name: str | None = None,
        sort: int | None = None,
        extraArgs: None = None,
        priority: int | None = None,
        appendTask: bool = False,
        uponDeath: Callable[..., object] | None = None,
        taskChain: str | None = None,
        *,
        delay: float | None = None,
    ) -> AsyncTask: ...
    @overload
    def do_method_later(
        self,
        delayTime: float,
        funcOrTask: PythonTask | Callable[..., int | TaskCoroutine[int | None] | None] | TaskCoroutine[Any],
        name: str | None,
        extraArgs: Sequence[Any] | None = None,
        sort: int | None = None,
        priority: int | None = None,
        taskChain: str | None = None,
        uponDeath: Callable[..., object] | None = None,
        appendTask: bool = False,
    ) -> PythonTask: ...
    @overload
    def do_method_later(
        self,
        delayTime: float,
        funcOrTask: AsyncTask,
        name: str | None,
        extraArgs: None = None,
        sort: int | None = None,
        priority: int | None = None,
        taskChain: str | None = None,
        uponDeath: Callable[..., object] | None = None,
        appendTask: bool = False,
    ) -> AsyncTask: ...
    def remove_task(self, taskOrName: AsyncTask | str) -> None: ...
    def remove_all_tasks(self) -> None: ...
    def detect_leaks(self) -> None: ...
    acceptOnce = accept_once
    ignoreAll = ignore_all
    isAccepting = is_accepting
    getAllAccepting = get_all_accepting
    isIgnoring = is_ignoring
    addTask = add_task
    doMethodLater = do_method_later
    removeTask = remove_task
    removeAllTasks = remove_all_tasks
    detectLeaks = detect_leaks
