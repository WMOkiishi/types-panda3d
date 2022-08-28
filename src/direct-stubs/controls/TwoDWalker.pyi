from .GravityWalker import GravityWalker

class TwoDWalker(GravityWalker):
    def __init__(
        self,
        gravity: float = -32.1740,
        standableGround: float = 0.707,
        hardLandingForce: float = 16.0,
    ) -> None: ...
    def jumpPressed(self) -> None: ...
