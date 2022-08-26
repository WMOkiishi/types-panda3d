from collections.abc import Mapping
from typing import ClassVar

from panda3d.core import BitMask_uint32_t_32, CollisionNode, CollisionTraverser, NodePath
from ..directnotify.Notifier import Notifier
from .DirectObject import DirectObject
from .PhasedObject import PhasedObject

class DistancePhasedNode(PhasedObject, DirectObject, NodePath):
    notify: ClassVar[Notifier]
    phaseParamMap: Mapping[str, float]
    phaseParamList: list[tuple[str, float]]
    autoCleanup: bool
    enterPrefix: str
    exitPrefix: str
    phaseCollideMask: BitMask_uint32_t_32
    cTrav: CollisionTraverser
    fromCollideNode: CollisionNode | None
    def __init__(
        self,
        name: str,
        phaseParamMap: Mapping[str, float],
        autoCleanup: bool = True,
        enterPrefix: str = 'enter',
        exitPrefix: str = 'exit',
        phaseCollideMask: BitMask_uint32_t_32 = ...,
        fromCollideNode: CollisionNode | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...
    def __str__(self) -> str: ...
    def cleanup(self) -> None: ...
    def setPhaseCollideMask(self, mask: BitMask_uint32_t_32) -> None: ...
    def reset(self) -> None: ...
    def setPhase(self, aPhase: int | str) -> None: ...

class BufferedDistancePhaseNode(DistancePhasedNode):
    notify: ClassVar[Notifier]
    bufferParamMap: Mapping[str, tuple[float, int]]
    bufferParamList: list[tuple[str, tuple[float, int]]]
    def __init__(
        self,
        name: str,
        bufferParamMap: Mapping[str, tuple[float, int]],
        autoCleanup: bool = True,
        enterPrefix: str = 'enter',
        exitPrefix: str = 'exit',
        phaseCollideMask: BitMask_uint32_t_32 = ...,
        fromCollideNode: CollisionNode | None = None,
    ) -> None: ...
    def __str__(self) -> str: ...
    def setPhase(self, aPhase: int | str) -> None: ...
