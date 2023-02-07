from _typeshed import StrOrBytesPath
from collections.abc import Sequence
from typing import Any, ClassVar, overload
from typing_extensions import Final, Literal, Self, TypeAlias

from panda3d.core._dtoolutil import istream, ostream
from panda3d.core._express import Datagram, DatagramIterator

_DCPackType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
_DCSubatomicType: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

class DCPackerInterface:
    """This defines the internal interface for packing values into a DCField.  The
    various different DC objects inherit from this.

    Normally these methods are called only by the DCPacker object; the user
    wouldn't normally call these directly.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def get_name(self) -> str:
        """Returns the name of this field, or empty string if the field is unnamed."""
    def find_seek_index(self, name: str) -> int:
        """Returns the index number to be passed to a future call to DCPacker::seek()
        to seek directly to the named field without having to look up the field
        name in a table later, or -1 if the named field cannot be found.

        If the named field is nested within a switch or some similar dynamic
        structure that reveals different fields based on the contents of the data,
        this mechanism cannot be used to pre-fetch the field index number--you must
        seek for the field by name.
        """
    def as_field(self) -> DCField: ...
    def as_switch_parameter(self) -> DCSwitchParameter: ...
    def as_class_parameter(self) -> DCClassParameter: ...
    @overload
    def check_match(self, other: DCPackerInterface) -> bool:
        """`(self, other: DCPackerInterface)`:
        Returns true if the other interface is bitwise the same as this one--that
        is, a uint32 only matches a uint32, etc.  Names of components, and range
        limits, are not compared.

        `(self, description: str, dcfile: DCFile = ...)`:
        Returns true if this interface is bitwise the same as the interface
        described with the indicated formatted string, e.g.  "(uint8, uint8,
        int16)", or false otherwise.

        If DCFile is not NULL, it specifies the DCFile that was previously loaded,
        from which some predefined structs and typedefs may be referenced in the
        description string.
        """
    @overload
    def check_match(self, description: str, dcfile: DCFile = ...) -> bool: ...
    getName = get_name
    findSeekIndex = find_seek_index
    asField = as_field
    asSwitchParameter = as_switch_parameter
    asClassParameter = as_class_parameter
    checkMatch = check_match

class DCKeywordList:
    """This is a list of keywords (see DCKeyword) that may be set on a particular
    field.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def has_keyword(self, keyword: DCKeyword) -> bool:
        """Returns true if this list includes the indicated keyword, false otherwise."""
    @overload
    def has_keyword(self, name: str) -> bool: ...
    def get_num_keywords(self) -> int:
        """Returns the number of keywords in the list."""
    def get_keyword(self, n: int) -> DCKeyword:
        """Returns the nth keyword in the list."""
    def get_keyword_by_name(self, name: str) -> DCKeyword:
        """Returns the keyword in the list with the indicated name, or NULL if there
        is no keyword in the list with that name.
        """
    def compare_keywords(self, other: DCKeywordList) -> bool:
        """Returns true if this list has the same keywords as the other list, false if
        some keywords differ.  Order is not considered important.
        """
    hasKeyword = has_keyword
    getNumKeywords = get_num_keywords
    getKeyword = get_keyword
    getKeywordByName = get_keyword_by_name
    compareKeywords = compare_keywords

class DCField(DCPackerInterface, DCKeywordList):
    """A single field of a Distributed Class, either atomic or molecular."""

    def upcast_to_DCPackerInterface(self) -> DCPackerInterface: ...
    def upcast_to_DCKeywordList(self) -> DCKeywordList: ...
    def get_number(self) -> int:
        """Returns a unique index number associated with this field.  This is defined
        implicitly when the .dc file(s) are read.
        """
    def get_class(self) -> DCClass:
        """Returns the DCClass pointer for the class that contains this field."""
    def as_atomic_field(self) -> DCAtomicField:
        """Returns the same field pointer converted to an atomic field pointer, if
        this is in fact an atomic field; otherwise, returns NULL.
        """
    def as_molecular_field(self) -> DCMolecularField:
        """Returns the same field pointer converted to a molecular field pointer, if
        this is in fact a molecular field; otherwise, returns NULL.
        """
    def as_parameter(self) -> DCParameter: ...
    def format_data(self, packed_data: bytes, show_field_names: bool = ...) -> str:
        """Given a blob that represents the packed data for this field, returns a
        string formatting it for human consumption.  Returns empty string if there
        is an error.
        """
    def parse_string(self, formatted_string: str) -> bytes:
        """Given a human-formatted string (for instance, as returned by format_data(),
        above) that represents the value of this field, parse the string and return
        the corresponding packed data.  Returns empty string if there is an error.
        """
    def validate_ranges(self, packed_data: bytes) -> bool:
        """Verifies that all of the packed values in the field data are within the
        specified ranges and that there are no extra bytes on the end of the
        record.  Returns true if all fields are valid, false otherwise.
        """
    def has_default_value(self) -> bool:
        """Returns true if a default value has been explicitly established for this
        field, false otherwise.
        """
    def get_default_value(self) -> bytes:
        """Returns the default value for this field.  If a default value has been
        explicitly set (e.g.  has_default_value() returns true), returns that
        value; otherwise, returns an implicit default for the field.
        """
    def is_bogus_field(self) -> bool:
        """Returns true if the field has been flagged as a bogus field.  This is set
        for fields that are generated by the parser as placeholder for missing
        fields, as when reading a partial file; it should not occur in a normal
        valid dc file.
        """
    def is_required(self) -> bool:
        """Returns true if the "required" flag is set for this field, false otherwise."""
    def is_broadcast(self) -> bool:
        """Returns true if the "broadcast" flag is set for this field, false
        otherwise.
        """
    def is_ram(self) -> bool:
        """Returns true if the "ram" flag is set for this field, false otherwise."""
    def is_db(self) -> bool:
        """Returns true if the "db" flag is set for this field, false otherwise."""
    def is_clsend(self) -> bool:
        """Returns true if the "clsend" flag is set for this field, false otherwise."""
    def is_clrecv(self) -> bool:
        """Returns true if the "clrecv" flag is set for this field, false otherwise."""
    def is_ownsend(self) -> bool:
        """Returns true if the "ownsend" flag is set for this field, false otherwise."""
    def is_ownrecv(self) -> bool:
        """Returns true if the "ownrecv" flag is set for this field, false otherwise."""
    def is_airecv(self) -> bool:
        """Returns true if the "airecv" flag is set for this field, false otherwise."""
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent_level: int) -> None:
        """Write a string representation of this instance to <out>."""
    def pack_args(self, packer: DCPacker, sequence) -> bool:
        """Packs the Python arguments from the indicated tuple into the packer.
        Returns true on success, false on failure.

        It is assumed that the packer is currently positioned on this field.
        """
    def unpack_args(self, packer: DCPacker):
        """Unpacks the values from the packer, beginning at the current point in the
        unpack_buffer, into a Python tuple and returns the tuple.

        It is assumed that the packer is currently positioned on this field.
        """
    def receive_update(self, packer: DCPacker, distobj) -> None:
        """Extracts the update message out of the datagram and applies it to the
        indicated object by calling the appropriate method.
        """
    def client_format_update(self, do_id: int, args) -> Datagram:
        """Generates a datagram containing the message necessary to send an update for
        the indicated distributed object from the client.
        """
    def ai_format_update(self, do_id: int, to_id: int, from_id: int, args) -> Datagram:
        """Generates a datagram containing the message necessary to send an update for
        the indicated distributed object from the AI.
        """
    def ai_format_update_msg_type(self, do_id: int, to_id: int, from_id: int, msg_type: int, args) -> Datagram:
        """Generates a datagram containing the message necessary to send an update,
        with the msg type, for the indicated distributed object from the AI.
        """
    upcastToDCPackerInterface = upcast_to_DCPackerInterface
    upcastToDCKeywordList = upcast_to_DCKeywordList
    getNumber = get_number
    getClass = get_class
    asAtomicField = as_atomic_field
    asMolecularField = as_molecular_field
    asParameter = as_parameter
    formatData = format_data
    parseString = parse_string
    validateRanges = validate_ranges
    hasDefaultValue = has_default_value
    getDefaultValue = get_default_value
    isBogusField = is_bogus_field
    isRequired = is_required
    isBroadcast = is_broadcast
    isRam = is_ram
    isDb = is_db
    isClsend = is_clsend
    isClrecv = is_clrecv
    isOwnsend = is_ownsend
    isOwnrecv = is_ownrecv
    isAirecv = is_airecv
    packArgs = pack_args
    unpackArgs = unpack_args
    receiveUpdate = receive_update
    clientFormatUpdate = client_format_update
    aiFormatUpdate = ai_format_update
    aiFormatUpdateMsgType = ai_format_update_msg_type

class DCPackData:
    """This is a block of data that receives the results of DCPacker."""

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: DCPackData = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear(self) -> None:
        """Empties the contents of the data (without necessarily freeing its allocated
        memory).
        """
    def get_string(self) -> str:
        """Returns the data buffer as a string.  Also see get_data()."""
    def get_length(self) -> int:
        """Returns the current length of the buffer.  This is the number of useful
        bytes stored in the buffer, not the amount of memory it takes up.
        """
    getString = get_string
    getLength = get_length

class DCPacker:
    """This class can be used for packing a series of numeric and string data into
    a binary stream, according to the DC specification.

    See also direct/src/doc/dcPacker.txt for a more complete description and
    examples of using this class.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: DCPacker = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear_data(self) -> None:
        """Empties the data in the pack buffer and unpack buffer.  This should be
        called between calls to begin_pack(), unless you want to concatenate all of
        the pack results together.
        """
    def begin_pack(self, root: DCPackerInterface) -> None:
        """Begins a packing session.  The parameter is the DC object that describes
        the packing format; it may be a DCParameter or DCField.

        Unless you call clear_data() between sessions, multiple packing sessions
        will be concatenated together into the same buffer.  If you wish to add
        bytes to the buffer between packing sessions, use append_data() or
        get_write_pointer().
        """
    def end_pack(self) -> bool:
        """Finishes a packing session.

        The return value is true on success, or false if there has been some error
        during packing.
        """
    def set_unpack_data(self, data: bytes) -> None:
        """Sets up the unpack_data pointer.  You may call this before calling the
        version of begin_unpack() that takes only one parameter.
        """
    def begin_unpack(self, root: DCPackerInterface) -> None:
        """Begins an unpacking session.  You must have previously called
        set_unpack_data() to specify a buffer to unpack.

        If there was data left in the buffer after a previous begin_unpack() ..
        end_unpack() session, the new session will resume from the current point.
        This method may be used, therefore, to unpack a sequence of objects from
        the same buffer.
        """
    def end_unpack(self) -> bool:
        """Finishes the unpacking session.

        The return value is true on success, or false if there has been some error
        during unpacking (or if all fields have not been unpacked).
        """
    def begin_repack(self, root: DCPackerInterface) -> None:
        """Begins a repacking session.  You must have previously called
        set_unpack_data() to specify a buffer to unpack.

        Unlike begin_pack() or begin_unpack() you may not concatenate the results
        of multiple begin_repack() sessions in one buffer.

        Also, unlike in packing or unpacking modes, you may not walk through the
        fields from beginning to end, or even pack two consecutive fields at once.
        Instead, you must call seek() for each field you wish to modify and pack
        only that one field; then call seek() again to modify another field.
        """
    def end_repack(self) -> bool:
        """Finishes the repacking session.

        The return value is true on success, or false if there has been some error
        during repacking (or if all fields have not been repacked).
        """
    @overload
    def seek(self, seek_index: int) -> bool:
        """`(self, seek_index: int)`:
        Seeks to the field indentified by seek_index, which was returned by an
        earlier call to DCField::find_seek_index() to get the index of some nested
        field.  Also see the version of seek() that accepts a field name.

        Returns true if successful, false if the field is not known (or if the
        packer is in an invalid mode).

        `(self, field_name: str)`:
        Sets the current unpack (or repack) position to the named field.  In unpack
        mode, the next call to unpack_*() or push() will begin to read the named
        field.  In repack mode, the next call to pack_*() or push() will modify the
        named field.

        Returns true if successful, false if the field is not known (or if the
        packer is in an invalid mode).
        """
    @overload
    def seek(self, field_name: str) -> bool: ...
    def has_nested_fields(self) -> bool:
        """Returns true if the current field has any nested fields (and thus expects a
        push() .. pop() interface), or false otherwise.  If this returns true,
        get_num_nested_fields() may be called to determine how many nested fields
        are expected.
        """
    def get_num_nested_fields(self) -> int:
        """Returns the number of nested fields associated with the current field, if
        has_nested_fields() returned true.

        The return value may be -1 to indicate that a variable number of nested
        fields are accepted by this field type (e.g.  a variable-length array).

        Note that this method is unreliable to determine how many fields you must
        traverse before you can call pop(), since particularly in the presence of a
        DCSwitch, it may change during traversal.  Use more_nested_fields()
        instead.
        """
    def more_nested_fields(self) -> bool:
        """Returns true if there are more nested fields to pack or unpack in the
        current push sequence, false if it is time to call pop().
        """
    def get_current_parent(self) -> DCPackerInterface:
        """Returns the field that we left in our last call to push(): the owner of the
        current level of fields.  This may be NULL at the beginning of the pack
        operation.
        """
    def get_current_field(self) -> DCPackerInterface:
        """Returns the field that will be referenced by the next call to pack_*() or
        unpack_*().  This will be NULL if we have unpacked (or packed) all fields,
        or if it is time to call pop().
        """
    def get_last_switch(self) -> DCSwitchParameter:
        """Returns a pointer to the last DCSwitch instance that we have passed by and
        selected one case of during the pack/unpack process.  Each time we
        encounter a new DCSwitch and select a case, this will change state.

        This may be used to detect when a DCSwitch has been selected.  At the
        moment this changes state, get_current_parent() will contain the particular
        SwitchCase that was selected by the switch.
        """
    def get_pack_type(self) -> _DCPackType:
        """Returns the type of value expected by the current field.  See the
        enumerated type definition at the top of DCPackerInterface.h.  If this
        returns one of PT_double, PT_int, PT_int64, or PT_string, then you should
        call the corresponding pack_double(), pack_int() function (or
        unpack_double(), unpack_int(), etc.) to transfer data.  Otherwise, you
        should call push() and begin packing or unpacking the nested fields.
        """
    def get_current_field_name(self) -> str:
        """Returns the name of the current field, if it has a name, or the empty
        string if the field does not have a name or there is no current field.
        """
    def push(self) -> None:
        """Marks the beginning of a nested series of fields.

        This must be called before filling the elements of an array or the
        individual fields in a structure field.  It must also be balanced by a
        matching pop().

        It is necessary to use push() / pop() only if has_nested_fields() returns
        true.
        """
    def pop(self) -> None:
        """Marks the end of a nested series of fields.

        This must be called to match a previous push() only after all the expected
        number of nested fields have been packed.  It is an error to call it too
        early, or too late.
        """
    def pack_double(self, value: float) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_int(self, value: int) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_uint(self, value: int) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_int64(self, value: int) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_uint64(self, value: int) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_string(self, value: str) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_blob(self, value: bytes) -> None:
        """Packs the indicated numeric or string value into the stream."""
    def pack_literal_value(self, value: bytes) -> None:
        """Adds the indicated string value into the stream, representing a single pre-
        packed field element, or a whole group of field elements at once.
        """
    def pack_default_value(self) -> None:
        """Adds the default value for the current element into the stream.  If no
        default has been set for the current element, creates a sensible default.
        """
    def unpack_double(self) -> float:
        """Unpacks the current numeric or string value from the stream."""
    def unpack_int(self) -> int:
        """Unpacks the current numeric or string value from the stream."""
    def unpack_uint(self) -> int:
        """Unpacks the current numeric or string value from the stream."""
    def unpack_int64(self) -> int:
        """Unpacks the current numeric or string value from the stream."""
    def unpack_uint64(self) -> int:
        """Unpacks the current numeric or string value from the stream."""
    def unpack_string(self) -> str:
        """Unpacks the current numeric or string value from the stream."""
    def unpack_blob(self) -> bytes:
        """Unpacks the current binary data value from the stream."""
    def unpack_literal_value(self) -> bytes:
        """Returns the literal string that represents the packed value of the current
        field, and advances the field pointer.
        """
    def unpack_validate(self) -> None:
        """Internally unpacks the current numeric or string value and validates it
        against the type range limits, but does not return the value.  If the
        current field contains nested fields, validates all of them.
        """
    def unpack_skip(self) -> None:
        """Skips the current field without unpacking it and advances to the next
        field.  If the current field contains nested fields, skips all of them.
        """
    def pack_object(self, object) -> None:
        """Packs the Python object of whatever type into the packer.  Each numeric
        object and string object maps to the corresponding pack_value() call; a
        tuple or sequence maps to a push() followed by all of the tuple's contents
        followed by a pop().
        """
    def unpack_object(self):
        """Unpacks a Python object of the appropriate type from the stream for the
        current field.  This may be an integer or a string for a simple field
        object; if the current field represents a list of fields it will be a
        tuple.
        """
    @overload
    def parse_and_pack(self, _in: istream) -> bool:
        """Parses an object's value according to the DC file syntax (e.g.  as a
        default value string) and packs it.  Returns true on success, false on a
        parse error.
        """
    @overload
    def parse_and_pack(self, formatted_object: str) -> bool: ...
    @overload
    def unpack_and_format(self, show_field_names: bool = ...) -> str:
        """Unpacks an object and formats its value into a syntax suitable for parsing
        in the dc file (e.g.  as a default value), or as an input to parse_object.
        """
    @overload
    def unpack_and_format(self, out: ostream, show_field_names: bool = ...) -> None: ...
    def had_parse_error(self) -> bool:
        """Returns true if there has been an parse error since the most recent call to
        begin(); this can only happen if you call parse_and_pack().
        """
    def had_pack_error(self) -> bool:
        """Returns true if there has been an packing error since the most recent call
        to begin(); in particular, this may be called after end() has returned
        false to determine the nature of the failure.

        A return value of true indicates there was a push/pop mismatch, or the
        push/pop structure did not match the data structure, or there were the
        wrong number of elements in a nested push/pop structure, or on unpack that
        the data stream was truncated.
        """
    def had_range_error(self) -> bool:
        """Returns true if there has been an range validation error since the most
        recent call to begin(); in particular, this may be called after end() has
        returned false to determine the nature of the failure.

        A return value of true indicates a value that was packed or unpacked did
        not fit within the specified legal range for a parameter, or within the
        limits of the field size.
        """
    def had_error(self) -> bool:
        """Returns true if there has been any error (either a pack error or a range
        error) since the most recent call to begin().  If this returns true, then
        the matching call to end() will indicate an error (false).
        """
    def get_num_unpacked_bytes(self) -> int:
        """Returns the number of bytes that have been unpacked so far, or after
        unpack_end(), the total number of bytes that were unpacked at all.  This
        can be used to validate that all of the bytes in the buffer were actually
        unpacked (which is not otherwise considered an error).
        """
    def get_length(self) -> int:
        """Returns the current length of the buffer.  This is the number of useful
        bytes stored in the buffer, not the amount of memory it takes up.
        """
    def get_string(self) -> str:
        """Returns the packed data buffer as a string.  Also see get_data()."""
    def get_bytes(self) -> bytes:
        """Returns the packed data buffer as a bytes object.  Also see get_data()."""
    def get_unpack_length(self) -> int:
        """Returns the total number of bytes in the unpack data buffer.  This is the
        buffer used when unpacking; it is separate from the pack data returned by
        get_length(), which is filled during packing.
        """
    def get_unpack_string(self) -> str:
        """Returns the unpack data buffer, as a string.  This is the buffer used when
        unpacking; it is separate from the pack data returned by get_string(),
        which is filled during packing.  Also see get_unpack_data().
        """
    @staticmethod
    def get_num_stack_elements_ever_allocated() -> int:
        """Returns the number of DCPacker::StackElement pointers ever simultaneously
        allocated; these are now either in active use or have been recycled into
        the deleted DCPacker::StackElement pool to be used again.
        """
    def raw_pack_int8(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_int16(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_int32(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_int64(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_uint8(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_uint16(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_uint32(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_uint64(self, value: int) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_float64(self, value: float) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_string(self, value: str) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_pack_blob(self, value: bytes) -> None:
        """Packs the data into the buffer between packing sessions."""
    def raw_unpack_int8(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_int16(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_int32(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_int64(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_uint8(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_uint16(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_uint32(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_uint64(self) -> int:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_float64(self) -> float:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_string(self) -> str:
        """Unpacks the data from the buffer between unpacking sessions."""
    def raw_unpack_blob(self) -> bytes:
        """Unpacks the data from the buffer between unpacking sessions."""
    clearData = clear_data
    beginPack = begin_pack
    endPack = end_pack
    setUnpackData = set_unpack_data
    beginUnpack = begin_unpack
    endUnpack = end_unpack
    beginRepack = begin_repack
    endRepack = end_repack
    hasNestedFields = has_nested_fields
    getNumNestedFields = get_num_nested_fields
    moreNestedFields = more_nested_fields
    getCurrentParent = get_current_parent
    getCurrentField = get_current_field
    getLastSwitch = get_last_switch
    getPackType = get_pack_type
    getCurrentFieldName = get_current_field_name
    packDouble = pack_double
    packInt = pack_int
    packUint = pack_uint
    packInt64 = pack_int64
    packUint64 = pack_uint64
    packString = pack_string
    packBlob = pack_blob
    packLiteralValue = pack_literal_value
    packDefaultValue = pack_default_value
    unpackDouble = unpack_double
    unpackInt = unpack_int
    unpackUint = unpack_uint
    unpackInt64 = unpack_int64
    unpackUint64 = unpack_uint64
    unpackString = unpack_string
    unpackBlob = unpack_blob
    unpackLiteralValue = unpack_literal_value
    unpackValidate = unpack_validate
    unpackSkip = unpack_skip
    packObject = pack_object
    unpackObject = unpack_object
    parseAndPack = parse_and_pack
    unpackAndFormat = unpack_and_format
    hadParseError = had_parse_error
    hadPackError = had_pack_error
    hadRangeError = had_range_error
    hadError = had_error
    getNumUnpackedBytes = get_num_unpacked_bytes
    getLength = get_length
    getString = get_string
    getBytes = get_bytes
    getUnpackLength = get_unpack_length
    getUnpackString = get_unpack_string
    getNumStackElementsEverAllocated = get_num_stack_elements_ever_allocated
    rawPackInt8 = raw_pack_int8
    rawPackInt16 = raw_pack_int16
    rawPackInt32 = raw_pack_int32
    rawPackInt64 = raw_pack_int64
    rawPackUint8 = raw_pack_uint8
    rawPackUint16 = raw_pack_uint16
    rawPackUint32 = raw_pack_uint32
    rawPackUint64 = raw_pack_uint64
    rawPackFloat64 = raw_pack_float64
    rawPackString = raw_pack_string
    rawPackBlob = raw_pack_blob
    rawUnpackInt8 = raw_unpack_int8
    rawUnpackInt16 = raw_unpack_int16
    rawUnpackInt32 = raw_unpack_int32
    rawUnpackInt64 = raw_unpack_int64
    rawUnpackUint8 = raw_unpack_uint8
    rawUnpackUint16 = raw_unpack_uint16
    rawUnpackUint32 = raw_unpack_uint32
    rawUnpackUint64 = raw_unpack_uint64
    rawUnpackFloat64 = raw_unpack_float64
    rawUnpackString = raw_unpack_string
    rawUnpackBlob = raw_unpack_blob

class DCParameter(DCField):
    """Represents the type specification for a single parameter within a field
    specification.  This may be a simple type, or it may be a class or an array
    reference.

    This may also be a typedef reference to another type, which has the same
    properties as the referenced type, but a different name.
    """

    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def as_simple_parameter(self) -> DCSimpleParameter: ...
    def as_array_parameter(self) -> DCArrayParameter: ...
    def make_copy(self) -> DCParameter: ...
    def is_valid(self) -> bool: ...
    def get_typedef(self) -> DCTypedef:
        """If this type has been referenced from a typedef, returns the DCTypedef
        instance, or NULL if the type was declared on-the-fly.
        """
    asSimpleParameter = as_simple_parameter
    asArrayParameter = as_array_parameter
    makeCopy = make_copy
    isValid = is_valid
    getTypedef = get_typedef

class DCArrayParameter(DCParameter):
    """This represents an array of some other kind of object, meaning this
    parameter type accepts an arbitrary (or possibly fixed) number of nested
    fields, all of which are of the same type.
    """

    def get_element_type(self) -> DCParameter:
        """Returns the type of the individual elements of this array."""
    def get_array_size(self) -> int:
        """Returns the fixed number of elements in this array, or -1 if the array may
        contain a variable number of elements.
        """
    getElementType = get_element_type
    getArraySize = get_array_size

class DCAtomicField(DCField):
    """A single atomic field of a Distributed Class, as read from a .dc file.
    This defines an interface to the Distributed Class, and is always
    implemented as a remote procedure method.
    """

    def get_num_elements(self) -> int:
        """Returns the number of elements (parameters) of the atomic field."""
    def get_element(self, n: int) -> DCParameter:
        """Returns the parameter object describing the nth element."""
    def get_element_default(self, n: int) -> bytes:
        """Returns the pre-formatted default value associated with the nth element of
        the field.  This is only valid if has_element_default() returns true, in
        which case this string represents the bytes that should be assigned to the
        field as a default value.

        If the element is an array-type element, the returned value will include
        the two-byte length preceding the array data.

        @deprecated use get_element() instead.
        """
    def has_element_default(self, n: int) -> bool:
        """Returns true if the nth element of the field has a default value specified,
        false otherwise.

        @deprecated use get_element() instead.
        """
    def get_element_name(self, n: int) -> str:
        """Returns the name of the nth element of the field.  This name is strictly
        for documentary purposes; it does not generally affect operation.  If a
        name is not specified, this will be the empty string.

        @deprecated use get_element()->get_name() instead.
        """
    def get_element_type(self, n: int) -> _DCSubatomicType:
        """Returns the numeric type of the nth element of the field.  This method is
        deprecated; use get_element() instead.
        """
    def get_element_divisor(self, n: int) -> int:
        """Returns the divisor associated with the nth element of the field.  This
        implements an implicit fixed-point system; floating-point values are to be
        multiplied by this value before encoding into a packet, and divided by this
        number after decoding.

        This method is deprecated; use get_element()->get_divisor() instead.
        """
    getNumElements = get_num_elements
    getElement = get_element
    getElementDefault = get_element_default
    hasElementDefault = has_element_default
    getElementName = get_element_name
    getElementType = get_element_type
    getElementDivisor = get_element_divisor

class DCDeclaration:
    """This is a common interface for a declaration in a DC file.  Currently, this
    is either a class or a typedef declaration (import declarations are still
    collected together at the top, and don't inherit from this object).  Its
    only purpose is so that classes and typedefs can be stored in one list
    together so they can be ordered correctly on output.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def as_class(self) -> DCClass: ...
    def as_switch(self) -> DCSwitch: ...
    def output(self, out: ostream) -> None:
        """Write a string representation of this instance to <out>."""
    def write(self, out: ostream, indent_level: int) -> None:
        """Write a string representation of this instance to <out>."""
    asClass = as_class
    asSwitch = as_switch

class DCClass(DCDeclaration):
    """Defines a particular DistributedClass as read from an input .dc file."""

    def get_dc_file(self) -> DCFile:
        """Returns the DCFile object that contains the class."""
    def get_name(self) -> str:
        """Returns the name of this class."""
    def get_number(self) -> int:
        """Returns a unique index number associated with this class.  This is defined
        implicitly when the .dc file(s) are read.
        """
    def get_num_parents(self) -> int:
        """Returns the number of base classes this class inherits from."""
    def get_parent(self, n: int) -> DCClass:
        """Returns the nth parent class this class inherits from."""
    def has_constructor(self) -> bool:
        """Returns true if this class has a constructor method, false if it just uses
        the default constructor.
        """
    def get_constructor(self) -> DCField:
        """Returns the constructor method for this class if it is defined, or NULL if
        the class uses the default constructor.
        """
    def get_num_fields(self) -> int:
        """Returns the number of fields defined directly in this class, ignoring
        inheritance.
        """
    def get_field(self, n: int) -> DCField:
        """Returns the nth field in the class.  This is not necessarily the field with
        index n; this is the nth field defined in the class directly, ignoring
        inheritance.
        """
    def get_field_by_name(self, name: str) -> DCField:
        """Returns a pointer to the DCField that shares the indicated name.  If the
        named field is not found in the current class, the parent classes will be
        searched, so the value returned may not actually be a field within this
        class.  Returns NULL if there is no such field defined.
        """
    def get_field_by_index(self, index_number: int) -> DCField:
        """Returns a pointer to the DCField that has the indicated index number.  If
        the numbered field is not found in the current class, the parent classes
        will be searched, so the value returned may not actually be a field within
        this class.  Returns NULL if there is no such field defined.
        """
    def get_num_inherited_fields(self) -> int:
        """Returns the total number of field fields defined in this class and all
        ancestor classes.
        """
    def get_inherited_field(self, n: int) -> DCField:
        """Returns the nth field field in the class and all of its ancestors.

        This *used* to be the same thing as get_field_by_index(), back when the
        fields were numbered sequentially within a class's inheritance hierarchy.
        Now that fields have a globally unique index number, this is no longer
        true.
        """
    def is_struct(self) -> bool:
        """Returns true if the class has been identified with the "struct" keyword in
        the dc file, false if it was declared with "dclass".
        """
    def is_bogus_class(self) -> bool:
        """Returns true if the class has been flagged as a bogus class.  This is set
        for classes that are generated by the parser as placeholder for missing
        classes, as when reading a partial file; it should not occur in a normal
        valid dc file.
        """
    def inherits_from_bogus_class(self) -> bool:
        """Returns true if this class, or any class in the inheritance heirarchy for
        this class, is a "bogus" class--a forward reference to an as-yet-undefined
        class.
        """
    def start_generate(self) -> None:
        """Starts the PStats timer going on the "generate" task, that is, marks the
        beginning of the process of generating a new object, for the purposes of
        timing this process.

        This should balance with a corresponding call to stop_generate().
        """
    def stop_generate(self) -> None:
        """Stops the PStats timer on the "generate" task.  This should balance with a
        preceding call to start_generate().
        """
    def has_class_def(self) -> bool:
        """Returns true if the DCClass object has an associated Python class
        definition, false otherwise.
        """
    def set_class_def(self, class_def) -> None:
        """Sets the class object associated with this DistributedClass.  This object
        will be used to construct new instances of the class.
        """
    def get_class_def(self):
        """Returns the class object that was previously associated with this
        DistributedClass.  This will return a new reference to the object.
        """
    def has_owner_class_def(self) -> bool:
        """Returns true if the DCClass object has an associated Python owner class
        definition, false otherwise.
        """
    def set_owner_class_def(self, owner_class_def) -> None:
        """Sets the owner class object associated with this DistributedClass.  This
        object will be used to construct new owner instances of the class.
        """
    def get_owner_class_def(self):
        """Returns the owner class object that was previously associated with this
        DistributedClass.  This will return a new reference to the object.
        """
    def receive_update(self, distobj, di: Datagram | DatagramIterator) -> None:
        """Extracts the update message out of the packer and applies it to the
        indicated object by calling the appropriate method.
        """
    def receive_update_broadcast_required(self, distobj, di: Datagram | DatagramIterator) -> None:
        """Processes a big datagram that includes all of the "required" fields that
        are sent along with a normal "generate with required" message.  This is all
        of the atomic fields that are marked "broadcast required".
        """
    def receive_update_broadcast_required_owner(self, distobj, di: Datagram | DatagramIterator) -> None:
        """Processes a big datagram that includes all of the "required" fields that
        are sent along with a normal "generate with required" message.  This is all
        of the atomic fields that are marked "broadcast ownrecv". Should be used
        for 'owner-view' objects.
        """
    def receive_update_all_required(self, distobj, di: Datagram | DatagramIterator) -> None:
        """Processes a big datagram that includes all of the "required" fields that
        are sent when an avatar is created.  This is all of the atomic fields that
        are marked "required", whether they are broadcast or not.
        """
    def receive_update_other(self, distobj, di: Datagram | DatagramIterator) -> None:
        """Processes a datagram that lists some additional fields that are broadcast
        in one chunk.
        """
    @overload
    def direct_update(self, distobj, field_name: str, datagram: Datagram) -> None:
        """`(self, distobj, field_name: str, datagram: Datagram)`:
        Processes an update for a named field from a packed datagram.

        `(self, distobj, field_name: str, value_blob: bytes)`:
        Processes an update for a named field from a packed value blob.
        """
    @overload
    def direct_update(self, distobj, field_name: str, value_blob: bytes) -> None: ...
    @overload
    def pack_required_field(self, packer: DCPacker, distobj, field: DCField) -> bool:
        """`(self, packer: DCPacker, distobj, field: DCField)`:
        Looks up the current value of the indicated field by calling the
        appropriate get*() function, then packs that value into the packer.  This
        field is presumably either a required field or a specified optional field,
        and we are building up a datagram for the generate-with-required message.

        Returns true on success, false on failure.

        `(self, datagram: Datagram, distobj, field: DCField)`:
        Looks up the current value of the indicated field by calling the
        appropriate get*() function, then packs that value into the datagram.  This
        field is presumably either a required field or a specified optional field,
        and we are building up a datagram for the generate-with-required message.

        Returns true on success, false on failure.
        """
    @overload
    def pack_required_field(self, datagram: Datagram, distobj, field: DCField) -> bool: ...
    def client_format_update(self, field_name: str, do_id: int, args) -> Datagram:
        """Generates a datagram containing the message necessary to send an update for
        the indicated distributed object from the client.
        """
    def ai_format_update(self, field_name: str, do_id: int, to_id: int, from_id: int, args) -> Datagram:
        """Generates a datagram containing the message necessary to send an update for
        the indicated distributed object from the AI.
        """
    def ai_format_update_msg_type(self, field_name: str, do_id: int, to_id: int, from_id: int, msg_type: int, args) -> Datagram:
        """Generates a datagram containing the message necessary to send an update,
        using the indicated msg type for the indicated distributed object from the
        AI.
        """
    def ai_format_generate(
        self, distobj, do_id: int, parent_id: int, zone_id: int, district_channel_id: int, from_channel_id: int, optional_fields
    ) -> Datagram: ...
    def client_format_generate_CMU(self, distobj, do_id: int, zone_id: int, optional_fields: Sequence[str] | None) -> Datagram:
        """Generates a datagram containing the message necessary to generate a new
        distributed object from the client.  This requires querying the object for
        the initial value of its required fields.

        optional_fields is a list of fieldNames to generate in addition to the
        normal required fields.

        This method is only called by the CMU implementation.
        """
    getDcFile = get_dc_file
    getName = get_name
    getNumber = get_number
    getNumParents = get_num_parents
    getParent = get_parent
    hasConstructor = has_constructor
    getConstructor = get_constructor
    getNumFields = get_num_fields
    getField = get_field
    getFieldByName = get_field_by_name
    getFieldByIndex = get_field_by_index
    getNumInheritedFields = get_num_inherited_fields
    getInheritedField = get_inherited_field
    isStruct = is_struct
    isBogusClass = is_bogus_class
    inheritsFromBogusClass = inherits_from_bogus_class
    startGenerate = start_generate
    stopGenerate = stop_generate
    hasClassDef = has_class_def
    setClassDef = set_class_def
    getClassDef = get_class_def
    hasOwnerClassDef = has_owner_class_def
    setOwnerClassDef = set_owner_class_def
    getOwnerClassDef = get_owner_class_def
    receiveUpdate = receive_update
    receiveUpdateBroadcastRequired = receive_update_broadcast_required
    receiveUpdateBroadcastRequiredOwner = receive_update_broadcast_required_owner
    receiveUpdateAllRequired = receive_update_all_required
    receiveUpdateOther = receive_update_other
    directUpdate = direct_update
    packRequiredField = pack_required_field
    clientFormatUpdate = client_format_update
    aiFormatUpdate = ai_format_update
    aiFormatUpdateMsgType = ai_format_update_msg_type
    aiFormatGenerate = ai_format_generate
    clientFormatGenerateCMU = client_format_generate_CMU

class DCClassParameter(DCParameter):
    """This represents a class (or struct) object used as a parameter itself.
    This means that all the fields of the class get packed into the message.
    """

    def get_class(self) -> DCClass:
        """Returns the class object this parameter represents."""
    getClass = get_class

class DCFile:
    """Represents the complete list of Distributed Class descriptions as read from
    a .dc file.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: DCFile = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def clear(self) -> None:
        """Removes all of the classes defined within the DCFile and prepares it for
        reading a new file.
        """
    def read_all(self) -> bool:
        """This special method reads all of the .dc files named by the "dc-file"
        config.prc variable, and loads them into the DCFile namespace.
        """
    @overload
    def read(self, filename: StrOrBytesPath) -> bool:
        """`(self, filename: Filename)`:
        Opens and reads the indicated .dc file by name.  The distributed classes
        defined in the file will be appended to the set of distributed classes
        already recorded, if any.

        Returns true if the file is successfully read, false if there was an error
        (in which case the file might have been partially read).

        `(self, _in: istream, filename: str = ...)`:
        Parses the already-opened input stream for distributed class descriptions.
        The filename parameter is optional and is only used when reporting errors.

        The distributed classes defined in the file will be appended to the set of
        distributed classes already recorded, if any.

        Returns true if the file is successfully read, false if there was an error
        (in which case the file might have been partially read).
        """
    @overload
    def read(self, _in: istream, filename: str = ...) -> bool: ...
    @overload
    def write(self, filename: StrOrBytesPath, brief: bool) -> bool:
        """`(self, filename: Filename, brief: bool)`:
        Opens the indicated filename for output and writes a parseable description
        of all the known distributed classes to the file.

        Returns true if the description is successfully written, false otherwise.

        `(self, out: ostream, brief: bool)`:
        Writes a parseable description of all the known distributed classes to the
        stream.

        Returns true if the description is successfully written, false otherwise.
        """
    @overload
    def write(self, out: ostream, brief: bool) -> bool: ...
    def get_num_classes(self) -> int:
        """Returns the number of classes read from the .dc file(s)."""
    def get_class(self, n: int) -> DCClass:
        """Returns the nth class read from the .dc file(s)."""
    def get_class_by_name(self, name: str) -> DCClass:
        """Returns the class that has the indicated name, or NULL if there is no such
        class.
        """
    def get_switch_by_name(self, name: str) -> DCSwitch:
        """Returns the switch that has the indicated name, or NULL if there is no such
        switch.
        """
    def get_field_by_index(self, index_number: int) -> DCField:
        """Returns a pointer to the one DCField that has the indicated index number,
        of all the DCFields across all classes in the file.

        This method is only valid if dc-multiple-inheritance is set true in the
        Config.prc file.  Without this setting, different DCFields may share the
        same index number, so this global lookup is not possible.
        """
    def all_objects_valid(self) -> bool:
        """Returns true if all of the classes read from the DC file were defined and
        valid, or false if any of them were undefined ("bogus classes").  If this
        is true, we might have read a partial file.
        """
    def get_num_import_modules(self) -> int:
        """Returns the number of import lines read from the .dc file(s)."""
    def get_import_module(self, n: int) -> str:
        """Returns the module named by the nth import line read from the .dc file(s)."""
    def get_num_import_symbols(self, n: int) -> int:
        """Returns the number of symbols explicitly imported by the nth import line.
        If this is 0, the line is "import modulename"; if it is more than 0, the
        line is "from modulename import symbol, symbol ... ".
        """
    def get_import_symbol(self, n: int, i: int) -> str:
        """Returns the ith symbol named by the nth import line read from the .dc
        file(s).
        """
    def get_num_typedefs(self) -> int:
        """Returns the number of typedefs read from the .dc file(s)."""
    def get_typedef(self, n: int) -> DCTypedef:
        """Returns the nth typedef read from the .dc file(s)."""
    def get_typedef_by_name(self, name: str) -> DCTypedef:
        """Returns the typedef that has the indicated name, or NULL if there is no
        such typedef name.
        """
    def get_num_keywords(self) -> int:
        """Returns the number of keywords read from the .dc file(s)."""
    def get_keyword(self, n: int) -> DCKeyword:
        """Returns the nth keyword read from the .dc file(s)."""
    def get_keyword_by_name(self, name: str) -> DCKeyword:
        """Returns the keyword that has the indicated name, or NULL if there is no
        such keyword name.
        """
    def get_hash(self) -> int:
        """Returns a 32-bit hash index associated with this file.  This number is
        guaranteed to be consistent if the contents of the file have not changed,
        and it is very likely to be different if the contents of the file do
        change.
        """
    readAll = read_all
    getNumClasses = get_num_classes
    getClass = get_class
    getClassByName = get_class_by_name
    getSwitchByName = get_switch_by_name
    getFieldByIndex = get_field_by_index
    allObjectsValid = all_objects_valid
    getNumImportModules = get_num_import_modules
    getImportModule = get_import_module
    getNumImportSymbols = get_num_import_symbols
    getImportSymbol = get_import_symbol
    getNumTypedefs = get_num_typedefs
    getTypedef = get_typedef
    getTypedefByName = get_typedef_by_name
    getNumKeywords = get_num_keywords
    getKeyword = get_keyword
    getKeywordByName = get_keyword_by_name
    getHash = get_hash

class DCKeyword(DCDeclaration):
    """This represents a single keyword declaration in the dc file.  It is used to
    define a communication property associated with a field, for instance
    "broadcast" or "airecv".
    """

    def get_name(self) -> str:
        """Returns the name of this keyword."""
    getName = get_name

class DCMolecularField(DCField):
    """A single molecular field of a Distributed Class, as read from a .dc file.
    This represents a combination of two or more related atomic fields, that
    will often be treated as a unit.
    """

    def get_num_atomics(self) -> int:
        """Returns the number of atomic fields that make up this molecular field."""
    def get_atomic(self, n: int) -> DCAtomicField:
        """Returns the nth atomic field that makes up this molecular field.  This may
        or may not be a field of this particular class; it might be defined in a
        parent class.
        """
    getNumAtomics = get_num_atomics
    getAtomic = get_atomic

class DCSimpleParameter(DCParameter):
    """This is the most fundamental kind of parameter type: a single number or
    string, one of the DCSubatomicType elements.  It may also optionally have a
    divisor, which is meaningful only for the numeric type elements (and
    represents a fixed-point numeric convention).
    """

    def get_type(self) -> _DCSubatomicType:
        """Returns the particular subatomic type represented by this instance."""
    def has_modulus(self) -> bool:
        """Returns true if there is a modulus associated, false otherwise.,"""
    def get_modulus(self) -> float:
        """Returns the modulus associated with this type, if any.  It is an error to
        call this if has_modulus() returned false.

        If present, this is the modulus that is used to constrain the numeric value
        of the field before it is packed (and range-checked).
        """
    def get_divisor(self) -> int:
        """Returns the divisor associated with this type.  This is 1 by default, but
        if this is other than one it represents the scale to apply when packing and
        unpacking numeric values (to store fixed-point values in an integer field).
        It is only meaningful for numeric-type fields.
        """
    getType = get_type
    hasModulus = has_modulus
    getModulus = get_modulus
    getDivisor = get_divisor

class DCSwitch(DCDeclaration):
    """This represents a switch statement, which can appear inside a class body
    and represents two or more alternative unpacking schemes based on the first
    field read.
    """

    def get_name(self) -> str:
        """Returns the name of this switch."""
    def get_key_parameter(self) -> DCField:
        """Returns the key parameter on which the switch is based.  The value of this
        parameter in the record determines which one of the several cases within
        the switch will be used.
        """
    def get_num_cases(self) -> int:
        """Returns the number of different cases within the switch.  The legal values
        for case_index range from 0 to get_num_cases() - 1.
        """
    def get_case_by_value(self, case_value: bytes) -> int:
        """Returns the index number of the case with the indicated packed value, or -1
        if no case has this value.
        """
    def get_case(self, n: int) -> DCPackerInterface:
        """Returns the DCPackerInterface that packs the nth case."""
    def get_default_case(self) -> DCPackerInterface:
        """Returns the DCPackerInterface that packs the default case, or NULL if there
        is no default case.
        """
    def get_value(self, case_index: int) -> bytes:
        """Returns the packed value associated with the indicated case."""
    def get_num_fields(self, case_index: int) -> int:
        """Returns the number of fields in the indicated case."""
    def get_field(self, case_index: int, n: int) -> DCField:
        """Returns the nth field in the indicated case."""
    def get_field_by_name(self, case_index: int, name: str) -> DCField:
        """Returns the field with the given name from the indicated case, or NULL if
        no field has this name.
        """
    getName = get_name
    getKeyParameter = get_key_parameter
    getNumCases = get_num_cases
    getCaseByValue = get_case_by_value
    getCase = get_case
    getDefaultCase = get_default_case
    getValue = get_value
    getNumFields = get_num_fields
    getField = get_field
    getFieldByName = get_field_by_name

class DCSwitchParameter(DCParameter):
    """This represents a switch object used as a parameter itself, which packs the
    appropriate fields of the switch into the message.
    """

    def get_switch(self) -> DCSwitch:
        """Returns the switch object this parameter represents."""
    getSwitch = get_switch

class DCTypedef(DCDeclaration):
    """This represents a single typedef declaration in the dc file.  It assigns a
    particular type to a new name, just like a C typedef.
    """

    def get_number(self) -> int:
        """Returns a unique index number associated with this typedef definition.
        This is defined implicitly when the .dc file(s) are read.
        """
    def get_name(self) -> str:
        """Returns the name of this typedef."""
    def get_description(self) -> str:
        """Returns a brief decription of the typedef, useful for human consumption."""
    def is_bogus_typedef(self) -> bool:
        """Returns true if the typedef has been flagged as a bogus typedef.  This is
        set for typedefs that are generated by the parser as placeholder for
        missing typedefs, as when reading a partial file; it should not occur in a
        normal valid dc file.
        """
    def is_implicit_typedef(self) -> bool:
        """Returns true if the typedef has been flagged as an implicit typedef,
        meaning it was created for a DCClass that was referenced inline as a type.
        """
    getNumber = get_number
    getName = get_name
    getDescription = get_description
    isBogusTypedef = is_bogus_typedef
    isImplicitTypedef = is_implicit_typedef

ST_int8: Final = 0
STInt8: Final = 0
ST_int16: Final = 1
STInt16: Final = 1
ST_int32: Final = 2
STInt32: Final = 2
ST_int64: Final = 3
STInt64: Final = 3
ST_uint8: Final = 4
STUint8: Final = 4
ST_uint16: Final = 5
STUint16: Final = 5
ST_uint32: Final = 6
STUint32: Final = 6
ST_uint64: Final = 7
STUint64: Final = 7
ST_float64: Final = 8
STFloat64: Final = 8
ST_string: Final = 9
STString: Final = 9
ST_blob: Final = 10
STBlob: Final = 10
ST_blob32: Final = 11
STBlob32: Final = 11
ST_int16array: Final = 12
STInt16array: Final = 12
ST_int32array: Final = 13
STInt32array: Final = 13
ST_uint16array: Final = 14
STUint16array: Final = 14
ST_uint32array: Final = 15
STUint32array: Final = 15
ST_int8array: Final = 16
STInt8array: Final = 16
ST_uint8array: Final = 17
STUint8array: Final = 17
ST_uint32uint8array: Final = 18
STUint32uint8array: Final = 18
ST_char: Final = 19
STChar: Final = 19
ST_invalid: Final = 20
STInvalid: Final = 20
PT_invalid: Final = 0
PTInvalid: Final = 0
PT_double: Final = 1
PTDouble: Final = 1
PT_int: Final = 2
PTInt: Final = 2
PT_uint: Final = 3
PTUint: Final = 3
PT_int64: Final = 4
PTInt64: Final = 4
PT_uint64: Final = 5
PTUint64: Final = 5
PT_string: Final = 6
PTString: Final = 6
PT_blob: Final = 7
PTBlob: Final = 7
PT_array: Final = 8
PTArray: Final = 8
PT_field: Final = 9
PTField: Final = 9
PT_class: Final = 10
PTClass: Final = 10
PT_switch: Final = 11
PTSwitch: Final = 11
