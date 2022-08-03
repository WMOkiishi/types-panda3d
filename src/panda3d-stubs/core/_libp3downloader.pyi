from os import PathLike
from typing import Any, ClassVar, Literal, TypeAlias, overload

_Filename: TypeAlias = Filename | ConfigVariableFilename | str | bytes | PathLike
_ISocketStream_ReadState: TypeAlias = Literal[0, 1, 2, 3]
_HTTPEnum_HTTPVersion: TypeAlias = Literal[0, 1, 2, 3]
_HTTPClient_VerifySSL: TypeAlias = Literal[0, 1, 2]
_DocumentSpec_RequestMode: TypeAlias = Literal[0, 1, 2, 3]
_DocumentSpec_CacheControl: TypeAlias = Literal[0, 1, 2]

class SSReader:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def receive_datagram(self, dg: Datagram) -> bool: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    def set_tcp_header_size(self, tcp_header_size: int) -> None: ...
    def get_tcp_header_size(self) -> int: ...
    receiveDatagram = receive_datagram
    isClosed = is_closed
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size

class SSWriter:
    DtoolClassDict: ClassVar[dict[str, Any]]
    def send_datagram(self, dg: Datagram) -> bool: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    def set_collect_tcp(self, collect_tcp: bool) -> None: ...
    def get_collect_tcp(self) -> bool: ...
    def set_collect_tcp_interval(self, interval: float) -> None: ...
    def get_collect_tcp_interval(self) -> float: ...
    def set_tcp_header_size(self, tcp_header_size: int) -> None: ...
    def get_tcp_header_size(self) -> int: ...
    def consider_flush(self) -> bool: ...
    def flush(self) -> bool: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    RS_initial: ClassVar[Literal[0]]
    RS_reading: ClassVar[Literal[1]]
    RS_complete: ClassVar[Literal[2]]
    RS_error: ClassVar[Literal[3]]
    def upcast_to_istream(self) -> istream: ...
    def upcast_to_SSReader(self) -> SSReader: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    def get_read_state(self) -> _ISocketStream_ReadState: ...
    upcastToIstream = upcast_to_istream
    upcastToSSReader = upcast_to_SSReader
    isClosed = is_closed
    getReadState = get_read_state
    RSInitial = RS_initial
    RSReading = RS_reading
    RSComplete = RS_complete
    RSError = RS_error

class OSocketStream(ostream, SSWriter):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def upcast_to_ostream(self) -> ostream: ...
    def upcast_to_SSWriter(self) -> SSWriter: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    def flush(self) -> bool: ...
    upcastToOstream = upcast_to_ostream
    upcastToSSWriter = upcast_to_SSWriter
    isClosed = is_closed

class SocketStream(iostream, SSReader, SSWriter):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def upcast_to_iostream(self) -> iostream: ...
    def upcast_to_SSReader(self) -> SSReader: ...
    def upcast_to_SSWriter(self) -> SSWriter: ...
    def is_closed(self) -> bool: ...
    def close(self) -> None: ...
    def set_tcp_header_size(self, tcp_header_size: int) -> None: ...
    def get_tcp_header_size(self) -> int: ...
    def flush(self) -> bool: ...
    upcastToIostream = upcast_to_iostream
    upcastToSSReader = upcast_to_SSReader
    upcastToSSWriter = upcast_to_SSWriter
    isClosed = is_closed
    setTcpHeaderSize = set_tcp_header_size
    getTcpHeaderSize = get_tcp_header_size

class URLSpec:
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
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: URLSpec) -> None: ...
    @overload
    def __init__(self, url: str, server_name_expected: bool = ...) -> None: ...
    @overload
    def __init__(self, url: URLSpec, path: _Filename) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: URLSpec) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, n: int) -> str: ...
    def __le__(self, other: URLSpec) -> bool: ...
    def assign(self, url: str) -> URLSpec: ...
    def compare_to(self, other: URLSpec) -> int: ...
    def get_hash(self) -> int: ...
    def has_scheme(self) -> bool: ...
    def has_authority(self) -> bool: ...
    def has_username(self) -> bool: ...
    def has_server(self) -> bool: ...
    def has_port(self) -> bool: ...
    def has_path(self) -> bool: ...
    def has_query(self) -> bool: ...
    def get_scheme(self) -> str: ...
    def get_authority(self) -> str: ...
    def get_username(self) -> str: ...
    def get_server(self) -> str: ...
    def get_port_str(self) -> str: ...
    def get_port(self) -> int: ...
    def get_server_and_port(self) -> str: ...
    def is_default_port(self) -> bool: ...
    @staticmethod
    def get_default_port_for_scheme(scheme: str) -> int: ...
    def get_path(self) -> str: ...
    def get_query(self) -> str: ...
    def get_path_and_query(self) -> str: ...
    def is_ssl(self) -> bool: ...
    def get_url(self) -> str: ...
    def set_scheme(self, scheme: str) -> None: ...
    def set_authority(self, authority: str) -> None: ...
    def set_username(self, username: str) -> None: ...
    def set_server(self, server: str) -> None: ...
    def set_port(self, port: int | str) -> None: ...
    def set_server_and_port(self, server_and_port: str) -> None: ...
    def set_path(self, path: str) -> None: ...
    def set_query(self, query: str) -> None: ...
    def set_url(self, url: str, server_name_expected: bool = ...) -> None: ...
    def c_str(self) -> str: ...
    def empty(self) -> bool: ...
    def length(self) -> int: ...
    def input(self, _in: istream) -> bool: ...
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def quote(source: str, safe: str = ...) -> str: ...
    @staticmethod
    def quote_plus(source: str, safe: str = ...) -> str: ...
    @staticmethod
    def unquote(source: str) -> str: ...
    @staticmethod
    def unquote_plus(source: str) -> str: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    HV_09: ClassVar[Literal[0]]
    HV_10: ClassVar[Literal[1]]
    HV_11: ClassVar[Literal[2]]
    HV_other: ClassVar[Literal[3]]
    M_options: ClassVar[Literal[0]]
    M_get: ClassVar[Literal[1]]
    M_head: ClassVar[Literal[2]]
    M_post: ClassVar[Literal[3]]
    M_put: ClassVar[Literal[4]]
    M_delete: ClassVar[Literal[5]]
    M_trace: ClassVar[Literal[6]]
    M_connect: ClassVar[Literal[7]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: HTTPEnum) -> None: ...
    HV09 = HV_09
    HV10 = HV_10
    HV11 = HV_11
    HVOther = HV_other
    MOptions = M_options
    MGet = M_get
    MHead = M_head
    MPost = M_post
    MPut = M_put
    MDelete = M_delete
    MTrace = M_trace
    MConnect = M_connect

class HTTPDate:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: HTTPDate) -> None: ...
    @overload
    def __init__(self, format: str) -> None: ...
    @overload
    def __init__(self, time: int) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: HTTPDate) -> bool: ...
    def __gt__(self, other: HTTPDate) -> bool: ...
    def __iadd__(self, seconds: int) -> HTTPDate: ...
    def __isub__(self, seconds: int) -> HTTPDate: ...
    def __add__(self, seconds: int) -> HTTPDate: ...
    @overload
    def __sub__(self, other: HTTPDate) -> int: ...
    @overload
    def __sub__(self, seconds: int) -> HTTPDate: ...
    def __le__(self, other: HTTPDate) -> bool: ...
    def assign(self, copy: HTTPDate) -> HTTPDate: ...
    @staticmethod
    def now() -> HTTPDate: ...
    def is_valid(self) -> bool: ...
    def get_string(self) -> str: ...
    def get_time(self) -> int: ...
    def compare_to(self, other: HTTPDate) -> int: ...
    def input(self, _in: istream) -> bool: ...
    def output(self, out: ostream) -> None: ...
    isValid = is_valid
    getString = get_string
    getTime = get_time
    compareTo = compare_to

class HTTPCookie:
    DtoolClassDict: ClassVar[dict[str, Any]]
    name: str
    value: str
    domain: str
    path: str
    expires: HTTPDate
    secure: bool
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: HTTPCookie) -> None: ...
    @overload
    def __init__(self, format: str, url: URLSpec) -> None: ...
    @overload
    def __init__(self, name: str, path: str, domain: str) -> None: ...
    def __lt__(self, other: HTTPCookie) -> bool: ...
    def set_name(self, name: str) -> None: ...
    def get_name(self) -> str: ...
    def set_value(self, value: str) -> None: ...
    def get_value(self) -> str: ...
    def set_domain(self, domain: str) -> None: ...
    def get_domain(self) -> str: ...
    def set_path(self, path: str) -> None: ...
    def get_path(self) -> str: ...
    def set_expires(self, expires: HTTPDate) -> None: ...
    def clear_expires(self) -> None: ...
    def has_expires(self) -> bool: ...
    def get_expires(self) -> HTTPDate: ...
    def set_secure(self, flag: bool) -> None: ...
    def get_secure(self) -> bool: ...
    def update_from(self, other: HTTPCookie) -> None: ...
    def parse_set_cookie(self, format: str, url: URLSpec) -> bool: ...
    def is_expired(self, now: HTTPDate = ...) -> bool: ...
    def matches_url(self, url: URLSpec) -> bool: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    VS_no_verify: ClassVar[Literal[0]]
    VS_no_date_check: ClassVar[Literal[1]]
    VS_normal: ClassVar[Literal[2]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: HTTPClient) -> None: ...
    def assign(self, copy: HTTPClient) -> HTTPClient: ...
    @staticmethod
    def init_random_seed() -> None: ...
    def set_proxy_spec(self, proxy_spec: str) -> None: ...
    def get_proxy_spec(self) -> str: ...
    def set_direct_host_spec(self, direct_host_spec: str) -> None: ...
    def get_direct_host_spec(self) -> str: ...
    def set_try_all_direct(self, try_all_direct: bool) -> None: ...
    def get_try_all_direct(self) -> bool: ...
    def clear_proxy(self) -> None: ...
    def add_proxy(self, scheme: str, proxy: URLSpec) -> None: ...
    def clear_direct_host(self) -> None: ...
    def add_direct_host(self, hostname: str) -> None: ...
    def get_proxies_for_url(self, url: URLSpec) -> str: ...
    def set_username(self, server: str, realm: str, username: str) -> None: ...
    def get_username(self, server: str, realm: str) -> str: ...
    def set_cookie(self, cookie: HTTPCookie) -> None: ...
    def clear_cookie(self, cookie: HTTPCookie) -> bool: ...
    def clear_all_cookies(self) -> None: ...
    def has_cookie(self, cookie: HTTPCookie) -> bool: ...
    def get_cookie(self, cookie: HTTPCookie) -> HTTPCookie: ...
    def copy_cookies_from(self, other: HTTPClient) -> None: ...
    def write_cookies(self, out: ostream) -> None: ...
    def send_cookies(self, out: ostream, url: URLSpec) -> None: ...
    def set_client_certificate_filename(self, filename: _Filename) -> None: ...
    def set_client_certificate_pem(self, pem: str) -> None: ...
    def set_client_certificate_passphrase(self, passphrase: str) -> None: ...
    def load_client_certificate(self) -> bool: ...
    def add_preapproved_server_certificate_filename(self, url: URLSpec, filename: _Filename) -> bool: ...
    def add_preapproved_server_certificate_pem(self, url: URLSpec, pem: str) -> bool: ...
    def add_preapproved_server_certificate_name(self, url: URLSpec, name: str) -> bool: ...
    def clear_preapproved_server_certificates(self, url: URLSpec) -> None: ...
    def clear_all_preapproved_server_certificates(self) -> None: ...
    def set_http_version(self, version: _HTTPEnum_HTTPVersion) -> None: ...
    def get_http_version(self) -> _HTTPEnum_HTTPVersion: ...
    def get_http_version_string(self) -> str: ...
    @staticmethod
    def parse_http_version_string(version: str) -> _HTTPEnum_HTTPVersion: ...
    def load_certificates(self, filename: _Filename) -> bool: ...
    def set_verify_ssl(self, verify_ssl: _HTTPClient_VerifySSL) -> None: ...
    def get_verify_ssl(self) -> _HTTPClient_VerifySSL: ...
    def set_cipher_list(self, cipher_list: str) -> None: ...
    def get_cipher_list(self) -> str: ...
    def make_channel(self, persistent_connection: bool) -> HTTPChannel: ...
    def post_form(self, url: URLSpec, body: str) -> HTTPChannel: ...
    def get_document(self, url: URLSpec) -> HTTPChannel: ...
    def get_header(self, url: URLSpec) -> HTTPChannel: ...
    @staticmethod
    def base64_encode(s: str) -> str: ...
    @staticmethod
    def base64_decode(s: str) -> str: ...
    @staticmethod
    def get_global_ptr() -> HTTPClient: ...
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
    VSNoVerify = VS_no_verify
    VSNoDateCheck = VS_no_date_check
    VSNormal = VS_normal

class HTTPEntityTag:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: HTTPEntityTag) -> None: ...
    @overload
    def __init__(self, text: str) -> None: ...
    @overload
    def __init__(self, weak: bool, tag: str) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: HTTPEntityTag) -> bool: ...
    def __le__(self, other: HTTPEntityTag) -> bool: ...
    def assign(self, copy: HTTPEntityTag) -> HTTPEntityTag: ...
    def is_weak(self) -> bool: ...
    def get_tag(self) -> str: ...
    def get_string(self) -> str: ...
    def strong_equiv(self, other: HTTPEntityTag) -> bool: ...
    def weak_equiv(self, other: HTTPEntityTag) -> bool: ...
    def compare_to(self, other: HTTPEntityTag) -> int: ...
    def output(self, out: ostream) -> None: ...
    isWeak = is_weak
    getTag = get_tag
    getString = get_string
    strongEquiv = strong_equiv
    weakEquiv = weak_equiv
    compareTo = compare_to

class DocumentSpec:
    DtoolClassDict: ClassVar[dict[str, Any]]
    url: URLSpec
    tag: HTTPEntityTag
    date: HTTPDate
    request_mode: _DocumentSpec_RequestMode
    cache_control: _DocumentSpec_CacheControl
    RM_any: ClassVar[Literal[0]]
    RM_equal: ClassVar[Literal[1]]
    RM_newer: ClassVar[Literal[2]]
    RM_equal_or_newer: ClassVar[Literal[3]]
    CC_allow_cache: ClassVar[Literal[0]]
    CC_revalidate: ClassVar[Literal[1]]
    CC_no_cache: ClassVar[Literal[2]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, copy: DocumentSpec) -> None: ...
    @overload
    def __init__(self, url: URLSpec | str) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: DocumentSpec) -> bool: ...
    def __le__(self, other: DocumentSpec) -> bool: ...
    def assign(self, copy: DocumentSpec) -> DocumentSpec: ...
    def compare_to(self, other: DocumentSpec) -> int: ...
    def set_url(self, url: URLSpec) -> None: ...
    def get_url(self) -> URLSpec: ...
    def set_tag(self, tag: HTTPEntityTag) -> None: ...
    def has_tag(self) -> bool: ...
    def get_tag(self) -> HTTPEntityTag: ...
    def clear_tag(self) -> None: ...
    def set_date(self, date: HTTPDate) -> None: ...
    def has_date(self) -> bool: ...
    def get_date(self) -> HTTPDate: ...
    def clear_date(self) -> None: ...
    def set_request_mode(self, request_mode: _DocumentSpec_RequestMode) -> None: ...
    def get_request_mode(self) -> _DocumentSpec_RequestMode: ...
    def set_cache_control(self, cache_control: _DocumentSpec_CacheControl) -> None: ...
    def get_cache_control(self) -> _DocumentSpec_CacheControl: ...
    def input(self, _in: istream) -> bool: ...
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
    RMAny = RM_any
    RMEqual = RM_equal
    RMNewer = RM_newer
    RMEqualOrNewer = RM_equal_or_newer
    CCAllowCache = CC_allow_cache
    CCRevalidate = CC_revalidate
    CCNoCache = CC_no_cache

class HTTPChannel(TypedReferenceCount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    SC_incomplete: ClassVar[Literal[0]]
    SC_internal_error: ClassVar[Literal[1]]
    SC_no_connection: ClassVar[Literal[2]]
    SC_timeout: ClassVar[Literal[3]]
    SC_lost_connection: ClassVar[Literal[4]]
    SC_non_http_response: ClassVar[Literal[5]]
    SC_invalid_http: ClassVar[Literal[6]]
    SC_socks_invalid_version: ClassVar[Literal[7]]
    SC_socks_no_acceptable_login_method: ClassVar[Literal[8]]
    SC_socks_refused: ClassVar[Literal[9]]
    SC_socks_no_connection: ClassVar[Literal[10]]
    SC_ssl_internal_failure: ClassVar[Literal[11]]
    SC_ssl_no_handshake: ClassVar[Literal[12]]
    SC_http_error_watermark: ClassVar[Literal[13]]
    SC_ssl_invalid_server_certificate: ClassVar[Literal[14]]
    SC_ssl_self_signed_server_certificate: ClassVar[Literal[15]]
    SC_ssl_unexpected_server: ClassVar[Literal[16]]
    SC_download_open_error: ClassVar[Literal[17]]
    SC_download_write_error: ClassVar[Literal[18]]
    SC_download_invalid_range: ClassVar[Literal[19]]
    def __init__(self, __param0: HTTPChannel) -> None: ...
    def get_client(self) -> HTTPClient: ...
    def is_valid(self) -> bool: ...
    def is_connection_ready(self) -> bool: ...
    def get_url(self) -> URLSpec: ...
    def get_document_spec(self) -> DocumentSpec: ...
    def get_http_version(self) -> _HTTPEnum_HTTPVersion: ...
    def get_http_version_string(self) -> str: ...
    def get_status_code(self) -> int: ...
    def get_status_string(self) -> str: ...
    def get_www_realm(self) -> str: ...
    def get_proxy_realm(self) -> str: ...
    def get_redirect(self) -> URLSpec: ...
    def get_header_value(self, key: str) -> str: ...
    def get_num_redirect_steps(self) -> int: ...
    def get_redirect_step(self, n: int) -> URLSpec: ...
    def set_persistent_connection(self, persistent_connection: bool) -> None: ...
    def get_persistent_connection(self) -> bool: ...
    def will_close_connection(self) -> bool: ...
    def set_allow_proxy(self, allow_proxy: bool) -> None: ...
    def get_allow_proxy(self) -> bool: ...
    def set_proxy_tunnel(self, proxy_tunnel: bool) -> None: ...
    def get_proxy_tunnel(self) -> bool: ...
    def set_connect_timeout(self, timeout_seconds: float) -> None: ...
    def get_connect_timeout(self) -> float: ...
    def set_blocking_connect(self, blocking_connect: bool) -> None: ...
    def get_blocking_connect(self) -> bool: ...
    def set_http_timeout(self, timeout_seconds: float) -> None: ...
    def get_http_timeout(self) -> float: ...
    def set_skip_body_size(self, skip_body_size: int) -> None: ...
    def get_skip_body_size(self) -> int: ...
    def set_idle_timeout(self, idle_timeout: float) -> None: ...
    def get_idle_timeout(self) -> float: ...
    def set_download_throttle(self, download_throttle: bool) -> None: ...
    def get_download_throttle(self) -> bool: ...
    def set_max_bytes_per_second(self, max_bytes_per_second: float) -> None: ...
    def get_max_bytes_per_second(self) -> float: ...
    def set_max_updates_per_second(self, max_updates_per_second: float) -> None: ...
    def get_max_updates_per_second(self) -> float: ...
    def set_content_type(self, content_type: str) -> None: ...
    def get_content_type(self) -> str: ...
    def set_expected_file_size(self, file_size: int) -> None: ...
    def get_file_size(self) -> int: ...
    def is_file_size_known(self) -> bool: ...
    def get_first_byte_requested(self) -> int: ...
    def get_last_byte_requested(self) -> int: ...
    def get_first_byte_delivered(self) -> int: ...
    def get_last_byte_delivered(self) -> int: ...
    def write_headers(self, out: ostream) -> None: ...
    def reset(self) -> None: ...
    def preserve_status(self) -> None: ...
    def clear_extra_headers(self) -> None: ...
    def send_extra_header(self, key: str, value: str) -> None: ...
    def get_document(self, url: DocumentSpec) -> bool: ...
    def get_subdocument(self, url: DocumentSpec, first_byte: int, last_byte: int) -> bool: ...
    def get_header(self, url: DocumentSpec) -> bool: ...
    def post_form(self, url: DocumentSpec, body: str) -> bool: ...
    def put_document(self, url: DocumentSpec, body: str) -> bool: ...
    def delete_document(self, url: DocumentSpec) -> bool: ...
    def get_trace(self, url: DocumentSpec) -> bool: ...
    def connect_to(self, url: DocumentSpec) -> bool: ...
    def get_options(self, url: DocumentSpec) -> bool: ...
    def begin_get_document(self, url: DocumentSpec) -> None: ...
    def begin_get_subdocument(self, url: DocumentSpec, first_byte: int, last_byte: int) -> None: ...
    def begin_get_header(self, url: DocumentSpec) -> None: ...
    def begin_post_form(self, url: DocumentSpec, body: str) -> None: ...
    def run(self) -> bool: ...
    def begin_connect_to(self, url: DocumentSpec) -> None: ...
    def open_read_body(self) -> ISocketStream: ...
    def close_read_body(self, stream: istream) -> None: ...
    def download_to_file(self, filename: _Filename, subdocument_resumes: bool = ...) -> bool: ...
    def download_to_ram(self, ramfile: Ramfile, subdocument_resumes: bool = ...) -> bool: ...
    def download_to_stream(self, strm: ostream, subdocument_resumes: bool = ...) -> bool: ...
    def get_connection(self) -> SocketStream: ...
    def get_bytes_downloaded(self) -> int: ...
    def get_bytes_requested(self) -> int: ...
    def is_download_complete(self) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
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
    getClassType = get_class_type
    getRedirectSteps = get_redirect_steps
    SCIncomplete = SC_incomplete
    SCInternalError = SC_internal_error
    SCNoConnection = SC_no_connection
    SCTimeout = SC_timeout
    SCLostConnection = SC_lost_connection
    SCNonHttpResponse = SC_non_http_response
    SCInvalidHttp = SC_invalid_http
    SCSocksInvalidVersion = SC_socks_invalid_version
    SCSocksNoAcceptableLoginMethod = SC_socks_no_acceptable_login_method
    SCSocksRefused = SC_socks_refused
    SCSocksNoConnection = SC_socks_no_connection
    SCSslInternalFailure = SC_ssl_internal_failure
    SCSslNoHandshake = SC_ssl_no_handshake
    SCHttpErrorWatermark = SC_http_error_watermark
    SCSslInvalidServerCertificate = SC_ssl_invalid_server_certificate
    SCSslSelfSignedServerCertificate = SC_ssl_self_signed_server_certificate
    SCSslUnexpectedServer = SC_ssl_unexpected_server
    SCDownloadOpenError = SC_download_open_error
    SCDownloadWriteError = SC_download_write_error
    SCDownloadInvalidRange = SC_download_invalid_range

class Decompressor:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def progress(self) -> float: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: Decompressor) -> None: ...
    @overload
    def initiate(self, source_file: _Filename) -> int: ...
    @overload
    def initiate(self, source_file: _Filename, dest_file: _Filename) -> int: ...
    def run(self) -> int: ...
    @overload
    def decompress(self, source_file: _Filename) -> bool: ...
    @overload
    def decompress(self, source_and_dest_file: Ramfile) -> bool: ...
    def get_progress(self) -> float: ...
    getProgress = get_progress

class DownloadDb:
    DtoolClassDict: ClassVar[dict[str, Any]]
    Status_incomplete: ClassVar[Literal[0]]
    Status_complete: ClassVar[Literal[1]]
    Status_decompressed: ClassVar[Literal[2]]
    Status_extracted: ClassVar[Literal[3]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: DownloadDb) -> None: ...
    @overload
    def __init__(self, server_file: Ramfile | _Filename, client_file: _Filename) -> None: ...
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def write_version_map(self, out: ostream) -> None: ...
    def write_client_db(self, file: _Filename) -> bool: ...
    def write_server_db(self, file: _Filename) -> bool: ...
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
    def client_multifile_exists(self, mfname: str) -> bool: ...
    def client_multifile_complete(self, mfname: str) -> bool: ...
    def client_multifile_decompressed(self, mfname: str) -> bool: ...
    def client_multifile_extracted(self, mfname: str) -> bool: ...
    def get_client_multifile_hash(self, mfname: str) -> HashVal: ...
    def set_client_multifile_hash(self, mfname: str, val: HashVal) -> None: ...
    def get_server_multifile_hash(self, mfname: str) -> HashVal: ...
    def set_server_multifile_hash(self, mfname: str, val: HashVal) -> None: ...
    def delete_client_multifile(self, mfname: str) -> None: ...
    def add_client_multifile(self, server_mfname: str) -> None: ...
    def expand_client_multifile(self, mfname: str) -> None: ...
    def create_new_server_db(self) -> None: ...
    def server_add_multifile(self, mfname: str, phase: float, size: int, status: int) -> None: ...
    def server_add_file(self, mfname: str, fname: str) -> None: ...
    def add_version(self, name: _Filename, hash: HashVal, version: int) -> None: ...
    def insert_new_version(self, name: _Filename, hash: HashVal) -> None: ...
    def has_version(self, name: _Filename) -> bool: ...
    def get_num_versions(self, name: _Filename) -> int: ...
    def set_num_versions(self, name: _Filename, num_versions: int) -> None: ...
    def get_version(self, name: _Filename, hash: HashVal) -> int: ...
    def get_hash(self, name: _Filename, version: int) -> HashVal: ...
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
    StatusIncomplete = Status_incomplete
    StatusComplete = Status_complete
    StatusDecompressed = Status_decompressed
    StatusExtracted = Status_extracted

class Extractor:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def progress(self) -> float: ...
    def __init__(self) -> None: ...
    def set_multifile(self, multifile_name: _Filename) -> bool: ...
    def set_extract_dir(self, extract_dir: _Filename) -> None: ...
    def reset(self) -> None: ...
    def request_subfile(self, subfile_name: _Filename) -> bool: ...
    def request_all_subfiles(self) -> int: ...
    def step(self) -> int: ...
    def get_progress(self) -> float: ...
    def run(self) -> bool: ...
    setMultifile = set_multifile
    setExtractDir = set_extract_dir
    requestSubfile = request_subfile
    requestAllSubfiles = request_all_subfiles
    getProgress = get_progress

class MultiplexStream(ostream):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self) -> None: ...
    def add_ostream(self, out: ostream, delete_later: bool = ...) -> None: ...
    def add_standard_output(self) -> None: ...
    def add_file(self, file: _Filename) -> bool: ...
    def add_system_debug(self) -> None: ...
    def flush(self) -> None: ...
    addOstream = add_ostream
    addStandardOutput = add_standard_output
    addFile = add_file
    addSystemDebug = add_system_debug

class VirtualFileHTTP(VirtualFile):
    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getClassType = get_class_type

class VirtualFileMountHTTP(VirtualFileMount):
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, root: URLSpec, http: HTTPClient = ...) -> None: ...
    def get_http_client(self) -> HTTPClient: ...
    def get_root(self) -> URLSpec: ...
    @staticmethod
    def reload_vfs_mount_url() -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getHttpClient = get_http_client
    getRoot = get_root
    reloadVfsMountUrl = reload_vfs_mount_url
    getClassType = get_class_type

class Patcher:
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: Patcher) -> None: ...
    @overload
    def __init__(self, buffer: Buffer) -> None: ...
    def initiate(self, patch: _Filename, infile: _Filename) -> int: ...
    def run(self) -> int: ...
    def get_progress(self) -> float: ...
    getProgress = get_progress

class StringStream(iostream):
    DtoolClassDict: ClassVar[dict[str, Any]]
    data: Any
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source: Any) -> None: ...
    def clear_data(self) -> None: ...
    def get_data_size(self) -> int: ...
    def get_data(self) -> bytes: ...
    def set_data(self, data: Any) -> None: ...
    clearData = clear_data
    getDataSize = get_data_size
    getData = get_data
    setData = set_data

def check_crc(name: _Filename) -> int: ...
def check_adler(name: _Filename) -> int: ...
checkCrc = check_crc
checkAdler = check_adler