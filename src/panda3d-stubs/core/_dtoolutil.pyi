from _typeshed import StrOrBytesPath
from collections.abc import Iterator, MutableMapping, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d._typing import SearchPathLike
from panda3d.core._dtoolbase import TypeHandle

_ios_base_seekdir: TypeAlias = Literal[0, 1, 2]
_ios_base_openmode: TypeAlias = int
_TextEncoder_Encoding: TypeAlias = Literal[0, 1, 2, 2]
_Filename_Type: TypeAlias = Literal[0, 1, 2]

class ios_base:
    """We need to expose one method in each class to force it to publish.
    But we'd like to expose some of these methods anyway, so no
    problem.
    """

    beg: Final = 0
    Beg: Final = 0
    cur: Final = 1
    Cur: Final = 1
    end: Final = 2
    End: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]

class basic_ios_char(ios_base):
    def good(self) -> bool: ...
    def eof(self) -> bool: ...
    def fail(self) -> bool: ...
    def bad(self) -> bool: ...
    def clear(self) -> None: ...

class istream(basic_ios_char):
    def upcast_to_basic_ios_char(self) -> basic_ios_char: ...
    def get(self) -> int: ...
    def tellg(self) -> int: ...
    @overload
    def seekg(self, pos: int) -> None: ...
    @overload
    def seekg(self, off: int, dir: _ios_base_seekdir) -> None: ...
    upcastToBasicIosChar = upcast_to_basic_ios_char

class ostream(basic_ios_char):
    def upcast_to_basic_ios_char(self) -> basic_ios_char: ...
    def put(self, c: str) -> None: ...
    def flush(self) -> None: ...
    def tellp(self) -> int: ...
    @overload
    def seekp(self, pos: int) -> None: ...
    @overload
    def seekp(self, off: int, dir: _ios_base_seekdir) -> None: ...
    upcastToBasicIosChar = upcast_to_basic_ios_char

class iostream(istream, ostream):  # type: ignore[misc]
    def upcast_to_istream(self) -> istream: ...
    def upcast_to_ostream(self) -> ostream: ...
    upcastToIstream = upcast_to_istream
    upcastToOstream = upcast_to_ostream

class fstream(iostream):
    def __init__(self) -> None: ...
    def close(self) -> None: ...

class ifstream(istream):
    def __init__(self) -> None: ...
    def close(self) -> None: ...

class ofstream(ostream):
    def __init__(self) -> None: ...
    def close(self) -> None: ...

class IFileStream(istream):
    """Implements a C++ stream object suitable for reading from files on disk.
    This is similar to ifstream, but it provides low-level support for Panda's
    simple-threading implementation (using this interface will block only the
    current thread, rather than the entire process, on I/O waits).
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, filename: str, mode: _ios_base_openmode = ...) -> None: ...
    def open(self, filename: str, mode: _ios_base_openmode = ...) -> None: ...
    def close(self) -> None: ...

class OFileStream(ostream):
    """Implements a C++ stream object suitable for writing to files on disk.  This
    is similar to ofstream, but it provides low-level support for Panda's
    simple-threading implementation (using this interface will block only the
    current thread, rather than the entire process, on I/O waits).
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, filename: str, mode: _ios_base_openmode = ...) -> None: ...
    def open(self, filename: str, mode: _ios_base_openmode = ...) -> None: ...
    def close(self) -> None: ...

class FileStream(iostream):
    """Implements a C++ stream object suitable for reading from and/or writing to
    files on disk.  This is similar to fstream, but it provides low-level
    support for Panda's simple-threading implementation (using this interface
    will block only the current thread, rather than the entire process, on I/O
    waits).
    """

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, filename: str, mode: _ios_base_openmode = ...) -> None: ...
    def open(self, filename: str, mode: _ios_base_openmode = ...) -> None: ...
    def close(self) -> None: ...

class TextEncoder:
    """This class can be used to convert text between multiple representations,
    e.g.  UTF-8 to UTF-16.  You may use it as a static class object, passing
    the encoding each time, or you may create an instance and use that object,
    which will record the current encoding and retain the current string.

    This class is also a base class of TextNode, which inherits this
    functionality.
    """

    E_iso8859: Final = 0
    EIso8859: Final = 0
    E_utf8: Final = 1
    EUtf8: Final = 1
    E_utf16be: Final = 2
    EUtf16be: Final = 2
    E_unicode: Final = 2
    EUnicode: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    default_encoding: _TextEncoder_Encoding
    text: str
    def __init__(self, copy: TextEncoder = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_encoding(self, encoding: _TextEncoder_Encoding) -> None:
        """Specifies how the string set via set_text() is to be interpreted.  The
        default, E_iso8859, means a standard string with one-byte characters (i.e.
        ASCII).  Other encodings are possible to take advantage of character sets
        with more than 256 characters.

        This affects only future calls to set_text(); it does not change text that
        was set previously.
        """
    def get_encoding(self) -> _TextEncoder_Encoding:
        """Returns the encoding by which the string set via set_text() is to be
        interpreted.  See set_encoding().
        """
    @staticmethod
    def set_default_encoding(encoding: _TextEncoder_Encoding) -> None:
        """Specifies the default encoding to be used for all subsequently created
        TextEncoder objects.  See set_encoding().
        """
    @staticmethod
    def get_default_encoding() -> _TextEncoder_Encoding:
        """Specifies the default encoding to be used for all subsequently created
        TextEncoder objects.  See set_encoding().
        """
    @overload
    def set_text(self, text: str) -> None: ...
    @overload
    def set_text(self, text: bytes, encoding: _TextEncoder_Encoding) -> None: ...
    def clear_text(self) -> None:
        """Removes the text from the TextEncoder."""
    def has_text(self) -> bool: ...
    def make_upper(self) -> None:
        """Adjusts the text stored within the encoder to all uppercase letters
        (preserving accent marks correctly).
        """
    def make_lower(self) -> None:
        """Adjusts the text stored within the encoder to all lowercase letters
        (preserving accent marks correctly).
        """
    @overload
    def get_text(self) -> str:
        """`(self)`:
        Returns the current text, as encoded via the current encoding system.

        `(self, encoding: _TextEncoder_Encoding)`:
        Returns the current text, as encoded via the indicated encoding system.
        """
    @overload
    def get_text(self, encoding: _TextEncoder_Encoding) -> bytes: ...
    def append_text(self, text: str) -> None: ...
    def append_unicode_char(self, character: int) -> None:
        """Appends a single character to the end of the stored text.  This may be a
        wide character, up to 16 bits in Unicode.
        """
    def get_num_chars(self) -> int:
        """Returns the number of characters in the stored text.  This is a count of
        wide characters, after the string has been decoded according to
        set_encoding().
        """
    def get_unicode_char(self, index: int) -> int:
        """Returns the Unicode value of the nth character in the stored text.  This
        may be a wide character (greater than 255), after the string has been
        decoded according to set_encoding().
        """
    def set_unicode_char(self, index: int, character: int) -> None:
        """Sets the Unicode value of the nth character in the stored text.  This may
        be a wide character (greater than 255), after the string has been decoded
        according to set_encoding().
        """
    def get_encoded_char(self, index: int, encoding: _TextEncoder_Encoding = ...) -> str:
        """Returns the nth char of the stored text, as a one-, two-, or three-byte
        encoded string.
        """
    def get_text_as_ascii(self) -> str:
        """Returns the text associated with the node, converted as nearly as possible
        to a fully-ASCII representation.  This means replacing accented letters
        with their unaccented ASCII equivalents.

        It is possible that some characters in the string cannot be converted to
        ASCII.  (The string may involve symbols like the copyright symbol, for
        instance, or it might involve letters in some other alphabet such as Greek
        or Cyrillic, or even Latin letters like thorn or eth that are not part of
        the ASCII character set.)  In this case, as much of the string as possible
        will be converted to ASCII, and the nonconvertible characters will remain
        encoded in the encoding specified by set_encoding().
        """
    @staticmethod
    def reencode_text(text: str, _from: _TextEncoder_Encoding, to: _TextEncoder_Encoding) -> str:
        """Given the indicated text string, which is assumed to be encoded via the
        encoding "from", decodes it and then reencodes it into the encoding "to",
        and returns the newly encoded string.  This does not change or affect any
        properties on the TextEncoder itself.
        """
    @staticmethod
    def unicode_isalpha(character: int) -> bool:
        """Returns true if the indicated character is an alphabetic letter, false
        otherwise.  This is akin to ctype's isalpha(), extended to Unicode.
        """
    @staticmethod
    def unicode_isdigit(character: int) -> bool:
        """Returns true if the indicated character is a numeric digit, false
        otherwise.  This is akin to ctype's isdigit(), extended to Unicode.
        """
    @staticmethod
    def unicode_ispunct(character: int) -> bool:
        """Returns true if the indicated character is a punctuation mark, false
        otherwise.  This is akin to ctype's ispunct(), extended to Unicode.
        """
    @staticmethod
    def unicode_islower(character: int) -> bool:
        """Returns true if the indicated character is a lowercase letter, false
        otherwise.  This is akin to ctype's islower(), extended to Unicode.
        """
    @staticmethod
    def unicode_isupper(character: int) -> bool:
        """Returns true if the indicated character is an uppercase letter, false
        otherwise.  This is akin to ctype's isupper(), extended to Unicode.
        """
    @staticmethod
    def unicode_isspace(character: int) -> bool:
        """Returns true if the indicated character is a whitespace letter, false
        otherwise.  This is akin to ctype's isspace(), extended to Unicode.
        """
    @staticmethod
    def unicode_toupper(character: int) -> int:
        """Returns the uppercase equivalent of the given Unicode character.  This is
        akin to ctype's toupper(), extended to Unicode.
        """
    @staticmethod
    def unicode_tolower(character: int) -> int:
        """Returns the uppercase equivalent of the given Unicode character.  This is
        akin to ctype's tolower(), extended to Unicode.
        """
    @staticmethod
    def upper(source: str, encoding: _TextEncoder_Encoding = ...) -> str:
        """`(source: str)`:
        Converts the string to uppercase, assuming the string is encoded in the
        default encoding.

        `(source: str, encoding: _TextEncoder_Encoding)`:
        Converts the string to uppercase, assuming the string is encoded in the
        indicated encoding.
        """
    @staticmethod
    def lower(source: str, encoding: _TextEncoder_Encoding = ...) -> str:
        """`(source: str)`:
        Converts the string to lowercase, assuming the string is encoded in the
        default encoding.

        `(source: str, encoding: _TextEncoder_Encoding)`:
        Converts the string to lowercase, assuming the string is encoded in the
        indicated encoding.
        """
    def set_wtext(self, wtext: str) -> None:
        """Changes the text that is stored in the encoder.  Subsequent calls to
        get_wtext() will return this same string, while get_text() will return the
        encoded version of the string.
        """
    def get_wtext(self) -> str:
        """Returns the text associated with the TextEncoder, as a wide-character
        string.
        """
    def append_wtext(self, text: str) -> None:
        """Appends the indicates string to the end of the stored wide-character text."""
    def get_wtext_as_ascii(self) -> str:
        """Returns the text associated with the node, converted as nearly as possible
        to a fully-ASCII representation.  This means replacing accented letters
        with their unaccented ASCII equivalents.

        It is possible that some characters in the string cannot be converted to
        ASCII.  (The string may involve symbols like the copyright symbol, for
        instance, or it might involve letters in some other alphabet such as Greek
        or Cyrillic, or even Latin letters like thorn or eth that are not part of
        the ASCII character set.)  In this case, as much of the string as possible
        will be converted to ASCII, and the nonconvertible characters will remain
        in their original form.
        """
    def is_wtext(self) -> bool:
        """Returns true if any of the characters in the string returned by get_wtext()
        are out of the range of an ASCII character (and, therefore, get_wtext()
        should be called in preference to get_text()).
        """
    @staticmethod
    def encode_wchar(ch: int, encoding: _TextEncoder_Encoding) -> bytes:
        """Encodes a single Unicode character into a one-, two-, three-, or four-byte
        string, according to the given encoding system.
        """
    def encode_wtext(self, wtext: str, encoding: _TextEncoder_Encoding = ...) -> bytes:
        """`(self, wtext: str)`:
        Encodes a wide-text string into a single-char string, according to the
        current encoding.

        `(self, wtext: str, encoding: _TextEncoder_Encoding)`:
        Encodes a wide-text string into a single-char string, according to the
        given encoding.
        """
    def decode_text(self, text: bytes, encoding: _TextEncoder_Encoding = ...) -> str: ...
    setEncoding = set_encoding
    getEncoding = get_encoding
    setDefaultEncoding = set_default_encoding
    getDefaultEncoding = get_default_encoding
    setText = set_text
    clearText = clear_text
    hasText = has_text
    makeUpper = make_upper
    makeLower = make_lower
    getText = get_text
    appendText = append_text
    appendUnicodeChar = append_unicode_char
    getNumChars = get_num_chars
    getUnicodeChar = get_unicode_char
    setUnicodeChar = set_unicode_char
    getEncodedChar = get_encoded_char
    getTextAsAscii = get_text_as_ascii
    reencodeText = reencode_text
    unicodeIsalpha = unicode_isalpha
    unicodeIsdigit = unicode_isdigit
    unicodeIspunct = unicode_ispunct
    unicodeIslower = unicode_islower
    unicodeIsupper = unicode_isupper
    unicodeIsspace = unicode_isspace
    unicodeToupper = unicode_toupper
    unicodeTolower = unicode_tolower
    setWtext = set_wtext
    getWtext = get_wtext
    appendWtext = append_wtext
    getWtextAsAscii = get_wtext_as_ascii
    isWtext = is_wtext
    encodeWchar = encode_wchar
    encodeWtext = encode_wtext
    decodeText = decode_text

class Filename:
    """The name of a file, such as a texture file or an Egg file.  Stores the full
    pathname, and includes functions for extracting out the directory prefix
    part and the file extension and stuff.

    A Filename is also aware of the mapping between the Unix-like filename
    convention we use internally, and the local OS's specific filename
    convention, and it knows how to perform basic OS-specific I/O, like testing
    for file existence and searching a searchpath, as well as the best way to
    open an fstream for reading or writing.
    """

    T_general: Final = 0
    TGeneral: Final = 0
    T_dso: Final = 1
    TDso: Final = 1
    T_executable: Final = 2
    TExecutable: Final = 2
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, path: StrOrBytesPath = ...) -> None:
        """`(self)`:
        Creates an empty Filename.

        `(self, dirname: Filename, basename: Filename)`:
        This constructor composes the filename out of a directory part and a
        basename part.  It will insert an intervening '/' if necessary.
        """
    @overload
    def __init__(self, dirname: StrOrBytesPath, basename: StrOrBytesPath) -> None: ...
    def __getitem__(self, n: int) -> str: ...
    def __fspath__(self) -> str: ...
    def __iadd__(self, other: str) -> Self: ...
    def __add__(self, other: str) -> Filename: ...
    def __truediv__(self, other: StrOrBytesPath) -> Filename: ...
    def __eq__(self, __other: object) -> bool:
        """Comparison operators are handy."""
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: str) -> bool: ...
    def __bool__(self) -> bool:
        """Returns true if the Filename is valid (not empty), or false if it is an
        empty string.

        This implements the Python equivalent to operator bool.  Defining an actual
        operator bool method for C++ use would work too, but it seems to cause too
        many ambiguities for the C++ compiler, so we use this Python-only approach
        instead.
        """
    @staticmethod
    def text_filename(filename: StrOrBytesPath) -> Filename:
        """Static constructors to explicitly create a filename that refers to a text
        or binary file.  This is in lieu of calling set_text() or set_binary() or
        set_type().
        """
    @staticmethod
    def binary_filename(filename: StrOrBytesPath) -> Filename: ...
    @staticmethod
    def dso_filename(filename: str) -> Filename: ...
    @staticmethod
    def executable_filename(filename: str) -> Filename: ...
    @staticmethod
    def pattern_filename(filename: str) -> Filename:
        """Constructs a filename that represents a sequence of numbered files.  See
        set_pattern().
        """
    @staticmethod
    def from_os_specific(os_specific: str, type: _Filename_Type = ...) -> Filename:
        """This named constructor returns a Panda-style filename (that is, using
        forward slashes, and no drive letter) based on the supplied filename string
        that describes a filename in the local system conventions (for instance, on
        Windows, it may use backslashes or begin with a drive letter and a colon).

        Use this function to create a Filename from an externally-given filename
        string.  Use to_os_specific() again later to reconvert it back to the local
        operating system's conventions.

        This function will do the right thing even if the filename is partially
        local conventions and partially Panda conventions; e.g.  some backslashes
        and some forward slashes.
        """
    @staticmethod
    def from_os_specific_w(os_specific: str, type: _Filename_Type = ...) -> Filename:
        """The wide-string variant of from_os_specific(). Returns a new Filename,
        converted from an os-specific wide-character string.
        """
    @staticmethod
    def expand_from(user_string: str, type: _Filename_Type = ...) -> Filename:
        """Returns the same thing as from_os_specific(), but embedded environment
        variable references (e.g.  "$DMODELS/foo.txt") are expanded out.  It also
        automatically elevates the file to its true case if needed.
        """
    @staticmethod
    def temporary(dirname: str, prefix: str, suffix: str = ..., type: _Filename_Type = ...) -> Filename:
        """Generates a temporary filename within the indicated directory, using the
        indicated prefix.  If the directory is empty, a system-defined directory is
        chosen instead.

        The generated filename did not exist when the Filename checked, but since
        it does not specifically create the file, it is possible that another
        process could simultaneously create a file by the same name.
        """
    @staticmethod
    def get_home_directory() -> Filename:
        """Returns a path to the user's home directory, if such a thing makes sense in
        the current OS, or to the nearest equivalent.  This may or may not be
        directly writable by the application.
        """
    @staticmethod
    def get_temp_directory() -> Filename:
        """Returns a path to a system-defined temporary directory."""
    @staticmethod
    def get_user_appdata_directory() -> Filename:
        """Returns a path to a system-defined directory appropriate for creating a
        subdirectory for storing application-specific data, specific to the current
        user.
        """
    @staticmethod
    def get_common_appdata_directory() -> Filename:
        """Returns a path to a system-defined directory appropriate for creating a
        subdirectory for storing application-specific data, common to all users.
        """
    @overload
    def assign(self, copy: StrOrBytesPath) -> Self:
        """Assignment is via the = operator."""
    @overload
    def assign(self, filename: str) -> Self: ...
    def c_str(self) -> str: ...
    def empty(self) -> bool: ...
    def length(self) -> int: ...
    def substr(self, begin: int, end: int = ...) -> str: ...
    def get_fullpath(self) -> str:
        """Returns the entire filename: directory, basename, extension.  This is the
        same thing returned by the string typecast operator.
        """
    def get_fullpath_w(self) -> str:
        """Returns the entire filename as a wide-character string."""
    def get_dirname(self) -> str:
        """Returns the directory part of the filename.  This is everything in the
        filename up to, but not including the rightmost slash.
        """
    def get_basename(self) -> str:
        """Returns the basename part of the filename.  This is everything in the
        filename after the rightmost slash, including any extensions.
        """
    def get_fullpath_wo_extension(self) -> str:
        """Returns the full filename--directory and basename parts--except for the
        extension.
        """
    def get_basename_wo_extension(self) -> str:
        """Returns the basename part of the filename, without the file extension."""
    def get_extension(self) -> str:
        """Returns the file extension.  This is everything after the rightmost dot, if
        there is one, or the empty string if there is not.
        """
    def set_fullpath(self, s: str) -> None:
        """Replaces the entire filename: directory, basename, extension.  This can
        also be achieved with the assignment operator.
        """
    def set_dirname(self, s: str) -> None:
        """Replaces the directory part of the filename.  This is everything in the
        filename up to, but not including the rightmost slash.
        """
    def set_basename(self, s: str) -> None:
        """Replaces the basename part of the filename.  This is everything in the
        filename after the rightmost slash, including any extensions.
        """
    def set_fullpath_wo_extension(self, s: str) -> None:
        """Replaces the full filename--directory and basename parts--except for the
        extension.
        """
    def set_basename_wo_extension(self, s: str) -> None:
        """Replaces the basename part of the filename, without the file extension."""
    def set_extension(self, s: str) -> None:
        """Replaces the file extension.  This is everything after the rightmost dot,
        if there is one, or the empty string if there is not.
        """
    def set_binary(self) -> None:
        """Setting these flags appropriately is helpful when opening or searching
        for a file; it helps the Filename resolve OS-specific conventions (for
        instance, that dynamic library names should perhaps be changed from .so
        to .dll).
        """
    def set_text(self) -> None:
        """Indicates that the filename represents a text file.  This is primarily
        relevant to the read_file() and write_file() methods, so they can set the
        appropriate flags to the OS.
        """
    def is_binary(self) -> bool:
        """Returns true if the Filename has been indicated to represent a binary file
        via a previous call to set_binary().  It is possible that neither
        is_binary() nor is_text() will be true, if neither set_binary() nor
        set_text() was ever called.
        """
    def is_text(self) -> bool:
        """Returns true if the Filename has been indicated to represent a text file
        via a previous call to set_text().  It is possible that neither is_binary()
        nor is_text() will be true, if neither set_binary() nor set_text() was ever
        called.
        """
    def is_binary_or_text(self) -> bool:
        """Returns true either is_binary() or is_text() is true; that is, that the
        filename has been specified as either binary or text.  If this is false,
        the filename has not been specified.
        """
    def set_type(self, type: _Filename_Type) -> None:
        """Sets the type of the file represented by the filename.  This is useful for
        to_os_specific(), resolve_filename(), test_existence(), and all such real-
        world access functions.  It helps the Filename know how to map the internal
        filename to the OS-specific filename (for instance, maybe executables
        should have an .exe extension).
        """
    def get_type(self) -> _Filename_Type:
        """Returns the type of the file represented by the filename, as previously set
        by set_type().
        """
    def set_pattern(self, pattern: bool) -> None:
        """Sets the flag indicating whether this is a filename pattern.  When this is
        true, the filename is understood to be a placeholder for a numbered
        sequence of filename, such as an image sequence.  In this case, a sequence
        of one or more hash characters ("#") should appear in the filename string;
        these characters will be filled in with the corresponding number (or more)
        of digits representing the sequence number.  Sequence numbers always begin
        counting at 0.

        When this is true, methods like has_hash() and get_hash_to_end() and
        get_filename_index() may be called.  Methods like is_exists() will
        implicitly test for existance of filename sequence 0.
        """
    def get_pattern(self) -> bool:
        """Returns the flag indicating whether this is a filename pattern.  See
        set_pattern().
        """
    def has_hash(self) -> bool:
        """Returns true if the filename is indicated to be a filename pattern (that
        is, set_pattern(true) was called), and the filename pattern did include a
        sequence of hash marks, or false if it was not a filename pattern or did
        not include hash marks.  If this is true, then get_filename_index() will
        return a different filename each time.
        """
    def get_filename_index(self, index: int) -> Filename:
        """If the pattern flag is set for this Filename and the filename string
        actually includes a sequence of hash marks, then this returns a new
        Filename with the sequence of hash marks replaced by the indicated index
        number.

        If the pattern flag is not set for this Filename or it does not contain a
        sequence of hash marks, this quietly returns the original filename.
        """
    def get_hash_to_end(self) -> str:
        """Returns the part of the filename beginning at the hash sequence (if any),
        and continuing to the end of the filename.
        """
    def set_hash_to_end(self, s: str) -> None:
        """Replaces the part of the filename from the beginning of the hash sequence
        to the end of the filename.
        """
    def standardize(self) -> None:
        """Converts the filename to standard form by replacing consecutive slashes
        with a single slash, removing a trailing slash if present, and backing up
        over .. sequences within the filename where possible.
        """
    def is_local(self) -> bool:
        """Returns true if the filename is local, e.g.  does not begin with a slash,
        or false if the filename is fully specified from the root.
        """
    def is_fully_qualified(self) -> bool:
        """Returns true if the filename is fully qualified, e.g.  begins with a slash.
        This is almost, but not quite, the same thing as !is_local().  It's not
        exactly the same because a special case is made for filenames that begin
        with a single dot followed by a slash--these are considered to be fully
        qualified (they are explicitly relative to the current directory, and do
        not refer to a filename on a search path somewhere).
        """
    def make_absolute(self, start_directory: StrOrBytesPath = ...) -> None:
        """`(self)`:
        Converts the filename to a fully-qualified pathname from the root (if it is
        a relative pathname), and then standardizes it (see standardize()).

        This is sometimes a little problematic, since it may convert the file to
        its 'true' absolute pathname, which could be an ugly NFS-named file,
        irrespective of symbolic links (e.g.
        /.automount/dimbo/root/usr2/fit/people/drose instead of /fit/people/drose);
        besides being ugly, filenames like this may not be consistent across
        multiple different platforms.

        `(self, start_directory: Filename)`:
        Converts the filename to a fully-qualified filename from the root (if it is
        a relative filename), and then standardizes it (see standardize()).  This
        flavor accepts a specific starting directory that the filename is known to
        be relative to.
        """
    def make_canonical(self) -> bool:
        """Converts this filename to a canonical name by replacing the directory part
        with the fully-qualified directory part.  This is done by changing to that
        directory and calling getcwd().

        This has the effect of (a) converting relative paths to absolute paths (but
        see make_absolute() if this is the only effect you want), and (b) always
        resolving a given directory name to the same string, even if different
        symbolic links are traversed, and (c) changing nice symbolic-link paths
        like fit/people/drose to ugly NFS automounter names like
        hosts/dimbo/usr2/fit/people/drose.  This can be troubling, but sometimes
        this is exactly what you want, particularly if you're about to call
        make_relative_to() between two filenames.

        The return value is true if successful, or false on failure (usually
        because the directory name does not exist or cannot be chdir'ed into).
        """
    def make_true_case(self) -> bool:
        """On a case-insensitive operating system (e.g.  Windows), this method looks
        up the file in the file system and resets the Filename to represent the
        actual case of the file as it exists on the disk.  The return value is true
        if the file exists and the conversion can be made, or false if there is
        some error.

        On a case-sensitive operating system, this method does nothing and always
        returns true.

        An empty filename is considered to exist in this case.
        """
    def to_os_specific(self) -> str:
        """Converts the filename from our generic Unix-like convention (forward
        slashes starting with the root at '/') to the corresponding filename in the
        local operating system (slashes in the appropriate direction, starting with
        the root at C:\\, for instance).  Returns the string representing the
        converted filename, but does not change the Filename itself.

        See also from_os_specific().
        """
    def to_os_specific_w(self) -> str:
        """The wide-string variant on to_os_specific()."""
    def to_os_generic(self) -> str:
        """This is similar to to_os_specific(), but it is designed to generate a
        filename that can be understood on as many platforms as possible.  Since
        Windows can usually understand a forward-slash-delimited filename, this
        means it does the same thing as to_os_specific(), but it uses forward
        slashes instead of backslashes.

        This method has a pretty limited use; it should generally be used for
        writing file references to a file that might be read on any operating
        system.
        """
    def to_os_short_name(self) -> str:
        """This works like to_os_generic(), but it returns the "short name" version of
        the filename, if it exists, or the original filename otherwise.

        On Windows platforms, this returns the 8.3 filename version of the given
        filename, if the file exists, and the same thing as to_os_specific()
        otherwise.  On non-Windows platforms, this always returns the same thing as
        to_os_specific().
        """
    def to_os_long_name(self) -> str:
        """This is the opposite of to_os_short_name(): it returns the "long name" of
        the filename, if the filename exists.  On non-Windows platforms, this
        returns the same thing as to_os_specific().
        """
    def exists(self) -> bool:
        """Returns true if the filename exists on the disk, false otherwise.  If the
        type is indicated to be executable, this also tests that the file has
        execute permission.
        """
    def is_regular_file(self) -> bool:
        """Returns true if the filename exists and is the name of a regular file (i.e.
        not a directory or device), false otherwise.
        """
    def is_writable(self) -> bool:
        """Returns true if the filename exists and is either a directory or a regular
        file that can be written to, or false otherwise.
        """
    def is_directory(self) -> bool:
        """Returns true if the filename exists and is a directory name, false
        otherwise.
        """
    def is_executable(self) -> bool:
        """Returns true if the filename exists and is executable"""
    def compare_timestamps(self, other: StrOrBytesPath, this_missing_is_old: bool = ..., other_missing_is_old: bool = ...) -> int:
        """Returns a number less than zero if the file named by this object is older
        than the given file, zero if they have the same timestamp, or greater than
        zero if this one is newer.

        If this_missing_is_old is true, it indicates that a missing file will be
        treated as if it were older than any other file; otherwise, a missing file
        will be treated as if it were newer than any other file.  Similarly for
        other_missing_is_old.
        """
    def get_timestamp(self) -> int:
        """Returns a time_t value that represents the time the file was last modified,
        to within whatever precision the operating system records this information
        (on a Windows95 system, for instance, this may only be accurate to within 2
        seconds).

        If the timestamp cannot be determined, either because it is not supported
        by the operating system or because there is some error (such as file not
        found), returns 0.
        """
    def get_access_timestamp(self) -> int:
        """Returns a time_t value that represents the time the file was last accessed,
        if this information is available.  See also get_timestamp(), which returns
        the last modification time.
        """
    def get_file_size(self) -> int:
        """Returns the size of the file in bytes, or 0 if there is an error."""
    def resolve_filename(self, searchpath: SearchPathLike, default_extension: str = ...) -> bool:
        """Searches the given search path for the filename.  If it is found, updates
        the filename to the full pathname found and returns true; otherwise,
        returns false.
        """
    def make_relative_to(self, directory: StrOrBytesPath, allow_backups: bool = ...) -> bool:
        """Adjusts this filename, which must be a fully-specified pathname beginning
        with a slash, to make it a relative filename, relative to the fully-
        specified directory indicated (which must also begin with, and may or may
        not end with, a slash--a terminating slash is ignored).

        This only performs a string comparsion, so it may be wise to call
        make_canonical() on both filenames before calling make_relative_to().

        If allow_backups is false, the filename will only be adjusted to be made
        relative if it is already somewhere within or below the indicated
        directory.  If allow_backups is true, it will be adjusted in all cases,
        even if this requires putting a series of .. characters before the filename
        --unless it would have to back all the way up to the root.

        Returns true if the file was adjusted, false if it was not.
        """
    def find_on_searchpath(self, searchpath: SearchPathLike) -> int:
        """Performs the reverse of the resolve_filename() operation: assuming that the
        current filename is fully-specified pathname (i.e.  beginning with '/'),
        look on the indicated search path for a directory under which the file can
        be found.  When found, adjust the Filename to be relative to the indicated
        directory name.

        Returns the index of the directory on the searchpath at which the file was
        found, or -1 if it was not found.
        """
    def scan_directory(self) -> list[str]: ...
    def open_read(self, stream: ifstream | pifstream) -> bool:
        """`(self, stream: pifstream)`:
        Opens the indicated pifstream for reading the file, if possible.  Returns
        true if successful, false otherwise.  This requires the setting of the
        set_text()/set_binary() flags to open the file appropriately as indicated;
        it is an error to call open_read() without first calling one of set_text()
        or set_binary().

        `(self, stream: ifstream)`:
        Opens the indicated ifstream for reading the file, if possible.  Returns
        true if successful, false otherwise.  This requires the setting of the
        set_text()/set_binary() flags to open the file appropriately as indicated;
        it is an error to call open_read() without first calling one of set_text()
        or set_binary().
        """
    def open_write(self, stream: ofstream | pofstream, truncate: bool = ...) -> bool:
        """`(self, stream: pofstream, truncate: bool = ...)`:
        Opens the indicated pifstream for writing the file, if possible.  Returns
        true if successful, false otherwise.  This requires the setting of the
        set_text()/set_binary() flags to open the file appropriately as indicated;
        it is an error to call open_read() without first calling one of set_text()
        or set_binary().

        If truncate is true, the file is truncated to zero length upon opening it,
        if it already exists.  Otherwise, the file is kept at its original length.

        `(self, stream: ofstream, truncate: bool = ...)`:
        Opens the indicated ifstream for writing the file, if possible.  Returns
        true if successful, false otherwise.  This requires the setting of the
        set_text()/set_binary() flags to open the file appropriately as indicated;
        it is an error to call open_read() without first calling one of set_text()
        or set_binary().

        If truncate is true, the file is truncated to zero length upon opening it,
        if it already exists.  Otherwise, the file is kept at its original length.
        """
    def open_append(self, stream: ofstream | pofstream) -> bool:
        """`(self, stream: pofstream)`:
        Opens the indicated pifstream for writing the file, if possible.  Returns
        true if successful, false otherwise.  This requires the setting of the
        set_text()/set_binary() flags to open the file appropriately as indicated;
        it is an error to call open_read() without first calling one of set_text()
        or set_binary().

        `(self, stream: ofstream)`:
        Opens the indicated ofstream for writing the file, if possible.  Returns
        true if successful, false otherwise.  This requires the setting of the
        set_text()/set_binary() flags to open the file appropriately as indicated;
        it is an error to call open_read() without first calling one of set_text()
        or set_binary().
        """
    def open_read_write(self, stream: fstream | pfstream, truncate: bool = ...) -> bool:
        """Opens the indicated fstream for read/write access to the file, if possible.
        Returns true if successful, false otherwise.  This requires the setting of
        the set_text()/set_binary() flags to open the file appropriately as
        indicated; it is an error to call open_read_write() without first calling
        one of set_text() or set_binary().
        """
    def open_read_append(self, stream: fstream | pfstream) -> bool:
        """`(self, stream: pfstream)`:
        Opens the indicated pfstream for reading and writing the file, if possible;
        writes are appended to the end of the file.  Returns true if successful,
        false otherwise.  This requires the setting of the set_text()/set_binary()
        flags to open the file appropriately as indicated; it is an error to call
        open_read() without first calling one of set_text() or set_binary().

        `(self, stream: fstream)`:
        Opens the indicated ifstream for reading and writing the file, if possible;
        writes are appended to the end of the file.  Returns true if successful,
        false otherwise.  This requires the setting of the set_text()/set_binary()
        flags to open the file appropriately as indicated; it is an error to call
        open_read() without first calling one of set_text() or set_binary().
        """
    def chdir(self) -> bool:
        """Changes directory to the specified location.  Returns true if successful,
        false if failure.
        """
    def touch(self) -> bool:
        """Updates the modification time of the file to the current time.  If the file
        does not already exist, it will be created.  Returns true if successful,
        false if there is an error.
        """
    def unlink(self) -> bool:
        """Permanently deletes the file associated with the filename, if possible.
        Returns true if successful, false if failure (for instance, because the
        file did not exist, or because permissions were inadequate).
        """
    def rename_to(self, other: StrOrBytesPath) -> bool:
        """Renames the file to the indicated new filename.  If the new filename is in
        a different directory, this will perform a move.  Returns true if
        successful, false on failure.
        """
    def copy_to(self, other: StrOrBytesPath) -> bool:
        """Copies the file to the indicated new filename, by reading the contents and
        writing it to the new file.  Returns true if successful, false on failure.
        The copy is always binary, regardless of the filename settings.
        """
    def make_dir(self) -> bool:
        """Creates all the directories in the path to the file specified in the
        filename, except for the basename itself.  This assumes that the Filename
        contains the name of a file, not a directory name; it ensures that the
        directory containing the file exists.

        However, if the filename ends in a slash, it assumes the Filename
        represents the name of a directory, and creates all the paths.
        """
    def mkdir(self) -> bool:
        """Creates the directory named by this filename.  Unlike make_dir(), this
        assumes that the Filename contains the directory name itself.  Also, parent
        directories are not automatically created; this function fails if any
        parent directory is missing.
        """
    def rmdir(self) -> bool:
        """The inverse of mkdir(): this removes the directory named by this Filename,
        if it is in fact a directory.
        """
    def compare_to(self, other: StrOrBytesPath) -> int: ...
    def get_hash(self) -> int:
        """Returns a hash code that attempts to be mostly unique for different
        Filenames.
        """
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def set_filesystem_encoding(encoding: _TextEncoder_Encoding) -> None:
        """Specifies the default encoding to be used for all subsequent Filenames.
        This is used to represent wide-character (Unicode) filenames internally.
        On non-Windows-based systems, the encoded filename is also passed to the
        underlying operating system.
        """
    @staticmethod
    def get_filesystem_encoding() -> _TextEncoder_Encoding:
        """Specifies the default encoding to be used for all subsequent Filenames
        objects.  See set_filesystem_encoding().
        """
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    textFilename = text_filename
    binaryFilename = binary_filename
    dsoFilename = dso_filename
    executableFilename = executable_filename
    patternFilename = pattern_filename
    fromOsSpecific = from_os_specific
    fromOsSpecificW = from_os_specific_w
    expandFrom = expand_from
    getHomeDirectory = get_home_directory
    getTempDirectory = get_temp_directory
    getUserAppdataDirectory = get_user_appdata_directory
    getCommonAppdataDirectory = get_common_appdata_directory
    cStr = c_str
    Fspath = __fspath__
    getFullpath = get_fullpath
    getFullpathW = get_fullpath_w
    getDirname = get_dirname
    getBasename = get_basename
    getFullpathWoExtension = get_fullpath_wo_extension
    getBasenameWoExtension = get_basename_wo_extension
    getExtension = get_extension
    setFullpath = set_fullpath
    setDirname = set_dirname
    setBasename = set_basename
    setFullpathWoExtension = set_fullpath_wo_extension
    setBasenameWoExtension = set_basename_wo_extension
    setExtension = set_extension
    setBinary = set_binary
    setText = set_text
    isBinary = is_binary
    isText = is_text
    isBinaryOrText = is_binary_or_text
    setType = set_type
    getType = get_type
    setPattern = set_pattern
    getPattern = get_pattern
    hasHash = has_hash
    getFilenameIndex = get_filename_index
    getHashToEnd = get_hash_to_end
    setHashToEnd = set_hash_to_end
    isLocal = is_local
    isFullyQualified = is_fully_qualified
    makeAbsolute = make_absolute
    makeCanonical = make_canonical
    makeTrueCase = make_true_case
    toOsSpecific = to_os_specific
    toOsSpecificW = to_os_specific_w
    toOsGeneric = to_os_generic
    toOsShortName = to_os_short_name
    toOsLongName = to_os_long_name
    isRegularFile = is_regular_file
    isWritable = is_writable
    isDirectory = is_directory
    isExecutable = is_executable
    compareTimestamps = compare_timestamps
    getTimestamp = get_timestamp
    getAccessTimestamp = get_access_timestamp
    getFileSize = get_file_size
    resolveFilename = resolve_filename
    makeRelativeTo = make_relative_to
    findOnSearchpath = find_on_searchpath
    scanDirectory = scan_directory
    openRead = open_read
    openWrite = open_write
    openAppend = open_append
    openReadWrite = open_read_write
    openReadAppend = open_read_append
    renameTo = rename_to
    copyTo = copy_to
    makeDir = make_dir
    compareTo = compare_to
    getHash = get_hash
    setFilesystemEncoding = set_filesystem_encoding
    getFilesystemEncoding = get_filesystem_encoding
    getClassType = get_class_type

class PandaSystem:
    """This class is used as a namespace to group several global properties of
    Panda.  Application developers can use this class to query the runtime
    version or capabilities of the current Panda environment.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def version_string(self) -> str: ...
    @property
    def major_version(self) -> int: ...
    @property
    def minor_version(self) -> int: ...
    @property
    def sequence_version(self) -> int: ...
    @property
    def official_version(self) -> bool: ...
    @property
    def memory_alignment(self) -> int: ...
    @property
    def distributor(self) -> str: ...
    @property
    def compiler(self) -> str: ...
    @property
    def build_date(self) -> str: ...
    @property
    def git_commit(self) -> str: ...
    @property
    def platform(self) -> str: ...
    @property
    def systems(self) -> Sequence[str]: ...
    @staticmethod
    def get_version_string() -> str:
        """Returns the current version of Panda, expressed as a string, e.g.  "1.0.0".
        The string will end in the letter "c" if this build does not represent an
        official version.
        """
    @staticmethod
    def get_package_version_string() -> str:
        """Returns the version of the Panda3D distributable package that provides this
        build of Panda.

        When the currently-executing version of Panda was loaded from a
        distributable package, such as via the browser plugin, then this string
        will be nonempty and will contain the corresponding version string.  You
        can build applications that use this particular version of Panda by
        requesting it in the pdef file, using "panda3d", this version string, and
        the download host provided by get_package_host_url().

        If this string is empty, then the currently-executing Panda was built
        independently, and is not part of a distributable package.

        This string is set explicitly at compilation time.  Normally, it should be
        set to a nonempty string only when building a Panda3D package for
        distribution.
        """
    @staticmethod
    def get_package_host_url() -> str:
        """Returns the URL of the download server that provides the Panda3D
        distributable package currently running.  This can be used, along with the
        get_package_version_string(), to uniquely identify the running version of
        Panda among distributable Panda versions.

        See get_package_version_string() for more information.

        This string is set explicitly at compilation time.  Normally, it should be
        set to a nonempty string only when building a Panda3D package for
        distribution.
        """
    @staticmethod
    def get_p3d_coreapi_version_string() -> str:
        """Returns the current version of Panda's Core API, expressed as a string of
        dot-delimited integers.  There are usually four integers in this version,
        but this is not guaranteed.

        The Core API is used during the runtime (plugin) environment only.  This
        may be the empty string if the current version of Panda is not built to
        provide a particular Core API, which will be the normal case in a
        development SDK.  However, you should not use this method to determine
        whether you are running in a runtime environment or not.
        """
    @staticmethod
    def get_major_version() -> int:
        """Returns the major version number of the current version of Panda.  This is
        the first number of the dotted triple returned by get_version_string().  It
        changes very rarely.
        """
    @staticmethod
    def get_minor_version() -> int:
        """Returns the minor version number of the current version of Panda.  This is
        the second number of the dotted triple returned by get_version_string().
        It changes with each release that introduces new features.
        """
    @staticmethod
    def get_sequence_version() -> int:
        """Returns the sequence version number of the current version of Panda.  This
        is the third number of the dotted triple returned by get_version_string().
        It changes with bugfix updates and very minor feature updates.
        """
    @staticmethod
    def is_official_version() -> bool:
        """Returns true if current version of Panda claims to be an "official"
        version, that is, one that was compiled by an official distributor of Panda
        using a specific version of the panda source tree.  If this is true, there
        will not be a "c" at the end of the version string returned by
        get_version_string().

        Note that we must take the distributor's word for it here.
        """
    @staticmethod
    def get_memory_alignment() -> int:
        """Returns the memory alignment that Panda's allocators are using."""
    @staticmethod
    def get_distributor() -> str:
        """Returns the string defined by the distributor of this version of Panda, or
        "homebuilt" if this version was built directly from the sources by the end-
        user.  This is a completely arbitrary string.
        """
    @staticmethod
    def get_compiler() -> str:
        """Returns a string representing the compiler that was used to generate this
        version of Panda, if it is available, or "unknown" if it is not.
        """
    @staticmethod
    def get_build_date() -> str:
        """Returns a string representing the date and time at which this version of
        Panda (or at least dtool) was compiled, if available.
        """
    @staticmethod
    def get_git_commit() -> str:
        """Returns a string representing the git commit hash that this source tree is
        based on, or the empty string if it has not been specified at build time.
        """
    @staticmethod
    def get_platform() -> str:
        """Returns a string representing the runtime platform that we are currently
        running on.  This will be something like "win32" or "osx_i386" or
        "linux_amd64".
        """
    def has_system(self, system: str) -> bool:
        """Returns true if the current version of Panda claims to have the indicated
        subsystem installed, false otherwise.  The set of available subsystems is
        implementation defined.
        """
    def get_num_systems(self) -> int:
        """Returns the number of Panda subsystems that have registered themselves.
        This can be used with get_system() to iterate through the entire list of
        available Panda subsystems.
        """
    def get_system(self, n: int) -> str:
        """Returns the nth Panda subsystem that has registered itself.  This list will
        be sorted in alphabetical order.
        """
    def get_system_tag(self, system: str, tag: str) -> str:
        """Returns the value associated with the indicated tag for the given system.
        This provides a standard way to query each subsystem's advertised
        capabilities.  The set of tags and values are per-system and
        implementation-defined.

        The return value is the empty string if the indicated system is undefined
        or if does not define the indicated tag.
        """
    def add_system(self, system: str) -> None:
        """Intended for use by each subsystem to register itself at startup."""
    def set_system_tag(self, system: str, tag: str, value: str) -> None:
        """Intended for use by each subsystem to register its set of capabilities at
        startup.
        """
    def heap_trim(self, pad: int) -> bool:
        """Attempts to release memory back to the system, if possible.  The pad
        argument is the minimum amount of unused memory to keep in the heap
        (against future allocations).  Any memory above that may be released to the
        system, reducing the memory size of this process.  There is no guarantee
        that any memory may be released.

        Returns true if any memory was actually released, false otherwise.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_ptr() -> PandaSystem:
        """Returns the global PandaSystem object."""
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    def get_systems(self) -> tuple[str, ...]: ...
    getVersionString = get_version_string
    getPackageVersionString = get_package_version_string
    getPackageHostUrl = get_package_host_url
    getP3dCoreapiVersionString = get_p3d_coreapi_version_string
    getMajorVersion = get_major_version
    getMinorVersion = get_minor_version
    getSequenceVersion = get_sequence_version
    isOfficialVersion = is_official_version
    getMemoryAlignment = get_memory_alignment
    getDistributor = get_distributor
    getCompiler = get_compiler
    getBuildDate = get_build_date
    getGitCommit = get_git_commit
    getPlatform = get_platform
    hasSystem = has_system
    getNumSystems = get_num_systems
    getSystem = get_system
    getSystemTag = get_system_tag
    addSystem = add_system
    setSystemTag = set_system_tag
    heapTrim = heap_trim
    getGlobalPtr = get_global_ptr
    getClassType = get_class_type
    getSystems = get_systems

class DSearchPath:
    """This class stores a list of directories that can be searched, in order, to
    locate a particular file.  It is normally constructed by passing it a
    traditional searchpath-style string, e.g.  a list of directory names
    delimited by spaces or colons, but it can also be built up explicitly.
    """

    class Results:
        DtoolClassDict: ClassVar[dict[str, Any]]
        def __init__(self, copy: DSearchPath.Results = ...) -> None: ...
        def __getitem__(self, n: int) -> Filename: ...
        def __len__(self) -> int:
            """Returns the num of filenames in the set.  This method is defined to make
            the Results object appear to be a list in Python.
            """
        def __copy__(self) -> Self: ...
        def __deepcopy__(self, __memo: object) -> Self: ...
        def __iter__(self) -> Iterator[Filename]: ...  # Doesn't actually exist
        def assign(self, copy: DSearchPath.Results) -> Self: ...
        def clear(self) -> None:
            """Removes all the files from the list."""
        def get_num_files(self) -> int:
            """Returns the number of files on the result list."""
        def get_file(self, n: int) -> Filename:
            """Returns the nth file on the result list."""
        def output(self, out: ostream) -> None: ...
        def write(self, out: ostream, indent_level: int = ...) -> None: ...
        getNumFiles = get_num_files
        getFile = get_file

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def directories(self) -> Sequence[Filename]: ...
    @overload
    def __init__(self, copy: SearchPathLike = ...) -> None: ...
    @overload
    def __init__(self, directory: StrOrBytesPath) -> None: ...
    @overload
    def __init__(self, path: str, separator: str = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: SearchPathLike) -> Self: ...
    def clear(self) -> None:
        """Removes all the directories from the search list."""
    def append_directory(self, directory: StrOrBytesPath) -> None:
        """Adds a new directory to the end of the search list."""
    def prepend_directory(self, directory: StrOrBytesPath) -> None:
        """Adds a new directory to the front of the search list."""
    @overload
    def append_path(self, path: SearchPathLike) -> None:
        """Adds all of the directories listed in the search path to the end of the
        search list.
        """
    @overload
    def append_path(self, path: str, separator: str = ...) -> None: ...
    def prepend_path(self, path: SearchPathLike) -> None:
        """Adds all of the directories listed in the search path to the beginning of
        the search list.
        """
    def is_empty(self) -> bool:
        """Returns true if the search list is empty, false otherwise."""
    def get_num_directories(self) -> int:
        """Returns the number of directories on the search list."""
    def get_directory(self, n: int) -> Filename:
        """Returns the nth directory on the search list."""
    def find_file(self, filename: StrOrBytesPath) -> Filename:
        """Searches all the directories in the search list for the indicated file, in
        order.  Returns the full matching pathname of the first match if found, or
        the empty string if not found.
        """
    @overload
    def find_all_files(self, filename: StrOrBytesPath) -> DSearchPath.Results:
        """`(self, filename: Filename)`:
        This variant of find_all_files() returns the new Results object, instead of
        filling on in on the parameter list.  This is a little more convenient to
        call from Python.

        `(self, filename: Filename, results: DSearchPath.Results)`:
        Searches all the directories in the search list for the indicated file, in
        order.  Fills up the results list with *all* of the matching filenames
        found, if any.  Returns the number of matches found.

        It is the responsibility of the the caller to clear the results list first;
        otherwise, the newly-found files will be appended to the list.
        """
    @overload
    def find_all_files(self, filename: StrOrBytesPath, results: DSearchPath.Results) -> int: ...
    @staticmethod
    def search_path(filename: StrOrBytesPath, path: str, separator: str = ...) -> Filename:
        """A quick-and-easy way to search a searchpath for a file when you don't feel
        like building or keeping around a DSearchPath object.  This simply
        constructs a temporary DSearchPath based on the indicated path string, and
        searches that.
        """
    def output(self, out: ostream, separator: str = ...) -> None: ...
    def write(self, out: ostream, indent_level: int = ...) -> None: ...
    def get_directories(self) -> tuple[Filename, ...]: ...
    appendDirectory = append_directory
    prependDirectory = prepend_directory
    appendPath = append_path
    prependPath = prepend_path
    isEmpty = is_empty
    getNumDirectories = get_num_directories
    getDirectory = get_directory
    findFile = find_file
    findAllFiles = find_all_files
    searchPath = search_path
    getDirectories = get_directories

class ExecutionEnvironment:
    """Encapsulates access to the environment variables and command-line arguments
    at the time of execution.  This is encapsulated to support accessing these
    things during static init time, which seems to be risky at best.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    binary_name: str
    dtool_name: str
    @property
    def environment_variables(self) -> MutableMapping[str, str]: ...
    @property
    def args(self) -> Sequence[str]: ...
    @property
    def cwd(self) -> Filename: ...
    def __init__(self, __param0: ExecutionEnvironment) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def has_environment_variable(var: str) -> bool:
        """Returns true if the indicated environment variable is defined."""
    @staticmethod
    def get_environment_variable(var: str) -> str:
        """Returns the definition of the indicated environment variable, or the empty
        string if the variable is undefined.
        """
    @staticmethod
    def set_environment_variable(var: str, value: str) -> None:
        """Changes the definition of the indicated environment variable."""
    @staticmethod
    def shadow_environment_variable(var: str, value: str) -> None:
        """Changes the apparent definition of the indicated environment variable by
        masking it within this class with a new value.  This does not change the
        actual environment variable, but future calls to get_environment_variable()
        will return this new value.
        """
    @staticmethod
    def clear_shadow(var: str) -> None:
        """Removes a value set by a previous call to shadow_environment_variable(),
        and lets the actual value of the variable show again.
        """
    @staticmethod
    def expand_string(str: str) -> str:
        """Reads the string, looking for environment variable names marked by a $.
        Expands all such variable names.  A repeated dollar sign ($$) is mapped to
        a single dollar sign.

        Returns the expanded string.
        """
    @staticmethod
    def get_num_args() -> int:
        """Returns the number of command-line arguments available, not counting arg 0,
        the binary name.
        """
    @staticmethod
    def get_arg(n: int) -> str:
        """Returns the nth command-line argument.  The index n must be in the range [0
        .. get_num_args()).  The first parameter, n == 0, is the first actual
        parameter, not the binary name.
        """
    @staticmethod
    def get_binary_name() -> str:
        """Returns the name of the binary executable that started this program, if it
        can be determined.
        """
    @staticmethod
    def get_dtool_name() -> str:
        """Returns the name of the libdtool DLL that is used in this program, if it
        can be determined.
        """
    @staticmethod
    def set_binary_name(name: str) -> None:
        """Do not use."""
    @staticmethod
    def set_dtool_name(name: str) -> None:
        """Do not use."""
    @staticmethod
    def get_cwd() -> Filename:
        """Returns the name of the current working directory."""
    hasEnvironmentVariable = has_environment_variable
    getEnvironmentVariable = get_environment_variable
    setEnvironmentVariable = set_environment_variable
    shadowEnvironmentVariable = shadow_environment_variable
    clearShadow = clear_shadow
    expandString = expand_string
    getNumArgs = get_num_args
    getArg = get_arg
    getBinaryName = get_binary_name
    getDtoolName = get_dtool_name
    setBinaryName = set_binary_name
    setDtoolName = set_dtool_name
    getCwd = get_cwd

class GlobPattern:
    """This class can be used to test for string matches against standard Unix-
    shell filename globbing conventions.  It serves as a portable standin for
    the Posix fnmatch() call.

    A GlobPattern is given a pattern string, which can contain operators like
    *, ?, and [].  Then it can be tested against any number of candidate
    strings; for each candidate, it will indicate whether the string matches
    the pattern or not.  It can be used, for example, to scan a directory for
    all files matching a particular pattern.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    pattern: str
    case_sensitive: bool
    nomatch_chars: str
    @overload
    def __init__(self, pattern: str = ...) -> None: ...
    @overload
    def __init__(self, copy: GlobPattern) -> None: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: GlobPattern | str) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: GlobPattern | str) -> Self: ...
    def set_pattern(self, pattern: str) -> None:
        """Changes the pattern string that the GlobPattern object matches."""
    def get_pattern(self) -> str:
        """Returns the pattern string that the GlobPattern object matches."""
    def set_case_sensitive(self, case_sensitive: bool) -> None:
        """Sets whether the match is case sensitive (true) or case insensitive
        (false).  The default is case sensitive.
        """
    def get_case_sensitive(self) -> bool:
        """Returns whether the match is case sensitive (true) or case insensitive
        (false).  The default is case sensitive.
        """
    def set_nomatch_chars(self, nomatch_chars: str) -> None:
        """Specifies a set of characters that are not matched by * or ?."""
    def get_nomatch_chars(self) -> str:
        """Returns the set of characters that are not matched by * or ?."""
    def matches(self, candidate: str) -> bool:
        """Returns true if the candidate string matches the pattern, false otherwise."""
    def matches_file(self, candidate: StrOrBytesPath) -> bool:
        """Treats the GlobPattern as a filename pattern, and returns true if the given
        filename matches the pattern.  Unlike matches(), this will not match slash
        characters for single asterisk characters, and it will ignore path
        components that only contain a dot.
        """
    def output(self, out: ostream) -> None: ...
    def has_glob_characters(self) -> bool:
        """Returns true if the pattern includes any special globbing characters, or
        false if it is just a literal string.
        """
    def get_const_prefix(self) -> str:
        """Returns the initial part of the pattern before the first glob character.
        Since many glob patterns begin with a sequence of static characters and end
        with one or more glob characters, this can be used to optimized searches
        through sorted indices.
        """
    def match_files(self, cwd: StrOrBytesPath = ...) -> list[str]: ...
    setPattern = set_pattern
    getPattern = get_pattern
    setCaseSensitive = set_case_sensitive
    getCaseSensitive = get_case_sensitive
    setNomatchChars = set_nomatch_chars
    getNomatchChars = get_nomatch_chars
    matchesFile = matches_file
    hasGlobCharacters = has_glob_characters
    getConstPrefix = get_const_prefix
    matchFiles = match_files

class LineStream(ostream):
    """This is a special ostream that writes to a memory buffer, like ostrstream.
    However, its contents can be continuously extracted as a sequence of lines
    of text.

    Unlike ostrstream, which can only be extracted from once (and then the
    buffer freezes and it can no longer be written to), the LineStream is not
    otherwise affected when a line of text is extracted.  More text can still
    be written to it and continuously extracted.
    """

    def __init__(self) -> None: ...
    def is_text_available(self) -> bool:
        """Returns true if there is at least one line of text (or even a partial line)
        available in the LineStream object.  If this returns true, the line may
        then be retrieved via get_line().
        """
    def get_line(self) -> str:
        """Extracts and returns the next line (or partial line) of text available in
        the LineStream object.  Once the line has been extracted, you may call
        has_newline() to determine whether or not there was an explicit newline
        character written following this line.
        """
    def has_newline(self) -> bool:
        """Returns true if the line of text most recently returned by get_line() was
        written out with a terminating newline, or false if a newline character has
        not yet been written to the LineStream.
        """
    isTextAvailable = is_text_available
    getLine = get_line
    hasNewline = has_newline

BasicIosChar = basic_ios_char
IosBase = ios_base
Fstream = fstream
Iostream = iostream
Istream = istream
Ostream = ostream
Ifstream = ifstream
ios = basic_ios_char
Ios = ios
Ofstream = ofstream
pifstream = IFileStream
Pifstream = pifstream
pofstream = OFileStream
Pofstream = pofstream
pfstream = FileStream
Pfstream = pfstream
