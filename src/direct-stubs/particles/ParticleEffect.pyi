from os import PathLike
from typing import ClassVar, overload
from typing_extensions import Literal, TypeAlias

from panda3d.core import ConfigVariableFilename, Filename, NodePath
from ..directnotify.Notifier import Notifier
from .ForceGroup import ForceGroup

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_OldBool: TypeAlias = Literal[0, 1]

class ParticleEffect(NodePath):
    notify: ClassVar[Notifier]
    pid: ClassVar[int]
    name: str
    fEnabled: bool | _OldBool
    particlesDict: dict
    forceGroupDict: dict[str, ForceGroup]
    renderParent = ...
    def __init__(self, name: str | None = None, particles = None) -> None: ...
    def cleanup(self) -> None: ...
    def getName(self) -> str: ...
    def reset(self) -> None: ...
    def start(self, parent: NodePath | None = None, renderParent = None) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def is_enabled(self) -> bool | _OldBool: ...
    def add_force_group(self, forceGroup: ForceGroup) -> None: ...
    def add_force(self, force) -> None: ...
    def remove_force_group(self, forceGroup) -> None: ...
    def remove_force(self, force) -> None: ...
    def remove_all_forces(self) -> None: ...
    def add_particles(self, particles) -> None: ...
    def remove_particles(self, particles) -> None: ...
    def remove_all_particles(self) -> None: ...
    def get_particles_list(self): ...
    def get_particles_named(self, name): ...
    def get_particles_dict(self): ...
    def get_force_group_list(self) -> list[ForceGroup]: ...
    @overload
    def get_force_group_named(self, name: str) -> ForceGroup | None: ...
    @overload
    def get_force_group_named(self, name: object) -> None: ...
    def get_force_group_dict(self) -> dict[str, ForceGroup]: ...
    def save_config(self, filename: _Filename) -> None: ...
    def load_config(self, filename: _Filename) -> None: ...
    def accelerate(self, time, stepCount: int = 1, stepTime: float = 0) -> None: ...
    def clear_to_initial(self) -> None: ...
    def soft_stop(self) -> None: ...
    def soft_start(self, firstBirthDelay = None) -> None: ...
    isEnabled = is_enabled
    addForceGroup = add_force_group
    addFroce = add_force
    removeForceGroup = remove_force_group
    removeForce = remove_force
    removeAllForces = remove_all_forces
    addParticles = add_particles
    removeParticles = remove_particles
    removeAllParticles = remove_all_particles
    getParticlesList = get_particles_list
    getParticlesNamed = get_particles_named
    getParticlesDict = get_particles_dict
    getForceGropNamed = get_force_group_named
    getForceGroupDict = get_force_group_dict
    saveConfig = save_config
    loadConfig = load_config
    clearToInitial = clear_to_initial
    softStop = soft_stop
    softStart = soft_start