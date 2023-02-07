from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d.core._dtoolbase import TypedObject
from panda3d.core._express import Datagram

class Socket_Address:
    """A simple place to store and manipulate tcp and port address for
    communication layer
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, port: int = ...) -> None:
        """Constructor that lets us set a port value"""
    @overload
    def __init__(self, inaddr: Socket_Address) -> None: ...
    def __eq__(self, __in: object) -> bool: ...
    def __ne__(self, __in: object) -> bool: ...
    def __lt__(self, _in: Socket_Address) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_any_IP(self, port: int) -> bool:
        """Set to any address and a specified port"""
    def set_any_IPv6(self, port: int) -> bool:
        """Set to any IPv6 address and a specified port."""
    def set_port(self, port: int) -> bool:
        """Set to a specified port"""
    def set_broadcast(self, port: int) -> bool:
        """Set to the broadcast address and a specified port"""
    @overload
    def set_host(self, hostname: str, port: int = ...) -> bool:
        """`(self, hostname: str)`:
        Initializes the address from a string specifying both the address and port,
        separated by a colon.  An IPv6 address must be enclosed in brackets.

        `(self, hostname: str, port: int)`:
        This function will take a port and string-based TCP address and initialize
        the address with this information.  Returns true on success; on failure, it
        returns false and the address may be undefined.
        """
    @overload
    def set_host(self, ip4addr: int, port: int) -> bool: ...
    def clear(self) -> None:
        """Set the internal values to a suitable known value"""
    def get_family(self) -> int:
        """Returns AF_INET if this is an IPv4 address, or AF_INET6 if this is an IPv6
        address.
        """
    def get_port(self) -> int:
        """Get the port portion as an integer"""
    def get_ip(self) -> str:
        """Return the IP address portion in dot notation string."""
    def get_ip_port(self) -> str:
        """Return the ip address/port in dot notation string.  If this is an IPv6
        address, it will be enclosed in square brackets.
        """
    def GetIPAddressRaw(self) -> int:
        """Returns a raw 32-bit unsigned integer representing the IPv4 address.
        @deprecated  Does not work with IPv6 addresses.
        """
    def is_any(self) -> bool:
        """True if the address is zero."""
    def is_mcast_range(self) -> bool:
        """True if the address is in the multicast range."""
    setAnyIP = set_any_IP
    setAnyIPv6 = set_any_IPv6
    setPort = set_port
    setBroadcast = set_broadcast
    setHost = set_host
    getFamily = get_family
    getPort = get_port
    getIp = get_ip
    getIpPort = get_ip_port
    isAny = is_any
    isMcastRange = is_mcast_range

class Socket_IP(TypedObject):
    """Base functionality for a INET domain Socket This call should be the
    starting point for all other unix domain sockets.

    SocketIP |
    ------------------------------------------------------------------- |
    |                       |                           | SocketTCP
    SocketTCP_Listen    SocketUDP_Incoming   SocketUDP_OutBound
    """

    def __init__(self, _in: int = ...) -> None:
        """`(self)`:
        Def Constructor

        `(self, _in: int)`:
        Assigns an existing socket to this class
        """
    def Close(self) -> None:
        """Closes a socket if it is open (allocated)."""
    @staticmethod
    def GetLastError() -> int:
        """Gets the last errcode from a socket operation."""
    def SetNonBlocking(self) -> int:
        """this function will throw a socket into non-blocking mode"""
    def SetBlocking(self) -> int:
        """Set the socket to block on subsequent calls to socket functions that
        address this socket
        """
    def SetReuseAddress(self, flag: bool = ...) -> bool:
        """Informs a socket to reuse IP address as needed"""
    def SetV6Only(self, flag: bool) -> bool:
        """Sets a flag indicating whether this IPv6 socket should operate in
        dual-stack mode or not.
        """
    def Active(self) -> bool:
        """Ask if the socket is open (allocated)"""
    def SetRecvBufferSize(self, size: int) -> int:
        """Ok it sets the recv buffer size for both tcp and UDP"""
    def SetSocket(self, ins: int) -> None:
        """Assigns an existing socket to this class"""
    def GetSocket(self) -> int:
        """`(self)`:
        Gets the base socket type

        `(self)`:
        Get The RAW file id of the socket
        """
    def GetPeerName(self) -> Socket_Address:
        """Wrapper on berkly getpeername..."""
    @staticmethod
    def InitNetworkDriver() -> int: ...

class Socket_TCP(Socket_IP):
    """Base functionality for a TCP connected socket This class is pretty useless
    by itself but it does hide some of the platform differences from machine to
    machine
    """

    def __init__(self, __param0: int = ...) -> None: ...
    def SetNoDelay(self, flag: bool = ...) -> int:
        """Disable Nagle algorithm.  Don't delay send to coalesce packets"""
    def SetLinger(self, interval_seconds: int = ...) -> int:
        """will control the behavior of SO_LINGER for a TCP socket"""
    def DontLinger(self) -> int:
        """Turn off the linger flag.  The socket will quickly release buffered items
        and free up OS resources.  You may lose a stream if you use this flag and
        do not negotiate the close at the application layer.
        """
    def SetSendBufferSize(self, insize: int) -> int:
        """Just like it sounds.  Sets a buffered socket recv buffer size.  This
        function does not refuse ranges outside hard-coded OS limits
        """
    def ActiveOpen(self, theaddress: Socket_Address, setdelay: bool) -> bool:
        """This function will try and set the socket up for active open to a specified
        address and port provided by the input parameter
        """
    def ActiveOpenNonBlocking(self, theaddress: Socket_Address) -> bool:
        """This function will try and set the socket up for active open to a specified
        address and port provided by the input parameter (non-blocking version)
        """
    def ErrorIs_WouldBlocking(self, err: int) -> bool: ...
    def ShutdownSend(self) -> bool: ...
    def SendData(self, str: str) -> int: ...
    def RecvData(self, max_len: int) -> str:
        """Read the data from the connection - if error 0 if socket closed for read or
        length is 0 + bytes read (May be smaller than requested)
        """
    ErrorIsWouldBlocking = ErrorIs_WouldBlocking

class Socket_TCP_Listen(Socket_IP):
    """Base functionality for a TCP rendezvous socket"""

    def __init__(self) -> None: ...
    @overload
    def OpenForListen(self, address: Socket_Address, backlog_size: int = ...) -> bool:
        """This function will initialize a listening Socket"""
    @overload
    def OpenForListen(self, port: int, backlog_size: int = ...) -> bool: ...
    def GetIncomingConnection(self, newsession: Socket_TCP | int, address: Socket_Address) -> bool: ...

class Socket_UDP_Incoming(Socket_IP):
    """Base functionality for a UDP Reader"""

    def __init__(self) -> None: ...
    @overload
    def OpenForInput(self, address: Socket_Address) -> bool:
        """Starts a UDP socket listening on a port"""
    @overload
    def OpenForInput(self, port: int) -> bool: ...
    def OpenForInputMCast(self, address: Socket_Address) -> bool:
        """Starts a UDP socket listening on a port"""
    def SendTo(self, data: str, len: int, address: Socket_Address) -> bool:
        """Send data to specified address"""
    def InitNoAddress(self) -> bool:
        """Set this socket to work without a bound external address."""
    def SetToBroadCast(self) -> bool:
        """Flips the OS bits that allow for brodcast packets to come in on this port."""

class Socket_UDP_Outgoing(Socket_IP):
    """Base functionality for a UDP sending socket"""

    def __init__(self) -> None: ...
    def InitToAddress(self, address: Socket_Address) -> bool:
        """Connects the Socket to a specified address"""
    def Send(self, data: str) -> bool:
        """Send data to connected address"""
    def InitNoAddress(self) -> bool:
        """use this interface for a none tagreted UDP connection"""
    def SendTo(self, data: str, address: Socket_Address) -> bool:
        """Send data to specified address"""
    def SetToBroadCast(self) -> bool:
        """Ask the OS to let us receive broadcast packets on this port."""

class Socket_fdset:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: Socket_fdset = ...) -> None:
        """The constructor"""
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def setForSocket(self, incon: Socket_IP | int) -> None: ...
    def IsSetFor(self, incon: Socket_IP | int) -> bool:
        """check to see if a socket object has been marked for reading"""
    def WaitForRead(self, zeroFds: bool, sleep_time: int = ...) -> int: ...
    def WaitForWrite(self, zeroFds: bool, sleep_time: int = ...) -> int:
        """This is the function that will wait till one of the sockets is ready for
        writing
        """
    def WaitForError(self, zeroFds: bool, sleep_time: int = ...) -> int:
        """This is the function that will wait till one of the sockets is in error
        state
        """
    def clear(self) -> None:
        """Marks the content as empty"""

class Buffered_DatagramConnection(Socket_TCP):
    """there are 3 states 1. Socket not even assigned,,,, 2. Socket Assigned and
    trying to get a active connect open 3. Socket is open and  writable.. (
    Fully powered up )...
    """

    def __init__(self, rbufsize: int, wbufsize: int, write_flush_point: int) -> None: ...
    def GetMessage(self, val: Datagram) -> bool:
        """Reads a message.  Returns false on failure."""
    def DoConnect(self) -> bool:
        """all the real state magic is in here"""
    def IsConnected(self) -> bool:
        """all the real state magic is in here"""
    def SendMessage(self, msg: Datagram) -> bool:
        """the reason thsi all exists"""
    def Flush(self) -> bool:
        """Flush all writes."""
    def Reset(self) -> None:
        """Reset"""
    def WaitForNetworkReadEvent(self, MaxTime: float) -> None: ...
    def AddressQueueSize(self) -> int:
        """address queue stuff"""
    def AddAddress(self, inadr: Socket_Address) -> None:
        """must be called to set value to the server"""
    def ClearAddresses(self) -> None: ...

class Socket_UDP(Socket_UDP_Incoming):
    """Base functionality for a combination UDP Reader and Writer.  This
    duplicates code from Socket_UDP_Outgoing, to avoid the problems of multiple
    inheritance.
    """

    def InitToAddress(self, address: Socket_Address) -> bool:
        """Connects the socket to a Specified address"""
    def Send(self, data: str) -> bool:
        """Send data to connected address"""
    def SendTo(self, data: str, address: Socket_Address) -> bool:  # type: ignore[override]
        """Send data to specified address"""
    def SetToBroadCast(self) -> bool:
        """Ask the OS to let us receive broadcast packets on this port."""

SocketAddress = Socket_Address
SocketIP = Socket_IP
SocketTCP = Socket_TCP
SocketTCPListen = Socket_TCP_Listen
SocketUDPIncoming = Socket_UDP_Incoming
SocketUDPOutgoing = Socket_UDP_Outgoing
SocketFdset = Socket_fdset
BufferedDatagramConnection = Buffered_DatagramConnection
SocketUDP = Socket_UDP
