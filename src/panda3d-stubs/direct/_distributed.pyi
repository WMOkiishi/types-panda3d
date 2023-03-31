from typing import Any, ClassVar
from typing_extensions import Self

from panda3d._typing import URL
from panda3d.core._downloader import HTTPChannel, SocketStream
from panda3d.core._express import Datagram, DatagramIterator
from panda3d.core._nativenet import Buffered_DatagramConnection
from panda3d.core._net import ConnectionWriter, QueuedConnectionManager, QueuedConnectionReader
from panda3d.core._pgraph import NodePath
from panda3d.direct._dcparser import DCClass, DCFile

class CConnectionRepository:
    """This class implements the C++ side of the ConnectionRepository object.  In
    particular, it manages the connection to the server once it has been opened
    (but does not open it directly).  It manages reading and writing datagrams
    on the connection and monitoring for unexpected disconnects as well as
    handling intentional disconnects.

    Certain server messages, like field updates, are handled entirely within
    the C++ layer, while server messages that are not understood by the C++
    layer are returned up to the Python layer for processing.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, has_owner_view: bool = ..., threaded_net: bool = ...) -> None: ...
    def get_dc_file(self) -> DCFile:
        """Returns the DCFile object associated with this repository."""
    def has_owner_view(self) -> bool:
        """Returns true if this repository can have 'owner' views of distributed
        objects.
        """
    def set_handle_c_updates(self, handle_c_updates: bool) -> None:
        """Set true to specify this repository should process distributed updates
        internally in C++ code, or false if it should return them to Python.
        """
    def get_handle_c_updates(self) -> bool:
        """Returns true if this repository will process distributed updates internally
        in C++ code, or false if it will return them to Python.
        """
    def set_client_datagram(self, client_datagram: bool) -> None:
        """Sets the client_datagram flag.  If this is true, incoming datagrams are not
        expected to be prefixed with the server routing information like message
        sender, channel number, etc.; otherwise, these server fields are parsed and
        removed from each incoming datagram.
        """
    def get_client_datagram(self) -> bool:
        """Returns the client_datagram flag."""
    def set_handle_datagrams_internally(self, handle_datagrams_internally: bool) -> None:
        """Sets the handle_datagrams_internally flag.  When true, certain message
        types can be handled by the C++ code in in this module.  When false, all
        datagrams, regardless of message type, are passed up to Python for
        processing.

        The CMU distributed-object implementation requires this to be set false.
        """
    def get_handle_datagrams_internally(self) -> bool:
        """Returns the handle_datagrams_internally flag."""
    def set_tcp_header_size(self, tcp_header_size: int) -> None:
        """Sets the header size of TCP packets.  At the present, legal values for this
        are 0, 2, or 4; this specifies the number of bytes to use encode the
        datagram length at the start of each TCP datagram.  Sender and receiver
        must independently agree on this.
        """
    def get_tcp_header_size(self) -> int:
        """Returns the current setting of TCP header size.  See set_tcp_header_size()."""
    def set_python_repository(self, python_repository) -> None:
        """Records the pointer to the Python class that derives from
        CConnectionRepository.  This allows the C++ implementation to directly
        manipulation some python structures on the repository.
        """
    def set_connection_http(self, channel: HTTPChannel) -> None:
        """Once a connection has been established via the HTTP interface, gets the
        connection and uses it.  The supplied HTTPChannel object must have a
        connection available via get_connection().
        """
    def get_stream(self) -> SocketStream:
        """Returns the SocketStream that internally represents the already-established
        HTTP connection.  Returns NULL if there is no current HTTP connection.
        """
    def try_connect_net(self, url: URL) -> bool:
        """Uses Panda's "net" library to try to connect to the server and port named
        in the indicated URL.  Returns true if successful, false otherwise.
        """
    def get_qcm(self) -> QueuedConnectionManager:
        """Returns the QueuedConnectionManager object associated with the repository."""
    def get_cw(self) -> ConnectionWriter:
        """Returns the ConnectionWriter object associated with the repository."""
    def get_qcr(self) -> QueuedConnectionReader:
        """Returns the QueuedConnectionReader object associated with the repository."""
    def connect_native(self, url: URL) -> bool:
        """Connects to the server using Panda's low-level and fast "native net"
        library.
        """
    def get_bdc(self) -> Buffered_DatagramConnection:
        """Returns the Buffered_DatagramConnection object associated with the
        repository.
        """
    def check_datagram(self) -> bool:
        """Returns true if a new datagram is available, false otherwise.  If the
        return value is true, the new datagram may be retrieved via get_datagram(),
        or preferably, with get_datagram_iterator() and get_msg_type().
        """
    def get_datagram(self, dg: Datagram) -> None:
        """Fills the datagram object with the datagram most recently retrieved by
        check_datagram().
        """
    def get_datagram_iterator(self, di: Datagram | DatagramIterator) -> None:
        """Fills the DatagramIterator object with the iterator for the datagram most
        recently retrieved by check_datagram().  This iterator has already read
        past the datagram header and the message type, and is positioned at the
        beginning of data.
        """
    def get_msg_channel(self, offset: int = ...) -> int:
        """Returns the channel(s) to which the current message was sent, according to
        the datagram headers.  This information is not available to the client.
        """
    def get_msg_channel_count(self) -> int: ...
    def get_msg_sender(self) -> int:
        """Returns the sender ID of the current message, according to the datagram
        headers.  This information is not available to the client.
        """
    def get_msg_type(self) -> int:
        """Returns the type ID of the current message, according to the datagram
        headers.
        """
    @staticmethod
    def get_overflow_event_name() -> str:
        """Returns event string that will be thrown if the datagram reader queue
        overflows.
        """
    def is_connected(self) -> bool:
        """Returns true if the connection to the gameserver is established and still
        good, false if we are not connected.  A false value means either (a) we
        never successfully connected, (b) we explicitly called disconnect(), or (c)
        we were connected, but the connection was spontaneously lost.
        """
    def send_datagram(self, dg: Datagram) -> bool:
        """Queues the indicated datagram for sending to the server.  It may not get
        sent immediately if collect_tcp is in effect; call flush() to guarantee it
        is sent now.
        """
    def set_want_message_bundling(self, flag: bool) -> None:
        """Enable/disable outbound message bundling"""
    def get_want_message_bundling(self) -> bool:
        """Returns true if message bundling enabled"""
    def set_in_quiet_zone(self, flag: bool) -> None:
        """Enables/disables quiet zone mode"""
    def get_in_quiet_zone(self) -> bool:
        """Returns true if repository is in quiet zone mode"""
    def start_message_bundle(self) -> None:
        """Send a set of messages to the state server that will be processed
        atomically.  For instance, you can do a combined setLocation/setPos and
        prevent race conditions where clients briefly get the setLocation but not
        the setPos, because the state server hasn't processed the setPos yet
        """
    def is_bundling_messages(self) -> bool:
        """Returns true if repository is queueing outgoing messages into a message
        bundle
        """
    def send_message_bundle(self, channel: int, sender_channel: int) -> None:
        """Send network messages queued up since startMessageBundle was called."""
    def abandon_message_bundles(self) -> None:
        """throw out any msgs that have been queued up for message bundles"""
    def bundle_msg(self, dg: Datagram) -> None: ...
    def consider_flush(self) -> bool:
        """Sends the most recently queued data if enough time has elapsed.  This only
        has meaning if set_collect_tcp() has been set to true.
        """
    def flush(self) -> bool:
        """Sends the most recently queued data now.  This only has meaning if
        set_collect_tcp() has been set to true.
        """
    def disconnect(self) -> None:
        """Closes the connection to the server."""
    def shutdown(self) -> None:
        """May be called at application shutdown to ensure all threads are cleaned up."""
    def set_simulated_disconnect(self, simulated_disconnect: bool) -> None:
        """Sets the simulated disconnect flag.  While this is true, no datagrams will
        be retrieved from or sent to the server.  The idea is to simulate a
        temporary network outage.
        """
    def get_simulated_disconnect(self) -> bool:
        """Returns the simulated disconnect flag.  While this is true, no datagrams
        will be retrieved from or sent to the server.  The idea is to simulate a
        temporary network outage.
        """
    def toggle_verbose(self) -> None:
        """Toggles the current setting of the verbose flag.  When true, this describes
        every message going back and forth on the wire.
        """
    def set_verbose(self, verbose: bool) -> None:
        """Directly sets the verbose flag.  When true, this describes every message
        going back and forth on the wire.
        """
    def get_verbose(self) -> bool:
        """Returns the current setting of the verbose flag.  When true, this describes
        every message going back and forth on the wire.
        """
    def set_time_warning(self, time_warning: float) -> None:
        """Directly sets the time_warning field.  When non zero, this describes every
        message going back and forth on the wire when the msg handling time is over
        it
        """
    def get_time_warning(self) -> float:
        """Returns the current setting of the time_warning field."""
    getDcFile = get_dc_file
    hasOwnerView = has_owner_view
    setHandleCUpdates = set_handle_c_updates
    getHandleCUpdates = get_handle_c_updates
    setClientDatagram = set_client_datagram
    getClientDatagram = get_client_datagram
    setHandleDatagramsInternally = set_handle_datagrams_internally
    getHandleDatagramsInternally = get_handle_datagrams_internally
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size
    setPythonRepository = set_python_repository
    setConnectionHttp = set_connection_http
    getStream = get_stream
    tryConnectNet = try_connect_net
    getQcm = get_qcm
    getCw = get_cw
    getQcr = get_qcr
    connectNative = connect_native
    getBdc = get_bdc
    checkDatagram = check_datagram
    getDatagram = get_datagram
    getDatagramIterator = get_datagram_iterator
    getMsgChannel = get_msg_channel
    getMsgChannelCount = get_msg_channel_count
    getMsgSender = get_msg_sender
    getMsgType = get_msg_type
    getOverflowEventName = get_overflow_event_name
    isConnected = is_connected
    sendDatagram = send_datagram
    setWantMessageBundling = set_want_message_bundling
    getWantMessageBundling = get_want_message_bundling
    setInQuietZone = set_in_quiet_zone
    getInQuietZone = get_in_quiet_zone
    startMessageBundle = start_message_bundle
    isBundlingMessages = is_bundling_messages
    sendMessageBundle = send_message_bundle
    abandonMessageBundles = abandon_message_bundles
    bundleMsg = bundle_msg
    considerFlush = consider_flush
    setSimulatedDisconnect = set_simulated_disconnect
    getSimulatedDisconnect = get_simulated_disconnect
    toggleVerbose = toggle_verbose
    setVerbose = set_verbose
    getVerbose = get_verbose
    setTimeWarning = set_time_warning
    getTimeWarning = get_time_warning

class CDistributedSmoothNodeBase:
    """This class defines some basic methods of DistributedSmoothNodeBase which
    have been moved into C++ as a performance optimization.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: CDistributedSmoothNodeBase = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_repository(self, repository: CConnectionRepository, is_ai: bool, ai_id: int) -> None:
        """Tells the C++ instance definition about the AI or Client repository, used
        for sending datagrams.
        """
    def set_clock_delta(self, clock_delta) -> None:
        """Tells the C++ instance definition about the global ClockDelta object."""
    def initialize(self, node_path: NodePath, dclass: DCClass, do_id: int) -> None:
        """Initializes the internal structures from some constructs that are normally
        stored only in Python.  Also reads the current node's pos & hpr values in
        preparation for transmitting them via one of the broadcast_pos_hpr_*()
        methods.
        """
    def send_everything(self) -> None:
        """Broadcasts the current pos/hpr in its complete form."""
    def broadcast_pos_hpr_full(self) -> None:
        """Examines the complete pos/hpr information to see which of the six elements
        have changed, and broadcasts the appropriate messages.
        """
    def broadcast_pos_hpr_xyh(self) -> None:
        """Examines only X, Y, and H of the pos/hpr information, and broadcasts the
        appropriate messages.
        """
    def broadcast_pos_hpr_xy(self) -> None:
        """Examines only X and Y of the pos/hpr information, and broadcasts the
        appropriate messages.
        """
    def set_curr_l(self, l: int) -> None:
        """Appends the timestamp and sends the update."""
    def print_curr_l(self) -> None: ...
    setRepository = set_repository
    setClockDelta = set_clock_delta
    sendEverything = send_everything
    broadcastPosHprFull = broadcast_pos_hpr_full
    broadcastPosHprXyh = broadcast_pos_hpr_xyh
    broadcastPosHprXy = broadcast_pos_hpr_xy
    setCurrL = set_curr_l
    printCurrL = print_curr_l
