from typing import Any, ClassVar
from typing_extensions import Self

from panda3d.core._dtoolbase import TypedObject

class BasicSkel:
    """This is the most basic of the skeleton classes.  It stores an integer, and
    will return it on request.

    The skeleton classes are intended to help you learn how to add C++ classes
    to panda.  See also the manual, "Adding C++ Classes to Panda."
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, __param0: BasicSkel = ...) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def set_value(self, n: int) -> None:
        """These inline functions allow you to get and set _value."""
    def get_value(self) -> int:
        """Retreives a value that was previously stored."""
    def set_value_alt(self, n: int) -> None:
        """Stores an integer value.  Exact same functionality as set_value, except
        that this isn't an inline function.
        """
    def get_value_alt(self) -> int:
        """Retreives a value that was previously stored.  Exact same functionality as
        get_value, except that this isn't an inline function.
        """
    setValue = set_value
    getValue = get_value
    setValueAlt = set_value_alt
    getValueAlt = get_value_alt

class TypedSkel(TypedObject):
    """Skeleton object that inherits from TypedObject.  Stores an integer, and
    will return it on request.

    The skeleton classes are intended to help you learn how to add C++ classes
    to panda.  See also the manual, "Adding C++ Classes to Panda."
    """

    def __init__(self) -> None: ...
    def set_value(self, n: int) -> None:
        """These inline functions allow you to get and set _value."""
    def get_value(self) -> int:
        """Retreives a value that was previously stored."""
    def set_value_alt(self, n: int) -> None:
        """Stores an integer value.  Exact same functionality as set_value, except
        that this isn't an inline function.
        """
    def get_value_alt(self) -> int:
        """Retreives a value that was previously stored.  Exact same functionality as
        get_value, except that this isn't an inline function.
        """
    setValue = set_value
    getValue = get_value
    setValueAlt = set_value_alt
    getValueAlt = get_value_alt
