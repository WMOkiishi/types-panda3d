from collections.abc import Sequence
from typing import Any, ClassVar, Final, Literal

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d.core import PythonTask

from .ClientRepository import ClientRepository

ASYNC_REQUEST_DEFAULT_TIMEOUT_IN_SECONDS: Final = 8.0
ASYNC_REQUEST_INFINITE_RETRIES: Final = -1
ASYNC_REQUEST_DEFAULT_NUM_RETRIES: Final = 0

class AsyncRequest(DirectObject):
    notify: ClassVar[Notifier]
    deletingMessage: str
    air: ClientRepository
    replyToChannelId: int | None
    timeoutTask: PythonTask | None
    neededObjects: dict[str | int, Any | None]
    def __init__(
        self, air: ClientRepository, replyToChannelId: int | None = None, timeoutTime: float = 8.0, numRetries: int = 0
    ) -> None: ...
    def delete(self) -> None: ...
    def askForObjectField(
        self, dclassName: str, fieldName: str, doId: int, key: str | None = None, context: int | None = None
    ) -> None: ...
    def askForObjectFields(
        self, dclassName: str, fieldNames: str, doId: int, key: str | None = None, context: int | None = None
    ) -> None: ...
    def askForObjectFieldsByString(
        self,
        dbId: int,
        dclassName: str,
        objString: str,
        fieldNames: Sequence[str],
        key: Sequence[str] | None = None,
        context: int | None = None,
    ) -> None: ...
    def askForObject(self, doId: int, context: int | None = None) -> None: ...
    def createObject(self, name: str, className: str, databaseId=None, values=None, context: int | None = None) -> None: ...
    def createObjectId(self, name: str, className: str, values=None, context: int | None = None) -> None: ...
    def finish(self) -> None: ...
    def timeout(self, task: PythonTask) -> Literal[1]: ...

def cleanupAsyncRequests() -> None: ...
