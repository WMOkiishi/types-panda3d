from panda3d.physics import BaseForce
from .ForceGroup import ForceGroup

class GlobalForceGroup(ForceGroup):
    def removeForce(self, force: BaseForce) -> None: ...
