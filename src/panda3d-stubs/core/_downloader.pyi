from _typeshed import StrOrBytesPath
from collections.abc import Iterator
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import URL
from panda3d.core._dtoolutil import iostream, istream, ostream
from panda3d.core._express import (
    Buffer,
    Datagram,
    HashVal,
    Ramfile,
    ReferenceCount,
    TypedReferenceCount,
    VirtualFile,
    VirtualFileMount,
)

_ISocketStream_ReadState: TypeAlias = Literal[0, 1, 2, 3]
_HTTPEnum_HTTPVersion: TypeAlias = Literal[0, 1, 2, 3]
_HTTPClient_VerifySSL: TypeAlias = Literal[0, 1, 2]
_DocumentSpec_RequestMode: TypeAlias = Literal[0, 1, 2, 3]
_DocumentSpec_CacheControl: TypeAlias = Literal[0, 1, 2]

class SSReader:
    """An internal class for reading from a socket stream.  This serves as a base
    class for both ISocketStream and SocketStream; its purpose is to minimize
    redundant code between them.  Do not use it directly.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def receive_datagram(self, dg: Datagram) -> bool:
        """Receives a datagram over the socket by expecting a little-endian 16-bit
        byte count as a prefix.  If the socket stream is non-blocking, may return
        false if the data is not available; otherwise, returns false only if the
        socket closes.
        """
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    def set_tcp_header_size(self, tcp_header_size: int) -> None:
        """Sets the header size for datagrams.  At the present, legal values for this
        are 0, 2, or 4; this specifies the number of bytes to use encode the
        datagram length at the start of each TCP datagram.  Sender and receiver
        must independently agree on this.
        """
    def get_tcp_header_size(self) -> int:
        """Returns the header size for datagrams.  See set_tcp_header_size()."""
    receiveDatagram = receive_datagram
    isClosed = is_closed
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size

class SSWriter:
    """An internal class for writing to a socket stream.  This serves as a base
    class for both OSocketStream and SocketStream; its purpose is to minimize
    redundant code between them.  Do not use it directly.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def send_datagram(self, dg: Datagram) -> bool:
        """Transmits the indicated datagram over the socket by prepending it with a
        little-endian 16-bit byte count.  Does not return until the data is sent or
        the connection is closed, even if the socket stream is non-blocking.
        """
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
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
    def set_tcp_header_size(self, tcp_header_size: int) -> None:
        """Sets the header size for datagrams.  At the present, legal values for this
        are 0, 2, or 4; this specifies the number of bytes to use encode the
        datagram length at the start of each TCP datagram.  Sender and receiver
        must independently agree on this.
        """
    def get_tcp_header_size(self) -> int:
        """Returns the header size for datagrams.  See set_tcp_header_size()."""
    def consider_flush(self) -> bool:
        """Sends the most recently queued data if enough time has elapsed.  This only
        has meaning if set_collect_tcp() has been set to true.
        """
    def flush(self) -> bool:
        """Sends the most recently queued data now.  This only has meaning if
        set_collect_tcp() has been set to true.
        """
    sendDatagram = send_datagram
    isClosed = is_closed
    setCollectTcp = set_collect_tcp
    getCollectTcp = get_collect_tcp
    setCollectTcpInterval = set_collect_tcp_interval
    getCollectTcpInterval = get_collect_tcp_interval
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size
    considerFlush = consider_flush

class ISocketStream(istream, SSReader):
    """This is a base class for istreams implemented in Panda that read from a
    (possibly non-blocking) socket.  It adds is_closed(), which can be called
    after an eof condition to check whether the socket has been closed, or
    whether more data may be available later.
    """

    RS_initial: Final = 0
    RSInitial: Final = 0
    RS_reading: Final = 1
    RSReading: Final = 1
    RS_complete: Final = 2
    RSComplete: Final = 2
    RS_error: Final = 3
    RSError: Final = 3
    def upcast_to_istream(self) -> istream: ...
    def upcast_to_SSReader(self) -> SSReader: ...
    def get_read_state(self) -> _ISocketStream_ReadState: ...
    upcastToIstream = upcast_to_istream
    upcastToSSReader = upcast_to_SSReader
    getReadState = get_read_state

class OSocketStream(ostream, SSWriter):
    """A base class for ostreams that write to a (possibly non-blocking) socket.
    It adds is_closed(), which can be called after any write operation fails to
    check whether the socket has been closed, or whether more data may be sent
    later.
    """

    def upcast_to_ostream(self) -> ostream: ...
    def upcast_to_SSWriter(self) -> SSWriter: ...
    def flush(self) -> bool:  # type: ignore[override]
        """Sends the most recently queued data now.  This only has meaning if
        set_collect_tcp() has been set to true.
        """
    upcastToOstream = upcast_to_ostream
    upcastToSSWriter = upcast_to_SSWriter

class SocketStream(iostream, SSReader, SSWriter):  # type: ignore[misc]
    """A base class for iostreams that read and write to a (possibly non-blocking)
    socket.
    """

    def upcast_to_iostream(self) -> iostream: ...
    def upcast_to_SSReader(self) -> SSReader: ...
    def upcast_to_SSWriter(self) -> SSWriter: ...
    def flush(self) -> bool:  # type: ignore[override]
        """Sends the most recently queued data now.  This only has meaning if
        set_collect_tcp() has been set to true.
        """
    upcastToIostream = upcast_to_iostream
    upcastToSSReader = upcast_to_SSReader
    upcastToSSWriter = upcast_to_SSWriter

class URLSpec:
    """A container for a URL, e.g.  "http://server:port/path".

    The URLSpec object is similar to a Filename in that it contains logic to
    identify the various parts of a URL and return (or modify) them separately.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    scheme: str
    authority: str
    username: str
    server: str
    port: int
    server_and_port: str
    path: str
    query: str
    @property
    def ssl(self) -> bool: ...
    @overload
    def __init__(self, __param0: URLSpec = ...) -> None:
        """Creates a URLSpec by appending a path to the end of the old URLSpec,
        inserting an intervening forward slash if necessary.
        """
    @overload
    def __init__(self, url: str, server_name_expected: bool = ...) -> None: ...
    @overload
    def __init__(self, url: URL, path: StrOrBytesPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: URL) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> str: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def __iter__(self) -> Iterator[str]: ...  # Doesn't actually exist
    def assign(self, url: str) -> Self: ...
    def compare_to(self, other: URL) -> int:
        """Returns a number less than zero if this URLSpec sorts before the other one,
        greater than zero if it sorts after, or zero if they are equivalent.
        """
    def get_hash(self) -> int: ...
    def has_scheme(self) -> bool:
        """Returns true if the URL specifies a scheme (e.g.  "http:"), false
        otherwise.
        """
    def has_authority(self) -> bool:
        """Returns true if the URL specifies an authority (this includes username,
        server, and/or port), false otherwise.
        """
    def has_username(self) -> bool:
        """Returns true if the URL specifies a username (and/or password), false
        otherwise.
        """
    def has_server(self) -> bool:
        """Returns true if the URL specifies a server name, false otherwise."""
    def has_port(self) -> bool:
        """Returns true if the URL specifies a port number, false otherwise."""
    def has_path(self) -> bool:
        """Returns true if the URL includes a path specification (that is, the
        particular filename on the server to retrieve), false otherwise.
        """
    def has_query(self) -> bool:
        """Returns true if the URL includes a query specification, false otherwise."""
    def get_scheme(self) -> str:
        """Returns the scheme specified by the URL, or empty string if no scheme is
        specified.
        """
    def get_authority(self) -> str:
        """Returns the authority specified by the URL (this includes username, server,
        and/or port), or empty string if no authority is specified.
        """
    def get_username(self) -> str:
        """Returns the username specified by the URL, if any.  This might also include
        a password, e.g.  "username:password", although putting a password on the
        URL is probably a bad idea.
        """
    def get_server(self) -> str:
        """Returns the server name specified by the URL, if any.  In case of an IPv6
        address, does not include the enclosing brackets.
        """
    def get_port_str(self) -> str:
        """Returns the port specified by the URL as a string, or the empty string if
        no port is specified.  Compare this with get_port(), which returns a
        default port number if no port is specified.
        """
    def get_port(self) -> int:
        """Returns the port number specified by the URL, or the default port if not
        specified.
        """
    def get_server_and_port(self) -> str:
        """Returns a string consisting of the server name, followed by a colon,
        followed by the port number.  If the port number is not explicitly given in
        the URL, this string will include the implicit port number.
        If the server is an IPv6 address, it will be enclosed in square brackets.
        """
    def is_default_port(self) -> bool:
        """Returns true if the port number encoded in this URL is the default port
        number for the scheme (or if there is no port number), or false if it is a
        nonstandard port.
        """
    @staticmethod
    def get_default_port_for_scheme(scheme: str) -> int:
        """Returns the default port number for the indicated scheme, or 0 if there is
        no known default.
        """
    def get_path(self) -> str:
        """Returns the path specified by the URL, or "/" if no path is specified."""
    def get_query(self) -> str:
        """Returns the query specified by the URL, or empty string if no query is
        specified.
        """
    def get_path_and_query(self) -> str:
        """Returns the path (or "/" if no path is specified), followed by the query if
        it is specified.
        """
    def is_ssl(self) -> bool:
        """Returns true if the URL's scheme specifies an SSL-secured protocol such as
        https, or false otherwise.
        """
    def get_url(self) -> str:
        """Returns the complete URL specification."""
    def set_scheme(self, scheme: str) -> None:
        """Replaces the scheme part of the URL specification."""
    def set_authority(self, authority: str) -> None:
        """Replaces the authority part of the URL specification.  This includes the
        username, server, and port.
        """
    def set_username(self, username: str) -> None:
        """Replaces the username part of the URL specification."""
    def set_server(self, server: str) -> None:
        """Replaces the server part of the URL specification.
        Unlike set_server_and_port, this method does not require IPv6 addresses to
        be enclosed in square brackets.
        """
    def set_port(self, port: int | str) -> None:
        """`(self, port: str)`:
        Replaces the port part of the URL specification.

        `(self, port: int)`:
        Replaces the port part of the URL specification, given a numeric port
        number.
        """
    def set_server_and_port(self, server_and_port: str) -> None:
        """Replaces the server and port parts of the URL specification simultaneously.
        The input string should be of the form "server:port", or just "server" to
        make the port number implicit.
        Any IPv6 address must be enclosed in square brackets.
        """
    def set_path(self, path: str) -> None:
        """Replaces the path part of the URL specification."""
    def set_query(self, query: str) -> None:
        """Replaces the query part of the URL specification."""
    def set_url(self, url: str, server_name_expected: bool = ...) -> None:
        """Completely replaces the URL with the indicated string.  If
        server_name_expected is true, it is a hint that an undecorated URL is
        probably a server name, not a local filename.
        """
    def c_str(self) -> str: ...
    def empty(self) -> bool:
        """Returns false if the URLSpec is valid (not empty), or true if it is an
        empty string.
        """
    def length(self) -> int: ...
    def input(self, _in: istream) -> bool: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def quote(source: str, safe: str = ...) -> str:
        """Returns the source string with all "unsafe" characters quoted, making a
        string suitable for placing in a URL.  Letters, digits, and the underscore,
        comma, period, and hyphen characters, as well as any included in the safe
        string, are left alone; all others are converted to hex representation.
        """
    @staticmethod
    def quote_plus(source: str, safe: str = ...) -> str:
        """Behaves like quote() with the additional behavior of replacing spaces with
        plus signs.
        """
    @staticmethod
    def unquote(source: str) -> str:
        """Reverses the operation of quote(): converts escaped characters of the form
        "%xx" to their ascii equivalent.
        """
    @staticmethod
    def unquote_plus(source: str) -> str:
        """Reverses the operation of quote_plus(): converts escaped characters of the
        form "%xx" to their ascii equivalent, and also converts plus signs to
        spaces.
        """
    compareTo = compare_to
    getHash = get_hash
    hasScheme = has_scheme
    hasAuthority = has_authority
    hasUsername = has_username
    hasServer = has_server
    hasPort = has_port
    hasPath = has_path
    hasQuery = has_query
    getScheme = get_scheme
    getAuthority = get_authority
    getUsername = get_username
    getServer = get_server
    getPortStr = get_port_str
    getPort = get_port
    getServerAndPort = get_server_and_port
    isDefaultPort = is_default_port
    getDefaultPortForScheme = get_default_port_for_scheme
    getPath = get_path
    getQuery = get_query
    getPathAndQuery = get_path_and_query
    isSsl = is_ssl
    getUrl = get_url
    setScheme = set_scheme
    setAuthority = set_authority
    setUsername = set_username
    setServer = set_server
    setPort = set_port
    setServerAndPort = set_server_and_port
    setPath = set_path
    setQuery = set_query
    setUrl = set_url
    cStr = c_str
    quotePlus = quote_plus
    unquotePlus = unquote_plus

class HTTPEnum:
    """This class is just used as a namespace wrapper for some of the enumerated
    types used by various classes within the HTTPClient family.
    """

    HV_09: Final = 0
    HV09: Final = 0
    HV_10: Final = 1
    HV10: Final = 1
    HV_11: Final = 2
    HV11: Final = 2
    HV_other: Final = 3
    HVOther: Final = 3
    M_options: Final = 0
    MOptions: Final = 0
    M_get: Final = 1
    MGet: Final = 1
    M_head: Final = 2
    MHead: Final = 2
    M_post: Final = 3
    MPost: Final = 3
    M_put: Final = 4
    MPut: Final = 4
    M_delete: Final = 5
    MDelete: Final = 5
    M_trace: Final = 6
    MTrace: Final = 6
    M_connect: Final = 7
    MConnect: Final = 7
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: HTTPEnum = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class HTTPDate:
    """A container for an HTTP-legal time/date indication.  This can accept a
    string from an HTTP header and will decode it into a C time_t value;
    conversely, it can accept a time_t value and encode it for output as a
    string.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: HTTPDate = ...) -> None:
        """Decodes the string into a sensible date.  Returns 0 (!is_valid()) if the
        string cannot be correctly decoded.
        """
    @overload
    def __init__(self, format: str) -> None: ...
    @overload
    def __init__(self, time: int) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: HTTPDate | int | str) -> bool: ...
    def __gt__(self, other: HTTPDate | int | str) -> bool: ...
    def __iadd__(self, seconds: int) -> Self: ...
    def __isub__(self, seconds: int) -> Self: ...  # type: ignore[misc]
    def __add__(self, seconds: int) -> HTTPDate: ...
    @overload
    def __sub__(self, other: HTTPDate | str) -> int: ...
    @overload
    def __sub__(self, seconds: int) -> HTTPDate: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: HTTPDate | int | str) -> Self: ...
    @staticmethod
    def now() -> HTTPDate:
        """Returns an HTTPDate that represents the current time and date."""
    def is_valid(self) -> bool:
        """Returns true if the date is meaningful, or false if it is -1 (which
        generally indicates the source string could not be parsed.)
        """
    def get_string(self) -> str: ...
    def get_time(self) -> int:
        """Returns the date as a C time_t value."""
    def compare_to(self, other: HTTPDate | int | str) -> int:
        """Returns a number less than zero if this HTTPDate sorts before the other
        one, greater than zero if it sorts after, or zero if they are equivalent.
        """
    def input(self, _in: istream) -> bool: ...
    def output(self, out: ostream) -> None: ...
    isValid = is_valid
    getString = get_string
    getTime = get_time
    compareTo = compare_to

class HTTPCookie:
    """A cookie sent from an HTTP server to be stored on the client and returned
    when the path and/or domain matches.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    name: str
    value: str
    domain: str
    path: str
    expires: HTTPDate
    secure: bool
    @overload
    def __init__(self, __param0: HTTPCookie = ...) -> None:
        """`(self)`:
        Constructs an empty cookie.

        `(self, format: str, url: URLSpec)`:
        Constructs a cookie according to the indicated string, presumably the tag
        of a Set-Cookie header.  There is no way to detect a formatting error in
        the string with this constructor.

        `(self, name: str, path: str, domain: str)`:
        Constructs a cookie with the indicated name, path, and domain values, but
        no other data.  This is most useful for looking up an existing cookie in
        the HTTPClient.
        """
    @overload
    def __init__(self, format: str, url: URL) -> None: ...
    @overload
    def __init__(self, name: str, path: str, domain: str) -> None: ...
    def __lt__(self, other: HTTPCookie) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_name(self, name: str) -> None: ...
    def get_name(self) -> str:
        """Returns the name of the cookie.  This is the key value specified by the
        server.
        """
    def set_value(self, value: str) -> None: ...
    def get_value(self) -> str:
        """Returns the value of the cookie.  This is the arbitrary string associated
        with the cookie's name, as specified by the server.
        """
    def set_domain(self, domain: str) -> None: ...
    def get_domain(self) -> str: ...
    def set_path(self, path: str) -> None: ...
    def get_path(self) -> str:
        """Returns the prefix of the URL paths on the server for which this cookie
        will be sent.
        """
    def set_expires(self, expires: HTTPDate | int | str) -> None: ...
    def clear_expires(self) -> None:
        """Removes the expiration date on the cookie."""
    def has_expires(self) -> bool:
        """Returns true if the cookie has an expiration date, false otherwise."""
    def get_expires(self) -> HTTPDate:
        """Returns the expiration date of the cookie if it is set, or an invalid date
        if it is not.
        """
    def set_secure(self, flag: bool) -> None: ...
    def get_secure(self) -> bool:
        """Returns true if the server has indicated this is a "secure" cookie which
        should only be sent over an HTTPS channel.
        """
    def update_from(self, other: HTTPCookie) -> None:
        """Assuming the operator < method, above, has already evaluated these two
        cookies as equal, then assign the remaining values (value, expiration date,
        secure flag) from the indicated cookie.  This is guaranteed not to change
        the ordering of the cookie in a set, and so can be used to update an
        existing cookie within a set with new values.
        """
    def parse_set_cookie(self, format: str, url: URL) -> bool:
        """Separates out the parameter/value pairs of the Set-Cookie header and
        assigns the values of the cookie appropriate.  Returns true if the header
        is parsed correctly, false if something is not understood.
        """
    def is_expired(self, now: HTTPDate | int | str = ...) -> bool:
        """Returns true if the cookie's expiration date is before the indicated date,
        false otherwise.
        """
    def matches_url(self, url: URL) -> bool:
        """Returns true if the cookie is appropriate to send with the indicated URL
        request, false otherwise.
        """
    def output(self, out: ostream) -> None: ...
    setName = set_name
    getName = get_name
    setValue = set_value
    getValue = get_value
    setDomain = set_domain
    getDomain = get_domain
    setPath = set_path
    getPath = get_path
    setExpires = set_expires
    clearExpires = clear_expires
    hasExpires = has_expires
    getExpires = get_expires
    setSecure = set_secure
    getSecure = get_secure
    updateFrom = update_from
    parseSetCookie = parse_set_cookie
    isExpired = is_expired
    matchesUrl = matches_url

class HTTPClient(ReferenceCount):
    """Handles contacting an HTTP server and retrieving a document.  Each
    HTTPClient object represents a separate context, and stores its own list of
    cookies, passwords, and certificates; however, a given HTTPClient is
    capable of making multiple simultaneous requests to the same or different
    servers.

    It is up to the programmer whether one HTTPClient should be used to
    retrieve all documents, or a separate one should be created each time.
    There is a default, global HTTPClient available in
    HTTPClient::get_global_ptr().
    """

    VS_no_verify: Final = 0
    VSNoVerify: Final = 0
    VS_no_date_check: Final = 1
    VSNoDateCheck: Final = 1
    VS_normal: Final = 2
    VSNormal: Final = 2
    def __init__(self, copy: HTTPClient = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    @staticmethod
    def init_random_seed() -> None:
        """This may be called once, presumably at the beginning of an application, to
        initialize OpenSSL's random seed.  On Windows, it is particularly important
        to call this at startup if you are going to be performing any https
        operations or otherwise use encryption, since the Windows algorithm for
        getting a random seed takes 2-3 seconds at startup, but can take 30 seconds
        or more after you have opened a 3-D graphics window and started rendering.

        There is no harm in calling this method multiple times, or in not calling
        it at all.
        """
    def set_proxy_spec(self, proxy_spec: str) -> None:
        """Specifies the complete set of proxies to use for all schemes.  This is
        either a semicolon-delimited set of hostname:ports, or a semicolon-
        delimited set of pairs of the form "scheme=hostname:port", or a
        combination.  Use the keyword DIRECT, or an empty string, to represent a
        direct connection.  A particular scheme and/or proxy host may be listed
        more than once.  This is a convenience function that can be used in place
        of explicit calls to add_proxy() for each scheme/proxy pair.
        """
    def get_proxy_spec(self) -> str:
        """Returns the complete set of proxies to use for all schemes.  This is a
        string of the form specified by set_proxy_spec(), above.  Note that the
        string returned by this function may not be exactly the same as the string
        passed into set_proxy_spec(), since the string is regenerated from the
        internal storage structures and may therefore be reordered.
        """
    def set_direct_host_spec(self, direct_host_spec: str) -> None:
        """Specifies the set of hosts that should be connected to directly, without
        using a proxy.  This is a semicolon-separated list of hostnames that may
        contain wildcard characters ("*").
        """
    def get_direct_host_spec(self) -> str:
        """Returns the set of hosts that should be connected to directly, without
        using a proxy, as a semicolon-separated list of hostnames that may contain
        wildcard characters ("*").
        """
    def set_try_all_direct(self, try_all_direct: bool) -> None:
        """If this is set true, then after a connection attempt through a proxy fails,
        we always try a direct connection, regardless of whether the host is listed
        on the direct_host_spec list.  If this is false, a direct attempt is not
        made when we have a proxy in effect, even if the proxy fails.
        """
    def get_try_all_direct(self) -> bool:
        """Returns whether a failed connection through a proxy will be followed up by
        a direct connection attempt, false otherwise.
        """
    def clear_proxy(self) -> None:
        """Resets the proxy spec to empty.  Subsequent calls to add_proxy() may be
        made to build up the set of proxy servers.
        """
    def add_proxy(self, scheme: str, proxy: URL) -> None:
        """Adds the indicated proxy host as a proxy for communications on the given
        scheme.  Usually the scheme is "http" or "https".  It may be the empty
        string to indicate a general proxy.  The proxy string may be the empty URL
        to indicate a direct connection.
        """
    def clear_direct_host(self) -> None:
        """Resets the set of direct hosts to empty.  Subsequent calls to
        add_direct_host() may be made to build up the list of hosts that do not
        require a proxy connection.
        """
    def add_direct_host(self, hostname: str) -> None:
        """Adds the indicated name to the set of hostnames that are connected to
        directly, without using a proxy.  This name may be either a DNS name or an
        IP address, and it may include the * as a wildcard character.
        """
    def get_proxies_for_url(self, url: URL) -> str:
        """Returns a semicolon-delimited list of proxies, in the order in which they
        should be tried, that are appropriate for the indicated URL.  The keyword
        DIRECT indicates a direct connection should be tried.
        """
    def set_username(self, server: str, realm: str, username: str) -> None:
        """Specifies the username:password string corresponding to a particular server
        and/or realm, when demanded by the server.  Either or both of the server or
        realm may be empty; if so, they match anything.  Also, the server may be
        set to the special string `"*proxy"`, which will match any proxy server.

        If the username is set to the empty string, this clears the password for
        the particular server/realm pair.
        """
    def get_username(self, server: str, realm: str) -> str:
        """Returns the username:password string set for this server/realm pair, or
        empty string if nothing has been set.  See set_username().
        """
    def set_cookie(self, cookie: HTTPCookie) -> None:
        """Stores the indicated cookie in the client's list of cookies, as if it had
        been received from a server.
        """
    def clear_cookie(self, cookie: HTTPCookie) -> bool:
        """Removes the cookie with the matching domain/path/name from the client's
        list of cookies.  Returns true if it was removed, false if the cookie was
        not matched.
        """
    def clear_all_cookies(self) -> None:
        """Removes the all stored cookies from the client."""
    def has_cookie(self, cookie: HTTPCookie) -> bool:
        """Returns true if there is a cookie in the client matching the given cookie's
        domain/path/name, false otherwise.
        """
    def get_cookie(self, cookie: HTTPCookie) -> HTTPCookie:
        """Looks up and returns the cookie in the client matching the given cookie's
        domain/path/name.  If there is no matching cookie, returns an empty cookie.
        """
    def copy_cookies_from(self, other: HTTPClient) -> None:
        """Copies all the cookies from the indicated HTTPClient into this one.
        Existing cookies in this client are not affected, unless they are shadowed
        by the new cookies.
        """
    def write_cookies(self, out: ostream) -> None:
        """Outputs the complete list of cookies stored on the client, for all domains,
        including the expired cookies (which will normally not be sent back to a
        host).
        """
    def send_cookies(self, out: ostream, url: URL) -> None:
        """Writes to the indicated ostream a "Cookie" header line for sending the
        cookies appropriate to the indicated URL along with an HTTP request.  This
        also removes expired cookies.
        """
    def set_client_certificate_filename(self, filename: StrOrBytesPath) -> None:
        """Sets the filename of the pem-formatted file that will be read for the
        client public and private keys if an SSL server requests a certificate.
        Either this or set_client_certificate_pem() may be used to specify a client
        certificate.
        """
    def set_client_certificate_pem(self, pem: str) -> None:
        """Sets the pem-formatted contents of the certificate that will be parsed for
        the client public and private keys if an SSL server requests a certificate.
        Either this or set_client_certificate_filename() may be used to specify a
        client certificate.
        """
    def set_client_certificate_passphrase(self, passphrase: str) -> None:
        """Sets the passphrase used to decrypt the private key in the certificate
        named by set_client_certificate_filename() or set_client_certificate_pem().
        """
    def load_client_certificate(self) -> bool:
        """Attempts to load the certificate named by set_client_certificate_filename()
        immediately, and returns true if successful, false otherwise.

        Normally this need not be explicitly called, since it will be called
        automatically if the server requests a certificate, but it may be useful to
        determine ahead of time if the certificate can be loaded correctly.
        """
    def add_preapproved_server_certificate_filename(self, url: URL, filename: StrOrBytesPath) -> bool:
        """Adds the certificate defined in the indicated PEM filename as a "pre-
        approved" certificate for the indicated server, defined by the hostname and
        port (only) from the given URL.

        If the server offers this particular certificate on a secure connection, it
        will be accepted without question.  This is particularly useful for
        communicating with a server using a known self-signed certificate.

        See also the similar add_preapproved_server_certificate_pem(), and the
        weaker add_preapproved_server_certificate_name().
        """
    def add_preapproved_server_certificate_pem(self, url: URL, pem: str) -> bool:
        """Adds the certificate defined in the indicated data string, formatted as a
        PEM block, as a "pre-approved" certificate for the indicated server,
        defined by the hostname and port (only) from the given URL.

        If the server offers this particular certificate on a secure connection, it
        will be accepted without question.  This is particularly useful for
        communicating with a server using a known self-signed certificate.

        See also the similar add_preapproved_server_certificate_filename(), and the
        weaker add_preapproved_server_certificate_name().
        """
    def add_preapproved_server_certificate_name(self, url: URL, name: str) -> bool:
        """Adds the certificate *name* only, as a "pre-approved" certificate name for
        the indicated server, defined by the hostname and port (only) from the
        given URL.

        This is a weaker function than
        add_preapproved_server_certificate_filename().  This checks only the
        subject name of the certificate, without checking for a particular
        certificate by key.  This means that a variety of server certificates may
        match the indicated name.

        Because this is a weaker verification, it only applies to server
        certificates that are signed by a recognized certificate authority.  Thus,
        it cannot be used to pre-approve self-signed certificates, but it can be
        used to accept a server certificate offered by a different hostname than
        the one in the cert itself.

        The certificate name should be formatted in the form
        type0=value0/type1=value1/type2=...
        """
    def clear_preapproved_server_certificates(self, url: URL) -> None:
        """Removes all preapproved server certificates for the indicated server and
        port.
        """
    def clear_all_preapproved_server_certificates(self) -> None:
        """Removes all preapproved server certificates for all servers."""
    def set_http_version(self, version: _HTTPEnum_HTTPVersion) -> None:
        """Specifies the version of HTTP that the client uses to identify itself to
        the server.  The default is HV_11, or HTTP 1.0; you can set this to HV_10
        (HTTP 1.0) to request the server use the older interface.
        """
    def get_http_version(self) -> _HTTPEnum_HTTPVersion:
        """Returns the client's current setting for HTTP version.  See
        set_http_version().
        """
    def get_http_version_string(self) -> str:
        """Returns the current HTTP version setting as a string, e.g.  "HTTP/1.0" or
        "HTTP/1.1".
        """
    @staticmethod
    def parse_http_version_string(version: str) -> _HTTPEnum_HTTPVersion:
        """Matches the string representing a particular HTTP version against any of
        the known versions and returns the appropriate enumerated value, or
        HV_other if the version is unknown.
        """
    def load_certificates(self, filename: StrOrBytesPath) -> bool:
        """Reads the certificate(s) (delimited by -----BEGIN CERTIFICATE----- and
        -----END CERTIFICATE-----) from the indicated file and makes them known as
        trusted public keys for validating future connections.  Returns true on
        success, false otherwise.
        """
    def set_verify_ssl(self, verify_ssl: _HTTPClient_VerifySSL) -> None:
        """Specifies whether the client will insist on verifying the identity of the
        servers it connects to via SSL (that is, https).

        The parameter value is an enumerated type which indicates the level of
        security to which the client will insist upon.
        """
    def get_verify_ssl(self) -> _HTTPClient_VerifySSL:
        """Returns whether the client will insist on verifying the identity of the
        servers it connects to via SSL (that is, https).  See set_verify_ssl().
        """
    def set_cipher_list(self, cipher_list: str) -> None:
        """Specifies the set of ciphers that are to be made available for SSL
        connections.  This is a string as described in the ciphers(1) man page of
        the OpenSSL documentation (or see
        https://www.openssl.org/docs/man1.1.1/man1/ciphers.html ).  If this isn't
        specified, the default is provided by the Config file.  You may also specify
        "DEFAULT" to use the built-in OpenSSL default value.
        """
    def get_cipher_list(self) -> str:
        """Returns the set of ciphers as set by set_cipher_list().  See
        set_cipher_list().
        """
    def make_channel(self, persistent_connection: bool) -> HTTPChannel:
        """Returns a new HTTPChannel object that may be used for reading multiple
        documents using the same connection, for greater network efficiency than
        calling HTTPClient::get_document() repeatedly (which would force a new
        connection for each document).

        Also, HTTPChannel has some additional, less common interface methods than
        the basic interface methods that exist on HTTPClient; if you wish to call
        any of these methods you must first obtain an HTTPChannel.

        Pass true for persistent_connection to gain this network efficiency.  If,
        on the other hand, your intention is to use the channel to retrieve only
        one document, then pass false to inform the server that we will be dropping
        the connection after the first document.
        """
    def post_form(self, url: URL, body: str) -> HTTPChannel:
        """Posts form data to a particular URL and retrieves the response.  Returns a
        new HTTPChannel object whether the document is successfully read or not;
        you can test is_valid() and get_return_code() to determine whether the
        document was retrieved.
        """
    def get_document(self, url: URL) -> HTTPChannel:
        """Opens the named document for reading.  Returns a new HTTPChannel object
        whether the document is successfully read or not; you can test is_valid()
        and get_return_code() to determine whether the document was retrieved.
        """
    def get_header(self, url: URL) -> HTTPChannel:
        """Like get_document(), except only the header associated with the document is
        retrieved.  This may be used to test for existence of the document; it
        might also return the size of the document (if the server gives us this
        information).
        """
    @staticmethod
    def base64_encode(s: str) -> str:
        """Implements HTTPAuthorization::base64_encode().  This is provided here just
        as a convenient place to publish it for access by the scripting language;
        C++ code should probably use HTTPAuthorization directly.
        """
    @staticmethod
    def base64_decode(s: str) -> str:
        """Implements HTTPAuthorization::base64_decode().  This is provided here just
        as a convenient place to publish it for access by the scripting language;
        C++ code should probably use HTTPAuthorization directly.
        """
    @staticmethod
    def get_global_ptr() -> HTTPClient:
        """Returns the default global HTTPClient."""
    initRandomSeed = init_random_seed
    setProxySpec = set_proxy_spec
    getProxySpec = get_proxy_spec
    setDirectHostSpec = set_direct_host_spec
    getDirectHostSpec = get_direct_host_spec
    setTryAllDirect = set_try_all_direct
    getTryAllDirect = get_try_all_direct
    clearProxy = clear_proxy
    addProxy = add_proxy
    clearDirectHost = clear_direct_host
    addDirectHost = add_direct_host
    getProxiesForUrl = get_proxies_for_url
    setUsername = set_username
    getUsername = get_username
    setCookie = set_cookie
    clearCookie = clear_cookie
    clearAllCookies = clear_all_cookies
    hasCookie = has_cookie
    getCookie = get_cookie
    copyCookiesFrom = copy_cookies_from
    writeCookies = write_cookies
    sendCookies = send_cookies
    setClientCertificateFilename = set_client_certificate_filename
    setClientCertificatePem = set_client_certificate_pem
    setClientCertificatePassphrase = set_client_certificate_passphrase
    loadClientCertificate = load_client_certificate
    addPreapprovedServerCertificateFilename = add_preapproved_server_certificate_filename
    addPreapprovedServerCertificatePem = add_preapproved_server_certificate_pem
    addPreapprovedServerCertificateName = add_preapproved_server_certificate_name
    clearPreapprovedServerCertificates = clear_preapproved_server_certificates
    clearAllPreapprovedServerCertificates = clear_all_preapproved_server_certificates
    setHttpVersion = set_http_version
    getHttpVersion = get_http_version
    getHttpVersionString = get_http_version_string
    parseHttpVersionString = parse_http_version_string
    loadCertificates = load_certificates
    setVerifySsl = set_verify_ssl
    getVerifySsl = get_verify_ssl
    setCipherList = set_cipher_list
    getCipherList = get_cipher_list
    makeChannel = make_channel
    postForm = post_form
    getDocument = get_document
    getHeader = get_header
    base64Encode = base64_encode
    base64Decode = base64_decode
    getGlobalPtr = get_global_ptr

class HTTPEntityTag:
    """A container for an "entity tag" from an HTTP server.  This is used to
    identify a particular version of a document or resource, particularly
    useful for verifying caches.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, copy: HTTPEntityTag = ...) -> None:
        """`(self, weak: bool, tag: str)`:
        This constructor accepts an explicit weak flag and a literal (not quoted)
        tag string.

        `(self, text: str)`:
        This constructor accepts a string as formatted from an HTTP server (e.g.
        the tag is quoted, with an optional W/ prefix.)
        """
    @overload
    def __init__(self, text: str) -> None: ...
    @overload
    def __init__(self, weak: bool, tag: str) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: HTTPEntityTag | str) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: HTTPEntityTag | str) -> Self: ...
    def is_weak(self) -> bool:
        """Returns true if the entity tag is marked as "weak". A consistent weak
        entity tag does not guarantee that its resource has not changed in any way,
        but it does promise that the resource has not changed in any semantically
        meaningful way.
        """
    def get_tag(self) -> str:
        """Returns the tag as a literal string."""
    def get_string(self) -> str:
        """Returns the entity tag formatted for sending to an HTTP server (the tag is
        quoted, with a conditional W prefix).
        """
    def strong_equiv(self, other: HTTPEntityTag | str) -> bool:
        """Returns true if the two tags have "strong" equivalence: they are the same
        tag, and both are "strong".
        """
    def weak_equiv(self, other: HTTPEntityTag | str) -> bool:
        """Returns true if the two tags have "weak" equivalence: they are the same
        tag, and one or both may be "weak".
        """
    def compare_to(self, other: HTTPEntityTag | str) -> int:
        """Returns a number less than zero if this HTTPEntityTag sorts before the
        other one, greater than zero if it sorts after, or zero if they are
        equivalent.
        """
    def output(self, out: ostream) -> None: ...
    isWeak = is_weak
    getTag = get_tag
    getString = get_string
    strongEquiv = strong_equiv
    weakEquiv = weak_equiv
    compareTo = compare_to

class DocumentSpec:
    """A descriptor that refers to a particular version of a document.  This
    includes the URL of the document and its identity tag and last-modified
    dates.

    The DocumentSpec may also be used to request a newer document than a
    particular one if available, for instance to refresh a cached document.
    """

    RM_any: Final = 0
    RMAny: Final = 0
    RM_equal: Final = 1
    RMEqual: Final = 1
    RM_newer: Final = 2
    RMNewer: Final = 2
    RM_equal_or_newer: Final = 3
    RMEqualOrNewer: Final = 3
    CC_allow_cache: Final = 0
    CCAllowCache: Final = 0
    CC_revalidate: Final = 1
    CCRevalidate: Final = 1
    CC_no_cache: Final = 2
    CCNoCache: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    url: URLSpec
    tag: HTTPEntityTag
    date: HTTPDate
    request_mode: _DocumentSpec_RequestMode
    cache_control: _DocumentSpec_CacheControl
    @overload
    def __init__(self, copy: DocumentSpec = ...) -> None: ...
    @overload
    def __init__(self, url: URLSpec | str) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: DocumentSpec | URL) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: DocumentSpec | URL) -> Self: ...
    def compare_to(self, other: DocumentSpec | URL) -> int: ...
    def set_url(self, url: URL) -> None:
        """Changes the URL of the DocumentSpec without modifying its other properties.
        Normally this would be a strange thing to do, because the tag and date are
        usually strongly associated with the URL.  To get a DocumentSpec pointing
        to a new URL, you would normally create a new DocumentSpec object.
        """
    def get_url(self) -> URLSpec:
        """Retrieves the URL of the DocumentSpec."""
    def set_tag(self, tag: HTTPEntityTag | str) -> None:
        """Changes the identity tag associated with the DocumentSpec."""
    def has_tag(self) -> bool:
        """Returns true if an identity tag is associated with the DocumentSpec."""
    def get_tag(self) -> HTTPEntityTag:
        """Returns the identity tag associated with the DocumentSpec, if there is one.
        It is an error to call this if has_tag() returns false.

        The identity tag is set by the HTTP server to uniquely refer to a
        particular version of a document.
        """
    def clear_tag(self) -> None:
        """Removes the identity tag associated with the DocumentSpec, if there is one."""
    def set_date(self, date: HTTPDate | int | str) -> None:
        """Changes the last-modified date associated with the DocumentSpec."""
    def has_date(self) -> bool:
        """Returns true if a last-modified date is associated with the DocumentSpec."""
    def get_date(self) -> HTTPDate:
        """Returns the last-modified date associated with the DocumentSpec, if there
        is one.  It is an error to call this if has_date() returns false.
        """
    def clear_date(self) -> None:
        """Removes the last-modified date associated with the DocumentSpec, if there
        is one.
        """
    def set_request_mode(self, request_mode: _DocumentSpec_RequestMode) -> None:
        """Sets the request mode of this DocumentSpec.  This is only relevant when
        using the DocumentSpec to generate a request (for instance, in
        HTTPChannel).  This specifies whether the document request will ask the
        server for a newer version than the indicated version, or the exact
        version, neither, or either.

        The possible values are:

        RM_any: ignore date and tag (if specified), and retrieve any document that
        matches the URL.  For a subrange request, if the document matches the
        version indicated exactly, retrieve the subrange only; otherwise, retrieve
        the entire document.

        RM_equal: request only the precise version of the document that matches the
        particular date and/or tag exactly, if specified; fail if this version is
        not available.

        RM_newer: request any document that is newer than the version indicated by
        the particular date and/or tag; fail if only that version (or older
        versions) are available.

        RM_newer_or_equal: request any document that matches the version indicated
        by the particular date and/or tag, or is a newer version; fail if only
        older versions are available.

        In any of the above, you may specify either or both of the last-modified
        date and the identity tag, whichever is known to the client.

        The default mode is RM_any.
        """
    def get_request_mode(self) -> _DocumentSpec_RequestMode:
        """Returns the request mode of this DocumentSpec.  See set_request_mode()."""
    def set_cache_control(self, cache_control: _DocumentSpec_CacheControl) -> None:
        """Specifies what kind of cached value is acceptable for this document.
        Warning: some HTTP proxies may not respect this setting and may return a
        cached result anyway.

        CC_allow_cache: the normal HTTP behavior; the server may return a cached
        value if it believes it is valid.

        CC_revalidate: a proxy is forced to contact the origin server and verify
        that is cached value is in fact still valid before it returns it.

        CC_no_cache: a proxy must not return its cached value at all, but is forced
        to go all the way back to the origin server for the official document.

        The default mode is CC_allow_cache.
        """
    def get_cache_control(self) -> _DocumentSpec_CacheControl:
        """Returns the request mode of this DocumentSpec.  See set_cache_control()."""
    def input(self, _in: istream) -> bool:
        """Can be used to read in the DocumentSpec from a stream generated either by
        output() or write().  Returns true on success, false on failure.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    compareTo = compare_to
    setUrl = set_url
    getUrl = get_url
    setTag = set_tag
    hasTag = has_tag
    getTag = get_tag
    clearTag = clear_tag
    setDate = set_date
    hasDate = has_date
    getDate = get_date
    clearDate = clear_date
    setRequestMode = set_request_mode
    getRequestMode = get_request_mode
    setCacheControl = set_cache_control
    getCacheControl = get_cache_control

class HTTPChannel(TypedReferenceCount):
    """A single channel of communication from an HTTPClient.  This is similar to
    the concept of a 'connection', except that HTTP is technically
    connectionless; in fact, a channel may represent one unbroken connection or
    it may transparently close and reopen a new connection with each request.

    A channel is conceptually a single thread of I/O. One document at a time
    may be requested using a channel; a new document may (in general) not be
    requested from the same HTTPChannel until the first document has been fully
    retrieved.
    """

    SC_incomplete: Final = 0
    SCIncomplete: Final = 0
    SC_internal_error: Final = 1
    SCInternalError: Final = 1
    SC_no_connection: Final = 2
    SCNoConnection: Final = 2
    SC_timeout: Final = 3
    SCTimeout: Final = 3
    SC_lost_connection: Final = 4
    SCLostConnection: Final = 4
    SC_non_http_response: Final = 5
    SCNonHttpResponse: Final = 5
    SC_invalid_http: Final = 6
    SCInvalidHttp: Final = 6
    SC_socks_invalid_version: Final = 7
    SCSocksInvalidVersion: Final = 7
    SC_socks_no_acceptable_login_method: Final = 8
    SCSocksNoAcceptableLoginMethod: Final = 8
    SC_socks_refused: Final = 9
    SCSocksRefused: Final = 9
    SC_socks_no_connection: Final = 10
    SCSocksNoConnection: Final = 10
    SC_ssl_internal_failure: Final = 11
    SCSslInternalFailure: Final = 11
    SC_ssl_no_handshake: Final = 12
    SCSslNoHandshake: Final = 12
    SC_http_error_watermark: Final = 13
    SCHttpErrorWatermark: Final = 13
    SC_ssl_invalid_server_certificate: Final = 14
    SCSslInvalidServerCertificate: Final = 14
    SC_ssl_self_signed_server_certificate: Final = 15
    SCSslSelfSignedServerCertificate: Final = 15
    SC_ssl_unexpected_server: Final = 16
    SCSslUnexpectedServer: Final = 16
    SC_download_open_error: Final = 17
    SCDownloadOpenError: Final = 17
    SC_download_write_error: Final = 18
    SCDownloadWriteError: Final = 18
    SC_download_invalid_range: Final = 19
    SCDownloadInvalidRange: Final = 19
    def __init__(self, __param0: HTTPChannel) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_client(self) -> HTTPClient:
        """Returns the HTTPClient object that owns this channel."""
    def is_valid(self) -> bool:
        """Returns true if the last-requested document was successfully retrieved and
        is ready to be read, false otherwise.
        """
    def is_connection_ready(self) -> bool:
        """Returns true if a connection has been established to the named server in a
        previous call to connect_to() or begin_connect_to(), false otherwise.
        """
    def get_url(self) -> URLSpec:
        """Returns the URL that was used to retrieve the most recent document:
        whatever URL was last passed to get_document() or get_header().  If a
        redirect has transparently occurred, this will return the new, redirected
        URL (the actual URL at which the document was located).
        """
    def get_document_spec(self) -> DocumentSpec:
        """Returns the DocumentSpec associated with the most recent document.  This
        includes its actual URL (following redirects) along with the identity tag
        and last-modified date, if supplied by the server.

        This structure may be saved and used to retrieve the same version of the
        document later, or to conditionally retrieve a newer version if it is
        available.
        """
    def get_http_version(self) -> _HTTPEnum_HTTPVersion:
        """Returns the HTTP version number returned by the server, as one of the
        HTTPClient enumerated types, e.g.  HTTPClient::HV_11.
        """
    def get_http_version_string(self) -> str:
        """Returns the HTTP version number returned by the server, formatted as a
        string, e.g.  "HTTP/1.1".
        """
    def get_status_code(self) -> int:
        """Returns the HTML return code from the document retrieval request.  This
        will be in the 200 range if the document is successfully retrieved, or some
        other value in the case of an error.

        Some proxy errors during an https-over-proxy request would return the same
        status code as a different error that occurred on the host server.  To
        differentiate these cases, status codes that are returned by the proxy
        during the CONNECT phase (except code 407) are incremented by 1000.
        """
    def get_status_string(self) -> str:
        """Returns the string as returned by the server describing the status code for
        humans.  This may or may not be meaningful.
        """
    def get_www_realm(self) -> str:
        """If the document failed to connect because of a 401 (Authorization
        required), this method will return the "realm" returned by the server in
        which the requested document must be authenticated.  This string may be
        presented to the user to request an associated username and password (which
        then should be stored in HTTPClient::set_username()).
        """
    def get_proxy_realm(self) -> str:
        """If the document failed to connect because of a 407 (Proxy authorization
        required), this method will return the "realm" returned by the proxy.  This
        string may be presented to the user to request an associated username and
        password (which then should be stored in HTTPClient::set_username()).
        """
    def get_redirect(self) -> URLSpec:
        """If the document failed with a redirect code (300 series), this will
        generally contain the new URL the server wants us to try.  In many cases,
        the client will automatically follow redirects; if these are successful the
        client will return a successful code and get_redirect() will return empty,
        but get_url() will return the new, redirected URL.
        """
    def get_header_value(self, key: str) -> str:
        """Returns the HTML header value associated with the indicated key, or empty
        string if the key was not defined in the message returned by the server.
        """
    def get_num_redirect_steps(self) -> int:
        """If the document automatically followed one or more redirects, this will
        return the number of redirects that were automatically followed.  Use
        get_redirect_step() to retrieve each URL in sequence.
        """
    def get_redirect_step(self, n: int) -> URLSpec:
        """Use in conjunction with get_num_redirect_steps() to extract the chain of
        URL's that the channel was automatically redirected through to arrive at
        the final document.
        """
    def set_persistent_connection(self, persistent_connection: bool) -> None:
        """Indicates whether the HTTPChannel should try to keep the connection to the
        server open and reuse that connection for multiple documents, or whether it
        should close the connection and open a new one for each request.  Set this
        true to keep the connections around when possible, false to recycle them.

        It makes most sense to set this false when the HTTPChannel will be used
        only once to retrieve a single document, true when you will be using the
        same HTTPChannel object to retrieve multiple documents.
        """
    def get_persistent_connection(self) -> bool:
        """Returns whether the HTTPChannel should try to keep the connection to the
        server open and reuse that connection for multiple documents, or whether it
        should close the connection and open a new one for each request.  See
        set_persistent_connection().
        """
    def will_close_connection(self) -> bool:
        """Returns true if the server has indicated it will close the connection after
        this document has been read, or false if it will remain open (and future
        documents may be requested on the same connection).
        """
    def set_allow_proxy(self, allow_proxy: bool) -> None:
        """If this is true (the normal case), the HTTPClient will be consulted for
        information about the proxy to be used for each connection via this
        HTTPChannel.  If this has been set to false by the user, then all
        connections will be made directly, regardless of the proxy settings
        indicated on the HTTPClient.
        """
    def get_allow_proxy(self) -> bool:
        """If this is true (the normal case), the HTTPClient will be consulted for
        information about the proxy to be used for each connection via this
        HTTPChannel.  If this has been set to false by the user, then all
        connections will be made directly, regardless of the proxy settings
        indicated on the HTTPClient.
        """
    def set_proxy_tunnel(self, proxy_tunnel: bool) -> None:
        """Normally, a proxy is itself asked for ordinary URL's, and the proxy decides
        whether to hand the client a cached version of the document or to contact
        the server for a fresh version.  The proxy may also modify the headers and
        transfer encoding on the way.

        If this is set to true, then instead of asking for URL's from the proxy, we
        will ask the proxy to open a connection to the server (for instance, on
        port 80); if the proxy honors this request, then we contact the server
        directly through this connection to retrieve the document.  If the proxy
        does not honor the connect request, then the retrieve operation fails.

        SSL connections (e.g.  https), and connections through a Socks proxy, are
        always tunneled, regardless of the setting of this flag.
        """
    def get_proxy_tunnel(self) -> bool:
        """Returns true if connections always tunnel through a proxy, or false (the
        normal case) if we allow the proxy to serve up documents.  See
        set_proxy_tunnel().
        """
    def set_connect_timeout(self, timeout_seconds: float) -> None:
        """Sets the maximum length of time, in seconds, that the channel will wait
        before giving up on establishing a TCP connection.

        At present, this is used only for the nonblocking interfaces (e.g.
        begin_get_document(), begin_connect_to()), but it is used whether
        set_blocking_connect() is true or false.
        """
    def get_connect_timeout(self) -> float:
        """Returns the length of time, in seconds, to wait for a new nonblocking
        socket to connect.  See set_connect_timeout().
        """
    def set_blocking_connect(self, blocking_connect: bool) -> None:
        """If this flag is true, a socket connect will block even for nonblocking I/O
        calls like begin_get_document(), begin_connect_to(), etc.  If false, a
        socket connect will not block for nonblocking I/O calls, but will block for
        blocking I/O calls (get_document(), connect_to(), etc.).

        Setting this true is useful when you want to use non-blocking I/O once you
        have established the connection, but you don't want to bother with polling
        for the initial connection.  It's also useful when you don't particularly
        care about non-blocking I/O, but you need to respect timeouts like
        connect_timeout and http_timeout.
        """
    def get_blocking_connect(self) -> bool:
        """If this flag is true, a socket connect will block even for nonblocking I/O
        calls like begin_get_document(), begin_connect_to(), etc.  If false, a
        socket connect will not block for nonblocking I/O calls, but will block for
        blocking I/O calls (get_document(), connect_to(), etc.).
        """
    def set_http_timeout(self, timeout_seconds: float) -> None:
        """Sets the maximum length of time, in seconds, that the channel will wait for
        the HTTP server to finish sending its response to our request.

        The timer starts counting after the TCP connection has been established
        (see set_connect_timeout(), above) and the request has been sent.

        At present, this is used only for the nonblocking interfaces (e.g.
        begin_get_document(), begin_connect_to()), but it is used whether
        set_blocking_connect() is true or false.
        """
    def get_http_timeout(self) -> float:
        """Returns the length of time, in seconds, to wait for the HTTP server to
        respond to our request.  See set_http_timeout().
        """
    def set_skip_body_size(self, skip_body_size: int) -> None:
        """Specifies the maximum number of bytes in a received (but unwanted) body
        that will be skipped past, in order to reset to a new request.

        That is, if this HTTPChannel requests a file via get_document(), but does
        not call download_to_ram(), download_to_file(), or open_read_body(), and
        instead immediately requests a new file, then the HTTPChannel has a choice
        whether to skip past the unwanted document, or to close the connection and
        open a new one.  If the number of bytes to skip is more than this
        threshold, the connection will be closed; otherwise, the data will simply
        be read and discarded.
        """
    def get_skip_body_size(self) -> int:
        """Returns the maximum number of bytes in a received (but unwanted) body that
        will be skipped past, in order to reset to a new request.  See
        set_skip_body_size().
        """
    def set_idle_timeout(self, idle_timeout: float) -> None:
        """Specifies the amount of time, in seconds, in which a previously-established
        connection is allowed to remain open and unused.  If a previous connection
        has remained unused for at least this number of seconds, it will be closed
        and a new connection will be opened; otherwise, the same connection will be
        reused for the next request (for this particular HTTPChannel).
        """
    def get_idle_timeout(self) -> float:
        """Returns the amount of time, in seconds, in which an previously-established
        connection is allowed to remain open and unused.  See set_idle_timeout().
        """
    def set_download_throttle(self, download_throttle: bool) -> None:
        """Specifies whether nonblocking downloads (via download_to_file() or
        download_to_ram()) will be limited so as not to use all available
        bandwidth.

        If this is true, when a download has been started on this channel it will
        be invoked no more frequently than get_max_updates_per_second(), and the
        total bandwidth used by the download will be no more than
        get_max_bytes_per_second().  If this is false, downloads will proceed as
        fast as the server can send the data.

        This only has effect on the nonblocking I/O methods like
        begin_get_document(), etc.  The blocking methods like get_document() always
        use as much CPU and bandwidth as they can get.
        """
    def get_download_throttle(self) -> bool:
        """Returns whether the nonblocking downloads will be bandwidth-limited.  See
        set_download_throttle().
        """
    def set_max_bytes_per_second(self, max_bytes_per_second: float) -> None:
        """When bandwidth throttling is in effect (see set_download_throttle()), this
        specifies the maximum number of bytes per second that may be consumed by
        this channel.
        """
    def get_max_bytes_per_second(self) -> float:
        """Returns the maximum number of bytes per second that may be consumed by this
        channel when get_download_throttle() is true.
        """
    def set_max_updates_per_second(self, max_updates_per_second: float) -> None:
        """When bandwidth throttling is in effect (see set_download_throttle()), this
        specifies the maximum number of times per second that run() will attempt to
        do any downloading at all.
        """
    def get_max_updates_per_second(self) -> float:
        """Returns the maximum number of times per second that run() will do anything
        at all, when get_download_throttle() is true.
        """
    def set_content_type(self, content_type: str) -> None:
        """Specifies the Content-Type header, useful for applications that require
        different types of content, such as JSON.
        """
    def get_content_type(self) -> str:
        """Returns the value of the Content-Type header."""
    def set_expected_file_size(self, file_size: int) -> None:
        """This may be called immediately after a call to get_document() or some
        related function to specify the expected size of the document we are
        retrieving, if we happen to know.  This is used as the return value to
        get_file_size() only in the case that the server does not tell us the
        actual file size.
        """
    def get_file_size(self) -> int:
        """Returns the size of the file, if it is known.  Returns the value set by
        set_expected_file_size() if the file size is not known, or 0 if this value
        was not set.

        If the file is dynamically generated, the size may not be available until a
        read has started (e.g.  open_read_body() has been called); and even then it
        may increase as more of the file is read due to the nature of HTTP/1.1
        requests which can change their minds midstream about how much data they're
        sending you.
        """
    def is_file_size_known(self) -> bool:
        """Returns true if the size of the file we are currently retrieving was told
        us by the server and thus is reliably known, or false if the size reported
        by get_file_size() represents an educated guess (possibly as set by
        set_expected_file_size(), or as inferred from a chunked transfer encoding
        in progress).
        """
    def get_first_byte_requested(self) -> int:
        """Returns the first byte of the file requested by the request.  This will
        normally be 0 to indicate that the file is being requested from the
        beginning, but if the file was requested via a get_subdocument() call, this
        will contain the first_byte parameter from that call.
        """
    def get_last_byte_requested(self) -> int:
        """Returns the last byte of the file requested by the request.  This will
        normally be 0 to indicate that the file is being requested to its last
        byte, but if the file was requested via a get_subdocument() call, this will
        contain the last_byte parameter from that call.
        """
    def get_first_byte_delivered(self) -> int:
        """Returns the first byte of the file (that will be) delivered by the server
        in response to the current request.  Normally, this is the same as
        get_first_byte_requested(), but some servers will ignore a subdocument
        request and always return the whole file, in which case this value will be
        0, regardless of what was requested to get_subdocument().
        """
    def get_last_byte_delivered(self) -> int:
        """Returns the last byte of the file (that will be) delivered by the server in
        response to the current request.  Normally, this is the same as
        get_last_byte_requested(), but some servers will ignore a subdocument
        request and always return the whole file, in which case this value will be
        0, regardless of what was requested to get_subdocument().
        """
    def write_headers(self, out: ostream) -> None:
        """Outputs a list of all headers defined by the server to the indicated output
        stream.
        """
    def reset(self) -> None:
        """Stops whatever file transaction is currently in progress, closes the
        connection, and resets to begin anew.  You shouldn't ever need to call
        this, since the channel should be able to reset itself cleanly between
        requests, but it is provided in case you are an especially nervous type.

        Don't call this after every request unless you set
        set_persistent_connection() to false, since calling reset() rudely closes
        the connection regardless of whether we have told the server we intend to
        keep it open or not.
        """
    def preserve_status(self) -> None:
        """Preserves the previous status code (presumably a failure) from the previous
        connection attempt.  If the subsequent connection attempt also fails, the
        returned status code will be the better of the previous code and the
        current code.

        This can be called to daisy-chain subsequent attempts to download the same
        document from different servers.  After all servers have been attempted,
        the final status code will reflect the attempt that most nearly succeeded.
        """
    def clear_extra_headers(self) -> None:
        """Resets the extra headers that were previously added via calls to
        send_extra_header().
        """
    def send_extra_header(self, key: str, value: str) -> None:
        """Specifies an additional key: value pair that is added into the header sent
        to the server with the next request.  This is passed along with no
        interpretation by the HTTPChannel code.  You may call this repeatedly to
        append multiple headers.

        This is persistent for one request only; it must be set again for each new
        request.
        """
    def get_document(self, url: DocumentSpec | URL) -> bool:
        """Opens the named document for reading, if available.  Returns true if
        successful, false otherwise.
        """
    def get_subdocument(self, url: DocumentSpec | URL, first_byte: int, last_byte: int) -> bool:
        """Retrieves only the specified byte range of the indicated document.  If
        last_byte is 0, it stands for the last byte of the document.  When a
        subdocument is requested, get_file_size() and get_bytes_downloaded() will
        report the number of bytes of the subdocument, not of the complete
        document.
        """
    def get_header(self, url: DocumentSpec | URL) -> bool:
        """Like get_document(), except only the header associated with the document is
        retrieved.  This may be used to test for existence of the document; it
        might also return the size of the document (if the server gives us this
        information).
        """
    def post_form(self, url: DocumentSpec | URL, body: str) -> bool:
        """Posts form data to a particular URL and retrieves the response."""
    def put_document(self, url: DocumentSpec | URL, body: str) -> bool:
        """Uploads the indicated body to the server to replace the indicated URL, if
        the server allows this.
        """
    def delete_document(self, url: DocumentSpec | URL) -> bool:
        """Requests the server to remove the indicated URL."""
    def get_trace(self, url: DocumentSpec | URL) -> bool:
        """Sends a TRACE message to the server, which should return back the same
        message as the server received it, allowing inspection of proxy hops, etc.
        """
    def connect_to(self, url: DocumentSpec | URL) -> bool:
        """Establish a direct connection to the server and port indicated by the URL,
        but do not issue any HTTP requests.  If successful, the connection may then
        be taken to use for whatever purposes you like by calling get_connection().

        This establishes a blocking I/O socket.  Also see begin_connect_to().
        """
    def get_options(self, url: DocumentSpec | URL) -> bool:
        """Sends an OPTIONS message to the server, which should query the available
        options, possibly in relation to a specified URL.
        """
    def begin_get_document(self, url: DocumentSpec | URL) -> None:
        """Begins a non-blocking request to retrieve a given document.  This method
        will return immediately, even before a connection to the server has
        necessarily been established; you must then call run() from time to time
        until the return value of run() is false.  Then you may check is_valid()
        and get_status_code() to determine the status of your request.

        If a previous request had been pending, that request is discarded.
        """
    def begin_get_subdocument(self, url: DocumentSpec | URL, first_byte: int, last_byte: int) -> None:
        """Begins a non-blocking request to retrieve only the specified byte range of
        the indicated document.  If last_byte is 0, it stands for the last byte of
        the document.  When a subdocument is requested, get_file_size() and
        get_bytes_downloaded() will report the number of bytes of the subdocument,
        not of the complete document.
        """
    def begin_get_header(self, url: DocumentSpec | URL) -> None:
        """Begins a non-blocking request to retrieve a given header.  See
        begin_get_document() and get_header().
        """
    def begin_post_form(self, url: DocumentSpec | URL, body: str) -> None:
        """Posts form data to a particular URL and retrieves the response, all using
        non-blocking I/O.  See begin_get_document() and post_form().

        It is important to note that you *must* call run() repeatedly after calling
        this method until run() returns false, and you may not call any other
        document posting or retrieving methods using the HTTPChannel object in the
        interim, or your form data may not get posted.
        """
    def run(self) -> bool:
        """This must be called from time to time when non-blocking I/O is in use.  It
        checks for data coming in on the socket and writes data out to the socket
        when possible, and does whatever processing is required towards completing
        the current task.

        The return value is true if the task is still pending (and run() will need
        to be called again in the future), or false if the current task is
        complete.
        """
    def begin_connect_to(self, url: DocumentSpec | URL) -> None:
        """Begins a non-blocking request to establish a direct connection to the
        server and port indicated by the URL.  No HTTP requests will be issued
        beyond what is necessary to establish the connection.  When run() has
        finished, you may call is_connection_ready() to determine if the connection
        was successfully established.

        If successful, the connection may then be taken to use for whatever
        purposes you like by calling get_connection().

        This establishes a nonblocking I/O socket.  Also see connect_to().
        """
    def open_read_body(self) -> ISocketStream:
        """Returns a newly-allocated istream suitable for reading the body of the
        document.  This may only be called immediately after a call to
        get_document() or post_form(), or after a call to run() has returned false.

        Note that, in nonblocking mode, the returned stream may report an early
        EOF, even before the actual end of file.  When this happens, you should
        call stream->is_closed() to determine whether you should attempt to read
        some more later.

        The user is responsible for passing the returned istream to
        close_read_body() later.
        """
    def close_read_body(self, stream: istream) -> None:
        """Closes a file opened by a previous call to open_read_body().  This really
        just deletes the istream pointer, but it is recommended to use this
        interface instead of deleting it explicitly, to help work around compiler
        issues.
        """
    def download_to_file(self, filename: StrOrBytesPath, subdocument_resumes: bool = ...) -> bool:
        """Specifies the name of a file to download the resulting document to.  This
        should be called immediately after get_document() or begin_get_document()
        or related functions.

        In the case of the blocking I/O methods like get_document(), this function
        will download the entire document to the file and return true if it was
        successfully downloaded, false otherwise.

        In the case of non-blocking I/O methods like begin_get_document(), this
        function simply indicates an intention to download to the indicated file.
        It returns true if the file can be opened for writing, false otherwise, but
        the contents will not be completely downloaded until run() has returned
        false.  At this time, it is possible that a communications error will have
        left a partial file, so is_download_complete() may be called to test this.

        If subdocument_resumes is true and the document in question was previously
        requested as a subdocument (i.e.  get_subdocument() with a first_byte value
        greater than zero), this will automatically seek to the appropriate byte
        within the file for writing the output.  In this case, the file must
        already exist and must have at least first_byte bytes in it.  If
        subdocument_resumes is false, a subdocument will always be downloaded
        beginning at the first byte of the file.
        """
    def download_to_ram(self, ramfile: Ramfile, subdocument_resumes: bool = ...) -> bool:
        """Specifies a Ramfile object to download the resulting document to.  This
        should be called immediately after get_document() or begin_get_document()
        or related functions.

        In the case of the blocking I/O methods like get_document(), this function
        will download the entire document to the Ramfile and return true if it was
        successfully downloaded, false otherwise.

        In the case of non-blocking I/O methods like begin_get_document(), this
        function simply indicates an intention to download to the indicated
        Ramfile.  It returns true if the file can be opened for writing, false
        otherwise, but the contents will not be completely downloaded until run()
        has returned false.  At this time, it is possible that a communications
        error will have left a partial file, so is_download_complete() may be
        called to test this.

        If subdocument_resumes is true and the document in question was previously
        requested as a subdocument (i.e.  get_subdocument() with a first_byte value
        greater than zero), this will automatically seek to the appropriate byte
        within the Ramfile for writing the output.  In this case, the Ramfile must
        already have at least first_byte bytes in it.
        """
    def download_to_stream(self, strm: ostream, subdocument_resumes: bool = ...) -> bool:
        """Specifies the name of an ostream to download the resulting document to.
        This should be called immediately after get_document() or
        begin_get_document() or related functions.

        In the case of the blocking I/O methods like get_document(), this function
        will download the entire document to the file and return true if it was
        successfully downloaded, false otherwise.

        In the case of non-blocking I/O methods like begin_get_document(), this
        function simply indicates an intention to download to the indicated file.
        It returns true if the file can be opened for writing, false otherwise, but
        the contents will not be completely downloaded until run() has returned
        false.  At this time, it is possible that a communications error will have
        left a partial file, so is_download_complete() may be called to test this.

        If subdocument_resumes is true and the document in question was previously
        requested as a subdocument (i.e.  get_subdocument() with a first_byte value
        greater than zero), this will automatically seek to the appropriate byte
        within the file for writing the output.  In this case, the file must
        already exist and must have at least first_byte bytes in it.  If
        subdocument_resumes is false, a subdocument will always be downloaded
        beginning at the first byte of the file.
        """
    def get_connection(self) -> SocketStream:
        """Returns the connection that was established via a previous call to
        connect_to() or begin_connect_to(), or NULL if the connection attempt
        failed or if those methods have not recently been called.

        This stream has been allocated from the free store.  It is the user's
        responsibility to delete this pointer when finished with it.
        """
    def get_bytes_downloaded(self) -> int:
        """Returns the number of bytes downloaded during the last (or current)
        download_to_file() or download_to_ram operation().  This can be used in
        conjunction with get_file_size() to report the percent complete (but be
        careful, since get_file_size() may return 0 if the server has not told us
        the size of the file).
        """
    def get_bytes_requested(self) -> int:
        """When download throttling is in effect (set_download_throttle() has been set
        to true) and non-blocking I/O methods (like begin_get_document()) are used,
        this returns the number of bytes "requested" from the server so far: that
        is, the theoretical maximum value for get_bytes_downloaded(), if the server
        has been keeping up with our demand.

        If this number is less than get_bytes_downloaded(), then the server has not
        been supplying bytes fast enough to meet our own download throttle rate.

        When download throttling is not in effect, or when the blocking I/O methods
        (like get_document(), etc.) are used, this returns 0.
        """
    def is_download_complete(self) -> bool:
        """Returns true when a download_to() or download_to_ram() has executed and the
        file has been fully downloaded.  If this still returns false after
        processing has completed, there was an error in transmission.

        Note that simply testing is_download_complete() does not prove that the
        requested document was successfully retrieved--you might have just
        downloaded the "404 not found" stub (for instance) that a server would
        provide in response to some error condition.  You should also check
        is_valid() to prove that the file you expected has been successfully
        retrieved.
        """
    def get_redirect_steps(self) -> tuple[URLSpec, ...]: ...
    getClient = get_client
    isValid = is_valid
    isConnectionReady = is_connection_ready
    getUrl = get_url
    getDocumentSpec = get_document_spec
    getHttpVersion = get_http_version
    getHttpVersionString = get_http_version_string
    getStatusCode = get_status_code
    getStatusString = get_status_string
    getWwwRealm = get_www_realm
    getProxyRealm = get_proxy_realm
    getRedirect = get_redirect
    getHeaderValue = get_header_value
    getNumRedirectSteps = get_num_redirect_steps
    getRedirectStep = get_redirect_step
    setPersistentConnection = set_persistent_connection
    getPersistentConnection = get_persistent_connection
    willCloseConnection = will_close_connection
    setAllowProxy = set_allow_proxy
    getAllowProxy = get_allow_proxy
    setProxyTunnel = set_proxy_tunnel
    getProxyTunnel = get_proxy_tunnel
    setConnectTimeout = set_connect_timeout
    getConnectTimeout = get_connect_timeout
    setBlockingConnect = set_blocking_connect
    getBlockingConnect = get_blocking_connect
    setHttpTimeout = set_http_timeout
    getHttpTimeout = get_http_timeout
    setSkipBodySize = set_skip_body_size
    getSkipBodySize = get_skip_body_size
    setIdleTimeout = set_idle_timeout
    getIdleTimeout = get_idle_timeout
    setDownloadThrottle = set_download_throttle
    getDownloadThrottle = get_download_throttle
    setMaxBytesPerSecond = set_max_bytes_per_second
    getMaxBytesPerSecond = get_max_bytes_per_second
    setMaxUpdatesPerSecond = set_max_updates_per_second
    getMaxUpdatesPerSecond = get_max_updates_per_second
    setContentType = set_content_type
    getContentType = get_content_type
    setExpectedFileSize = set_expected_file_size
    getFileSize = get_file_size
    isFileSizeKnown = is_file_size_known
    getFirstByteRequested = get_first_byte_requested
    getLastByteRequested = get_last_byte_requested
    getFirstByteDelivered = get_first_byte_delivered
    getLastByteDelivered = get_last_byte_delivered
    writeHeaders = write_headers
    preserveStatus = preserve_status
    clearExtraHeaders = clear_extra_headers
    sendExtraHeader = send_extra_header
    getDocument = get_document
    getSubdocument = get_subdocument
    getHeader = get_header
    postForm = post_form
    putDocument = put_document
    deleteDocument = delete_document
    getTrace = get_trace
    connectTo = connect_to
    getOptions = get_options
    beginGetDocument = begin_get_document
    beginGetSubdocument = begin_get_subdocument
    beginGetHeader = begin_get_header
    beginPostForm = begin_post_form
    beginConnectTo = begin_connect_to
    openReadBody = open_read_body
    closeReadBody = close_read_body
    downloadToFile = download_to_file
    downloadToRam = download_to_ram
    downloadToStream = download_to_stream
    getConnection = get_connection
    getBytesDownloaded = get_bytes_downloaded
    getBytesRequested = get_bytes_requested
    isDownloadComplete = is_download_complete
    getRedirectSteps = get_redirect_steps

class Decompressor:
    """This manages run-time decompression of a zlib-compressed stream, as a
    background or foreground task.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def progress(self) -> float: ...
    def __init__(self, __param0: Decompressor = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def initiate(self, source_file: StrOrBytesPath, dest_file: StrOrBytesPath = ...) -> int:
        """`(self, source_file: Filename)`:
        Begins a background decompression of the named file (whose filename must
        end in ".pz") to a new file without the .pz extension.  The source file is
        removed after successful completion.

        `(self, source_file: Filename, dest_file: Filename)`:
        Begins a background decompression from the named source file to the named
        destination file.  The source file is removed after successful completion.
        """
    def run(self) -> int:
        """Called each frame to do the next bit of work in the background task.
        Returns EU_ok if a chunk is completed but there is more to go, or
        EU_success when we're all done.  Any other return value indicates an error.
        """
    @overload
    def decompress(self, source_file: StrOrBytesPath) -> bool:
        """`(self, source_file: Filename)`:
        Performs a foreground decompression of the named file; does not return
        until the decompression is complete.

        `(self, source_and_dest_file: Ramfile)`:
        Does an in-memory decompression of the indicated Ramfile.  The decompressed
        contents are written back into the same Ramfile on completion.
        """
    @overload
    def decompress(self, source_and_dest_file: Ramfile) -> bool: ...
    def get_progress(self) -> float:
        """Returns the ratio through the decompression step in the background."""
    getProgress = get_progress

class DownloadDb:
    """A listing of files within multifiles for management of client-side
    synchronization with a server-provided set of files.

    This class manages one copy of the database for the client, representing
    the files on the client system, and another copy for the server,
    representing the files the server has available.
    """

    Status_incomplete: Final = 0
    StatusIncomplete: Final = 0
    Status_complete: Final = 1
    StatusComplete: Final = 1
    Status_decompressed: Final = 2
    StatusDecompressed: Final = 2
    Status_extracted: Final = 3
    StatusExtracted: Final = 3
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: DownloadDb = ...) -> None:
        """`(self)`:
        Primarily used for testing.

        `(self, server_file: Filename, client_file: Filename)`; `(self, server_file: Ramfile, client_file: Filename)`:
        Create a download db with these client and server dbs
        """
    @overload
    def __init__(self, server_file: Ramfile | StrOrBytesPath, client_file: StrOrBytesPath) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def write_version_map(self, out: ostream) -> None: ...
    def write_client_db(self, file: StrOrBytesPath) -> bool:
        """Write a database file"""
    def write_server_db(self, file: StrOrBytesPath) -> bool: ...
    def get_client_num_multifiles(self) -> int: ...
    def get_server_num_multifiles(self) -> int: ...
    def get_client_multifile_name(self, index: int) -> str: ...
    def get_server_multifile_name(self, index: int) -> str: ...
    def get_client_multifile_size(self, mfname: str) -> int: ...
    def set_client_multifile_size(self, mfname: str, size: int) -> None: ...
    def set_client_multifile_delta_size(self, mfname: str, size: int) -> int: ...
    def get_server_multifile_size(self, mfname: str) -> int: ...
    def set_server_multifile_size(self, mfname: str, size: int) -> None: ...
    def get_client_multifile_phase(self, mfname: str) -> float: ...
    def get_server_multifile_phase(self, mfname: str) -> float: ...
    def set_client_multifile_incomplete(self, mfname: str) -> None: ...
    def set_client_multifile_complete(self, mfname: str) -> None: ...
    def set_client_multifile_decompressed(self, mfname: str) -> None: ...
    def set_client_multifile_extracted(self, mfname: str) -> None: ...
    def get_server_num_files(self, mfname: str) -> int: ...
    def get_server_file_name(self, mfname: str, index: int) -> str: ...
    def client_multifile_exists(self, mfname: str) -> bool:
        """Queries from the Launcher"""
    def client_multifile_complete(self, mfname: str) -> bool:
        """A multifile is complete when it is completely downloaded.  Note: it may
        already be decompressed or extracted and it is still complete
        """
    def client_multifile_decompressed(self, mfname: str) -> bool: ...
    def client_multifile_extracted(self, mfname: str) -> bool: ...
    def get_client_multifile_hash(self, mfname: str) -> HashVal:
        """Return the hash value of the file we are working on"""
    def set_client_multifile_hash(self, mfname: str, val: HashVal) -> None:
        """Set the hash value of file we are working on"""
    def get_server_multifile_hash(self, mfname: str) -> HashVal:
        """Return the hash value of the server file"""
    def set_server_multifile_hash(self, mfname: str, val: HashVal) -> None:
        """Set the hash value of file we are working on"""
    def delete_client_multifile(self, mfname: str) -> None:
        """Operations on multifiles"""
    def add_client_multifile(self, server_mfname: str) -> None: ...
    def expand_client_multifile(self, mfname: str) -> None: ...
    def create_new_server_db(self) -> None:
        """Used on the server side makefiles to create a new clean server db"""
    def server_add_multifile(self, mfname: str, phase: float, size: int, status: int) -> None: ...
    def server_add_file(self, mfname: str, fname: str) -> None: ...
    def add_version(self, name: StrOrBytesPath, hash: HashVal, version: int) -> None:
        """Appends a new version of the file onto the end of the list, or changes the
        hash associated with a version previously added.

        Note: version numbers start at 1
        """
    def insert_new_version(self, name: StrOrBytesPath, hash: HashVal) -> None:
        """Inserts a new version 1 copy of the file, sliding all the other versions up
        by one.
        """
    def has_version(self, name: StrOrBytesPath) -> bool:
        """Returns true if the indicated file has version information, false
        otherwise.  Some files recorded in the database may not bother to track
        versions.
        """
    def get_num_versions(self, name: StrOrBytesPath) -> int:
        """Returns the number of versions stored for the indicated file."""
    def set_num_versions(self, name: StrOrBytesPath, num_versions: int) -> None:
        """Reduces the number of versions of a particular file stored in the ddb by
        throwing away all versions higher than the indicated index.
        """
    def get_version(self, name: StrOrBytesPath, hash: HashVal) -> int:
        """Returns the version number of this particular file, determined by looking
        up the hash generated from the file.  Returns -1 if the version number
        cannot be determined.
        """
    def get_hash(self, name: StrOrBytesPath, version: int) -> HashVal:
        """Returns the MD5 hash associated with the indicated version of the indicated
        file.
        """
    writeVersionMap = write_version_map
    writeClientDb = write_client_db
    writeServerDb = write_server_db
    getClientNumMultifiles = get_client_num_multifiles
    getServerNumMultifiles = get_server_num_multifiles
    getClientMultifileName = get_client_multifile_name
    getServerMultifileName = get_server_multifile_name
    getClientMultifileSize = get_client_multifile_size
    setClientMultifileSize = set_client_multifile_size
    setClientMultifileDeltaSize = set_client_multifile_delta_size
    getServerMultifileSize = get_server_multifile_size
    setServerMultifileSize = set_server_multifile_size
    getClientMultifilePhase = get_client_multifile_phase
    getServerMultifilePhase = get_server_multifile_phase
    setClientMultifileIncomplete = set_client_multifile_incomplete
    setClientMultifileComplete = set_client_multifile_complete
    setClientMultifileDecompressed = set_client_multifile_decompressed
    setClientMultifileExtracted = set_client_multifile_extracted
    getServerNumFiles = get_server_num_files
    getServerFileName = get_server_file_name
    clientMultifileExists = client_multifile_exists
    clientMultifileComplete = client_multifile_complete
    clientMultifileDecompressed = client_multifile_decompressed
    clientMultifileExtracted = client_multifile_extracted
    getClientMultifileHash = get_client_multifile_hash
    setClientMultifileHash = set_client_multifile_hash
    getServerMultifileHash = get_server_multifile_hash
    setServerMultifileHash = set_server_multifile_hash
    deleteClientMultifile = delete_client_multifile
    addClientMultifile = add_client_multifile
    expandClientMultifile = expand_client_multifile
    createNewServerDb = create_new_server_db
    serverAddMultifile = server_add_multifile
    serverAddFile = server_add_file
    addVersion = add_version
    insertNewVersion = insert_new_version
    hasVersion = has_version
    getNumVersions = get_num_versions
    setNumVersions = set_num_versions
    getVersion = get_version
    getHash = get_hash

class Extractor:
    """This class automatically extracts the contents of a Multifile to the
    current directory (or to a specified directory) in the background.

    It is designed to limit its use of system resources and run unobtrusively
    in the background.  After specifying the files you wish to extract via
    repeated calls to request_subfile(), begin the process by calling run()
    repeatedly.  Each call to run() extracts another small portion of the
    Multifile.  Call run() whenever you have spare cycles until run() returns
    EU_success.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def progress(self) -> float: ...
    def __init__(self) -> None: ...
    def set_multifile(self, multifile_name: StrOrBytesPath) -> bool:
        """Specifies the filename of the Multifile that the Extractor will read.
        Returns true on success, false if the mulifile name is invalid.
        """
    def set_extract_dir(self, extract_dir: StrOrBytesPath) -> None:
        """Specifies the directory into which all extracted subfiles will be written.
        Relative paths of subfiles within the Multifile will be written as relative
        paths to this directory.
        """
    def reset(self) -> None:
        """Interrupts the Extractor in the middle of its business and makes it ready
        to accept a new list of subfiles to extract.
        """
    def request_subfile(self, subfile_name: StrOrBytesPath) -> bool:
        """Requests a particular subfile to be extracted when step() or run() is
        called.  Returns true if the subfile exists, false otherwise.
        """
    def request_all_subfiles(self) -> int:
        """Requests all subfiles in the Multifile to be extracted.  Returns the number
        requested.
        """
    def step(self) -> int:
        """After all of the requests have been made via request_file() or
        request_all_subfiles(), call step() repeatedly until it stops returning
        EU_ok.

        step() extracts the next small unit of data from the Multifile.  Returns
        EU_ok if progress is continuing, EU_error_abort if there is a problem, or
        EU_success when the last piece has been extracted.

        Also see run().
        """
    def get_progress(self) -> float:
        """Returns the fraction of the Multifile extracted so far."""
    def run(self) -> bool:
        """A convenience function to extract the Multifile all at once, when you don't
        care about doing it in the background.

        First, call request_file() or request_all_files() to specify the files you
        would like to extract, then call run() to do the extraction.  Also see
        step() for when you would like the extraction to happen as a background
        task.
        """
    setMultifile = set_multifile
    setExtractDir = set_extract_dir
    requestSubfile = request_subfile
    requestAllSubfiles = request_all_subfiles
    getProgress = get_progress

class MultiplexStream(ostream):
    """This is a special ostream that forwards the data that is written to it to
    any number of other sources, for instance other ostreams, or explicitly to
    a disk file or to system logging utilities.  It's a very handy thing to set
    Notify to refer to when running in batch mode.
    """

    def __init__(self) -> None: ...
    def add_ostream(self, out: ostream, delete_later: bool = ...) -> None:
        """Adds the indicated generic ostream to the multiplex output.  The ostream
        will receive whatever data is sent to the pipe.
        """
    def add_standard_output(self) -> None:
        """Adds the standard output channel."""
    def add_file(self, file: StrOrBytesPath) -> bool:
        """Adds the given file to the multiplex output.  The file is opened in append
        mode with line buffering.  Returns false if the file cannot be opened.
        """
    def add_system_debug(self) -> None:
        """Adds the system debug output the the multiplex output.  This may map to a
        syslog or some such os-specific output system.  It may do nothing on a
        particular system.

        Presently, this maps only to OutputDebugString() on Windows.
        """
    def flush(self) -> None:
        """Forces out all output that hasn't yet been written."""
    addOstream = add_ostream
    addStandardOutput = add_standard_output
    addFile = add_file
    addSystemDebug = add_system_debug

class VirtualFileHTTP(VirtualFile):
    """This maps a document retrieved from an HTTPClient into the
    VirtualFileSystem, allowing models etc.  to be loaded directly from a web
    page.
    """

class VirtualFileMountHTTP(VirtualFileMount):
    """Maps a web page (URL root) into the VirtualFileSystem."""

    def __init__(self, root: URL, http: HTTPClient = ...) -> None: ...
    def get_http_client(self) -> HTTPClient:
        """Returns the HTTPClient object that services this mount point."""
    def get_root(self) -> URLSpec:
        """Returns the URL that represents the root of this mount point."""
    @staticmethod
    def reload_vfs_mount_url() -> None:
        """Reads all of the vfs-mount-url lines in the Config.prc file and replaces
        the mount settings to match them.

        This will mount any url's mentioned in the config file, and unmount and
        unmount any url's no longer mentioned in the config file.  Normally, it is
        called automatically at startup, and need not be called again, unless you
        have fiddled with some config settings.
        """
    getHttpClient = get_http_client
    getRoot = get_root
    reloadVfsMountUrl = reload_vfs_mount_url

class Patcher:
    """Applies a patch synchronously"""

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, __param0: Patcher = ...) -> None: ...
    @overload
    def __init__(self, buffer: Buffer) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def initiate(self, patch: StrOrBytesPath, infile: StrOrBytesPath) -> int: ...
    def run(self) -> int: ...
    def get_progress(self) -> float: ...
    getProgress = get_progress

class StringStream(iostream):
    """A bi-directional stream object that reads and writes data to an internal
    buffer, which can be retrieved and/or set as a string in Python 2 or a
    bytes object in Python 3.
    """

    data: bytes
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source) -> None: ...
    def clear_data(self) -> None:
        """Empties the buffer."""
    def get_data_size(self) -> int:
        """Returns the number of characters available to be read from the data stream."""
    def get_data(self) -> bytes:
        """Returns the contents of the data stream as a string."""
    def set_data(self, data: bytes) -> None: ...
    clearData = clear_data
    getDataSize = get_data_size
    getData = get_data
    setData = set_data

def check_crc(name: StrOrBytesPath) -> int: ...
def check_adler(name: StrOrBytesPath) -> int: ...

checkCrc = check_crc
checkAdler = check_adler
