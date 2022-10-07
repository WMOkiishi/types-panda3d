__all__ = ['install']

from collections.abc import Callable
from types import TracebackType
from typing import Any

from direct.directnotify.Notifier import Notifier

notify: Notifier
reentry: int
sReentry: int
oldExcepthook: Callable[[type[BaseException], BaseException, TracebackType | None], Any] | None
wantStackDumpLog: bool
wantStackDumpUpload: bool
variableDumpReasons: list
dumpOnExceptionInit: bool

def install(log: bool, upload: bool) -> None: ...
