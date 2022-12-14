from _typeshed import StrOrBytesPath

from direct.distributed.DistributedObject import DistributedObject

class DistributedLargeBlobSender(DistributedObject):
    complete: bool
    doneEvent: str | None
    mode: int
    useDisk: bool
    targetAvId: int
    blob: str
    def setMode(self, mode: int) -> None: ...
    def setTargetAvId(self, avId: int) -> None: ...
    def setChunk(self, chunk: str) -> None: ...
    def setFilename(self, filename: StrOrBytesPath) -> None: ...
    def isComplete(self) -> bool: ...
    def setDoneEvent(self, event: str | None) -> None: ...
    def privOnBlobComplete(self) -> None: ...
    def getBlob(self) -> str: ...
    def sendAck(self) -> None: ...
