from typing import ClassVar

from direct._typing import Incomplete
from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject

from .DoCollectionManager import DoCollectionManager

class InterestWatcher(DirectObject):
    notify: ClassVar[Notifier]
    closingParent2zones: dict[Incomplete, set[Incomplete]]
    def __init__(
        self,
        interestMgr,
        name: str,
        doneEvent: str | None = ...,
        recurse: bool = ...,
        start: bool = ...,
        mustCollect: bool = ...,
        doCollectionMgr: DoCollectionManager | None = ...,
    ) -> None: ...
    def startCollect(self, mustCollect: bool = ...) -> None: ...
    def stopCollect(self) -> None: ...
    def destroy(self) -> None: ...
    def getName(self) -> str: ...
    def getDoneEvent(self) -> str: ...
