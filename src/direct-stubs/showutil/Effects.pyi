from collections.abc import Sequence
from typing_extensions import Literal, TypeAlias

from panda3d.core import NodePath
from ..interval import MetaInterval

_BounceType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]

SX_BOUNCE: Literal[0]
SY_BOUNCE: Literal[1]
SZ_BOUNCE: Literal[2]
TX_BOUNCE: Literal[3]
TY_BOUNCE: Literal[4]
TZ_BOUNCE: Literal[5]
H_BOUNCE: Literal[6]
P_BOUNCE: Literal[7]
R_BOUNCE: Literal[8]

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
