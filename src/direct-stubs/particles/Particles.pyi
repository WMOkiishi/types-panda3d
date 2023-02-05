from _typeshed import SupportsWrite
from typing import ClassVar

from direct.directnotify.Notifier import Notifier
from panda3d.core import NodePath
from panda3d.physics import ArcEmitter, BaseForce, ParticleSystem, PhysicalNode, PointParticleFactory, PointParticleRenderer

class Particles(ParticleSystem):
    notify: ClassVar[Notifier]
    id: ClassVar[int]
    name: str
    node: PhysicalNode
    nodePath: NodePath[PhysicalNode]
    factory: PointParticleFactory | None
    factoryType: str
    renderer: PointParticleRenderer | None
    rendererType: str
    emitter: ArcEmitter | None
    emitterType: str
    fEnabled: bool
    geomReference: str
    def __init__(self, name: str | None = None, poolSize: int = 1024) -> None: ...
    def cleanup(self) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def is_enabled(self) -> bool: ...
    def getNode(self) -> PhysicalNode: ...
    def set_factory(self, type: str) -> None: ...  # type: ignore[override]
    def set_renderer(self, type: str) -> None: ...  # type: ignore[override]
    def set_emitter(self, type: str) -> None: ...  # type: ignore[override]
    def add_force(self, force: BaseForce) -> None: ...
    def remove_force(self, force: BaseForce) -> None: ...
    def set_render_node_path(self, nodePath: NodePath) -> None: ...
    def getName(self) -> str: ...
    def get_factory(self) -> PointParticleFactory | None: ...  # type: ignore[override]
    def get_emitter(self) -> ArcEmitter | None: ...  # type: ignore[override]
    def get_renderer(self) -> PointParticleRenderer | None: ...  # type: ignore[override]
    def print_params(self, file: SupportsWrite[str] = ..., targ: str = 'self') -> None: ...
    def get_pool_size_ranges(self) -> dict[str, float]: ...
    def accelerate(self, time: float, stepCount: int = 1, stepTime: float = 0.0) -> None: ...
    isEnabled = is_enabled
    setFactory = set_factory  # type: ignore[assignment]
    setRenderer = set_renderer  # type: ignore[assignment]
    setEmitter = set_emitter  # type: ignore[assignment]
    addForce = add_force
    removeForce = remove_force
    setRenderNodePath = set_render_node_path
    getFactory = get_factory  # type: ignore[assignment]
    getEmitter = get_emitter  # type: ignore[assignment]
    getRenderer = get_renderer  # type: ignore[assignment]
    printParams = print_params
    getPoolSizeRanges = get_pool_size_ranges
