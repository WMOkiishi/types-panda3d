from _typeshed import Incomplete
from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from direct.distributed.DoInterestManager import DoInterestManager
from direct.showbase.DirectObject import DirectObject

from .DoCollectionManager import DoCollectionManager

class InterestWatcher(DirectObject):
    notify: ClassVar[Notifier]
    closingParent2zones: dict[Incomplete, set[Incomplete]]
    def __init__(
        self,
        interestMgr: DoInterestManager,
        name: str,
        doneEvent: str | None = None,
        recurse: bool = True,
        start: bool = True,
        mustCollect: bool = False,
        doCollectionMgr: DoCollectionManager | None = None,
    ) -> None: ...
    def startCollect(self, mustCollect: bool = False) -> None: ...
    def stopCollect(self) -> None: ...
    def destroy(self) -> None: ...
    def getName(self) -> str: ...
    def getDoneEvent(self) -> str: ...
