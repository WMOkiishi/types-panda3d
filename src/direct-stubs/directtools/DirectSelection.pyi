from collections.abc import Callable, Sequence
from typing_extensions import Final, Literal

from direct.showbase.DirectObject import DirectObject
from panda3d._typing import Vec3f, Vec4f
from panda3d.core import (
    BitMask32,
    BoundingSphere,
    CollisionEntry,
    CollisionHandlerQueue,
    CollisionNode,
    CollisionSolid,
    CollisionTraverser,
    LMatrix4f,
    LPoint3f,
    LVector3f,
    NodePath,
    TransformState,
)
from .DirectGeometry import LineNodePath

COA_ORIGIN: Final[Literal[0]]
COA_CENTER: Final[Literal[1]]

class DirectNodePath(NodePath):
    bbox: DirectBoundingBox
    mCoa2Dnp: LMatrix4f
    tDnp2Widget: TransformState
    def __init__(self, nodePath: NodePath, bboxColor: Vec4f | None = ...) -> None: ...
    def highlight(self, fRecompute: bool = ...) -> None: ...
    def dehighlight(self) -> None: ...
    def getCenter(self) -> LPoint3f: ...
    def getRadius(self) -> LVector3f: ...
    def getMin(self) -> LPoint3f: ...
    def getMax(self) -> LPoint3f: ...

class SelectedNodePaths(DirectObject):
    selectedDict: dict[int, DirectNodePath]
    selectedList: list[DirectNodePath]
    deselectedDict: dict[int, DirectNodePath]
    last: DirectNodePath | None
    tagList: list[str]
    def __init__(self) -> None: ...
    def addTag(self, tag: str) -> None: ...
    def removeTag(self, tag: str) -> None: ...
    def reset(self) -> None: ...
    def select(
        self, nodePath: DirectNodePath | None, fMultiSelect: bool = ..., fSelectTag: bool = ...
    ) -> DirectNodePath | None: ...
    def deselect(self, nodePath: DirectNodePath) -> DirectNodePath | None: ...
    def getSelectedAsList(self) -> list[DirectNodePath]: ...
    def __getitem__(self, index: int) -> DirectNodePath: ...
    def getSelectedDict(self, id: int) -> DirectNodePath | None: ...
    def getDeselectedAsList(self) -> list[DirectNodePath]: ...
    def getDeselectedDict(self, id: int) -> DirectNodePath | None: ...
    def forEachSelectedNodePathDo(self, func: Callable[[DirectNodePath], object]) -> None: ...
    def forEachDeselectedNodePathDo(self, func: Callable[[DirectNodePath], object]) -> None: ...
    def getWrtAll(self) -> None: ...
    def getWrt(self, nodePath: DirectNodePath) -> None: ...
    def moveWrtWidgetAll(self) -> None: ...
    def moveWrtWidget(self, nodePath: NodePath) -> None: ...
    def deselectAll(self) -> None: ...
    def highlightAll(self) -> None: ...
    def dehighlightAll(self) -> None: ...
    def removeSelected(self) -> None: ...
    def removeAll(self) -> None: ...
    def toggleVisSelected(self) -> None: ...
    def toggleVisAll(self) -> None: ...
    def isolateSelected(self) -> None: ...
    def getDirectNodePath(self, nodePath: NodePath) -> DirectNodePath | None: ...
    def getNumSelected(self) -> int: ...

class DirectBoundingBox:
    nodePath: NodePath
    lines: LineNodePath
    min: LPoint3f
    max: LPoint3f
    center: LPoint3f
    radius: LVector3f
    bounds: BoundingSphere
    def __init__(self, nodePath: NodePath, bboxColor: Vec4f | None = ...) -> None: ...
    def recompute(self) -> None: ...
    def computeTightBounds(self) -> None: ...
    def computeBounds(self) -> None: ...
    def createBBoxLines(self, bboxColor: Vec4f | None = ...) -> LineNodePath: ...
    def setBoxColorScale(self, r: float, g: float, b: float, a: float) -> None: ...
    def updateBBoxLines(self) -> None: ...
    def getBounds(self) -> BoundingSphere: ...
    def show(self) -> None: ...
    def hide(self) -> None: ...
    def getCenter(self) -> LPoint3f: ...
    def getRadius(self) -> LVector3f: ...
    def getMin(self) -> LPoint3f: ...
    def getMax(self) -> LPoint3f: ...
    def vecAsString(self, vec: Sequence[float]) -> str: ...

class SelectionQueue(CollisionHandlerQueue):
    index: int
    entry: CollisionEntry | None
    skipFlags: int
    collisionNodePath: NodePath[CollisionNode]
    collisionNode: CollisionNode
    ct: CollisionTraverser
    unpickable: list[str]
    collider: CollisionSolid
    def __init__(self, parentNP: NodePath | None = ...) -> None: ...
    def setParentNP(self, parentNP: NodePath) -> None: ...
    def addCollider(self, collider: CollisionSolid) -> None: ...
    def collideWithBitMask(self, bitMask: BitMask32) -> None: ...
    def collideWithGeom(self) -> None: ...
    def collideWithWidget(self) -> None: ...
    def addUnpickable(self, item: str) -> None: ...
    def removeUnpickable(self, item: str) -> None: ...
    def setCurrentIndex(self, index: int) -> None: ...
    def setCurrentEntry(self, entry: CollisionEntry) -> None: ...
    def getCurrentEntry(self) -> CollisionEntry | None: ...
    def isEntryBackfacing(self, entry: CollisionEntry) -> bool: ...
    def findNextCollisionEntry(self, skipFlags: int = ...) -> CollisionEntry: ...
    def findCollisionEntry(self, skipFlags: int = ..., startIndex: int = ...) -> CollisionEntry: ...

class SelectionRay(SelectionQueue):
    def pick(self, targetNodePath: NodePath, xy: Sequence[float] | None = ...) -> None: ...
    def pickBitMask(
        self, bitMask: BitMask32 = ..., targetNodePath: NodePath | None = ..., skipFlags: int = ...
    ) -> CollisionEntry: ...
    def pickGeom(
        self, targetNodePath: NodePath | None = ..., skipFlags: int = ..., xy: Sequence[float] | None = ...
    ) -> CollisionEntry: ...
    def pickWidget(self, targetNodePath: NodePath | None = ..., skipFlags: int = ...) -> CollisionEntry: ...
    def pick3D(self, targetNodePath: NodePath, origin: Vec3f, dir: Vec3f) -> None: ...
    def pickGeom3D(
        self, targetNodePath: NodePath | None = ..., origin: Vec3f = ..., dir: Vec3f = ..., skipFlags: int = ...
    ) -> CollisionEntry: ...
    def pickBitMask3D(
        self,
        bitMask: BitMask32 = ...,
        targetNodePath: NodePath | None = ...,
        origin: Vec3f = ...,
        dir: Vec3f = ...,
        skipFlags: int = ...,
    ) -> CollisionEntry: ...

class SelectionSegment(SelectionQueue):
    colliders: list[CollisionSolid]
    numColliders: int
    def __init__(self, parentNP: NodePath | None = ..., numSegments: int = ...) -> None: ...
    def pickGeom(
        self, targetNodePath: NodePath | None = ..., endPointList: Sequence[tuple[Vec3f, Vec3f]] = ..., skipFlags: int = ...
    ) -> CollisionEntry: ...
    def pickBitMask(
        self,
        bitMask: BitMask32 = ...,
        targetNodePath: NodePath | None = ...,
        endPointList: Sequence[tuple[Vec3f, Vec3f]] = ...,
        skipFlags: int = ...,
    ) -> CollisionEntry: ...

class SelectionSphere(SelectionQueue):
    colliders: list[CollisionSolid]
    numColliders: int
    def __init__(self, parentNP: NodePath | None = ..., numSpheres: int = ...) -> None: ...
    def setCenter(self, i: int, center: Vec3f) -> None: ...
    def setRadius(self, i: int, radius: Vec3f) -> None: ...
    def setCenterRadius(self, i: int, center: Vec3f, radius: Vec3f) -> None: ...
    def pick(self, targetNodePath: NodePath, skipFlags: int) -> CollisionEntry: ...
    def pickGeom(self, targetNodePath: NodePath | None = ..., skipFlags: int = ...) -> CollisionEntry: ...
    def pickBitMask(
        self, bitMask: BitMask32 = ..., targetNodePath: NodePath | None = ..., skipFlags: int = ...
    ) -> CollisionEntry: ...
