from .DistributedObject import DistributedObject

class SampleObject(DistributedObject):
    def setColor(self, red: int = ..., green: int = ..., blue: int = ...) -> None: ...
    def getColor(self) -> tuple[int, int, int]: ...
