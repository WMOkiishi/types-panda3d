from panda3d.core import NodePath, PandaNode
from panda3d.physics import ActorNode, LinearVectorForce, PhysicsManager

class RotationTest(NodePath[PandaNode]):
    actorNode: ActorNode
    phys: PhysicsManager
    gravity: LinearVectorForce
    spin: LinearVectorForce
    momentumForce: LinearVectorForce
    avatarNodePath: NodePath
    def __init__(self) -> None: ...
    def setup(self) -> None: ...
