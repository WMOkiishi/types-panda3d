from collections.abc import Sequence
from typing import ClassVar
from typing_extensions import Final, Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import PythonTask
from .ClientRepository import ClientRepository

ASYNC_REQUEST_DEFAULT_TIMEOUT_IN_SECONDS: Final[float]
ASYNC_REQUEST_INFINITE_RETRIES: Final[Literal[-1]]
ASYNC_REQUEST_DEFAULT_NUM_RETRIES: Final[Literal[0]]

class AsyncRequest(DirectObject):
    notify: ClassVar[Notifier]
    deletingMessage: str
    air: ClientRepository
    replyToChannelId: int | None
    timeoutTask: PythonTask | None
    neededObjects: dict
    def __init__(
        self, air: ClientRepository, replyToChannelId: int | None = None, timeoutTime: float = ..., numRetries: int = ...
    ) -> None: ...
    def delete(self) -> None: ...
    def askForObjectField(self, dclassName: str, fieldName: str, doId: int, key=None, context: int | None = None) -> None: ...
    def askForObjectFields(self, dclassName: str, fieldNames: str, doId: int, key=None, context: int | None = None) -> None: ...
    def askForObjectFieldsByString(
        self, dbId: int, dclassName: str, objString: str, fieldNames: Sequence[str], key=None, context: int | None = None
    ) -> None: ...
    def askForObject(self, doId: int, context: int | None = None) -> None: ...
    def createObject(self, name: str, className: str, databaseId=None, values=None, context: int | None = None) -> None: ...
    def createObjectId(self, name: str, className: str, values=None, context: int | None = None) -> None: ...
    def finish(self) -> None: ...
    def timeout(self, task: PythonTask) -> Literal[1]: ...

def cleanupAsyncRequests() -> None: ...
