from .DistributedObjectAI import DistributedObjectAI

class TimeManagerAI(DistributedObjectAI):
    def requestServerTime(self, context: int) -> None: ...
