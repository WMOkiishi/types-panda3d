from collections.abc import Sequence
from enum import Enum
from typing import Any, ClassVar, Literal, TypeAlias, overload
from panda3d.core import (
    ButtonEventList,
    ButtonHandle,
    DataNode,
    LMatrix4f,
    LOrientationf,
    LPoint3f,
    PointerData,
    PointerEventList,
    TypeHandle,
    TypedReferenceCount,
    ostream,
)

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class TrackerData:
    """Stores the kinds of data that a tracker might output."""
    DtoolClassDict: ClassVar[dict[str, Any]]
    time: float
    pos: LPoint3f
    orient: LOrientationf
    dt: float

class InputDevice(TypedReferenceCount):
    """This is a structure representing a single input device.  Input devices may
    have zero or more buttons, pointers, or axes associated with them, and
    optionally a motion tracker.
    
    These devices are brought under a common interface because there is such a
    large range of devices out there that may support any number of these types
    of axes, we couldn't even begin to cover them with type-specific
    subclasses.
    
    Use the various has_() and get_num_() methods to determine information about
    the device capabilities. For instance, has_keyboard() will give an
    indication that you can receive keystroke events from this device, and
    get_num_buttons() will tell you that the device may send button events.
    
    There is the DeviceType enumeration, however, which will (if known) contain
    identification of the general category of devices this fits in, such as
    keyboard, mouse, gamepad, or flight stick.
    
    @since 1.10.0
    """
    class DeviceClass(Enum):
        unknown: int
        virtual_device: int
        keyboard: int
        mouse: int
        touch: int
        gamepad: int
        flight_stick: int
        steering_wheel: int
        dance_pad: int
        hmd: int
        spatial_mouse: int
        digitizer: int
    class Feature(Enum):
        pointer: int
        keyboard: int
        tracker: int
        vibration: int
        battery: int
    class Axis(Enum):
        none: int
        x: int
        y: int
        z: int
        yaw: int
        pitch: int
        roll: int
        left_x: int
        left_y: int
        left_trigger: int
        right_x: int
        right_y: int
        right_trigger: int
        throttle: int
        rudder: int
        wheel: int
        accelerator: int
        brake: int
        pressure: int
    class ButtonState:
        DtoolClassDict: ClassVar[dict[str, Any]]
        @property
        def known(self) -> bool: ...
        @property
        def pressed(self) -> bool: ...
        @property
        def handle(self) -> ButtonHandle: ...
        def __init__(self, __param0: InputDevice.ButtonState) -> None: ...
        def __bool__(self) -> bool: ...
    class AxisState:
        DtoolClassDict: ClassVar[dict[str, Any]]
        axis: InputDevice.Axis
        value: float
        known: bool
        def __init__(self, __param0: InputDevice.AxisState) -> None: ...
        def __bool__(self) -> bool: ...
    class BatteryData:
        DtoolClassDict: ClassVar[dict[str, Any]]
        level: int
        max_level: int
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, __param0: InputDevice.BatteryData) -> None: ...
    DtoolClassDict: ClassVar[dict[str, Any]]
    S_unknown: ClassVar[Literal[0]]
    S_up: ClassVar[Literal[1]]
    S_down: ClassVar[Literal[2]]
    @property
    def name(self) -> str: ...
    @property
    def manufacturer(self) -> str: ...
    @property
    def serial_number(self) -> str: ...
    @property
    def vendor_id(self) -> int: ...
    @property
    def product_id(self) -> int: ...
    @property
    def connected(self) -> bool: ...
    @property
    def device_class(self) -> InputDevice.DeviceClass: ...
    @property
    def tracker(self) -> TrackerData: ...
    @property
    def battery(self) -> InputDevice.BatteryData: ...
    @property
    def buttons(self) -> Sequence[InputDevice.ButtonState]: ...
    @property
    def axes(self) -> Sequence[InputDevice.AxisState]: ...
    @property
    def _pointer_data(self) -> PointerData: ...
    @property
    def _battery_data(self) -> InputDevice.BatteryData: ...
    @property
    def _tracker_data(self) -> TrackerData: ...
    def has_feature(self, feature: InputDevice.Feature) -> bool: ...
    def map_button(self, index: int, handle: ButtonHandle) -> None: ...
    def map_axis(self, index: int, axis: InputDevice.Axis) -> None: ...
    def find_button(self, handle: ButtonHandle) -> InputDevice.ButtonState: ...
    def find_axis(self, axis: InputDevice.Axis) -> InputDevice.AxisState: ...
    def set_vibration(self, strong: float, weak: float) -> None: ...
    def enable_pointer_events(self) -> None: ...
    def disable_pointer_events(self) -> None: ...
    def poll(self) -> None: ...
    def has_button_event(self) -> bool: ...
    def get_button_events(self) -> ButtonEventList: ...
    def has_pointer_event(self) -> bool: ...
    def get_pointer_events(self) -> PointerEventList: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    hasFeature = has_feature
    mapButton = map_button
    mapAxis = map_axis
    findButton = find_button
    findAxis = find_axis
    setVibration = set_vibration
    enablePointerEvents = enable_pointer_events
    disablePointerEvents = disable_pointer_events
    hasButtonEvent = has_button_event
    getButtonEvents = get_button_events
    hasPointerEvent = has_pointer_event
    getPointerEvents = get_pointer_events
    getClassType = get_class_type
    SUnknown = S_unknown
    SUp = S_up
    SDown = S_down

class ClientBase(TypedReferenceCount):
    """An abstract base class for a family of client device interfaces--including
    trackers, buttons, dials, and other analog inputs.
    
    This provides a common interface to connect to such devices and extract
    their data; it is used by TrackerNode etc.  to put these devices in the
    data graph.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def fork_asynchronous_thread(self, poll_time: float) -> bool: ...
    def is_forked(self) -> bool: ...
    def poll(self) -> bool: ...
    def get_last_poll_time(self) -> float: ...
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_coordinate_system(self) -> _CoordinateSystem: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    forkAsynchronousThread = fork_asynchronous_thread
    isForked = is_forked
    getLastPollTime = get_last_poll_time
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system
    getClassType = get_class_type

class AnalogNode(DataNode):
    """This is the primary interface to analog controls like sliders and joysticks
    associated with a ClientBase.  This creates a node that connects to the
    named analog device, if it exists, and provides hooks to the user to read
    the state of any of the sequentially numbered controls associated with that
    device.
    
    Each control can return a value ranging from -1 to 1, reflecting the
    current position of the control within its total range of motion.
    
    The user may choose up to two analog controls to place on the data graph as
    the two channels of an xy datagram, similarly to the way a mouse places its
    position data.  In this way, an AnalogNode may be used in place of a mouse.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: AnalogNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_num_controls(self) -> int: ...
    def get_control_state(self, index: int) -> float: ...
    def is_control_known(self, index: int) -> bool: ...
    def set_output(self, channel: int, index: int, flip: bool) -> None: ...
    def clear_output(self, channel: int) -> None: ...
    def get_output(self, channel: int) -> int: ...
    def is_output_flipped(self, channel: int) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getNumControls = get_num_controls
    getControlState = get_control_state
    isControlKnown = is_control_known
    setOutput = set_output
    clearOutput = clear_output
    getOutput = get_output
    isOutputFlipped = is_output_flipped
    getClassType = get_class_type

class ButtonNode(DataNode):
    """This is the primary interface to on/off button devices associated with a
    ClientBase.  This creates a node that connects to the named button device,
    if it exists, and provides hooks to the user to read the state of any of
    the sequentially numbered buttons associated with that device.
    
    It also can associate an arbitrary ButtonHandle with each button; when
    buttons are associated with ButtonHandles, this node will put appropriate
    up and down events on the data graph for each button state change.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: ButtonNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_num_buttons(self) -> int: ...
    def set_button_map(self, index: int, button: ButtonHandle) -> None: ...
    def get_button_map(self, index: int) -> ButtonHandle: ...
    def get_button_state(self, index: int) -> bool: ...
    def is_button_known(self, index: int) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getNumButtons = get_num_buttons
    setButtonMap = set_button_map
    getButtonMap = get_button_map
    getButtonState = get_button_state
    isButtonKnown = is_button_known
    getClassType = get_class_type

class DialNode(DataNode):
    """This is the primary interface to infinite dial type devices associated with
    a ClientBase.  This creates a node that connects to the named dial device,
    if it exists, and provides hooks to the user to read the state of any of
    the sequentially numbered dial controls associated with that device.
    
    A dial is a rotating device that does not have stops--it can keep rotating
    any number of times.  Therefore it does not have a specific position at any
    given time, unlike an AnalogDevice.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: DialNode) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_num_dials(self) -> int: ...
    def read_dial(self, index: int) -> float: ...
    def is_dial_known(self, index: int) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getNumDials = get_num_dials
    readDial = read_dial
    isDialKnown = is_dial_known
    getClassType = get_class_type

class InputDeviceSet:
    """Manages a list of InputDevice objects, as returned by various
    InputDeviceManager methods.  This is implemented like a set, meaning the
    same device cannot occur more than once.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: InputDeviceSet) -> None: ...
    def __getitem__(self, index: int) -> InputDevice: ...
    def __len__(self) -> int: ...
    def assign(self, copy: InputDeviceSet) -> InputDeviceSet: ...
    def clear(self) -> None: ...
    def reserve(self, num: int) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...

class InputDeviceManager:
    """This class keeps track of all the devices on a system, and sends out events
    when a device has been hot-plugged.
    
    @since 1.10.0
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def get_devices(self) -> InputDeviceSet: ...
    @overload
    def get_devices(self, device_class: InputDevice.DeviceClass) -> InputDeviceSet: ...
    def add_device(self, device: InputDevice) -> None: ...
    def remove_device(self, device: InputDevice) -> None: ...
    def update(self) -> None: ...
    @staticmethod
    def get_global_ptr() -> InputDeviceManager: ...
    getDevices = get_devices
    addDevice = add_device
    removeDevice = remove_device
    getGlobalPtr = get_global_ptr

class InputDeviceNode(DataNode):
    """Reads the controller data sent from the InputDeviceManager, and transmits
    it down the data graph.
    
    This is intended to only be accessed from the app thread.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    device: InputDevice
    @overload
    def __init__(self, __param0: InputDeviceNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice, name: str) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class TrackerNode(DataNode):
    """This class reads the position and orientation information from a tracker
    device and makes it available as a transformation on the data graph.
    It is also the primary interface to a Tracker object associated with a
    ClientBase.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, __param0: TrackerNode) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def is_valid(self) -> bool: ...
    def get_pos(self) -> LPoint3f: ...
    def get_orient(self) -> LOrientationf: ...
    def get_transform(self) -> LMatrix4f: ...
    def get_time(self) -> float: ...
    def has_time(self) -> bool: ...
    def set_tracker_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_tracker_coordinate_system(self) -> _CoordinateSystem: ...
    def set_graph_coordinate_system(self, cs: _CoordinateSystem) -> None: ...
    def get_graph_coordinate_system(self) -> _CoordinateSystem: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    isValid = is_valid
    getPos = get_pos
    getOrient = get_orient
    getTransform = get_transform
    getTime = get_time
    hasTime = has_time
    setTrackerCoordinateSystem = set_tracker_coordinate_system
    getTrackerCoordinateSystem = get_tracker_coordinate_system
    setGraphCoordinateSystem = set_graph_coordinate_system
    getGraphCoordinateSystem = get_graph_coordinate_system
    getClassType = get_class_type

class VirtualMouse(DataNode):
    """Poses as a MouseAndKeyboard object in the datagraph, but accepts input from
    user calls, rather than reading the actual mouse and keyboard from an input
    device.  The user can write high-level code to put the mouse wherever
    he/she wants, and to insert keypresses on demand.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: VirtualMouse) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def set_mouse_pos(self, x: int, y: int) -> None: ...
    def set_window_size(self, width: int, height: int) -> None: ...
    def set_mouse_on(self, flag: bool) -> None: ...
    def press_button(self, button: ButtonHandle) -> None: ...
    def release_button(self, button: ButtonHandle) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    setMousePos = set_mouse_pos
    setWindowSize = set_window_size
    setMouseOn = set_mouse_on
    pressButton = press_button
    releaseButton = release_button
    getClassType = get_class_type
