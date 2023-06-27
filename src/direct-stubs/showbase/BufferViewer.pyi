__all__ = ['BufferViewer']

from collections.abc import MutableMapping
from typing import ClassVar, Literal
from typing_extensions import TypeAlias, TypeGuard

from direct._typing import Unused
from direct.directnotify.Notifier import Notifier
from panda3d.core import CardMaker, GeomNode, GraphicsEngine, GraphicsOutput, NodePath, PythonTask, Texture, WindowProperties

_Layout: TypeAlias = Literal['vline', 'hline', 'vgrid', 'hgrid', 'cycle']
_Position: TypeAlias = Literal['llcorner', 'lrcorner', 'ulcorner', 'urcorner']
_Texture: TypeAlias = Texture | GraphicsOutput | Literal['all']

class BufferViewer:
    notify: ClassVar[Notifier]
    enabled: bool
    sizex: float
    sizey: float
    position: _Position
    layout: _Layout
    include: _Texture | list[_Texture]
    exclude: _Texture | list[_Texture]
    cullbin: str
    cullsort: int
    win: GraphicsOutput | WindowProperties
    engine: GraphicsEngine
    renderParent: NodePath
    cards: list[NodePath]
    cardindex: int
    cardmaker: CardMaker
    task: PythonTask | Literal[0]
    dirty: bool
    def __init__(self, win: GraphicsOutput | WindowProperties, parent: NodePath) -> None: ...
    def refreshReadout(self) -> None: ...
    def isValidTextureSet(self, x: object) -> TypeGuard[_Texture | list[_Texture]]: ...
    def isEnabled(self) -> bool: ...
    def enable(self, x: bool) -> None: ...
    def toggleEnable(self) -> None: ...
    def setCardSize(self, x: float, y: float) -> None: ...
    def setPosition(self, pos: _Position) -> None: ...
    def setLayout(self, lay: _Layout) -> None: ...
    def selectCard(self, i: int) -> None: ...
    def advanceCard(self) -> None: ...
    def setInclude(self, x: _Texture | list[_Texture]) -> None: ...
    def setExclude(self, x: _Texture | list[_Texture]) -> None: ...
    def setSort(self, bin: str, sort: int) -> None: ...
    def setRenderParent(self, renderParent: NodePath) -> None: ...
    def analyzeTextureSet(
        self, x: _Texture | GraphicsEngine | list[_Texture | GraphicsEngine], set: MutableMapping[Texture, int]
    ) -> None: ...
    def makeFrame(self, sizex: float, sizey: float) -> NodePath[GeomNode]: ...
    def maintainReadout(self, task: Unused) -> Literal[0, 1]: ...
