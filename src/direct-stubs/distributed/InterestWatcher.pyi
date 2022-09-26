from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject

class InterestWatcher(DirectObject):
    notify: ClassVar[Notifier]
    closingParent2zones: dict
    def __init__(
        self,
        interestMgr,
        name: str,
        doneEvent: str | None = None,
        recurse: bool = True,
        start: bool = True,
        mustCollect: bool = False,
        doCollectionMgr=None,
    ) -> None: ...
    def startCollect(self, mustCollect: bool = False) -> None: ...
    def stopCollect(self) -> None: ...
    def destroy(self) -> None: ...
    def getName(self) -> str: ...
    def getDoneEvent(self) -> str: ...
