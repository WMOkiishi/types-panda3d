from typing_extensions import Final, Literal

from panda3d.core import BitMask_uint32_t_32, LPoint3f, LVector3f, NodePath

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

DIRECT_FLASH_DURATION: Final[float]
MANIPULATION_MOVE_DELAY: Final[float]
Q_EPSILON: Final[float]

DIRECT_NO_MOD: Final[Literal[0b000]]
DIRECT_SHIFT_MOD: Final[Literal[0b001]]
DIRECT_CONTROL_MOD: Final[Literal[0b010]]
DIRECT_ALT_MOD: Final[Literal[0b100]]

SKIP_NONE: Final[Literal[0b00000]]
SKIP_HIDDEN: Final[Literal[0b00001]]
SKIP_BACKFACE: Final[Literal[0b00010]]
SKIP_CAMERA: Final[Literal[0b00100]]
SKIP_UNPICKABLE: Final[Literal[0b01000]]
SKIP_WIDGET: Final[Literal[0b10000]]
SKIP_ALL: Final[Literal[0b11111]]

EDIT_TYPE_UNMOVABLE: Final[Literal[0b001]]
EDIT_TYPE_UNSCALABLE: Final[Literal[0b010]]
EDIT_TYPE_UNROTATABLE: Final[Literal[0b100]]
EDIT_TYPE_UNEDITABLE: Final[Literal[0b111]]

LE_TOP_CAM_MASK: Final[BitMask_uint32_t_32]
LE_FRONT_CAM_MASK: Final[BitMask_uint32_t_32]
LE_LEFT_CAM_MASK: Final[BitMask_uint32_t_32]
LE_PERSP_CAM_MASK: Final[BitMask_uint32_t_32]
LE_CAM_MASKS: Final[dict[Literal['persp', 'left', 'front', 'top'], BitMask_uint32_t_32]]

def LE_showInAllCam(nodePath: NodePath) -> None: ...
def LE_showInOneCam(nodePath: NodePath, thisCamName: str) -> None: ...
