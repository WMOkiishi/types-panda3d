from collections.abc import Sequence
from typing import ClassVar
from typing_extensions import Literal, TypeAlias

from direct.showbase.DirectObject import DirectObject
from panda3d.core import (
    BitArray,
    BitMask_uint16_t_16,
    BitMask_uint32_t_32,
    BitMask_uint64_t_64,
    DisplayRegion,
    GraphicsOutput,
    GraphicsPipe,
    GraphicsStateGuardian,
    MouseWatcher,
    MouseWatcherRegion,
    NodePath,
    OrthographicLens,
    PythonTask,
    TextNode,
    Texture,
)

_BitMask: TypeAlias = BitArray | BitMask_uint16_t_16 | BitMask_uint32_t_32 | BitMask_uint64_t_64
_Unused: TypeAlias = object

class TexMemWatcher(DirectObject):
    NextIndex: ClassVar[int]
    StatusHeight: ClassVar[int]
    name: str
    cleanedUp: bool
    top: float
    quantize: int
    maxHeight: int
    totalSize: int
    placedSize: int
    placedQSize: int
    gsg: GraphicsStateGuardian
    winSize: tuple[int, int]
    pipe: GraphicsPipe
    win: GraphicsOutput
    background: None
    nextTexRecordKey: int
    rollover: TexRecord | None
    isolate: NodePath | None
    isolated: TexRecord | None
    needsRepack: bool
    task: PythonTask
    render2d: NodePath
    lens: OrthographicLens
    aspect2d: NodePath
    statusBackground: NodePath
    status: NodePath
    statusText: TextNode
    statusTextNP: NodePath[TextNode]
    sizeText: TextNode
    canvasRoot: NodePath
    canvas: NodePath
    canvasDR: DisplayRegion
    canvasLens: OrthographicLens
    mw: MouseWatcher
    checkTex: Texture
    canvasBackground: NodePath
    limit: int | None
    lruLimit: bool
    dynamicLimit: bool
    texRecordsByTex: dict[Texture, TexRecord]
    texRecordsByKey: dict[int, TexRecord]
    bitmasks: list[BitArray]
    w: int
    h: int
    area: int
    def __init__(self, gsg: GraphicsOutput | GraphicsStateGuardian | None = None, limit: int | None = None) -> None: ...
    def setupGui(self) -> None: ...
    def setupCanvas(self) -> None: ...
    def makeCanvasBackground(self) -> None: ...
    def setLimit(self, limit: int | None = None) -> None: ...
    def cleanup(self) -> None: ...
    def graphicsMemoryLimitChanged(self) -> None: ...
    def windowEvent(self, win: GraphicsOutput) -> None: ...
    def enterRegion(self, region: DisplayRegion, buttonName: _Unused) -> None: ...
    def leaveRegion(self, region: DisplayRegion, buttonName: _Unused) -> None: ...
    def mouseClick(self) -> None: ...
    def setRollover(self, tr: TexRecord, pi: _Unused) -> None: ...
    def isolateTexture(self, tr: TexRecord) -> None: ...
    def reconfigureWindow(self) -> None: ...
    def updateTextures(self, task: PythonTask) -> Literal[2]: ...
    def repack(self) -> None: ...
    def formatSize(self, size: float) -> str: ...
    def unplaceTexture(self, tr: TexRecord) -> None: ...
    def placeTexture(self, tr: TexRecord) -> None: ...
    def findHole(self, area: int, w: int, h: int) -> tuple[float, TexPlacement] | None: ...
    def findHolePieces(self, area: int) -> list[TexPlacement] | None: ...
    def findLargestHole(self) -> tuple[int, TexPlacement]: ...
    def findAvailableHoles(self, area: int, w: int | None = None, h: int | None = None) -> list[tuple[int, TexPlacement]]: ...
    def findOverflowHole(self, area: int, w: int, h: int) -> TexPlacement: ...
    def findEmptyRuns(self, bm: _BitMask) -> set[tuple[int, int]]: ...

class TexRecord:
    key: int
    tex: Texture
    active: bool
    root: NodePath | None
    regions: list[MouseWatcherRegion]
    placements: list[TexPlacement]
    overflowed: bool
    size: int
    tw: float
    th: float
    w: int
    h: int
    area: int
    matte: NodePath
    backing: NodePath
    card: NodePath
    frame: NodePath
    def __init__(self, key: int, tex: Texture, size: int, active: bool) -> None: ...
    def setSize(self, size: int) -> None: ...
    def computePlacementSize(self, tmw: TexMemWatcher) -> None: ...
    def setActive(self, flag: bool) -> None: ...
    def clearCard(self, tmw: TexMemWatcher) -> None: ...
    def makeCard(self, tmw: TexMemWatcher) -> None: ...

class TexPlacement:
    p: tuple[int, int, int, int]
    area: int
    rotated: bool
    overflowed: bool
    def __init__(self, l: int, r: int, b: int, t: int) -> None: ...
    def intersects(self, other: TexPlacement) -> bool: ...
    def setBitmasks(self, bitmasks: Sequence[BitArray]) -> None: ...
    def clearBitmasks(self, bitmasks: Sequence[BitArray]) -> None: ...
    def hasOverlap(self, bitmasks: Sequence[BitArray]) -> bool: ...
