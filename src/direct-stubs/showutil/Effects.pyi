from collections.abc import Sequence
from typing_extensions import Final, Literal, TypeAlias

from panda3d.core import NodePath
from ..interval import MetaInterval

_BounceType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]

SX_BOUNCE: Final[Literal[0]]
SY_BOUNCE: Final[Literal[1]]
SZ_BOUNCE: Final[Literal[2]]
TX_BOUNCE: Final[Literal[3]]
TY_BOUNCE: Final[Literal[4]]
TZ_BOUNCE: Final[Literal[5]]
H_BOUNCE: Final[Literal[6]]
P_BOUNCE: Final[Literal[7]]
R_BOUNCE: Final[Literal[8]]

def createScaleXBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createScaleYBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createScaleZBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createXBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createYBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createZBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createHBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createPBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createRBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
) -> MetaInterval.Sequence: ...
def createBounce(
    nodeObj: NodePath,
    numBounces: int,
    startValues: Sequence[float],
    totalTime: float,
    amplitude: float,
    bounceType: _BounceType = 2,
) -> MetaInterval.Sequence: ...
