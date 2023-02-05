__all__ = ['DirectGuiBase', 'DirectGuiWidget']

from _typeshed import Self
from collections.abc import Callable, Iterable, Mapping
from typing import Any, ClassVar, TypeVar, overload
from typing_extensions import Final, Literal, ParamSpec, TypeAlias

from direct._typing import Unused
from direct.showbase.DirectObject import DirectObject
from panda3d.core import LPoint3f, MouseWatcherParameter, NodePath, PGFrameStyle, PGItem, PStatCollector

_T = TypeVar('_T')
_P = ParamSpec('_P')

_Args: TypeAlias = tuple[Any, ...] | list[Any] | set[Any]
_PGFrameStyle_Type: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]

guiObjectCollector: Final[PStatCollector]

class DirectGuiBase(DirectObject):
    guiId: str
    postInitialiseFuncList: list[Callable[[], object]]
    fInit: bool
    def __init__(self) -> None: ...
    def defineoptions(
        self,
        keywords: Mapping[str, Any],
        optionDefs: Iterable[tuple[str, Any, Callable[[], object] | None]],
        dynamicGroups: Iterable[str] = ...,
    ) -> None: ...
    def addoptions(
        self, optionDefs: Iterable[tuple[str, Any, Callable[[], object] | None]], optionkeywords: Mapping[str, Any]
    ) -> None: ...
    def initialiseoptions(self, myClass: type[DirectGuiBase]) -> None: ...
    def postInitialiseFunc(self) -> None: ...
    def isinitoption(self, option: str) -> bool: ...
    def options(self) -> list[tuple[str, Any, bool]]: ...
    @overload
    def configure(self, option: str) -> tuple[str, Any, Any]: ...  # type: ignore[misc]
    @overload
    def configure(self, option: None = None) -> dict[str, tuple[str, Any, Any]]: ...  # type: ignore[misc]
    @overload
    def configure(self, option: str | None = None, **kw: Any) -> None: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, option: str) -> Any: ...
    cget = __getitem__
    @overload
    def createcomponent(
        self,
        componentName: str,
        componentAliases: Iterable[tuple[str, str]],
        componentGroup: str,
        widgetClass: Callable[_P, _T],
        *widgetArgs: _P.args,
        **kw: _P.kwargs,
    ) -> _T: ...
    @overload
    def createcomponent(
        self,
        componentName: str,
        componentAliases: Iterable[tuple[str, str]],
        componentGroup: str,
        widgetClass: None,
        *widgetArgs: object,
        **kw: object,
    ) -> None: ...
    def component(self, name: str) -> Any: ...
    def components(self) -> list[str]: ...
    def hascomponent(self, component: str) -> bool: ...
    def destroycomponent(self, name: str) -> None: ...
    def destroy(self) -> None: ...
    def bind(self, event: str, command: Callable[..., Any], extraArgs: _Args = ...) -> None: ...
    def unbind(self, event: str) -> None: ...

def toggleGuiGridSnap() -> None: ...
def setGuiGridSpacing(spacing: float) -> None: ...

class DirectGuiWidget(DirectGuiBase, NodePath[PGItem]):
    snapToGrid: ClassVar[bool]
    gridSpacing: ClassVar[float]
    guiEdit: ClassVar[bool]
    inactiveInitState: ClassVar[Literal['normal', 'disabled']]
    guiDict: ClassVar[dict[str, DirectGuiWidget]]
    guiItem: PGItem
    stateNodePath: list[NodePath[PGItem]]
    frameStyle: list[PGFrameStyle]
    ll: LPoint3f
    ur: LPoint3f
    bounds: tuple[float, float, float, float]
    def __init__(self, parent: NodePath | None = None, **kw: Any) -> None: ...
    def frameInitialiseFunc(self) -> None: ...
    def enableEdit(self) -> None: ...
    def disableEdit(self) -> None: ...
    def editStart(self, event: MouseWatcherParameter) -> None: ...
    def guiScaleTask(self, state: Any) -> Literal[1]: ...
    def guiDragTask(self, state: Any) -> Literal[1]: ...
    def editStop(self, event: Unused) -> None: ...
    def setState(self) -> None: ...  # type: ignore[override]
    def resetFrameSize(self) -> None: ...
    def setFrameSize(self, fClearFrame: bool = ...) -> None: ...
    def getBounds(self, state: int = 0) -> tuple[float, float, float, float]: ...  # type: ignore[override]
    def getWidth(self) -> float: ...
    def getHeight(self) -> float: ...
    def getCenter(self) -> tuple[float, float]: ...
    def getFrameType(self, state: int = 0) -> _PGFrameStyle_Type: ...
    def updateFrameStyle(self) -> None: ...
    def setRelief(self, fSetStyle: bool = ...) -> None: ...
    def setFrameColor(self) -> None: ...
    def setFrameTexture(self) -> None: ...
    def setFrameVisibleScale(self) -> None: ...
    def setBorderWidth(self) -> None: ...
    def setBorderUvWidth(self) -> None: ...
    def printConfig(self, indent: int = 0) -> None: ...
    def copyOptions(self: Self, other: Self) -> None: ...
    def taskName(self, idString: str) -> str: ...
    def uniqueName(self, idString: str) -> str: ...
    def setProp(self, propString: str, value: Any) -> None: ...
