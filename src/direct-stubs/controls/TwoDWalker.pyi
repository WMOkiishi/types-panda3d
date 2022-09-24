from .GravityWalker import GravityWalker

class TwoDWalker(GravityWalker):
    def __init__(
        self,
        gravity: float = ...,
        standableGround: float = ...,
        hardLandingForce: float = ...,
    ) -> None: ...
    def jumpPressed(self) -> None: ...
