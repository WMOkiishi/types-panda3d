__all__ = ['install']

from ..directnotify.Notifier import Notifier

notify: Notifier
reentry: int
sReentry: int
oldExcepthook = ...
wantStackDumpLog: bool
wantStackDumpUpload: bool
variableDumpReasons: list
dumpOnExceptionInit: bool
def install(log: bool, upload: bool) -> None: ...
