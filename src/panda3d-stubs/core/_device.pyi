from collections.abc import Iterator, Sequence
from enum import Enum
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d.core._dgraph import DataNode
from panda3d.core._dtoolutil import ostream
from panda3d.core._event import ButtonEventList, PointerEventList
from panda3d.core._express import TypedReferenceCount
from panda3d.core._linmath import LMatrix4, LOrientation, LPoint3
from panda3d.core._putil import ButtonHandle, PointerData

_CoordinateSystem: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class TrackerData:
    """Stores the kinds of data that a tracker might output."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    time: float
    pos: LPoint3
    orient: LOrientation
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
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...

    class AxisState:
        DtoolClassDict: ClassVar[dict[str, Any]]
        axis: InputDevice.Axis
        value: float
        known: bool
        def __init__(self, __param0: InputDevice.AxisState) -> None: ...
        def __bool__(self) -> bool: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...

    class BatteryData:
        DtoolClassDict: ClassVar[dict[str, Any]]
        level: int
        """Ranges from 0 through max_level."""
        max_level: int
        """Maximum value of 'level' field."""
        def __init__(self, __param0: InputDevice.BatteryData = ...) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...

    S_unknown: Final = 0
    SUnknown: Final = 0
    S_up: Final = 1
    SUp: Final = 1
    S_down: Final = 2
    SDown: Final = 2
    @property
    def name(self) -> str:
        """The human-readable name of this input device."""
    @property
    def manufacturer(self) -> str:
        """The device's manufacturer, or the empty string if not known."""
    @property
    def serial_number(self) -> str:
        """The device's serial number, or the empty string if not known."""
    @property
    def vendor_id(self) -> int:
        """USB vendor ID of the device, or 0 if not known."""
    @property
    def product_id(self) -> int:
        """USB product ID of the device, or 0 if not known."""
    @property
    def connected(self) -> bool:
        """This is false if we know that the device is not currently connected.
        May report false positives if we can't know this with certainty.
        """
    @property
    def device_class(self) -> InputDevice.DeviceClass:
        """This contains an identification of the general type of device.  If
        this could not be determined, it is set to DC_unknown.
        """
    @property
    def tracker(self) -> TrackerData:
        """Getters for the various types of device data."""
    @property
    def battery(self) -> InputDevice.BatteryData: ...
    @property
    def buttons(self) -> Sequence[InputDevice.ButtonState]:
        """Make device buttons and axes iterable"""
    @property
    def axes(self) -> Sequence[InputDevice.AxisState]: ...
    @property
    def _pointer_data(self) -> PointerData: ...
    @property
    def _battery_data(self) -> InputDevice.BatteryData: ...
    @property
    def _tracker_data(self) -> TrackerData: ...
    def has_feature(self, feature: InputDevice.Feature) -> bool:
        """Returns true if the device supports the indicated feature."""
    def map_button(self, index: int, handle: ButtonHandle | str) -> None:
        """Associates the indicated ButtonHandle with the button of the indicated index
        number.  When the given button index changes state, a corresponding
        ButtonEvent will be generated with the given ButtonHandle.  Pass
        ButtonHandle::none() to turn off any association.

        It is not necessary to call this if you simply want to query the state of
        the various buttons by index number; this is only necessary in order to
        generate ButtonEvents when the buttons change state.
        """
    def map_axis(self, index: int, axis: InputDevice.Axis) -> None:
        """Associates the indicated Axis with the axis of the indicated index
        number.  Pass Axis::none to turn off any association.

        It is not necessary to call this if you simply want to query the state of
        the various axes by index number.
        """
    def find_button(self, handle: ButtonHandle | str) -> InputDevice.ButtonState:
        """Returns the first ButtonState found with the given axis, or throw an assert
        if the button handle was not found in the list.
        """
    def find_axis(self, axis: InputDevice.Axis) -> InputDevice.AxisState:
        """Returns the first AnalogAxis found with the given axis, or throw an assert
        if the axis was not found in the list.
        """
    def set_vibration(self, strong: float, weak: float) -> None:
        """Sets the strength of the vibration effect, if supported.  The values are
        clamped to 0-1 range. The first value axes the low-frequency rumble
        motor, whereas the second axes the high-frequency motor, if present.
        """
    def enable_pointer_events(self) -> None:
        """Enables the generation of mouse-movement events."""
    def disable_pointer_events(self) -> None:
        """Disables the generation of mouse-movement events."""
    def poll(self) -> None:
        """Polls the input device for new activity, to ensure it contains the latest
        events.  This will only have any effect for some types of input devices;
        others may be updated automatically, and this method will be a no-op.
        """
    def has_button_event(self) -> bool:
        """Returns true if this device has a pending button event (a mouse button or
        keyboard button down/up), false otherwise.  If this returns true, the
        particular event may be extracted via get_button_event().
        """
    def get_button_events(self) -> ButtonEventList:
        """Returns the list of recently-generated ButtonEvents.
        The list is also cleared.
        """
    def has_pointer_event(self) -> bool:
        """Returns true if this device has a pending pointer event (a mouse movement),
        or false otherwise.  If this returns true, the particular event may be
        extracted via get_pointer_event().
        """
    def get_pointer_events(self) -> PointerEventList:
        """Returns a PointerEventList containing all the recent pointer events.
        Clears the list.
        """
    def output(self, out: ostream) -> None:
        """Writes a one-line string describing the device."""
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

class ClientBase(TypedReferenceCount):
    """An abstract base class for a family of client device interfaces--including
    trackers, buttons, dials, and other analog inputs.

    This provides a common interface to connect to such devices and extract
    their data; it is used by TrackerNode etc.  to put these devices in the
    data graph.
    """

    def fork_asynchronous_thread(self, poll_time: float) -> bool:
        """Forks a separate thread to do all the polling of connected devices.  The
        forked thread will poll after every poll_time seconds has elapsed.  Returns
        true if the fork was successful, or false otherwise (for instance, because
        we were already forked, or because asynchronous threads are disabled).
        """
    def is_forked(self) -> bool:
        """Returns true if the ClientBase has been forked (and, therefore, poll() does
        not need to be called), false otherwise.
        """
    def poll(self) -> bool:
        """Initiates a poll of the client devices, if we are not forked and if we have
        not already polled this frame.  Returns true if the poll occurred, or false
        if it did not.
        """
    def get_last_poll_time(self) -> float:
        """Returns the time (according to the global ClockObject's get_real_time()
        method) of the last device poll.
        """
    def set_coordinate_system(self, cs: _CoordinateSystem) -> None:
        """Specifies the coordinate system that all devices associated with this
        client will operate in.  Normally, this is CS_default.
        """
    def get_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system that all devices associated with this client
        will operate in.  Normally, this is CS_default.
        """
    forkAsynchronousThread = fork_asynchronous_thread
    isForked = is_forked
    getLastPollTime = get_last_poll_time
    setCoordinateSystem = set_coordinate_system
    getCoordinateSystem = get_coordinate_system

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

    @overload
    def __init__(self, __param0: AnalogNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def is_valid(self) -> bool:
        """Returns true if the AnalogNode is valid and connected to a server, false
        otherwise.
        """
    def get_num_controls(self) -> int:
        """Returns the number of analog controls known to the AnalogNode.  This number
        may change as more controls are discovered.
        """
    def get_control_state(self, index: int) -> float:
        """Returns the current position of indicated analog control identified by its
        index number, or 0.0 if the control is unknown.  The normal range of a
        single control is -1.0 to 1.0.
        """
    def is_control_known(self, index: int) -> bool:
        """Returns true if the state of the indicated analog control is known, or
        false if we have never heard anything about this particular control.
        """
    def set_output(self, channel: int, index: int, flip: bool) -> None:
        """Causes a particular analog control to be placed in the data graph for the
        indicated channel.  Normally, a mouse uses channels 0 and 1 for the X and Y
        information, respectively; channels 0, 1, and 2 are available.  If flip is
        true, the analog control value will be reversed before outputting it.
        """
    def clear_output(self, channel: int) -> None:
        """Removes the output to the data graph associated with the indicated channel.
        See set_output().
        """
    def get_output(self, channel: int) -> int:
        """Returns the analog control index that is output to the data graph on the
        indicated channel, or -1 if no control is output on that channel.  See
        set_output().
        """
    def is_output_flipped(self, channel: int) -> bool:
        """Returns true if the analog control index that is output to the data graph
        on the indicated channel is flipped.  See set_output().
        """
    isValid = is_valid
    getNumControls = get_num_controls
    getControlState = get_control_state
    isControlKnown = is_control_known
    setOutput = set_output
    clearOutput = clear_output
    getOutput = get_output
    isOutputFlipped = is_output_flipped

class ButtonNode(DataNode):
    """This is the primary interface to on/off button devices associated with a
    ClientBase.  This creates a node that connects to the named button device,
    if it exists, and provides hooks to the user to read the state of any of
    the sequentially numbered buttons associated with that device.

    It also can associate an arbitrary ButtonHandle with each button; when
    buttons are associated with ButtonHandles, this node will put appropriate
    up and down events on the data graph for each button state change.
    """

    @overload
    def __init__(self, __param0: ButtonNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def is_valid(self) -> bool:
        """Returns true if the ButtonNode is valid and connected to a server, false
        otherwise.
        """
    def get_num_buttons(self) -> int:
        """Returns the number of buttons known to the ButtonNode.  This includes those
        buttons whose state has been seen, as well as buttons that have been
        associated with a ButtonHandle even if their state is unknown.  This number
        may change as more buttons are discovered.
        """
    def set_button_map(self, index: int, button: ButtonHandle | str) -> None:
        """Associates the indicated ButtonHandle with the button of the indicated
        index number.  When the given button index changes state, a corresponding
        ButtonEvent will be generated with the given ButtonHandle.  Pass
        ButtonHandle::none() to turn off any association.

        It is not necessary to call this if you simply want to query the state of
        the various buttons by index number; this is only necessary in order to
        generate ButtonEvents when the buttons change state.
        """
    def get_button_map(self, index: int) -> ButtonHandle:
        """Returns the ButtonHandle that was previously associated with the given
        index number by a call to set_button_map(), or ButtonHandle::none() if no
        button was associated.
        """
    def get_button_state(self, index: int) -> bool:
        """Returns true if the indicated button (identified by its index number) is
        currently known to be down, or false if it is up or unknown.
        """
    def is_button_known(self, index: int) -> bool:
        """Returns true if the state of the indicated button is known, or false if we
        have never heard anything about this particular button.
        """
    isValid = is_valid
    getNumButtons = get_num_buttons
    setButtonMap = set_button_map
    getButtonMap = get_button_map
    getButtonState = get_button_state
    isButtonKnown = is_button_known

class DialNode(DataNode):
    """This is the primary interface to infinite dial type devices associated with
    a ClientBase.  This creates a node that connects to the named dial device,
    if it exists, and provides hooks to the user to read the state of any of
    the sequentially numbered dial controls associated with that device.

    A dial is a rotating device that does not have stops--it can keep rotating
    any number of times.  Therefore it does not have a specific position at any
    given time, unlike an AnalogDevice.
    """

    @overload
    def __init__(self, __param0: DialNode) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def is_valid(self) -> bool:
        """Returns true if the DialNode is valid and connected to a server, false
        otherwise.
        """
    def get_num_dials(self) -> int:
        """Returns the number of dial dials known to the DialNode.  This number may
        change as more dials are discovered.
        """
    def read_dial(self, index: int) -> float:
        """Returns the number of complete revolutions of the dial since the last time
        read_dial() was called.  This is a destructive operation; it is not
        possible to read the dial without resetting the counter.
        """
    def is_dial_known(self, index: int) -> bool:
        """Returns true if the state of the indicated dial dial is known, or false if
        we have never heard anything about this particular dial.
        """
    isValid = is_valid
    getNumDials = get_num_dials
    readDial = read_dial
    isDialKnown = is_dial_known

class InputDeviceSet:
    """Manages a list of InputDevice objects, as returned by various
    InputDeviceManager methods.  This is implemented like a set, meaning the
    same device cannot occur more than once.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, copy: InputDeviceSet = ...) -> None: ...
    def __getitem__(self, index: int) -> InputDevice:
        """Returns the nth InputDevice in the collection."""
    def __len__(self) -> int:
        """Returns the number of devices in the collection."""
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[InputDevice]: ...  # Doesn't actually exist
    def assign(self, copy: Self) -> Self: ...
    def clear(self) -> None:
        """Removes all InputDevices from the collection."""
    def reserve(self, num: int) -> None:
        """This is a hint to Panda to allocate enough memory to hold the given number
        of InputDevices, if you know ahead of time how many you will be adding.
        """
    def output(self, out: ostream) -> None:
        """Writes a brief one-line description of the InputDeviceSet to the indicated
        output stream.
        """
    def write(self, out: ostream, indent_level: int = ...) -> None:
        """Writes a complete multi-line description of the InputDeviceSet to the
        indicated output stream.
        """

class InputDeviceManager:
    """This class keeps track of all the devices on a system, and sends out events
    when a device has been hot-plugged.

    @since 1.10.0
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_devices(self, device_class: InputDevice.DeviceClass = ...) -> InputDeviceSet:
        """`(self)`:
        Description: Returns all currently connected devices.

        `(self, device_class: InputDevice.DeviceClass)`:
        Description: Returns all currently connected devices of the given device class.
        """
    def add_device(self, device: InputDevice) -> None:
        """Called when a new device has been discovered.  This may also be used to
        register virtual devices.

        This causes a connect-device event to be thrown.
        """
    def remove_device(self, device: InputDevice) -> None:
        """Called when a device has been removed, or when a device should otherwise no
        longer be tracked.

        This causes a disconnect-device event to be thrown.
        """
    def update(self) -> None:
        """Polls the system to see if there are any new devices.  In some
        implementations this is a no-op.
        """
    @staticmethod
    def get_global_ptr() -> InputDeviceManager:
        """Returns the singleton InputDeviceManager instance."""
    getDevices = get_devices
    addDevice = add_device
    removeDevice = remove_device
    getGlobalPtr = get_global_ptr

class InputDeviceNode(DataNode):
    """Reads the controller data sent from the InputDeviceManager, and transmits
    it down the data graph.

    This is intended to only be accessed from the app thread.
    """

    device: InputDevice
    @overload
    def __init__(self, __param0: InputDeviceNode) -> None: ...
    @overload
    def __init__(self, device: InputDevice, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class TrackerNode(DataNode):
    """This class reads the position and orientation information from a tracker
    device and makes it available as a transformation on the data graph.
    It is also the primary interface to a Tracker object associated with a
    ClientBase.
    """

    @overload
    def __init__(self, device: InputDevice) -> None: ...
    @overload
    def __init__(self, __param0: TrackerNode) -> None: ...
    @overload
    def __init__(self, client: ClientBase, device_name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def is_valid(self) -> bool:
        """Returns true if the TrackerNode is valid and connected to a server, false
        otherwise.
        """
    def get_pos(self) -> LPoint3:
        """Returns the current position of the tracker, if it is available."""
    def get_orient(self) -> LOrientation:
        """Returns the current orientation of the tracker, if it is available."""
    def get_transform(self) -> LMatrix4:  # type: ignore[override]
        """Returns the current position and orientation of the tracker, as a combined
        matrix.
        """
    def get_time(self) -> float:
        """Returns the time of the tracker's last update."""
    def has_time(self) -> bool:
        """True if this data comes with timestamps."""
    def set_tracker_coordinate_system(self, cs: _CoordinateSystem) -> None:
        """Specifies the coordinate system that the tracker associated with this node
        will operate in.  Normally, this is set from the ClientBase that's used to
        create the TrackerNode, so it should not need to be set on an individual
        tracker basis.
        """
    def get_tracker_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system that the tracker associated with this node
        will operate in.
        """
    def set_graph_coordinate_system(self, cs: _CoordinateSystem) -> None:
        """Specifies the coordinate system that the TrackerNode will convert its
        transform into for passing down the data graph.  Normally, this is
        CS_default.
        """
    def get_graph_coordinate_system(self) -> _CoordinateSystem:
        """Returns the coordinate system that the TrackerNode will convert its
        transform into for passing down the data graph.  Normally, this is
        CS_default.
        """
    isValid = is_valid
    getPos = get_pos
    getOrient = get_orient
    getTransform = get_transform  # type: ignore[assignment]
    getTime = get_time
    hasTime = has_time
    setTrackerCoordinateSystem = set_tracker_coordinate_system
    getTrackerCoordinateSystem = get_tracker_coordinate_system
    setGraphCoordinateSystem = set_graph_coordinate_system
    getGraphCoordinateSystem = get_graph_coordinate_system

class VirtualMouse(DataNode):
    """Poses as a MouseAndKeyboard object in the datagraph, but accepts input from
    user calls, rather than reading the actual mouse and keyboard from an input
    device.  The user can write high-level code to put the mouse wherever
    he/she wants, and to insert keypresses on demand.
    """

    @overload
    def __init__(self, __param0: VirtualMouse) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_mouse_pos(self, x: int, y: int) -> None:
        """Sets the current mouse pixel location, where (0,0) is the upper left, and
        (width-1, height-1) is the lower right pixel of the virtual window.
        """
    def set_window_size(self, width: int, height: int) -> None:
        """Sets the size of the "window" in which the mouse rolls.  This changes the
        meaning of the values passed to set_mouse_pos().
        """
    def set_mouse_on(self, flag: bool) -> None:
        """Sets whether the mouse should appear to be within the window or not.  If
        this is true, the mouse is within the window; if false, the mouse is not
        within the window (and set_mouse_pos() means nothing).
        """
    def press_button(self, button: ButtonHandle | str) -> None:
        """Simulates a mouse or keyboard button being depressed.  This should be
        followed up by a call to release_button() sometime later (possibly
        immediately).
        """
    def release_button(self, button: ButtonHandle | str) -> None:
        """Simulates the button being released.  This should follow a previous call to
        press_button().
        """
    setMousePos = set_mouse_pos
    setWindowSize = set_window_size
    setMouseOn = set_mouse_on
    pressButton = press_button
    releaseButton = release_button
