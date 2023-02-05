__all__: list[str] = []

from collections.abc import Callable
from typing import Any
from typing_extensions import Final, Literal, TypeAlias, TypedDict

from panda3d.core import TextFont

_PGFrameStyle_Type: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]

defaultFont: TextFont | None
defaultFontFunc: Callable[[], TextFont]
defaultClickSound: Any | None
defaultRolloverSound: Any | None
defaultDialogGeom: Any | None
defaultDialogRelief: _PGFrameStyle_Type | None
drawOrder: int
panel: Any | None

INITOPT: Final[list[Literal['initopt']]]

LMB: Final = 0
MMB: Final = 1
RMB: Final = 2

NORMAL: Final = 'normal'
DISABLED: Final = 'disabled'

FLAT: Final = 1
RAISED: Final = 2
SUNKEN: Final = 3
GROOVE: Final = 4
RIDGE: Final = 5
TEXTUREBORDER: Final = 6

class _FrameStyleDict(TypedDict):
    flat: Literal[1]
    raised: Literal[2]
    sunken: Literal[3]
    groove: Literal[4]
    ridge: Literal[5]
    texture_border: Literal[6]

FrameStyleDict: Final[_FrameStyleDict]

HORIZONTAL: Final = 'horizontal'
VERTICAL: Final = 'vertical'
VERTICAL_INVERTED: Final = 'vertical_inverted'

DIALOG_NO: Final = 0
DIALOG_OK: Final = 1
DIALOG_YES: Final = 1
DIALOG_RETRY: Final = 1
DIALOG_CANCEL: Final = -1

DESTROY: Final = 'destroy-'
PRINT: Final = 'print-'
ENTER: Final[str]
EXIT: Final[str]
WITHIN: Final[str]
WITHOUT: Final[str]
B1CLICK: Final[str]
B2CLICK: Final[str]
B3CLICK: Final[str]
B1PRESS: Final[str]
B2PRESS: Final[str]
B3PRESS: Final[str]
B1RELEASE: Final[str]
B2RELEASE: Final[str]
B3RELEASE: Final[str]
OVERFLOW: Final[str]
ACCEPT: Final[str]
ACCEPTFAILED: Final[str]
TYPE: Final[str]
ERASE: Final[str]
CURSORMOVE: Final[str]
ADJUST: Final[str]

IMAGE_SORT_INDEX: Final = 10
GEOM_SORT_INDEX: Final = 20
TEXT_SORT_INDEX: Final = 30
FADE_SORT_INDEX: Final = 1000
NO_FADE_SORT_INDEX: Final = 2000
BACKGROUND_SORT_INDEX: Final = -100
MIDGROUND_SORT_INDEX: Final = 0
FOREGROUND_SORT_INDEX: Final = 100

BUTTON_READY_STATE: Final = 0
BUTTON_DEPRESSED_STATE: Final = 1
BUTTON_ROLLOVER_STATE: Final = 2
BUTTON_INACTIVE_STATE: Final = 3

def get_default_rollover_sound() -> Any | None: ...
def set_default_rollover_sound(newSound: Any) -> None: ...
def get_default_click_sound() -> Any | None: ...
def set_default_click_sound(newSound: Any) -> None: ...
def get_default_font() -> TextFont: ...
def set_default_font(newFont: TextFont | None) -> None: ...
def setDefaultFontFunc(newFontFunc: Callable[[], TextFont]) -> None: ...
def get_default_dialog_geom() -> Any | None: ...
def get_default_dialog_relief() -> _PGFrameStyle_Type | None: ...
def set_default_dialog_geom(newDialogGeom: Any, relief: _PGFrameStyle_Type | None = None) -> None: ...
def get_default_draw_order() -> int: ...
def set_default_draw_order(newDrawOrder: int) -> None: ...
def get_default_panel() -> Any | None: ...
def set_default_panel(newPanel: Any) -> None: ...

getDefaultRolloverSound = get_default_rollover_sound
setDefaultRolloverSound = set_default_rollover_sound
getDefaultClickSound = get_default_click_sound
setDefaultClickSound = set_default_click_sound
getDefaultFont = get_default_font
setDefaultFont = set_default_font
getDefaultDialogGeom = get_default_dialog_geom
getDefaultDialogRelief = get_default_dialog_relief
setDefaultDialogGeom = set_default_dialog_geom
getDefaultDrawOrder = get_default_draw_order
setDefaultDrawOrder = set_default_draw_order
getDefaultPanel = get_default_panel
setDefaultPanel = set_default_panel
