from typing import Final, Literal

from panda3d.core import BitMask32, LPoint3f, LVector3f, NodePath

UNPICKABLE: Final[list[str]]

X_AXIS: Final[LVector3f]
Y_AXIS: Final[LVector3f]
Z_AXIS: Final[LVector3f]
NEG_X_AXIS: Final[LVector3f]
NEG_Y_AXIS: Final[LVector3f]
NEG_Z_AXIS: Final[LVector3f]
ZERO_VEC: Final[LVector3f]
ORIGIN: Final[LVector3f]
UNIT_VEC: Final[LVector3f]
ZERO_POINT: Final[LPoint3f]

DIRECT_FLASH_DURATION: Final = 1.5
MANIPULATION_MOVE_DELAY: Final = 0.65
Q_EPSILON: Final = 1e-10

DIRECT_NO_MOD: Final = 0b000
DIRECT_SHIFT_MOD: Final = 0b001
DIRECT_CONTROL_MOD: Final = 0b010
DIRECT_ALT_MOD: Final = 0b100

SKIP_NONE: Final = 0b00000
SKIP_HIDDEN: Final = 0b00001
SKIP_BACKFACE: Final = 0b00010
SKIP_CAMERA: Final = 0b00100
SKIP_UNPICKABLE: Final = 0b01000
SKIP_WIDGET: Final = 0b10000
SKIP_ALL: Final = 0b11111

EDIT_TYPE_UNMOVABLE: Final = 0b001
EDIT_TYPE_UNSCALABLE: Final = 0b010
EDIT_TYPE_UNROTATABLE: Final = 0b100
EDIT_TYPE_UNEDITABLE: Final = 0b111

LE_TOP_CAM_MASK: Final[BitMask32]
LE_FRONT_CAM_MASK: Final[BitMask32]
LE_LEFT_CAM_MASK: Final[BitMask32]
LE_PERSP_CAM_MASK: Final[BitMask32]
LE_CAM_MASKS: Final[dict[Literal['persp', 'left', 'front', 'top'], BitMask32]]

def LE_showInAllCam(nodePath: NodePath) -> None: ...
def LE_showInOneCam(nodePath: NodePath, thisCamName: str) -> None: ...
