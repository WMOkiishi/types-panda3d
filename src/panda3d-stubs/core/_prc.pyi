from _typeshed import StrOrBytesPath
from collections.abc import Iterator, Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d import core
from panda3d._typing import SearchPathLike
from panda3d.core._dtoolutil import DSearchPath, Filename, iostream, istream, ostream

_ConfigFlags_ValueType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_NotifySeverity: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6]

class ConfigFlags:
    """This class is the base class of both ConfigVariable and ConfigVariableCore.
    It exists only to provide a convenient name scoping for some enumerated
    values common to both classes.
    """

    VT_undefined: Final = 0
    VTUndefined: Final = 0
    VT_list: Final = 1
    VTList: Final = 1
    VT_string: Final = 2
    VTString: Final = 2
    VT_filename: Final = 3
    VTFilename: Final = 3
    VT_bool: Final = 4
    VTBool: Final = 4
    VT_int: Final = 5
    VTInt: Final = 5
    VT_double: Final = 6
    VTDouble: Final = 6
    VT_enum: Final = 7
    VTEnum: Final = 7
    VT_search_path: Final = 8
    VTSearchPath: Final = 8
    VT_int64: Final = 9
    VTInt64: Final = 9
    VT_color: Final = 10
    VTColor: Final = 10
    F_trust_level_mask: Final = 4095
    FTrustLevelMask: Final = 4095
    F_open: Final = 4096
    FOpen: Final = 4096
    F_closed: Final = 8192
    FClosed: Final = 8192
    F_dynamic: Final = 16384
    FDynamic: Final = 16384
    F_dconfig: Final = 32768
    FDconfig: Final = 32768
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: ConfigFlags = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...

class ConfigPage:
    """A page of ConfigDeclarations that may be loaded or unloaded.  Typically
    this represents a single .prc file that is read from disk at runtime, but
    it may also represent a list of declarations built up by application code
    and explicitly loaded.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    sort: int
    trust_level: int
    @property
    def name(self) -> str: ...
    @property
    def special(self) -> bool: ...
    @property
    def implicit(self) -> bool: ...
    @property
    def page_seq(self) -> int: ...
    @property
    def signature(self) -> str: ...
    @property
    def declarations(self) -> Sequence[ConfigDeclaration]: ...
    @staticmethod
    def get_default_page() -> ConfigPage:
        """Returns a pointer to the global "default page".  This is the ConfigPage
        that lists all variables' original default values.
        """
    @staticmethod
    def get_local_page() -> ConfigPage:
        """Returns a pointer to the global "local page".  This is the ConfigPage that
        lists the locally-assigned values for any variables in the world that have
        such a local assignment.
        """
    def get_name(self) -> str:
        """Returns the name of the page.  If the page was loaded from a .prc file,
        this is usually the filename.
        """
    def is_special(self) -> bool:
        """Returns true if this is the special "default" or "local" page, or false if
        it is an ordinary page, e.g.  an implicit page loaded from a prc file at
        startup, or an explicit page created by
        ConfigPageManager::make_explicit_page().
        """
    def is_implicit(self) -> bool:
        """Returns true if the page was loaded by implicitly searching the config path
        on startup, or false if it was explicitly loaded by dynamic code after
        initial startup.
        """
    def set_sort(self, sort: int) -> None:
        """Changes the explicit sort order of this particular ConfigPage.  Lower-
        numbered pages supercede higher-numbered pages.  Initially, all explicitly-
        loaded pages have sort value 0, and implicitly-loaded pages (found on disk)
        have sort value 10; you may set an individual page higher or lower to
        influence its priority relative to other pages.
        """
    def get_sort(self) -> int:
        """Returns the explicit sort order of this particular ConfigPage.  See
        set_sort().
        """
    def get_page_seq(self) -> int:
        """Returns the sequence number of the page.

        Sequence numbers for a particular class (implicit vs.  explicit) of pages
        are assigned as each page is loaded; each page is given a higher sequence
        number than all the pages loaded before it.

        The implicit_load pages, which are discovered in the file system
        automatically, have a different set of sequence numbers than the explicit
        pages.
        """
    def get_trust_level(self) -> int:
        """Returns the trust level associated with this page.  An untrusted page is
        trust level 0; if the page was loaded from a signed .prc file, its trust
        level is the index number of the certificate that signed it.  Generally, a
        higher trust level value represents a greater level of trust.
        """
    def set_trust_level(self, trust_level: int) -> None:
        """Explicitly sets the trust level on this particular page.  Note that any
        subsequent changes to the page, or to any variable declarations on it, will
        reset the trust level to zero.
        """
    def get_signature(self) -> str:
        """Returns the raw binary signature that was found in the prc file, if any.
        This method is probably not terribly useful for most applications.
        """
    def clear(self) -> None:
        """Removes all of the declarations from the page."""
    def read_prc(self, _in: istream) -> bool:
        """Reads the contents of a complete prc file, as returned by the indicated
        istream, into the current page file.  Returns true on success, or false on
        some I/O error.

        This is a low-level interface.  Normally you do not need to call it
        directly.  See the global functions load_prc_file() and unload_prc_file(),
        defined in panda/src/putil, for a higher-level interface.
        """
    def read_encrypted_prc(self, _in: istream, password: str) -> bool:
        """Automatically decrypts and reads the stream, given the indicated password.
        Note that if the password is incorrect, the result may be garbage.
        """
    def make_declaration(self, variable: ConfigVariableCore | str, value: str) -> ConfigDeclaration:
        """Adds the indicated variable/value pair as a new declaration on the page."""
    def delete_declaration(self, decl: ConfigDeclaration) -> bool:
        """Removes the indicated declaration from the page and deletes it.  Returns
        true if the declaration is successfully removed, false if it was not on the
        page.
        """
    def get_num_declarations(self) -> int:
        """Returns the number of declarations on the page."""
    def get_declaration(self, n: int) -> ConfigDeclaration:
        """Returns the nth declaration on the page."""
    def modify_declaration(self, n: int) -> ConfigDeclaration:
        """Returns a modifiable pointer to the nth declaration on the page.  Any
        modifications will appear in the output, if the page is written out with
        ConfigPage::write().
        """
    def get_variable_name(self, n: int) -> str:
        """Returns the variable named by the nth declaration on the page."""
    def get_string_value(self, n: int) -> str:
        """Returns the value assigned by the nth declaration on the page."""
    def is_variable_used(self, n: int) -> bool:
        """Returns true if the nth active variable on the page has been used by code,
        false otherwise.
        """
    def output(self, out: ostream) -> None: ...
    def output_brief_signature(self, out: ostream) -> None:
        """Outputs the first few hex digits of the signature."""
    def write(self, out: ostream) -> None: ...
    getDefaultPage = get_default_page
    getLocalPage = get_local_page
    getName = get_name
    isSpecial = is_special
    isImplicit = is_implicit
    setSort = set_sort
    getSort = get_sort
    getPageSeq = get_page_seq
    getTrustLevel = get_trust_level
    setTrustLevel = set_trust_level
    getSignature = get_signature
    readPrc = read_prc
    readEncryptedPrc = read_encrypted_prc
    makeDeclaration = make_declaration
    deleteDeclaration = delete_declaration
    getNumDeclarations = get_num_declarations
    getDeclaration = get_declaration
    modifyDeclaration = modify_declaration
    getVariableName = get_variable_name
    getStringValue = get_string_value
    isVariableUsed = is_variable_used
    outputBriefSignature = output_brief_signature

class ConfigDeclaration(ConfigFlags):
    """A single declaration of a config variable, typically defined as one line in
    a .prc file, e.g.  "show-frame-rate-meter 1".  This is really just a
    pairing of a string name (actually, a ConfigVariableCore pointer) to a
    string value.
    """

    @property
    def page(self) -> ConfigPage: ...
    @property
    def variable(self) -> ConfigVariableCore: ...
    def get_page(self) -> ConfigPage:
        """Returns the page on which this declaration can be found."""
    def get_variable(self) -> ConfigVariableCore:
        """Returns the variable that this declaration names.  This variable may or may
        not have been defined by the time the declaration is read.
        """
    def get_string_value(self) -> str:
        """Returns the value assigned to this variable.  This is the original one-line
        text defined for the variable in the .prc file (or passed to
        ConfigPage::make_declaration()).
        """
    def set_string_value(self, value: str) -> None:
        """Changes the value assigned to this variable."""
    def get_num_words(self) -> int:
        """Returns the number of words in the declaration's value.  A word is defined
        as a sequence of non-whitespace characters delimited by whitespace.
        """
    def has_string_word(self, n: int) -> bool:
        """Returns true if the declaration's value has a valid string value for the
        nth word.  This is really the same thing as asking if there are at least n
        words in the value.
        """
    def has_bool_word(self, n: int) -> bool:
        """Returns true if the declaration's value has a valid boolean value for the
        nth word.
        """
    def has_int_word(self, n: int) -> bool:
        """Returns true if the declaration's value has a valid integer value for the
        nth word.
        """
    def has_int64_word(self, n: int) -> bool:
        """Returns true if the declaration's value has a valid int64 value for the nth
        word.
        """
    def has_double_word(self, n: int) -> bool:
        """Returns true if the declaration's value has a valid integer value for the
        nth word.
        """
    def get_string_word(self, n: int) -> str:
        """Returns the string value of the nth word of the declaration's value, or
        empty string if there is no nth value.  See also has_string_word().
        """
    def get_bool_word(self, n: int) -> bool:
        """Returns the boolean value of the nth word of the declaration's value, or
        false if there is no nth value.  See also has_bool_word().
        """
    def get_int_word(self, n: int) -> int:
        """Returns the integer value of the nth word of the declaration's value, or 0
        if there is no nth value.  See also has_int_word().
        """
    def get_int64_word(self, n: int) -> int:
        """Returns the int64 value of the nth word of the declaration's value, or 0 if
        there is no nth value.  See also has_int64_word().
        """
    def get_double_word(self, n: int) -> float:
        """Returns the integer value of the nth word of the declaration's value, or 0
        if there is no nth value.  See also has_double_word().
        """
    def set_string_word(self, n: int, value: str) -> None:
        """Changes the nth word to the indicated value without affecting the other
        words.
        """
    def set_bool_word(self, n: int, value: bool) -> None:
        """Changes the nth word to the indicated value without affecting the other
        words.
        """
    def set_int_word(self, n: int, value: int) -> None:
        """Changes the nth word to the indicated value without affecting the other
        words.
        """
    def set_int64_word(self, n: int, value: int) -> None:
        """Changes the nth word to the indicated value without affecting the other
        words.
        """
    def set_double_word(self, n: int, value: float) -> None:
        """Changes the nth word to the indicated value without affecting the other
        words.
        """
    def get_filename_value(self) -> Filename:
        """Interprets the string value as a filename and returns it, with any
        variables expanded.
        """
    def get_decl_seq(self) -> int:
        """Returns the sequence number of the declaration within the page.  Sequence
        numbers are assigned as each declaration is created; each declaration is
        given a higher sequence number than all the declarations created in the
        page before it.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    getPage = get_page
    getVariable = get_variable
    getStringValue = get_string_value
    setStringValue = set_string_value
    getNumWords = get_num_words
    hasStringWord = has_string_word
    hasBoolWord = has_bool_word
    hasIntWord = has_int_word
    hasInt64Word = has_int64_word
    hasDoubleWord = has_double_word
    getStringWord = get_string_word
    getBoolWord = get_bool_word
    getIntWord = get_int_word
    getInt64Word = get_int64_word
    getDoubleWord = get_double_word
    setStringWord = set_string_word
    setBoolWord = set_bool_word
    setIntWord = set_int_word
    setInt64Word = set_int64_word
    setDoubleWord = set_double_word
    getFilenameValue = get_filename_value
    getDeclSeq = get_decl_seq

class ConfigVariableCore(ConfigFlags):
    """The internal definition of a ConfigVariable.  This object is shared between
    all instances of a ConfigVariable that use the same variable name.

    You cannot create a ConfigVariableCore instance directly; instead, use the
    make() method, which may return a shared instance.  Once created, these
    objects are never destructed.
    """

    value_type: _ConfigFlags_ValueType
    description: str
    default_value: ConfigDeclaration
    @property
    def declarations(self) -> Sequence[ConfigDeclaration]: ...
    @property
    def name(self) -> str: ...
    @property
    def used(self) -> bool: ...
    @property
    def closed(self) -> bool: ...
    @property
    def trust_level(self) -> int: ...
    @property
    def dynamic(self) -> bool: ...
    @property
    def references(self) -> Sequence[ConfigDeclaration]: ...
    @property
    def trusted_references(self) -> Sequence[ConfigDeclaration]: ...
    @property
    def unique_references(self) -> Sequence[ConfigDeclaration]: ...
    def get_name(self) -> str:
        """Returns the name of the variable."""
    def is_used(self) -> bool:
        """Returns true if the variable has been referenced by a ConfigVariable
        somewhere in code, false otherwise.
        """
    def get_value_type(self) -> _ConfigFlags_ValueType:
        """Returns the stated type of this variable.  If the variable has not yet been
        defined, this will be VT_undefined.
        """
    def get_description(self) -> str:
        """Returns the brief description of this variable, if it has been defined."""
    def get_flags(self) -> int:
        """Returns the flags value as set by set_flags().  This includes the trust
        level and some other settings.  See the individual methods is_closed(),
        get_trust_level(), etc.  to pull out the semantic meaning of these flags
        individually.
        """
    def is_closed(self) -> bool:
        """Returns true if the variable is not trusted by any prc file (and hence
        cannot be modified from its compiled-in default value), or false for the
        normal case, in which the variable can be modified by any prc file at or
        above its trust level (see get_trust_level()).

        This value only has effect in a release build (specifically, when
        PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
        """
    def get_trust_level(self) -> int:
        """Returns the minimum trust_level a prc file must demonstrate in order to
        redefine the value for this variable.  Arguably, this should be called the
        "mistrust level", since the larger the value, the more suspicious we are of
        prc files.  This value is not used if is_closed() returns true, which
        indicates no file may be trusted.

        This value only has effect in a release build (specifically, when
        PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
        """
    def is_dynamic(self) -> bool:
        """Returns true if the variable was indicated as "dynamic" by its constructor,
        indicating that its name was dynamically generated, possibly from a large
        pool, and it should not be listed along with the other variables.
        """
    def get_default_value(self) -> ConfigDeclaration:
        """Returns the default variable specified for this variable.  If the variable
        has not yet been defined, this will return NULL.
        """
    def set_value_type(self, value_type: _ConfigFlags_ValueType) -> None:
        """Specifies the type of this variable.  See get_value_type().  It is not an
        error to call this multiple times, but if the value changes once
        get_declaration() has been called, a warning is printed.
        """
    def set_flags(self, flags: int) -> None:
        """Specifies the trust level of this variable.  See get_flags().  It is not an
        error to call this multiple times, but if the value changes once
        get_declaration() has been called, a warning is printed.
        """
    def set_description(self, description: str) -> None:
        """Specifies the one-line description of this variable.  See
        get_description().  It is not an error to call this multiple times, but if
        the value changes once get_declaration() has been called, a warning is
        printed.
        """
    def set_default_value(self, default_value: str) -> None:
        """Specifies the default value for this variable if it is not defined in any
        prc file.
        """
    def set_used(self) -> None:
        """Marks that the variable has been "declared" by a ConfigVariable."""
    def make_local_value(self) -> ConfigDeclaration:
        """Creates a new local value for this variable, if there is not already one
        specified.  This will shadow any values defined in the various .prc files.

        If there is already a local value defined for this variable, simply returns
        that one.

        Use clear_local_value() to remove the local value definition.
        """
    def clear_local_value(self) -> bool:
        """Removes the local value defined for this variable, and allows its value to
        be once again retrieved from the .prc files.

        Returns true if the value was successfully removed, false if it did not
        exist in the first place.
        """
    def has_local_value(self) -> bool:
        """Returns true if this variable's value has been shadowed by a local
        assignment (as created via make_local_value()), or false otherwise.
        """
    def has_value(self) -> bool:
        """Returns true if this variable has an explicit value, either from a prc file
        or locally set, or false if variable has its default value.
        """
    def get_num_declarations(self) -> int:
        """Returns the number of declarations that contribute to this variable's
        value.  If the variable has been defined, this will always be at least 1
        (for the default value, at least).
        """
    def get_declaration(self, n: int) -> ConfigDeclaration:
        """Returns the nth declarations that contributes to this variable's value.
        The declarations are arranged in order such that earlier declarations
        shadow later declarations; thus, get_declaration(0) is always defined and
        always returns the current value of the variable.
        """
    def get_num_references(self) -> int:
        """Returns the number of prc files that reference this variable.  This is not
        exactly the same as the number of declarations; see get_reference().
        """
    def get_reference(self, n: int) -> ConfigDeclaration:
        """Returns the nth declaration in a prc file that references this variable.
        This is similar, but not identical to, get_declaration().  The difference
        is that this will list *only* true references in a prc file, and will not
        list default values or locally-assigned values; it also will list even the
        untrusted files.
        """
    def get_num_trusted_references(self) -> int:
        """Returns the number of trusted prc files that reference this variable.  See
        also get_num_references().
        """
    def get_trusted_reference(self, n: int) -> ConfigDeclaration:
        """Returns the nth declaration in a trusted prc file that references this
        variable.  This is similar, but not identical to, get_declaration().  The
        difference is that this will list *only* true references in a prc file, and
        will not list default values or locally-assigned values.

        This is also similar to get_reference(), except that it only lists the
        trusted declarations, omitting the untrusted ones.
        """
    def get_num_unique_references(self) -> int:
        """Returns the number of trusted, unique (by string value) values there exist
        for this variable.
        """
    def get_unique_reference(self, n: int) -> ConfigDeclaration:
        """Returns the nth trusted, unique value for this variable.  This is similar
        to get_trusted_reference(), except that duplicate values are removed.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def get_declarations(self) -> tuple[ConfigDeclaration, ...]: ...
    def get_references(self) -> tuple[ConfigDeclaration, ...]: ...
    def get_trusted_references(self) -> tuple[ConfigDeclaration, ...]: ...
    def get_unique_references(self) -> tuple[ConfigDeclaration, ...]: ...
    getName = get_name
    isUsed = is_used
    getValueType = get_value_type
    getDescription = get_description
    getFlags = get_flags
    isClosed = is_closed
    getTrustLevel = get_trust_level
    isDynamic = is_dynamic
    getDefaultValue = get_default_value
    setValueType = set_value_type
    setFlags = set_flags
    setDescription = set_description
    setDefaultValue = set_default_value
    setUsed = set_used
    makeLocalValue = make_local_value
    clearLocalValue = clear_local_value
    hasLocalValue = has_local_value
    hasValue = has_value
    getNumDeclarations = get_num_declarations
    getDeclaration = get_declaration
    getNumReferences = get_num_references
    getReference = get_reference
    getNumTrustedReferences = get_num_trusted_references
    getTrustedReference = get_trusted_reference
    getNumUniqueReferences = get_num_unique_references
    getUniqueReference = get_unique_reference
    getDeclarations = get_declarations
    getReferences = get_references
    getTrustedReferences = get_trusted_references
    getUniqueReferences = get_unique_references

class Notify:
    """An object that handles general error reporting to the user.  It contains a
    pointer to an ostream, initially cerr, which can be reset at will to point
    to different output devices, according to the needs of the application.
    All output generated within Panda should vector through the Notify ostream.

    This also includes a collection of Categories and Severities, which may be
    independently enabled or disabled, so that error messages may be squelched
    or respected according to the wishes of the user.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: Notify = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_ostream_ptr(self, ostream_ptr, delete_later: bool) -> None: ...
    def get_ostream_ptr(self) -> ostream:
        """Returns the system-wide ostream for all Notify messages."""
    def clear_assert_handler(self) -> None:
        """Removes the installed assert handler and restores default behavior of
        nassertr() and nassertv().
        """
    def has_assert_handler(self) -> bool:
        """Returns true if a user assert handler has been installed, false otherwise."""
    def has_assert_failed(self) -> bool:
        """Returns true if an assertion test has failed (and not been ignored) since
        the last call to clear_assert_failed().

        When an assertion test fails, the assert handler may decide either to
        abort, return, or ignore the assertion.  Naturally, if it decides to abort,
        this flag is irrelevant.  If it chooses to ignore the assertion, the flag
        is not set.  However, if the assert handler chooses to return out of the
        function (the normal case), it will also set this flag to indicate that an
        assertion failure has occurred.

        This will also be the behavior in the absence of a user-defined assert
        handler.
        """
    def get_assert_error_message(self) -> str:
        """Returns the error message that corresponds to the assertion that most
        recently failed.
        """
    def clear_assert_failed(self) -> None:
        """Resets the assert_failed flag that is set whenever an assertion test fails.
        See has_assert_failed().
        """
    def get_top_category(self) -> NotifyCategory:
        """Returns the topmost Category in the hierarchy.  This may be used to
        traverse the hierarchy of available Categories.
        """
    @overload
    def get_category(self, fullname: str) -> NotifyCategory:
        """`(self, fullname: str)`:
        Finds or creates a new Category given the fullname of the Category.  This
        name should be a sequence of colon-separated names of parent Categories,
        ending in the basename of this Category, e.g.  display:glxdisplay.  This is
        a shorthand way to define a Category when a pointer to its parent is not
        handy.

        `(self, basename: str, parent_category: NotifyCategory)`:
        Finds or creates a new Category given the basename of the category and its
        parent in the category hierarchy.  The parent pointer may be NULL to
        indicate this is a top-level Category.

        `(self, basename: str, parent_fullname: str)`:
        Finds or creates a new Category given the basename of the category and the
        fullname of its parent.  This is another way to create a category when you
        don't have a pointer to its parent handy, but you know the name of its
        parent.  If the parent Category does not already exist, it will be created.
        """
    @overload
    def get_category(self, basename: str, parent_category: NotifyCategory) -> NotifyCategory: ...
    @overload
    def get_category(self, basename: str, parent_fullname: str) -> NotifyCategory: ...
    @staticmethod
    def out() -> ostream:
        """A convenient way to get the ostream that should be written to for a Notify-
        type message.  Also see Category::out() for a message that is specific to a
        particular Category.
        """
    @staticmethod
    def null() -> ostream:
        """A convenient way to get an ostream that doesn't do anything.  Returned by
        Category::out() when a particular Category and/or Severity is disabled.
        """
    @staticmethod
    def write_string(str: str) -> None:
        """A convenient way for scripting languages, which may know nothing about
        ostreams, to write to Notify.  This writes a single string, followed by an
        implicit newline, to the Notify output stream.
        """
    @staticmethod
    def ptr() -> Notify:
        """Returns the pointer to the global Notify object.  There is only one of
        these in the world.
        """
    setOstreamPtr = set_ostream_ptr
    getOstreamPtr = get_ostream_ptr
    clearAssertHandler = clear_assert_handler
    hasAssertHandler = has_assert_handler
    hasAssertFailed = has_assert_failed
    getAssertErrorMessage = get_assert_error_message
    clearAssertFailed = clear_assert_failed
    getTopCategory = get_top_category
    getCategory = get_category
    writeString = write_string

class ConfigPageManager(ConfigFlags):
    """A global object that maintains the set of ConfigPages everywhere in the
    world, and keeps them in sorted order.
    """

    @property
    def search_path(self) -> DSearchPath: ...
    @property
    def prc_patterns(self) -> Sequence[str]: ...
    @property
    def prc_encrypted_patterns(self) -> Sequence[str]: ...
    @property
    def prc_executable_patterns(self) -> Sequence[str]: ...
    @property
    def implicit_pages(self) -> Sequence[ConfigPage]: ...
    @property
    def explicit_pages(self) -> Sequence[ConfigPage]: ...
    def loaded_implicit_pages(self) -> bool:
        """Returns true if the implicit `*.prc` files have already been loaded, false
        otherwise.  Normally this will only be false briefly before startup.
        """
    def load_implicit_pages(self) -> None:
        """Searches the PRC_DIR and/or PRC_PATH directories for `*.prc` files and loads
        them in as pages.  This is normally called automatically at startup time,
        when the first variable's value is referenced.  See also
        reload_implicit_pages().
        """
    def reload_implicit_pages(self) -> None:
        """Searches the PRC_DIR and/or PRC_PATH directories for *.prc files and loads
        them in as pages.

        This may be called after startup, to force the system to re-read all of the
        implicit prc files.
        """
    def get_search_path(self) -> DSearchPath:
        """Returns the search path used to locate implicit .prc files.  This is
        determined by the PRC_DIR and PRC_PATH environment variables.  The object
        returned by this method may be modified to change the path at runtime, and
        then reload_implicit_pages() called.
        """
    def get_num_prc_patterns(self) -> int:
        """Returns the number of patterns, like `*.prc`, that are compiled in that
        will be searched for as default config filenames.  Normally there is only
        one pattern, and it is `*.prc`, but others may be specified with the
        PRC_FILENAME variable in Config.pp.
        """
    def get_prc_pattern(self, n: int) -> str:
        """Returns the nth filename pattern that will be considered a match as a valid
        config file.  See get_num_prc_patterns().
        """
    def get_num_prc_encrypted_patterns(self) -> int:
        """Returns the number of patterns, like `*.pre`, that are compiled in that
        will be searched for as special config files that are understood to be
        encrypted.
        """
    def get_prc_encrypted_pattern(self, n: int) -> str:
        """Returns the nth filename pattern that will be considered a match as a valid
        encrypted config file.  See get_num_prc_encrypted_patterns().
        """
    def get_num_prc_executable_patterns(self) -> int:
        """Returns the number of patterns, like `*.exe`, that are compiled in that
        will be searched for as special config files that are to be executed as a
        program, and their output taken to be input.  This is normally empty.
        """
    def get_prc_executable_pattern(self, n: int) -> str:
        """Returns the nth filename pattern that will be considered a match as a valid
        executable-style config file.  See get_num_prc_executable_patterns().
        """
    def make_explicit_page(self, name: str) -> ConfigPage:
        """Creates and returns a new, empty ConfigPage.  This page will be stacked on
        top of any pages that were created before; it may shadow variable
        declarations that are defined in previous pages.
        """
    def delete_explicit_page(self, page: ConfigPage) -> bool:
        """Removes a previously-constructed ConfigPage from the set of active pages,
        and deletes it.  The ConfigPage object is no longer valid after this call.
        Returns true if the page is successfully deleted, or false if it was
        unknown (which should never happen if the page was legitimately
        constructed).
        """
    def get_num_implicit_pages(self) -> int:
        """Returns the current number of implicitly-loaded ConfigPages in the world.
        These represent files that were automatically discovered on the disk as
        .prc files.
        """
    def get_implicit_page(self, n: int) -> ConfigPage:
        """Returns the nth implicit ConfigPage in the world.  See
        get_num_implicit_pages().
        """
    def get_num_explicit_pages(self) -> int:
        """Returns the current number of explicitly-loaded ConfigPages in the world.
        These represent pages that were loaded dynamically at runtime by explicit
        calls to ConfigPageManager::make_explicit_page().
        """
    def get_explicit_page(self, n: int) -> ConfigPage:
        """Returns the nth explicit ConfigPage in the world.  See
        get_num_explicit_pages().
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def get_global_ptr() -> ConfigPageManager: ...
    loadedImplicitPages = loaded_implicit_pages
    loadImplicitPages = load_implicit_pages
    reloadImplicitPages = reload_implicit_pages
    getSearchPath = get_search_path
    getNumPrcPatterns = get_num_prc_patterns
    getPrcPattern = get_prc_pattern
    getNumPrcEncryptedPatterns = get_num_prc_encrypted_patterns
    getPrcEncryptedPattern = get_prc_encrypted_pattern
    getNumPrcExecutablePatterns = get_num_prc_executable_patterns
    getPrcExecutablePattern = get_prc_executable_pattern
    makeExplicitPage = make_explicit_page
    deleteExplicitPage = delete_explicit_page
    getNumImplicitPages = get_num_implicit_pages
    getImplicitPage = get_implicit_page
    getNumExplicitPages = get_num_explicit_pages
    getExplicitPage = get_explicit_page
    getGlobalPtr = get_global_ptr

class ConfigVariableManager:
    """A global object that maintains the set of ConfigVariables (actually,
    ConfigVariableCores) everywhere in the world, and keeps them in sorted
    order.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def variables(self) -> Sequence[ConfigVariableCore]: ...
    def make_variable(self, name: str) -> ConfigVariableCore:
        """Creates and returns a new, undefined ConfigVariableCore with the indicated
        name; or if a variable with this name has already been created, returns
        that one instead.
        """
    def make_variable_template(
        self, pattern: str, type: _ConfigFlags_ValueType, default_value: str, description: str = ..., flags: int = ...
    ) -> ConfigVariableCore:
        """Defines a variable "template" to match against dynamically-defined
        variables that may or may not be created in the future.

        The template consists of a glob pattern, e.g.  `notify-level-*`, which will
        be tested against any config variable passed to a future call to
        make_variable().  If the pattern matches, the returned ConfigVariableCore
        is copied to define the new variable, instead of creating a default, empty
        one.

        This is useful to pre-specify default values for a family of variables that
        all have similar properties, and all may not be created at the same time.
        It is especially useful to avoid cluttering up the list of available
        variables with user-declared variables that have not been defined yet by
        the application (e.g. `egg-object-type-*`).

        This method basically pre-defines all variables that match the specified
        glob pattern.
        """
    def get_num_variables(self) -> int:
        """Returns the current number of active ConfigVariableCores in the world."""
    def get_variable(self, n: int) -> ConfigVariableCore:
        """Returns the nth active ConfigVariableCore in the world."""
    def get_variable_name(self, n: int) -> str:
        """Returns the name of the nth active ConfigVariable in the list."""
    def is_variable_used(self, n: int) -> bool:
        """Returns true if the nth active ConfigVariable in the list has been used by
        code, false otherwise.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    def write_prc_variables(self, out: ostream) -> None:
        """Writes all of the prc-set config variables, as they appear in a prc file
        somewhere, one per line, very concisely.  This lists the dominant value in
        the prc file; it does not list shadowed values, and it does not list
        locally-set values.

        This is mainly intended for generating a hash of the input config file
        state.
        """
    def list_unused_variables(self) -> None:
        """Writes a list of all the variables that have been defined in a prc file
        without having been declared somewhere in code.
        """
    def list_variables(self) -> None:
        """Writes a list of all the variables that have been declared somewhere in
        code, along with a brief description.
        """
    def list_dynamic_variables(self) -> None:
        """Writes a list of all the "dynamic" variables that have been declared
        somewhere in code, along with a brief description.  This is a (usually
        large) list of config variables that are declared with a generated variable
        name.
        """
    @staticmethod
    def get_global_ptr() -> ConfigVariableManager: ...
    def get_variables(self) -> tuple[ConfigVariableCore, ...]: ...
    makeVariable = make_variable
    makeVariableTemplate = make_variable_template
    getNumVariables = get_num_variables
    getVariable = get_variable
    getVariableName = get_variable_name
    isVariableUsed = is_variable_used
    writePrcVariables = write_prc_variables
    listUnusedVariables = list_unused_variables
    listVariables = list_variables
    listDynamicVariables = list_dynamic_variables
    getGlobalPtr = get_global_ptr
    getVariables = get_variables

class ConfigVariableBase(ConfigFlags):
    """This class is the base class for both ConfigVariableList and ConfigVariable
    (and hence for all of the ConfigVariableBool, ConfigVaribleString, etc.
    classes).  It collects together the common interface for all generic
    ConfigVariables.

    Mostly, this class serves as a thin wrapper around ConfigVariableCore
    and/or ConfigDeclaration, more or less duplicating the interface presented
    there.
    """

    @property
    def name(self) -> str: ...
    @property
    def value_type(self) -> _ConfigFlags_ValueType: ...
    @property
    def description(self) -> str: ...
    @property
    def closed(self) -> bool: ...
    @property
    def trust_level(self) -> int: ...
    @property
    def dynamic(self) -> bool: ...
    def get_name(self) -> str:
        """Returns the name of the variable."""
    def get_value_type(self) -> _ConfigFlags_ValueType:
        """Returns the stated type of this variable.  This should be VT_list, unless a
        later variable declaration has changed it.
        """
    def get_description(self) -> str:
        """Returns the brief description of this variable, if it has been defined."""
    def get_flags(self) -> int:
        """Returns the flags value as set by set_flags().  This includes the trust
        level and some other settings.  See the individual methods is_closed(),
        get_trust_level(), etc.  to pull out the semantic meaning of these flags
        individually.
        """
    def is_closed(self) -> bool:
        """Returns true if the variable is not trusted by any prc file (and hence
        cannot be modified from its compiled-in default value), or false for the
        normal case, in which the variable can be modified by any prc file at or
        above its trust level (see get_trust_level()).

        This value only has effect in a release build (specifically, when
        PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
        """
    def get_trust_level(self) -> int:
        """Returns the minimum trust_level a prc file must demonstrate in order to
        redefine the value for this variable.  Arguably, this should be called the
        "mistrust level", since the larger the value, the more suspicious we are of
        prc files.  This value is not used if is_closed() returns true, which
        indicates no file may be trusted.

        This value only has effect in a release build (specifically, when
        PRC_RESPECT_TRUST_LEVEL is defined true in Config.pp).
        """
    def is_dynamic(self) -> bool:
        """Returns true if the variable was indicated as "dynamic" by its constructor,
        indicating that its name was dynamically generated, possibly from a large
        pool, and it should not be listed along with the other variables.
        """
    def clear_local_value(self) -> bool:
        """Removes the local value defined for this variable, and allows its value to
        be once again retrieved from the .prc files.

        Returns true if the value was successfully removed, false if it did not
        exist in the first place.
        """
    def has_local_value(self) -> bool:
        """Returns true if this variable's value has been shadowed by a local
        assignment (as created via make_local_value()), or false otherwise.
        """
    def has_value(self) -> bool:
        """Returns true if this variable has an explicit value, either from a prc file
        or locally set, or false if variable has its default value.
        """
    def output(self, out: ostream) -> None: ...
    def write(self, out: ostream) -> None: ...
    getName = get_name
    getValueType = get_value_type
    getDescription = get_description
    getFlags = get_flags
    isClosed = is_closed
    getTrustLevel = get_trust_level
    isDynamic = is_dynamic
    clearLocalValue = clear_local_value
    hasLocalValue = has_local_value
    hasValue = has_value

class ConfigVariable(ConfigVariableBase):
    """This is a generic, untyped ConfigVariable.  It is also the base class for
    the typed ConfigVariables, and contains all of the code common to
    ConfigVariables of all types (except ConfigVariableList, which is a bit of
    a special case).

    Mostly, this class serves as a thin wrapper around ConfigVariableCore
    and/or ConfigDeclaration, more or less duplicating the interface presented
    there.
    """

    @overload
    def __init__(self, __param0: ConfigVariable) -> None:
        """Use this constructor to make a ConfigVariable of an unspecified type.
        Usually you'd want to do this just to reference a previously-defined
        ConfigVariable of a specific type, without having to know what type it is.
        """
    @overload
    def __init__(self, name: str) -> None: ...
    def get_string_value(self) -> str:
        """Returns the toplevel value of the variable, formatted as a string."""
    def set_string_value(self, value: str) -> None:
        """Changes the value assigned to this variable.  This creates a local value
        that shadows any values defined in the .prc files, until
        clear_local_value() is called.
        """
    def clear_value(self) -> None:
        """Removes the value assigned to this variable, and lets its original value
        (as read from the prc files) show through.
        """
    def get_num_words(self) -> int:
        """Returns the number of words in the variable's value.  A word is defined as
        a sequence of non-whitespace characters delimited by whitespace.
        """
    getStringValue = get_string_value
    setStringValue = set_string_value
    clearValue = clear_value
    getNumWords = get_num_words

class ConfigVariableBool(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as a boolean type."""

    value: bool
    @property
    def default_value(self) -> bool: ...
    @overload
    def __init__(self, __param0: ConfigVariableBool) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: bool | str, description: str = ..., flags: int = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int:
        """Returns the number of unique words in the variable."""
    def __getitem__(self, n: int) -> bool: ...
    def __iter__(self) -> Iterator[bool]: ...  # Doesn't actually exist
    def assign(self, value: bool) -> Self: ...
    def set_value(self, value: bool) -> None:
        """Reassigns the variable's local value."""
    def get_value(self) -> bool:
        """Returns the variable's value."""
    def get_default_value(self) -> bool:
        """Returns the variable's default value."""
    def get_word(self, n: int) -> bool:
        """Returns the variable's nth value."""
    def set_word(self, n: int, value: bool) -> None:
        """Reassigns the variable's nth value.  This makes a local copy of the
        variable's overall value.
        """
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value
    getWord = get_word
    setWord = set_word

class ConfigVariableDouble(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as a floating-
    point type.
    """

    value: float
    @property
    def default_value(self) -> float: ...
    @overload
    def __init__(self, __param0: ConfigVariableDouble) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: float | str, description: str = ..., flags: int = ...) -> None: ...
    def __float__(self) -> float: ...
    def __len__(self) -> int:
        """Returns the number of unique words in the variable."""
    def __getitem__(self, n: int) -> float: ...
    def __iter__(self) -> Iterator[float]: ...  # Doesn't actually exist
    def assign(self, value: float) -> Self: ...
    def set_value(self, value: float) -> None:
        """Reassigns the variable's local value."""
    def get_value(self) -> float:
        """Returns the variable's value."""
    def get_default_value(self) -> float:
        """Returns the variable's default value."""
    def get_word(self, n: int) -> float:
        """Returns the variable's nth value."""
    def set_word(self, n: int, value: float) -> None:
        """Reassigns the variable's nth value.  This makes a local copy of the
        variable's overall value.
        """
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value
    getWord = get_word
    setWord = set_word

class ConfigVariableFilename(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as a Filename
    type.  It is almost the same thing as ConfigVariableString, except it
    handles an implicit Filename::expand_from() operation so that the user may
    put OS-specific filenames, or filenames based on environment variables, in
    the prc file.
    """

    value: Filename
    @property
    def default_value(self) -> Filename: ...
    @overload
    def __init__(self, __param0: ConfigVariableFilename) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: StrOrBytesPath, description: str = ..., flags: int = ...) -> None: ...
    def __getitem__(self, n: int) -> str: ...
    def __eq__(self, __other: object) -> bool:
        """Comparison operators are handy."""
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: StrOrBytesPath) -> bool: ...
    def __fspath__(self) -> str:
        """Allows a ConfigVariableFilename object to be passed to any Python function
        that accepts an os.PathLike object.

        @since 1.10.13
        """
    def operator_typecast(self) -> Filename: ...
    def assign(self, value: StrOrBytesPath) -> Self: ...
    def c_str(self) -> str:
        """These methods help the ConfigVariableFilename act like a Filename object."""
    def empty(self) -> bool: ...
    def length(self) -> int: ...
    def get_fullpath(self) -> str:
        """Returns the entire filename: directory, basename, extension.  This is the
        same thing returned by the string typecast operator, so this function is a
        little redundant.
        """
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
    def set_value(self, value: StrOrBytesPath) -> None:
        """Reassigns the variable's local value."""
    def get_value(self) -> Filename:
        """Returns the variable's value."""
    def get_default_value(self) -> Filename:
        """Returns the variable's default value."""
    def get_word(self, n: int) -> Filename:
        """Returns the variable's nth value."""
    def set_word(self, n: int, value: StrOrBytesPath) -> None:
        """Reassigns the variable's nth value.  This makes a local copy of the
        variable's overall value.
        """
    operatorTypecast = operator_typecast
    cStr = c_str
    getFullpath = get_fullpath
    getDirname = get_dirname
    getBasename = get_basename
    getFullpathWoExtension = get_fullpath_wo_extension
    getBasenameWoExtension = get_basename_wo_extension
    getExtension = get_extension
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value
    getWord = get_word
    setWord = set_word
    Fspath = __fspath__

class ConfigVariableInt(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as an integer
    type.
    """

    value: int
    @property
    def default_value(self) -> int: ...
    @overload
    def __init__(self, __param0: ConfigVariableInt) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: int | str, description: str = ..., flags: int = ...) -> None: ...
    def __int__(self) -> int: ...
    def __len__(self) -> int:
        """Returns the number of unique words in the variable."""
    def __getitem__(self, n: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    def assign(self, value: int) -> Self: ...
    def set_value(self, value: int) -> None:
        """Reassigns the variable's local value."""
    def get_value(self) -> int:
        """Returns the variable's value."""
    def get_default_value(self) -> int:
        """Returns the variable's default value."""
    def get_word(self, n: int) -> int:
        """Returns the variable's nth value."""
    def set_word(self, n: int, value: int) -> None:
        """Reassigns the variable's nth value.  This makes a local copy of the
        variable's overall value.
        """
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value
    getWord = get_word
    setWord = set_word

class ConfigVariableInt64(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as a 64-bit
    integer type.
    """

    value: int
    @property
    def default_value(self) -> int: ...
    @overload
    def __init__(self, __param0: ConfigVariableInt64) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: int | str, description: str = ..., flags: int = ...) -> None: ...
    def __int__(self) -> int: ...
    def __len__(self) -> int:
        """Returns the number of unique words in the variable."""
    def __getitem__(self, n: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...  # Doesn't actually exist
    def assign(self, value: int) -> Self: ...
    def set_value(self, value: int) -> None:
        """Reassigns the variable's local value."""
    def get_value(self) -> int:
        """Returns the variable's value."""
    def get_default_value(self) -> int:
        """Returns the variable's default value."""
    def get_word(self, n: int) -> int:
        """Returns the variable's nth value."""
    def set_word(self, n: int, value: int) -> None:
        """Reassigns the variable's nth value.  This makes a local copy of the
        variable's overall value.
        """
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value
    getWord = get_word
    setWord = set_word

class ConfigVariableList(ConfigVariableBase):
    """This class is similar to ConfigVariable, but it reports its value as a list
    of strings.  In this special case, all of the declarations of the variable
    are returned as the elements of this list, in order.

    Note that this is different from a normal ConfigVariableString, which just
    returns its topmost value, which can optionally be treated as a number of
    discrete words by dividing it at the spaces.

    A ConfigVariableList cannot be modified locally.
    """

    @overload
    def __init__(self, __param0: ConfigVariableList) -> None: ...
    @overload
    def __init__(self, name: str, description: str = ..., flags: int = ...) -> None: ...
    def __len__(self) -> int:
        """Returns the number of unique values of the variable."""
    def __getitem__(self, n: int) -> str: ...
    def __iter__(self) -> Iterator[str]: ...  # Doesn't actually exist
    def get_num_values(self) -> int:
        """Returns the number of values in the variable."""
    def get_string_value(self, n: int) -> str:
        """Returns the nth value of the variable."""
    def get_num_unique_values(self) -> int:
        """Returns the number of unique values in the variable."""
    def get_unique_value(self, n: int) -> str:
        """Returns the nth unique value of the variable."""
    getNumValues = get_num_values
    getStringValue = get_string_value
    getNumUniqueValues = get_num_unique_values
    getUniqueValue = get_unique_value

class ConfigVariableSearchPath(ConfigVariableBase):
    """This is similar to a ConfigVariableList, but it returns its list as a
    DSearchPath, as a list of directories.

    You may locally append directories to the end of the search path with the
    methods here, or prepend them to the beginning.  Use these methods to make
    adjustments to the path; do not attempt to directly modify the const
    DSearchPath object returned by get_value().

    Unlike other ConfigVariable types, local changes (made by calling
    append_directory() and prepend_directory()) are specific to this particular
    instance of the ConfigVariableSearchPath.  A separate instance of the same
    variable, created by using the same name to the constructor, will not
    reflect the local changes.
    """

    @property
    def value(self) -> DSearchPath: ...
    @property
    def default_value(self) -> DSearchPath: ...
    @property
    def directories(self) -> Sequence[Filename]: ...
    @overload
    def __init__(self, name: str, description: str = ..., flags: int = ...) -> None: ...
    @overload
    def __init__(self, name: str, default_value: SearchPathLike, description: str, flags: int = ...) -> None: ...
    def operator_typecast_DSearchPath(self) -> DSearchPath: ...
    def get_value(self) -> DSearchPath: ...
    def get_default_value(self) -> DSearchPath: ...
    def clear_local_value(self) -> bool:
        """Removes all the directories locally added to the search list, and restores
        it to its original form.
        """
    def clear(self) -> None:
        """Removes all the directories locally added to the search list, and restores
        it to its original form.
        """
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
    def get_directories(self) -> tuple[Filename, ...]: ...
    operatorTypecastDSearchPath = operator_typecast_DSearchPath
    getValue = get_value
    getDefaultValue = get_default_value
    clearLocalValue = clear_local_value
    appendDirectory = append_directory
    prependDirectory = prepend_directory
    appendPath = append_path
    prependPath = prepend_path
    isEmpty = is_empty
    getNumDirectories = get_num_directories
    getDirectory = get_directory
    findFile = find_file
    findAllFiles = find_all_files
    getDirectories = get_directories

class ConfigVariableString(ConfigVariable):
    """This is a convenience class to specialize ConfigVariable as a string type."""

    value: str
    @property
    def default_value(self) -> str: ...
    @overload
    def __init__(self, __param0: ConfigVariableString) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, name: str, default_value: str, description: str = ..., flags: int = ...) -> None: ...
    def __getitem__(self, n: int) -> str: ...
    def __eq__(self, __other: object) -> bool:
        """Comparison operators are handy."""
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: str) -> bool: ...
    def assign(self, value: str) -> Self: ...
    def c_str(self) -> str:
        """These methods help the ConfigVariableString act like a C++ string object."""
    def empty(self) -> bool: ...
    def length(self) -> int: ...
    def set_value(self, value: str) -> None:
        """Reassigns the variable's local value."""
    def get_value(self) -> str:
        """Returns the variable's value."""
    def get_default_value(self) -> str:
        """Returns the variable's default value."""
    def get_word(self, n: int) -> str:
        """Returns the variable's nth value."""
    def set_word(self, n: int, value: str) -> None:
        """Reassigns the variable's nth value.  This makes a local copy of the
        variable's overall value.
        """
    cStr = c_str
    setValue = set_value
    getValue = get_value
    getDefaultValue = get_default_value
    getWord = get_word
    setWord = set_word

class NotifyCategory(ConfigFlags):
    """A particular category of error messages.  Typically there will be one of
    these per package, so that we can turn on or off error messages at least at
    a package level; further nested categories can be created within a package
    if a finer grain of control is required.
    """

    severity: _NotifySeverity
    @property
    def fullname(self) -> str: ...
    @property
    def basename(self) -> str: ...
    @property
    def children(self) -> Sequence[NotifyCategory]: ...
    def __init__(self, __param0: NotifyCategory) -> None: ...
    def upcast_to_ConfigFlags(self) -> ConfigFlags: ...
    def get_fullname(self) -> str: ...
    def get_basename(self) -> str: ...
    def get_severity(self) -> _NotifySeverity: ...
    def set_severity(self, severity: _NotifySeverity) -> None:
        """Sets the severity level of messages that will be reported from this
        Category.  This allows any message of this severity level or higher.
        """
    def is_on(self, severity: _NotifySeverity) -> bool:
        """Returns true if messages of the indicated severity level ought to be
        reported for this Category.
        """
    def is_spam(self) -> bool:
        """When NOTIFY_DEBUG is not defined, the categories will never be set to
        "spam" or "debug" severities, and these methods are redefined to be
        static to make it more obvious to the compiler.  However, we still want
        to present a consistent interface to our scripting language, so during
        the interrogate pass (that is, when CPPPARSER is defined), we still
        pretend they're nonstatic.
        """
    def is_debug(self) -> bool:
        """A shorthand way to write is_on(NS_debug)."""
    def is_info(self) -> bool:
        """A shorthand way to write is_on(NS_info)."""
    def is_warning(self) -> bool:
        """A shorthand way to write is_on(NS_warning)."""
    def is_error(self) -> bool:
        """A shorthand way to write is_on(NS_error)."""
    def is_fatal(self) -> bool:
        """A shorthand way to write is_on(NS_fatal)."""
    def out(self, severity: _NotifySeverity, prefix: bool = ...) -> ostream:
        """Begins a new message to this Category at the indicated severity level.  If
        the indicated severity level is enabled, this writes a prefixing string to
        the Notify::out() stream and returns that.  If the severity level is
        disabled, this returns Notify::null().
        """
    def spam(self, prefix: bool = ...) -> ostream:
        """A shorthand way to write out(NS_spam)."""
    def debug(self, prefix: bool = ...) -> ostream:
        """A shorthand way to write out(NS_debug)."""
    def info(self, prefix: bool = ...) -> ostream:
        """A shorthand way to write out(NS_info)."""
    def warning(self, prefix: bool = ...) -> ostream:
        """A shorthand way to write out(NS_warning)."""
    def error(self, prefix: bool = ...) -> ostream:
        """A shorthand way to write out(NS_error)."""
    def fatal(self, prefix: bool = ...) -> ostream:
        """A shorthand way to write out(NS_fatal)."""
    def get_num_children(self) -> int:
        """Returns the number of child Categories of this particular Category."""
    def get_child(self, i: int) -> NotifyCategory:
        """Returns the nth child Category of this particular Category."""
    @staticmethod
    def set_server_delta(delta: int) -> None:
        """Sets a global delta (in seconds) between the local time and the server's
        time, for the purpose of synchronizing the time stamps in the log messages
        of the client with that of a known server.
        """
    def get_children(self) -> tuple[NotifyCategory, ...]: ...
    upcastToConfigFlags = upcast_to_ConfigFlags
    getFullname = get_fullname
    getBasename = get_basename
    getSeverity = get_severity
    setSeverity = set_severity
    isOn = is_on
    isSpam = is_spam
    isDebug = is_debug
    isInfo = is_info
    isWarning = is_warning
    isError = is_error
    isFatal = is_fatal
    getNumChildren = get_num_children
    getChild = get_child
    setServerDelta = set_server_delta
    getChildren = get_children

class IDecryptStream(istream):
    """An input stream object that uses OpenSSL to decrypt the input from another
    source stream on-the-fly.

    Attach an IDecryptStream to an existing istream that provides encrypted
    data, as generated by an OEncryptStream, and read the corresponding
    unencrypted data from the IDecryptStream.

    Seeking is not supported.
    """

    @property
    def algorithm(self) -> str: ...
    @property
    def key_length(self) -> int: ...
    @property
    def iteration_count(self) -> int: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source: istream, owns_source: bool, password: str) -> None: ...
    def open(self, source: istream, owns_source: bool, password: str) -> IDecryptStream: ...
    def close(self) -> IDecryptStream:
        """Resets the EncryptStream to empty, but does not actually close the source
        istream unless owns_source was true.
        """
    def get_algorithm(self) -> str:
        """Returns the encryption algorithm that was read from the stream."""
    def get_key_length(self) -> int:
        """Returns the encryption key length, in bits, that was read from the stream."""
    def get_iteration_count(self) -> int:
        """Returns the value that was was read from the stream."""
    getAlgorithm = get_algorithm
    getKeyLength = get_key_length
    getIterationCount = get_iteration_count

class OEncryptStream(ostream):
    """An input stream object that uses OpenSSL to encrypt data to another
    destination stream on-the-fly.

    Attach an OEncryptStream to an existing ostream that will accept encrypted
    data, and write your unencrypted source data to the OEncryptStream.

    Seeking is not supported.
    """

    algorithm: str
    key_length: int
    iteration_count: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, dest: ostream, owns_dest: bool, password: str) -> None: ...
    def open(self, dest: ostream, owns_dest: bool, password: str) -> OEncryptStream: ...
    def close(self) -> OEncryptStream:
        """Resets the EncryptStream to empty, but does not actually close the dest
        ostream unless owns_dest was true.
        """
    def set_algorithm(self, algorithm: str) -> None:
        """Specifies the encryption algorithm that should be used for future calls to
        open().  The default is whatever is specified by the encryption-algorithm
        config variable.  The complete set of available algorithms is defined by
        the current version of OpenSSL.

        If an invalid algorithm is specified, there is no immediate error return
        code, but open() will fail.
        """
    def set_key_length(self, key_length: int) -> None:
        """Specifies the length of the key, in bits, that should be used to encrypt
        the stream in future calls to open().  The default is whatever is specified
        by the encryption-key-length config variable.

        If an invalid key_length for the chosen algorithm is specified, there is no
        immediate error return code, but open() will fail.
        """
    def set_iteration_count(self, iteration_count: int) -> None:
        """Specifies the number of times to repeatedly hash the key before writing it
        to the stream in future calls to open().  Its purpose is to make it
        computationally more expensive for an attacker to search the key space
        exhaustively.  This should be a multiple of 1,000 and should not exceed
        about 65 million; the value 0 indicates just one application of the hashing
        algorithm.

        The default is whatever is specified by the encryption-iteration-count
        config variable.
        """
    setAlgorithm = set_algorithm
    setKeyLength = set_key_length
    setIterationCount = set_iteration_count

class StreamReader:
    """A class to read sequential binary data directly from an istream.  Its
    interface is similar to DatagramIterator by design; see also StreamWriter.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def istream(self) -> istream: ...
    @overload
    def __init__(self, copy: StreamReader) -> None:
        """`(self, copy: StreamReader)`:
        The copy constructor does not copy ownership of the stream.

        `(self, _in: istream, owns_stream: bool)`:
        If owns_stream is true, the stream pointer will be deleted when the
        StreamReader destructs.
        """
    @overload
    def __init__(self, _in: core.istream, owns_stream: bool) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_istream(self) -> core.istream:
        """Returns the stream in use."""
    def get_bool(self) -> bool:
        """Extracts a boolean value."""
    def get_int8(self) -> str:
        """Extracts a signed 8-bit integer."""
    def get_uint8(self) -> str:
        """Extracts an unsigned 8-bit integer."""
    def get_int16(self) -> int:
        """Extracts a signed 16-bit integer."""
    def get_int32(self) -> int:
        """Extracts a signed 32-bit integer."""
    def get_int64(self) -> int:
        """Extracts a signed 64-bit integer."""
    def get_uint16(self) -> int:
        """Extracts an unsigned 16-bit integer."""
    def get_uint32(self) -> int:
        """Extracts an unsigned 32-bit integer."""
    def get_uint64(self) -> int:
        """Extracts an unsigned 64-bit integer."""
    def get_float32(self) -> float:
        """Extracts a 32-bit single-precision floating-point number.  Since this kind
        of float is not necessarily portable across different architectures,
        special care is required.
        """
    def get_float64(self) -> float:
        """Extracts a 64-bit floating-point number."""
    def get_be_int16(self) -> int:
        """Extracts a signed big-endian 16-bit integer."""
    def get_be_int32(self) -> int:
        """Extracts a signed big-endian 32-bit integer."""
    def get_be_int64(self) -> int:
        """Extracts a signed big-endian 64-bit integer."""
    def get_be_uint16(self) -> int:
        """Extracts an unsigned big-endian 16-bit integer."""
    def get_be_uint32(self) -> int:
        """Extracts an unsigned big-endian 32-bit integer."""
    def get_be_uint64(self) -> int:
        """Extracts an unsigned big-endian 64-bit integer."""
    def get_be_float32(self) -> float:
        """Extracts a 32-bit single-precision big-endian floating-point number.  Since
        this kind of float is not necessarily portable across different
        architectures, special care is required.
        """
    def get_be_float64(self) -> float:
        """Extracts a 64-bit big-endian floating-point number."""
    def get_string(self) -> str:
        """Extracts a variable-length string."""
    def get_string32(self) -> str:
        """Extracts a variable-length string with a 32-bit length field."""
    def get_z_string(self) -> str:
        """Extracts a variable-length string, as a NULL-terminated string."""
    def get_fixed_string(self, size: int) -> str:
        """Extracts a fixed-length string.  However, if a zero byte occurs within the
        string, it marks the end of the string.
        """
    def skip_bytes(self, size: int) -> None:
        """Skips over the indicated number of bytes in the stream."""
    def extract_bytes(self, size: int) -> bytes:
        """Extracts the indicated number of bytes in the stream and returns them as a
        string.  Returns empty string at end-of-file.
        """
    def readline(self) -> bytes:
        """Assumes the stream represents a text file, and extracts one line up to and
        including the trailing newline character.  Returns empty string when the
        end of file is reached.

        The interface here is intentionally designed to be similar to that for
        Python's File.readline() function.
        """
    def readlines(self) -> list[bytes]: ...
    getIstream = get_istream
    getBool = get_bool
    getInt8 = get_int8
    getUint8 = get_uint8
    getInt16 = get_int16
    getInt32 = get_int32
    getInt64 = get_int64
    getUint16 = get_uint16
    getUint32 = get_uint32
    getUint64 = get_uint64
    getFloat32 = get_float32
    getFloat64 = get_float64
    getBeInt16 = get_be_int16
    getBeInt32 = get_be_int32
    getBeInt64 = get_be_int64
    getBeUint16 = get_be_uint16
    getBeUint32 = get_be_uint32
    getBeUint64 = get_be_uint64
    getBeFloat32 = get_be_float32
    getBeFloat64 = get_be_float64
    getString = get_string
    getString32 = get_string32
    getZString = get_z_string
    getFixedString = get_fixed_string
    skipBytes = skip_bytes
    extractBytes = extract_bytes

class StreamWriter:
    """A StreamWriter object is used to write sequential binary data directly to
    an ostream.  Its interface is very similar to Datagram by design; it's
    primarily intended as a convenience to eliminate the overhead of writing
    bytes to a Datagram and then writing the Datagram to a stream.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    softspace: int
    """Python 2 needs this for printing to work correctly."""
    @property
    def ostream(self) -> ostream: ...
    @overload
    def __init__(self, copy: StreamWriter) -> None:
        """The copy constructor does not copy ownership of the stream."""
    @overload
    def __init__(self, out: core.ostream, owns_stream: bool) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def assign(self, copy: Self) -> Self: ...
    def get_ostream(self) -> core.ostream:
        """Returns the stream in use."""
    def add_bool(self, value: bool) -> None:
        """Adds a boolean value to the stream."""
    def add_int8(self, value: str) -> None:
        """Adds a signed 8-bit integer to the stream."""
    def add_uint8(self, value: str) -> None:
        """Adds an unsigned 8-bit integer to the stream."""
    def add_int16(self, value: int) -> None:
        """Adds a signed 16-bit integer to the stream."""
    def add_int32(self, value: int) -> None:
        """Adds a signed 32-bit integer to the stream."""
    def add_int64(self, value: int) -> None:
        """Adds a signed 64-bit integer to the stream."""
    def add_uint16(self, value: int) -> None:
        """Adds an unsigned 16-bit integer to the stream."""
    def add_uint32(self, value: int) -> None:
        """Adds an unsigned 32-bit integer to the stream."""
    def add_uint64(self, value: int) -> None:
        """Adds an unsigned 64-bit integer to the stream."""
    def add_float32(self, value: float) -> None:
        """Adds a 32-bit single-precision floating-point number to the stream.  Since
        this kind of float is not necessarily portable across different
        architectures, special care is required.
        """
    def add_float64(self, value: float) -> None:
        """Adds a 64-bit floating-point number to the stream."""
    def add_be_int16(self, value: int) -> None:
        """Adds a signed 16-bit big-endian integer to the streamWriter."""
    def add_be_int32(self, value: int) -> None:
        """Adds a signed 32-bit big-endian integer to the streamWriter."""
    def add_be_int64(self, value: int) -> None:
        """Adds a signed 64-bit big-endian integer to the streamWriter."""
    def add_be_uint16(self, value: int) -> None:
        """Adds an unsigned 16-bit big-endian integer to the streamWriter."""
    def add_be_uint32(self, value: int) -> None:
        """Adds an unsigned 32-bit big-endian integer to the streamWriter."""
    def add_be_uint64(self, value: int) -> None:
        """Adds an unsigned 64-bit big-endian integer to the streamWriter."""
    def add_be_float32(self, value: float) -> None:
        """Adds a 32-bit single-precision big-endian floating-point number to the
        stream.  Since this kind of float is not necessarily portable across
        different architectures, special care is required.
        """
    def add_be_float64(self, value: float) -> None:
        """Adds a 64-bit big-endian floating-point number to the streamWriter."""
    def add_string(self, str: str) -> None:
        """Adds a variable-length string to the stream.  This actually adds a count
        followed by n bytes.
        """
    def add_string32(self, str: str) -> None:
        """Adds a variable-length string to the stream, using a 32-bit length field."""
    def add_z_string(self, str: str) -> None:
        """Adds a variable-length string to the stream, as a NULL-terminated string."""
    def add_fixed_string(self, str: str, size: int) -> None:
        """Adds a fixed-length string to the stream.  If the string given is less than
        the requested size, this will pad the string out with zeroes; if it is
        greater than the requested size, this will silently truncate the string.
        """
    def pad_bytes(self, size: int) -> None:
        """Adds the indicated number of zero bytes to the stream."""
    def append_data(self, data) -> None: ...
    def flush(self) -> None:
        """Calls flush() on the underlying stream."""
    def write(self, str: str) -> None:
        """A synonym of append_data().  This is useful when assigning the StreamWriter
        to sys.stderr and/or sys.stdout in Python.
        """
    getOstream = get_ostream
    addBool = add_bool
    addInt8 = add_int8
    addUint8 = add_uint8
    addInt16 = add_int16
    addInt32 = add_int32
    addInt64 = add_int64
    addUint16 = add_uint16
    addUint32 = add_uint32
    addUint64 = add_uint64
    addFloat32 = add_float32
    addFloat64 = add_float64
    addBeInt16 = add_be_int16
    addBeInt32 = add_be_int32
    addBeInt64 = add_be_int64
    addBeUint16 = add_be_uint16
    addBeUint32 = add_be_uint32
    addBeUint64 = add_be_uint64
    addBeFloat32 = add_be_float32
    addBeFloat64 = add_be_float64
    addString = add_string
    addString32 = add_string32
    addZString = add_z_string
    addFixedString = add_fixed_string
    padBytes = pad_bytes
    appendData = append_data

class StreamWrapperBase:
    """The base class for both IStreamWrapper and OStreamWrapper, this provides
    the common locking interface.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def acquire(self) -> None:
        """Acquires the internal lock.

        User code should call this to take temporary possession of the stream and
        perform direct I/O operations on it, for instance to make several
        sequential atomic reads.  You may not call any of the StreamWrapper methods
        while the lock is held, other than release().

        Use with extreme caution!  This is a very low-level, non-recursive lock.
        You must call acquire() only once, and you must later call release()
        exactly once.  Failing to do so may result in a hard deadlock with no
        available debugging features.
        """
    def release(self) -> None:
        """Releases the internal lock.  Must be called exactly once following a call
        to acquire().  See the cautions with acquire().
        """

class IStreamWrapper(StreamWrapperBase):
    """This class provides a locking wrapper around an arbitrary istream pointer.
    A thread may use this class to perform an atomic seek/read/gcount
    operation.
    """

    @property
    def istream(self) -> istream: ...
    def __init__(self, stream: core.istream) -> None: ...
    def upcast_to_StreamWrapperBase(self) -> StreamWrapperBase: ...
    def get_istream(self) -> core.istream:
        """Returns the istream this object is wrapping."""
    upcastToStreamWrapperBase = upcast_to_StreamWrapperBase
    getIstream = get_istream

class OStreamWrapper(StreamWrapperBase):
    """This class provides a locking wrapper around an arbitrary ostream pointer.
    A thread may use this class to perform an atomic seek/write operation.
    """

    @property
    def ostream(self) -> ostream: ...
    def __init__(self, stream: core.ostream) -> None: ...
    def upcast_to_StreamWrapperBase(self) -> StreamWrapperBase: ...
    def get_ostream(self) -> core.ostream:
        """Returns the ostream this object is wrapping."""
    upcastToStreamWrapperBase = upcast_to_StreamWrapperBase
    getOstream = get_ostream

class StreamWrapper(IStreamWrapper, OStreamWrapper):  # type: ignore[misc]
    """This class provides a locking wrapper around a combination ostream/istream
    pointer.
    """

    @property
    def iostream(self) -> iostream: ...  # noqa: F811
    def __init__(self, stream: core.iostream) -> None: ...
    def upcast_to_IStreamWrapper(self) -> IStreamWrapper: ...
    def upcast_to_OStreamWrapper(self) -> OStreamWrapper: ...
    def get_iostream(self) -> core.iostream:
        """Returns the iostream this object is wrapping."""
    upcastToIStreamWrapper = upcast_to_IStreamWrapper
    upcastToOStreamWrapper = upcast_to_OStreamWrapper
    getIostream = get_iostream

NS_unspecified: Final = 0
NSUnspecified: Final = 0
NS_spam: Final = 1
NSSpam: Final = 1
NS_debug: Final = 2
NSDebug: Final = 2
NS_info: Final = 3
NSInfo: Final = 3
NS_warning: Final = 4
NSWarning: Final = 4
NS_error: Final = 5
NSError: Final = 5
NS_fatal: Final = 6
NSFatal: Final = 6
