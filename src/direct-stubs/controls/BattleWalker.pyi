from .GravityWalker import GravityWalker

BattleStrafe: bool

def ToggleStrafe() -> None: ...
def SetStrafe(status: bool) -> None: ...

class BattleWalker(GravityWalker):
    advanceSpeed: float
    def __init__(self) -> None: ...
    def getSpeeds(self) -> tuple[float, float, float, float]: ...  # type: ignore[override]
