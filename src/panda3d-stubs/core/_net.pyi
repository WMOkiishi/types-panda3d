from collections.abc import Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d.core._dtoolutil import ostream
from panda3d.core._express import Datagram, DatagramGenerator, DatagramSink, PointerToVoid, ReferenceCount
from panda3d.core._nativenet import Socket_Address, Socket_IP

class PointerToBase_Connection(PointerToVoid):
    def clear(self) -> None: ...
    def output(self, out: ostream) -> None: ...

class PointerTo_Connection(PointerToBase_Connection):
    @overload
    def __init__(self, ptr: Connection = ...) -> None: ...
    @overload
    def __init__(self, copy: Connection) -> None: ...
    @overload
    def __init__(self, __param0: None) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def p(self) -> Connection:
        """If your base class is a derivative of TypedObject, you might want to use
        the DCAST macro defined in typedObject.h instead, e.g.  DCAST(MyType,
        ptr).  This provides a clean downcast that doesn't require .p() or any
        double-casting, and it can be run-time checked for correctness.
        """
    @overload
    def assign(self, ptr: Connection) -> Self: ...
    @overload
    def assign(self, copy: Connection) -> Self: ...

class NetAddress:
    """Represents a network address to which UDP packets may be sent or to which a
    TCP socket may be bound.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: NetAddress = ...) -> None:
        """`(self)`:
        Constructs an unspecified address.

        `(self, addr: Socket_Address)`:
        Constructs an address from a given Socket_Address.  Normally, this
        constructor should not be used by user code; instead, create a default
        NetAddress and use one of the set_*() functions to set up an address.
        """
    @overload
    def __init__(self, addr: Socket_Address) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_any(self, port: int) -> bool:
        """Sets the address up to refer to a particular port, but not to any
        particular IP.  Returns true if successful, false otherwise (currently,
        this only returns true).
        """
    def set_localhost(self, port: int) -> bool:
        """Sets the address up to refer to a particular port, on this host."""
    def set_broadcast(self, port: int) -> bool:
        """Sets the address to the broadcast address."""
    def set_host(self, hostname: str, port: int) -> bool:
        """Sets the address up to refer to a particular port on a particular host.
        Returns true if the hostname is known, false otherwise.
        """
    def clear(self) -> None:
        """Resets the NetAddress to its initial state."""
    def get_port(self) -> int:
        """Returns the port number to which this address refers."""
    def set_port(self, port: int) -> None:
        """Resets the port number without otherwise changing the address."""
    def get_ip_string(self) -> str:
        """Returns the IP address to which this address refers, formatted as a string."""
    def is_any(self) -> bool:
        """Returns true if the IP address has only zeroes."""
    def get_ip(self) -> int:
        """Returns the IP address to which this address refers, as a 32-bit integer,
        in host byte order.
        @deprecated  Does not work with IPv6 addresses.
        """
    def get_ip_component(self, n: int) -> str:
        """Returns the nth 8-bit component of the IP address.  An IP address has four
        components; component 0 is the first (leftmost), and component 3 is the
        last (rightmost) in the dotted number convention.
        """
    def get_addr(self) -> Socket_Address:
        """Returns the Socket_Address for this address."""
    def output(self, out: ostream) -> None: ...
    def get_hash(self) -> int: ...
    setAny = set_any
    setLocalhost = set_localhost
    setBroadcast = set_broadcast
    setHost = set_host
    getPort = get_port
    setPort = set_port
    getIpString = get_ip_string
    isAny = is_any
    getIp = get_ip
    getIpComponent = get_ip_component
    getAddr = get_addr
    getHash = get_hash

class Connection(ReferenceCount):
    """Represents a single TCP or UDP socket for input or output."""

    def __init__(self, manager: ConnectionManager, socket: Socket_IP | int) -> None:
        """Creates a connection.  Normally this constructor should not be used
        directly by user code; use one of the methods in ConnectionManager to make
        a new connection.
        """
    def get_address(self) -> NetAddress:
        """Returns the address bound to this connection, if it is a TCP connection."""
    def get_manager(self) -> ConnectionManager:
        """Returns a pointer to the ConnectionManager object that serves this
        connection.
        """
    def get_socket(self) -> Socket_IP:
        """Returns the internal Socket_IP that defines the connection."""
    def set_collect_tcp(self, collect_tcp: bool) -> None:
        """Enables or disables "collect-tcp" mode.  In this mode, individual TCP
        packets are not sent immediately, but rather they are collected together
        and accumulated to be sent periodically as one larger TCP packet.  This
        cuts down on overhead from the TCP/IP protocol, especially if many small
        packets need to be sent on the same connection, but it introduces
        additional latency (since packets must be held before they can be sent).

        See set_collect_tcp_interval() to specify the interval of time for which to
        hold packets before sending them.

        If you enable this mode, you may also need to periodically call
        consider_flush() to flush the queue if no packets have been sent recently.
        """
    def get_collect_tcp(self) -> bool:
        """Returns the current setting of "collect-tcp" mode.  See set_collect_tcp()."""
    def set_collect_tcp_interval(self, interval: float) -> None:
        """Specifies the interval in time, in seconds, for which to hold TCP packets
        before sending all of the recently received packets at once.  This only has
        meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
        """
    def get_collect_tcp_interval(self) -> float:
        """Returns the interval in time, in seconds, for which to hold TCP packets
        before sending all of the recently received packets at once.  This only has
        meaning if "collect-tcp" mode is enabled; see set_collect_tcp().
        """
    def consider_flush(self) -> bool:
        """Sends the most recently queued TCP datagram(s) if enough time has elapsed.
        This only has meaning if set_collect_tcp() has been set to true.
        """
    def flush(self) -> bool:
        """Sends the most recently queued TCP datagram(s) now.  This only has meaning
        if set_collect_tcp() has been set to true.
        """
    def set_linger(self, flag: bool, time: float) -> None:
        """Sets the time to linger on close if data is present.  If flag is false,
        when you close a socket with data available the system attempts to deliver
        the data to the peer (the default behavior).  If flag is false but time is
        zero, the system discards any undelivered data when you close the socket.
        If flag is false but time is nonzero, the system waits up to time seconds
        to deliver the data.
        """
    def set_reuse_addr(self, flag: bool) -> None:
        """Sets whether local address reuse is allowed."""
    def set_keep_alive(self, flag: bool) -> None:
        """Sets whether the connection is periodically tested to see if it is still
        alive.
        """
    def set_recv_buffer_size(self, size: int) -> None:
        """Sets the size of the receive buffer, in bytes."""
    def set_send_buffer_size(self, size: int) -> None:
        """Sets the size of the send buffer, in bytes."""
    def set_ip_time_to_live(self, ttl: int) -> None:
        """Sets IP time-to-live."""
    def set_ip_type_of_service(self, tos: int) -> None:
        """Sets IP type-of-service and precedence."""
    def set_no_delay(self, flag: bool) -> None:
        """If flag is true, this disables the Nagle algorithm, and prevents delaying
        of send to coalesce packets.
        """
    def set_max_segment(self, size: int) -> None:
        """Sets the maximum segment size."""
    getAddress = get_address
    getManager = get_manager
    getSocket = get_socket
    setCollectTcp = set_collect_tcp
    getCollectTcp = get_collect_tcp
    setCollectTcpInterval = set_collect_tcp_interval
    getCollectTcpInterval = get_collect_tcp_interval
    considerFlush = consider_flush
    setLinger = set_linger
    setReuseAddr = set_reuse_addr
    setKeepAlive = set_keep_alive
    setRecvBufferSize = set_recv_buffer_size
    setSendBufferSize = set_send_buffer_size
    setIpTimeToLive = set_ip_time_to_live
    setIpTypeOfService = set_ip_type_of_service
    setNoDelay = set_no_delay
    setMaxSegment = set_max_segment

class ConnectionReader:
    """This is an abstract base class for a family of classes that listen for
    activity on a socket and respond to it, for instance by reading a datagram
    and serving it (or queueing it up for later service).

    A ConnectionReader may define an arbitrary number of threads (at least one)
    to process datagrams coming in from an arbitrary number of sockets that it
    is monitoring.  The number of threads is specified at construction time and
    cannot be changed, but the set of sockets that is to be monitored may be
    constantly modified at will.

    This is an abstract class because it doesn't define how to process each
    received datagram.  See QueuedConnectionReader.  Also note that
    ConnectionListener derives from this class, extending it to accept
    connections on a rendezvous socket rather than read datagrams.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def add_connection(self, connection: Connection) -> bool:
        """Adds a new socket to the list of sockets the ConnectionReader will monitor.
        A datagram that comes in on any of the monitored sockets will be reported.
        In the case of a ConnectionListener, this adds a new rendezvous socket; any
        activity on any of the monitored sockets will cause a connection to be
        accepted.

        The return value is true if the connection was added, false if it was
        already there.

        add_connection() is thread-safe, and may be called at will by any thread.
        """
    def remove_connection(self, connection: Connection) -> bool:
        """Removes a socket from the list of sockets being monitored.  Returns true if
        the socket was correctly removed, false if it was not on the list in the
        first place.

        remove_connection() is thread-safe, and may be called at will by any
        thread.
        """
    def is_connection_ok(self, connection: Connection) -> bool:
        """Returns true if the indicated connection has been added to the
        ConnectionReader and is being monitored properly, false if it is not known,
        or if there was some error condition detected on the connection.  (If there
        was an error condition, normally the ConnectionManager would have been
        informed and closed the connection.)
        """
    def poll(self) -> None:
        """Explicitly polls the available sockets to see if any of them have any
        noise.  This function does nothing unless this is a polling-type
        ConnectionReader, i.e.  it was created with zero threads (and is_polling()
        will return true).

        It is not necessary to call this explicitly for a QueuedConnectionReader.
        """
    def get_manager(self) -> ConnectionManager:
        """Returns a pointer to the ConnectionManager object that serves this
        ConnectionReader.
        """
    def is_polling(self) -> bool:
        """Returns true if the reader is a polling reader, i.e.  it has no threads."""
    def get_num_threads(self) -> int:
        """Returns the number of threads the ConnectionReader has been created with."""
    def set_raw_mode(self, mode: bool) -> None:
        """Sets the ConnectionReader into raw mode (or turns off raw mode).  In raw
        mode, datagram headers are not expected; instead, all the data available on
        the pipe is treated as a single datagram.

        This is similar to set_tcp_header_size(0), except that it also turns off
        headers for UDP packets.
        """
    def get_raw_mode(self) -> bool:
        """Returns the current setting of the raw mode flag.  See set_raw_mode()."""
    def set_tcp_header_size(self, tcp_header_size: int) -> None:
        """Sets the header size of TCP packets.  At the present, legal values for this
        are 0, 2, or 4; this specifies the number of bytes to use encode the
        datagram length at the start of each TCP datagram.  Sender and receiver
        must independently agree on this.
        """
    def get_tcp_header_size(self) -> int:
        """Returns the current setting of TCP header size.  See set_tcp_header_size()."""
    def shutdown(self) -> None:
        """Terminates all threads cleanly.  Normally this is only called by the
        destructor, but it may be called explicitly before destruction.
        """
    addConnection = add_connection
    removeConnection = remove_connection
    isConnectionOk = is_connection_ok
    getManager = get_manager
    isPolling = is_polling
    getNumThreads = get_num_threads
    setRawMode = set_raw_mode
    getRawMode = get_raw_mode
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size

class ConnectionListener(ConnectionReader):
    """This is a special kind of ConnectionReader that waits for activity on a
    rendezvous port and accepts a TCP connection (instead of attempting to read
    a datagram from the rendezvous port).

    It is itself an abstract class, as it doesn't define what to do with the
    established connection.  See QueuedConnectionListener.
    """

class NetDatagram(Datagram):
    """A specific kind of Datagram, especially for sending across or receiving
    from a network.  It's different only in that it knows which Connection
    and/or NetAddress it is to be sent to or was received from.
    """

    def __init__(self, copy: Datagram = ...) -> None:
        """Constructs an empty datagram."""
    def assign(self, copy: Datagram) -> Self: ...
    def set_connection(self, connection: Connection) -> None:
        """Specifies the socket to which the datagram should be written."""
    def get_connection(self) -> Connection:
        """Retrieves the socket from which the datagram was read, or to which it is
        scheduled to be written.
        """
    def set_address(self, address: NetAddress | Socket_Address) -> None:
        """Specifies the host to which the datagram should be sent."""
    def get_address(self) -> NetAddress:
        """Retrieves the host from which the datagram was read, or to which it is
        scheduled to be sent.
        """
    setConnection = set_connection
    getConnection = get_connection
    setAddress = set_address
    getAddress = get_address

class ConnectionManager:
    """The primary interface to the low-level networking layer in this package.  A
    ConnectionManager is used to establish and destroy TCP and UDP connections.
    Communication on these connections, once established, is handled via
    ConnectionReader, ConnectionWriter, and ConnectionListener.

    You may use this class directly if you don't care about tracking which
    connections have been unexpectedly closed; otherwise, you should use
    QueuedConnectionManager to get reports about these events (or derive your
    own class to handle these events properly).
    """

    class Interface:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, __param0: ConnectionManager.Interface) -> None: ...
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def get_name(self) -> str: ...
        def get_mac_address(self) -> str: ...
        def has_ip(self) -> bool: ...
        def get_ip(self) -> NetAddress: ...
        def has_netmask(self) -> bool: ...
        def get_netmask(self) -> NetAddress: ...
        def has_broadcast(self) -> bool: ...
        def get_broadcast(self) -> NetAddress: ...
        def has_p2p(self) -> bool: ...
        def get_p2p(self) -> NetAddress: ...
        def output(self, out: ostream) -> None: ...
        getName = get_name
        getMacAddress = get_mac_address
        hasIp = has_ip
        getIp = get_ip
        hasNetmask = has_netmask
        getNetmask = get_netmask
        hasBroadcast = has_broadcast
        getBroadcast = get_broadcast
        hasP2p = has_p2p
        getP2p = get_p2p

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def host_name(self) -> str: ...
    @property
    def interfaces(self) -> Sequence[ConnectionManager.Interface]: ...
    def __init__(self) -> None: ...
    @overload
    def open_UDP_connection(self, port: int = ...) -> Connection:
        """`(self, hostname: str, port: int, for_broadcast: bool = ...)`:
        Opens a socket for sending and/or receiving UDP packets.  If the port
        number is greater than zero, the UDP connection will be opened for
        listening on the indicated port; otherwise, it will be useful only for
        sending.

        This variant accepts both a hostname and port to listen on a particular
        interface; if the hostname is empty, all interfaces will be available,
        both IPv4 and IPv6.

        If for_broadcast is true, this UDP connection will be configured to send
        and/or receive messages on the broadcast address (255.255.255.255);
        otherwise, these messages may be automatically filtered by the OS.

        Use a ConnectionReader and ConnectionWriter to handle the actual
        communication.

        `(self, port: int = ...)`:
        Opens a socket for sending and/or receiving UDP packets.  If the port
        number is greater than zero, the UDP connection will be opened for
        listening on the indicated port; otherwise, it will be useful only for
        sending.

        Use a ConnectionReader and ConnectionWriter to handle the actual
        communication.
        """
    @overload
    def open_UDP_connection(self, hostname: str, port: int, for_broadcast: bool = ...) -> Connection: ...
    @overload
    def open_TCP_server_rendezvous(self, address: NetAddress | Socket_Address, backlog: int) -> Connection:
        """`(self, address: NetAddress, backlog: int)`:
        Creates a socket to be used as a rendezvous socket for a server to listen
        for TCP connections.  The socket returned by this call should only be added
        to a ConnectionListener (not to a generic ConnectionReader).

        This variant of this method accepts a NetAddress, which allows you to
        specify a specific interface to listen to.

        backlog is the maximum length of the queue of pending connections.

        `(self, hostname: str, port: int, backlog: int)`:
        Creates a socket to be used as a rendezvous socket for a server to listen
        for TCP connections.  The socket returned by this call should only be added
        to a ConnectionListener (not to a generic ConnectionReader).

        This variant of this method accepts a "hostname", which is usually just an
        IP address in dotted notation, and a port number.  It will listen on the
        interface indicated by the IP address.  If the IP address is empty string,
        it will listen on all interfaces.

        backlog is the maximum length of the queue of pending connections.

        `(self, port: int, backlog: int)`:
        Creates a socket to be used as a rendezvous socket for a server to listen
        for TCP connections.  The socket returned by this call should only be added
        to a ConnectionListener (not to a generic ConnectionReader).

        This variant of this method accepts a single port, and will listen to that
        port on all available interfaces, both IPv4 and IPv6.

        backlog is the maximum length of the queue of pending connections.
        """
    @overload
    def open_TCP_server_rendezvous(self, port: int, backlog: int) -> Connection: ...
    @overload
    def open_TCP_server_rendezvous(self, hostname: str, port: int, backlog: int) -> Connection: ...
    @overload
    def open_TCP_client_connection(self, address: NetAddress | Socket_Address, timeout_ms: int) -> Connection:
        """`(self, address: NetAddress, timeout_ms: int)`:
        Attempts to establish a TCP client connection to a server at the indicated
        address.  If the connection is not established within timeout_ms
        milliseconds, a null connection is returned.

        `(self, hostname: str, port: int, timeout_ms: int)`:
        This is a shorthand version of the function to directly establish
        communications to a named host and port.
        """
    @overload
    def open_TCP_client_connection(self, hostname: str, port: int, timeout_ms: int) -> Connection: ...
    def close_connection(self, connection: Connection) -> bool:
        """Terminates a UDP or TCP socket previously opened.  This also removes it
        from any associated ConnectionReader or ConnectionListeners.

        The socket itself may not be immediately closed--it will not be closed
        until all outstanding pointers to it are cleared, including any pointers
        remaining in NetDatagrams recently received from the socket.

        The return value is true if the connection was marked to be closed, or
        false if close_connection() had already been called (or the connection did
        not belong to this ConnectionManager).  In neither case can you infer
        anything about whether the connection has *actually* been closed yet based
        on the return value.
        """
    def wait_for_readers(self, timeout: float) -> bool:
        """Blocks the process for timeout number of seconds, or until any data is
        available on any of the non-threaded ConnectionReaders or
        ConnectionListeners, whichever comes first.  The return value is true if
        there is data available (but you have to iterate through all readers to
        find it), or false if the timeout occurred without any data.

        If the timeout value is negative, this will block forever or until data is
        available.

        This only works if all ConnectionReaders and ConnectionListeners are non-
        threaded.  If any threaded ConnectionReaders are part of the
        ConnectionManager, the timeout value is implicitly treated as 0.
        """
    @staticmethod
    def get_host_name() -> str:
        """Returns the name of this particular machine on the network, if available,
        or the empty string if the hostname cannot be determined.
        """
    def scan_interfaces(self) -> None:
        """Repopulates the list reported by get_num_interface()/get_interface().  It
        is not necessary to call this explicitly, unless you want to re-determine
        the connected interfaces (for instance, if you suspect the hardware has
        recently changed).
        """
    def get_num_interfaces(self) -> int:
        """This returns the number of usable network interfaces detected on this
        machine.  See scan_interfaces() to repopulate this list.
        """
    def get_interface(self, n: int) -> ConnectionManager.Interface:
        """Returns the nth usable network interface detected on this machine.
        See scan_interfaces() to repopulate this list.
        """
    def get_interfaces(self) -> tuple[ConnectionManager.Interface, ...]: ...
    openUDPConnection = open_UDP_connection
    openTCPServerRendezvous = open_TCP_server_rendezvous
    openTCPClientConnection = open_TCP_client_connection
    closeConnection = close_connection
    waitForReaders = wait_for_readers
    getHostName = get_host_name
    scanInterfaces = scan_interfaces
    getNumInterfaces = get_num_interfaces
    getInterface = get_interface
    getInterfaces = get_interfaces

class ConnectionWriter:
    """This class handles threaded delivery of datagrams to various TCP or UDP
    sockets.

    A ConnectionWriter may define an arbitrary number of threads (0 or more) to
    write its datagrams to sockets.  The number of threads is specified at
    construction time and cannot be changed.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, manager: ConnectionManager, num_threads: int, thread_name: str = ...) -> None:
        """Creates a new ConnectionWriter with the indicated number of threads to
        handle output.

        If num_threads is 0, all datagrams will be sent immediately instead of
        queueing for later transmission by a thread.
        """
    def set_max_queue_size(self, max_size: int) -> None:
        """Limits the number of packets that may be pending on the outbound queue.
        This only has an effect when using threads; if num_threads is 0, then all
        packets are sent immediately.
        """
    def get_max_queue_size(self) -> int:
        """Returns the maximum size the queue is allowed to grow to.  See
        set_max_queue_size().
        """
    def get_current_queue_size(self) -> int:
        """Returns the current number of things in the queue."""
    @overload
    def send(self, datagram: Datagram, connection: Connection, block: bool = ...) -> bool:
        """`(self, datagram: Datagram, connection: Connection, address: NetAddress, block: bool = ...)`:
        Enqueues a datagram for transmittal on the indicated socket.  This form of
        the function allows the specification of a destination host address, and so
        is appropriate for UDP packets.  Use the other send() method for sending
        TCP packets.

        Returns true if successful, false if there was an error.  In the normal,
        threaded case, this function only returns false if the send queue is
        filled; it's impossible to detect a transmission error at this point.

        If block is true, this will not return false if the send queue is filled;
        instead, it will wait until there is space available.

        `(self, datagram: Datagram, connection: Connection, block: bool = ...)`:
        Enqueues a datagram for transmittal on the indicated socket.  Since the
        host address is not specified with this form, this function should only be
        used for sending TCP packets.  Use the other send() method for sending UDP
        packets.

        Returns true if successful, false if there was an error.  In the normal,
        threaded case, this function only returns false if the send queue is
        filled; it's impossible to detect a transmission error at this point.

        If block is true, this will not return false if the send queue is filled;
        instead, it will wait until there is space available.
        """
    @overload
    def send(
        self, datagram: Datagram, connection: Connection, address: NetAddress | Socket_Address, block: bool = ...
    ) -> bool: ...
    def is_valid_for_udp(self, datagram: Datagram) -> bool:
        """Returns true if the datagram is small enough to be sent over a UDP packet,
        false otherwise.
        """
    def get_manager(self) -> ConnectionManager:
        """Returns a pointer to the ConnectionManager object that serves this
        ConnectionWriter.
        """
    def is_immediate(self) -> bool:
        """Returns true if the writer is an immediate writer, i.e.  it has no threads."""
    def get_num_threads(self) -> int:
        """Returns the number of threads the ConnectionWriter has been created with."""
    def set_raw_mode(self, mode: bool) -> None:
        """Sets the ConnectionWriter into raw mode (or turns off raw mode).  In raw
        mode, datagrams are not sent along with their headers; the bytes in the
        datagram are simply sent down the pipe.

        Setting the ConnectionWriter to raw mode must be done with care.  This can
        only be done when the matching ConnectionReader is also set to raw mode, or
        when the ConnectionWriter is communicating to a process that does not
        expect datagrams.
        """
    def get_raw_mode(self) -> bool:
        """Returns the current setting of the raw mode flag.  See set_raw_mode()."""
    def set_tcp_header_size(self, tcp_header_size: int) -> None:
        """Sets the header size of TCP packets.  At the present, legal values for this
        are 0, 2, or 4; this specifies the number of bytes to use encode the
        datagram length at the start of each TCP datagram.  Sender and receiver
        must independently agree on this.
        """
    def get_tcp_header_size(self) -> int:
        """Returns the current setting of TCP header size.  See set_tcp_header_size()."""
    def shutdown(self) -> None:
        """Stops all the threads and cleans them up.  This is called automatically by
        the destructor, but it may be called explicitly before destruction.
        """
    setMaxQueueSize = set_max_queue_size
    getMaxQueueSize = get_max_queue_size
    getCurrentQueueSize = get_current_queue_size
    isValidForUdp = is_valid_for_udp
    getManager = get_manager
    isImmediate = is_immediate
    getNumThreads = get_num_threads
    setRawMode = set_raw_mode
    getRawMode = get_raw_mode
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size

class QueuedReturn_Datagram:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_max_queue_size(self, max_size: int) -> None: ...
    def get_max_queue_size(self) -> int: ...
    def get_current_queue_size(self) -> int: ...
    def get_overflow_flag(self) -> bool: ...
    def reset_overflow_flag(self) -> None: ...
    setMaxQueueSize = set_max_queue_size
    getMaxQueueSize = get_max_queue_size
    getCurrentQueueSize = get_current_queue_size
    getOverflowFlag = get_overflow_flag
    resetOverflowFlag = reset_overflow_flag

class DatagramGeneratorNet(DatagramGenerator, ConnectionReader, QueuedReturn_Datagram):
    """This class provides datagrams one-at-a-time as read directly from the net,
    via a TCP connection.  If a datagram is not available, get_datagram() will
    block until one is.
    """

    def __init__(self, manager: ConnectionManager, num_threads: int) -> None:
        """Creates a new DatagramGeneratorNet with the indicated number of threads to
        handle requests.  Normally num_threads should be either 0 or 1 to guarantee
        that datagrams are generated in the same order in which they were received.
        """
    def upcast_to_DatagramGenerator(self) -> DatagramGenerator: ...
    def upcast_to_ConnectionReader(self) -> ConnectionReader: ...
    def upcast_to_QueuedReturn_Datagram(self) -> QueuedReturn_Datagram: ...
    def get_datagram(self, data: Datagram) -> bool:
        """Reads the next datagram from the stream.  Blocks until a datagram is
        available.  Returns true on success, false on stream closed or error.
        """
    def is_eof(self) -> bool:
        """Returns true if the stream has been closed normally.  This test may only be
        made after a call to get_datagram() has failed.
        """
    def is_error(self) -> bool:
        """Returns true if the stream has an error condition."""
    upcastToDatagramGenerator = upcast_to_DatagramGenerator
    upcastToConnectionReader = upcast_to_ConnectionReader
    upcastToQueuedReturnDatagram = upcast_to_QueuedReturn_Datagram
    getDatagram = get_datagram
    isEof = is_eof
    isError = is_error

class DatagramSinkNet(DatagramSink, ConnectionWriter):
    """This class accepts datagrams one-at-a-time and sends them over the net, via
    a TCP connection.
    """

    def __init__(self, manager: ConnectionManager, num_threads: int) -> None:
        """Creates a new DatagramSinkNet with the indicated number of threads to
        handle writing.  Normally num_threads should be either 0 or 1 to guarantee
        that datagrams are delivered in the same order in which they were sent.
        """
    def upcast_to_DatagramSink(self) -> DatagramSink: ...
    def upcast_to_ConnectionWriter(self) -> ConnectionWriter: ...
    def set_target(self, connection: Connection) -> None:
        """Specifies the Connection that will receive all future Datagrams sent."""
    def get_target(self) -> Connection:
        """Returns the current target Connection, or NULL if the target has not yet
        been set.  See set_target().
        """
    def put_datagram(self, data: Datagram) -> bool:
        """Sends the given datagram to the target.  Returns true on success, false if
        there is an error.  Blocks if necessary until the target is ready.
        """
    def is_error(self) -> bool:
        """Returns true if there is an error on the target connection, or if the
        target has never been set.
        """
    def flush(self) -> None:
        """Ensures that all datagrams previously written will be visible on the
        stream.
        """
    upcastToDatagramSink = upcast_to_DatagramSink
    upcastToConnectionWriter = upcast_to_ConnectionWriter
    setTarget = set_target
    getTarget = get_target
    putDatagram = put_datagram
    isError = is_error

class QueuedReturn_ConnectionListenerData:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_max_queue_size(self, max_size: int) -> None: ...
    def get_max_queue_size(self) -> int: ...
    def get_current_queue_size(self) -> int: ...
    def get_overflow_flag(self) -> bool: ...
    def reset_overflow_flag(self) -> None: ...
    setMaxQueueSize = set_max_queue_size
    getMaxQueueSize = get_max_queue_size
    getCurrentQueueSize = get_current_queue_size
    getOverflowFlag = get_overflow_flag
    resetOverflowFlag = reset_overflow_flag

class QueuedConnectionListener(ConnectionListener, QueuedReturn_ConnectionListenerData):
    """This flavor of ConnectionListener will queue up all of the TCP connections
    it established for later detection by the client code.
    """

    def __init__(self, manager: ConnectionManager, num_threads: int) -> None: ...
    def upcast_to_ConnectionListener(self) -> ConnectionListener: ...
    def upcast_to_QueuedReturn_ConnectionListenerData(self) -> QueuedReturn_ConnectionListenerData: ...
    def new_connection_available(self) -> bool:
        """Returns true if a new connection was recently established; the connection
        information may then be retrieved via get_new_connection().
        """
    @overload
    def get_new_connection(self, new_connection: Connection | PointerTo_Connection) -> bool:
        """`(self, new_connection: PointerTo_Connection)`:
        This flavor of get_new_connection() simply returns a new connection,
        assuming the user doesn't care about the rendezvous socket that originated
        it or the address it came from.

        `(self, rendezvous: PointerTo_Connection, address: NetAddress, new_connection: PointerTo_Connection)`:
        If a previous call to new_connection_available() returned true, this
        function will return information about the newly established connection.

        The rendezvous parameter is the particular rendezvous socket this new
        connection originally communicated with; it is provided in case the
        ConnectionListener was monitorind more than one and you care which one it
        was.  The address parameter is the net address of the new client, and
        new_connection is the socket of the newly established connection.

        The return value is true if a connection was successfully returned, or
        false if there was, in fact, no new connection.  (This may happen if there
        are multiple threads accessing the QueuedConnectionListener).
        """
    @overload
    def get_new_connection(
        self,
        rendezvous: Connection | PointerTo_Connection,
        address: NetAddress | Socket_Address,
        new_connection: Connection | PointerTo_Connection,
    ) -> bool: ...
    upcastToConnectionListener = upcast_to_ConnectionListener
    upcastToQueuedReturnConnectionListenerData = upcast_to_QueuedReturn_ConnectionListenerData
    newConnectionAvailable = new_connection_available
    getNewConnection = get_new_connection

class QueuedReturn_PointerTo_Connection:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_max_queue_size(self, max_size: int) -> None: ...
    def get_max_queue_size(self) -> int: ...
    def get_current_queue_size(self) -> int: ...
    def get_overflow_flag(self) -> bool: ...
    def reset_overflow_flag(self) -> None: ...
    setMaxQueueSize = set_max_queue_size
    getMaxQueueSize = get_max_queue_size
    getCurrentQueueSize = get_current_queue_size
    getOverflowFlag = get_overflow_flag
    resetOverflowFlag = reset_overflow_flag

class QueuedConnectionManager(ConnectionManager, QueuedReturn_PointerTo_Connection):
    """This flavor of ConnectionManager will queue up all of the reset-connection
    messages from the ConnectionReaders and ConnectionWriters and report them
    to the client on demand.

    When a reset connection has been discovered via
    reset_connection_available()/get_reset_connection(), it is still the
    responsibility of the client to call close_connection() on that connection
    to free up its resources.
    """

    def upcast_to_ConnectionManager(self) -> ConnectionManager: ...
    def upcast_to_QueuedReturn_PointerTo_Connection(self) -> QueuedReturn_PointerTo_Connection: ...
    def reset_connection_available(self) -> bool:
        """Returns true if one of the readers/writers/listeners reported a connection
        reset recently.  If so, the particular connection that has been reset can
        be extracted via get_reset_connection().

        Only connections which were externally reset are certain to appear in this
        list.  Those which were explicitly closed via a call to close_connection()
        may or may not be reported.  Furthermore, it is the responsibility of the
        caller to subsequently call close_connection() with any connection reported
        reset by this call.  (There is no harm in calling close_connection() more
        than once on a given socket.)
        """
    def get_reset_connection(self, connection: Connection | PointerTo_Connection) -> bool:
        """If a previous call to reset_connection_available() returned true, this
        function will return information about the newly reset connection.

        Only connections which were externally reset are certain to appear in this
        list.  Those which were explicitly closed via a call to close_connection()
        may or may not be reported.  Furthermore, it is the responsibility of the
        caller to subsequently call close_connection() with any connection reported
        reset by this call.  (There is no harm in calling close_connection() more
        than once on a given socket.)

        The return value is true if a connection was successfully returned, or
        false if there was, in fact, no reset connection.  (This may happen if
        there are multiple threads accessing the QueuedConnectionManager).
        """
    upcastToConnectionManager = upcast_to_ConnectionManager
    upcastToQueuedReturnPointerToConnection = upcast_to_QueuedReturn_PointerTo_Connection
    resetConnectionAvailable = reset_connection_available
    getResetConnection = get_reset_connection

class QueuedReturn_NetDatagram:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def set_max_queue_size(self, max_size: int) -> None: ...
    def get_max_queue_size(self) -> int: ...
    def get_current_queue_size(self) -> int: ...
    def get_overflow_flag(self) -> bool: ...
    def reset_overflow_flag(self) -> None: ...
    setMaxQueueSize = set_max_queue_size
    getMaxQueueSize = get_max_queue_size
    getCurrentQueueSize = get_current_queue_size
    getOverflowFlag = get_overflow_flag
    resetOverflowFlag = reset_overflow_flag

class QueuedConnectionReader(ConnectionReader, QueuedReturn_NetDatagram):
    """This flavor of ConnectionReader will read from its sockets and queue up all
    of the datagrams read for later receipt by the client code.  This class is
    useful for client code that doesn't want to deal with threading and is
    willing to poll for datagrams at its convenience.
    """

    def __init__(self, manager: ConnectionManager, num_threads: int) -> None: ...
    def upcast_to_ConnectionReader(self) -> ConnectionReader: ...
    def upcast_to_QueuedReturn_NetDatagram(self) -> QueuedReturn_NetDatagram: ...
    def data_available(self) -> bool:
        """Returns true if a datagram is available on the queue; call get_data() to
        extract the datagram.
        """
    def get_data(self, result: Datagram) -> bool:
        """`(self, result: Datagram)`:
        This flavor of QueuedConnectionReader::get_data(), works like the other,
        except that it only fills a Datagram object, not a NetDatagram object.
        This means that the Datagram cannot be queried for its source Connection
        and/or NetAddress, but it is useful in all other respects.

        `(self, result: NetDatagram)`:
        If a previous call to data_available() returned true, this function will
        return the datagram that has become available.

        The return value is true if a datagram was successfully returned, or false
        if there was, in fact, no datagram available.  (This may happen if there
        are multiple threads accessing the QueuedConnectionReader).
        """
    upcastToConnectionReader = upcast_to_ConnectionReader
    upcastToQueuedReturnNetDatagram = upcast_to_QueuedReturn_NetDatagram
    dataAvailable = data_available
    getData = get_data

class RecentConnectionReader(ConnectionReader):
    """This flavor of ConnectionReader will read from its sockets and retain only
    the single most recent datagram for inspection by client code.  It's useful
    particularly for reading telemetry-type data from UDP sockets where you
    don't care about getting every last socket, and in fact if the sockets are
    coming too fast you'd prefer to skip some of them.

    This class will always create one thread for itself.
    """

    def __init__(self, manager: ConnectionManager) -> None: ...
    def data_available(self) -> bool:
        """Returns true if a datagram is available on the queue; call get_data() to
        extract the datagram.
        """
    def get_data(self, result: Datagram) -> bool:
        """`(self, result: Datagram)`:
        This flavor of RecentConnectionReader::get_data(), works like the other,
        except that it only fills a Datagram object, not a NetDatagram object.
        This means that the Datagram cannot be queried for its source Connection
        and/or NetAddress, but it is useful in all other respects.

        `(self, result: NetDatagram)`:
        If a previous call to data_available() returned true, this function will
        return the datagram that has become available.

        The return value is true if a datagram was successfully returned, or false
        if there was, in fact, no datagram available.  (This may happen if there
        are multiple threads accessing the RecentConnectionReader).
        """
    dataAvailable = data_available
    getData = get_data

PointerToConnection = PointerTo_Connection
PointerToBaseConnection = PointerToBase_Connection
QueuedReturnDatagram = QueuedReturn_Datagram
QueuedReturnConnectionListenerData = QueuedReturn_ConnectionListenerData
QueuedReturnPointerToConnection = QueuedReturn_PointerTo_Connection
QueuedReturnNetDatagram = QueuedReturn_NetDatagram
