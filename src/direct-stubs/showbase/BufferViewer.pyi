__all__ = ['BufferViewer']

from _typeshed import Unused
from collections.abc import MutableMapping
from typing import ClassVar, Literal
from typing_extensions import TypeAlias, TypeGuard

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
    def refresh_readout(self) -> None: ...
    def is_valid_texture_set(self, x: object) -> TypeGuard[_Texture | list[_Texture]]: ...
    def is_enabled(self) -> bool: ...
    def enable(self, x: bool) -> None: ...
    def toggle_enable(self) -> None: ...
    def set_card_size(self, x: float, y: float) -> None: ...
    def set_position(self, pos: _Position) -> None: ...
    def set_layout(self, lay: _Layout) -> None: ...
    def select_card(self, i: int) -> None: ...
    def advance_card(self) -> None: ...
    def set_include(self, x: _Texture | list[_Texture]) -> None: ...
    def set_exclude(self, x: _Texture | list[_Texture]) -> None: ...
    def set_sort(self, bin: str, sort: int) -> None: ...
    def set_render_parent(self, renderParent: NodePath) -> None: ...
    def analyze_texture_set(
        self, x: _Texture | GraphicsEngine | list[_Texture | GraphicsEngine], set: MutableMapping[Texture, int]
    ) -> None: ...
    def make_frame(self, sizex: float, sizey: float) -> NodePath[GeomNode]: ...
    def maintain_readout(self, task: Unused) -> Literal[0, 1]: ...
    refreshReadout = refresh_readout
    isValidTextureSet = is_valid_texture_set
    isEnabled = is_enabled
    toggleEnable = toggle_enable
    setCardSize = set_card_size
    setPosition = set_position
    setLayout = set_layout
    selectCard = select_card
    advanceCard = advance_card
    setInclude = set_include
    setExclude = set_exclude
    setSort = set_sort
    setRenderParent = set_render_parent
    analyzeTextureSet = analyze_texture_set
    makeFrame = make_frame
    maintainReadout = maintain_readout
