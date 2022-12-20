__all__ = ['Audio3DManager']

from _typeshed import StrOrBytesPath
from typing_extensions import Literal

from direct._typing import Unused
from panda3d.core import AudioManager, AudioSound, LVecBase3f, NodePath

class Audio3DManager:
    audio_manager: AudioManager
    listener_target: NodePath | None
    root: NodePath
    sound_dict: dict[NodePath, list[AudioSound]]
    vel_dict: dict[AudioSound, LVecBase3f | None]
    listener_vel: LVecBase3f | None
    def __init__(
        self,
        audio_manager: AudioManager,
        listener_target: NodePath | None = ...,
        root: NodePath | None = ...,
        taskPriority: int = ...,
    ) -> None: ...
    def load_sfx(self, name: StrOrBytesPath) -> AudioSound: ...
    def set_distance_factor(self, factor: float) -> None: ...
    def get_distance_factor(self) -> float: ...
    def set_doppler_factor(self, factor: float) -> None: ...
    def get_doppler_factor(self) -> float: ...
    def set_drop_off_factor(self, factor: float) -> None: ...
    def get_drop_off_factor(self) -> float: ...
    def set_sound_min_distance(self, sound: AudioSound, dist: float) -> None: ...
    def get_sound_min_distance(self, sound: AudioSound) -> float: ...
    def set_sound_max_distance(self, sound: AudioSound, dist: float) -> None: ...
    def get_sound_max_distance(self, sound: AudioSound) -> float: ...
    # `velocity` is purposely not `Vec3OrTuple`
    def set_sound_velocity(self, sound: AudioSound, velocity: LVecBase3f | tuple[float, float, float]) -> None: ...
    def set_sound_velocity_auto(self, sound: AudioSound) -> None: ...
    def get_sound_velocity(self, sound: AudioSound) -> LVecBase3f: ...
    # `velocity` is purposely not `Vec3OrTuple`
    def set_listener_velocity(self, velocity: LVecBase3f | tuple[float, float, float]) -> None: ...
    def set_listener_velocity_auto(self) -> None: ...
    def get_listener_velocity(self) -> LVecBase3f: ...
    def attach_sound_to_object(self, sound: AudioSound, object: NodePath) -> Literal[1]: ...
    def detach_sound(self, sound: AudioSound) -> bool: ...
    def get_sounds_on_object(self, object: NodePath) -> list[AudioSound]: ...
    def attach_listener(self, object: NodePath) -> Literal[1]: ...
    def detach_listener(self) -> Literal[1]: ...
    def update(self, task: Unused = ...) -> Literal[1]: ...
    def disable(self) -> None: ...
    loadSfx = load_sfx
    setDistanceFactor = set_distance_factor
    getDistanceFactor = get_distance_factor
    setDopplerFactor = set_doppler_factor
    getDopplerFactor = get_doppler_factor
    setDropOffFactor = set_drop_off_factor
    getDropOffFactor = get_drop_off_factor
    setSoundMinDistance = set_sound_min_distance
    getSoundMinDistance = get_sound_min_distance
    setSoundMaxDistance = set_sound_max_distance
    getSoundMaxDistance = get_sound_max_distance
    setSoundVelocity = set_sound_velocity
    setSoundVelocityAuto = set_sound_velocity_auto
    getSoundVelocity = get_sound_velocity
    setListenerVelocity = set_listener_velocity
    setListenerVelocityAuto = set_listener_velocity_auto
    getListenerVelocity = get_listener_velocity
    attachSoundToObject = attach_sound_to_object
    detachSound = detach_sound
    getSoundsOnObject = get_sounds_on_object
    attachListener = attach_listener
    detachListener = detach_listener
