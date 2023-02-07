import builtins
from collections.abc import Sequence
from typing import Any, ClassVar
from typing_extensions import Final, Literal, Self, TypeAlias, final

from panda3d.core._dtoolutil import ostream

_TypeHandle_MemoryClass: TypeAlias = Literal[0, 1, 2, 3, 4]

class NeverFreeMemory:
    """This class is used to allocate bytes of memory from a pool that is never
    intended to be freed.  It is particularly useful to support DeletedChain,
    which allocates memory in just such a fashion.

    When it is known that memory will not be freed, it is preferable to use
    this instead of the standard malloc() (or global_operator_new()) call,
    since this will help reduce fragmentation problems in the dynamic heap.
    Also, memory allocated from here will exhibit less wasted space.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @staticmethod
    def get_total_alloc() -> int:
        """Returns the total number of bytes consumed by all the pages allocated
        internally by this object.
        """
    @staticmethod
    def get_total_used() -> int:
        """Returns the total number of bytes requested by the application in calls to
        NeverFreeMemory::alloc().
        """
    @staticmethod
    def get_total_unused() -> int:
        """Returns the difference between get_total_alloc() and get_total_used().
        This represents bytes in allocated pages that have not (yet) been used by
        the application.
        """
    getTotalAlloc = get_total_alloc
    getTotalUsed = get_total_used
    getTotalUnused = get_total_unused

@final
class TypeHandle:
    """TypeHandle is the identifier used to differentiate C++ class types.  Any
    C++ classes that inherit from some base class, and must be differentiated
    at run time, should store a static TypeHandle object that can be queried
    through a static member function named get_class_type().  Most of the time,
    it is also desirable to inherit from TypedObject, which provides some
    virtual functions to return the TypeHandle for a particular instance.

    At its essence, a TypeHandle is simply a unique identifier that is assigned
    by the TypeRegistry.  The TypeRegistry stores a tree of TypeHandles, so
    that ancestry of a particular type may be queried, and the type name may be
    retrieved for run-time display.
    """

    MC_singleton: Final = 0
    MCSingleton: Final = 0
    MC_array: Final = 1
    MCArray: Final = 1
    MC_deleted_chain_active: Final = 2
    MCDeletedChainActive: Final = 2
    MC_deleted_chain_inactive: Final = 3
    MCDeletedChainInactive: Final = 3
    MC_limit: Final = 4
    MCLimit: Final = 4
    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def index(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def parent_classes(self) -> Sequence[TypeHandle]: ...
    @property
    def child_classes(self) -> Sequence[TypeHandle]: ...
    def __init__(self, __param0: TypeHandle | type = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: TypeHandle | type) -> bool: ...
    def __le__(self, other: TypeHandle | type) -> bool: ...
    def __gt__(self, other: TypeHandle | type) -> bool: ...
    def __ge__(self, other: TypeHandle | type) -> bool: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    @staticmethod
    def make(classobj: type) -> TypeHandle: ...
    def compare_to(self, other: TypeHandle | type) -> int:
        """Sorts TypeHandles arbitrarily (according to <, >, etc.).  Returns a number
        less than 0 if this type sorts before the other one, greater than zero if
        it sorts after, 0 if they are equivalent.
        """
    def get_hash(self) -> int:
        """Returns a hash code suitable for phash_map."""
    def get_name(self, object: TypedObject = ...) -> str:
        """Returns the name of the type.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def is_derived_from(self, parent: TypeHandle | type, object: TypedObject = ...) -> bool:
        """Returns true if this type is derived from the indicated type, false
        otherwise.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def get_num_parent_classes(self, object: TypedObject = ...) -> int:
        """Returns the number of parent classes that this type is known to have.  This
        may then be used to index into get_parent_class().  The result will be 0 if
        this class does not inherit from any other classes, 1 if normal, single
        inheritance is in effect, or greater than one if multiple inheritance is in
        effect.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def get_parent_class(self, index: int) -> TypeHandle:
        """Returns the nth parent class of this type.  The index should be in the
        range 0 <= index < get_num_parent_classes().
        """
    def get_num_child_classes(self, object: TypedObject = ...) -> int:
        """Returns the number of child classes that this type is known to have.  This
        may then be used to index into get_child_class().

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def get_child_class(self, index: int) -> TypeHandle:
        """Returns the nth child class of this type.  The index should be in the range
        0 <= index < get_num_child_classes().
        """
    def get_parent_towards(self, ancestor: TypeHandle | type, object: TypedObject = ...) -> TypeHandle:
        """Returns the parent class that is in a direct line of inheritance to the
        indicated ancestor class.  This is useful in the presence of multiple
        inheritance to try to determine what properties an unknown type may have.

        The return value is TypeHandle::none() if the type does not inherit from
        the ancestor.  If ancestor is the same as this type, the return value is
        this type.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def get_memory_usage(self, memory_class: _TypeHandle_MemoryClass) -> int:
        """Returns the total allocated memory used by objects of this type, for the
        indicated memory class.  This is only updated if track-memory-usage is set
        true in your Config.prc file.
        """
    def inc_memory_usage(self, memory_class: _TypeHandle_MemoryClass, size: int) -> None:
        """Adds the indicated amount to the record for the total allocated memory for
        objects of this type.
        """
    def dec_memory_usage(self, memory_class: _TypeHandle_MemoryClass, size: int) -> None:
        """Subtracts the indicated amount from the record for the total allocated
        memory for objects of this type.
        """
    def get_index(self) -> int:
        """Returns the integer index associated with this TypeHandle.  Each different
        TypeHandle will have a different index.  However, you probably shouldn't be
        using this method; you should just treat the TypeHandles as opaque classes.
        This is provided for the convenience of non-C++ scripting languages to
        build a hashtable of TypeHandles.
        """
    def output(self, out: ostream) -> None: ...
    @staticmethod
    def none() -> TypeHandle: ...
    compareTo = compare_to
    getHash = get_hash
    getName = get_name
    isDerivedFrom = is_derived_from
    getNumParentClasses = get_num_parent_classes
    getParentClass = get_parent_class
    getNumChildClasses = get_num_child_classes
    getChildClass = get_child_class
    getParentTowards = get_parent_towards
    getMemoryUsage = get_memory_usage
    incMemoryUsage = inc_memory_usage
    decMemoryUsage = dec_memory_usage
    getIndex = get_index

class TypeRegistry:
    """The TypeRegistry class maintains all the assigned TypeHandles in a given
    system.  There should be only one TypeRegistry class during the lifetime of
    the application.  It will be created on the local heap initially, and it
    should be migrated to shared memory as soon as shared memory becomes
    available.
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def typehandles(self) -> Sequence[TypeHandle]: ...
    @property
    def root_classes(self) -> Sequence[TypeHandle]: ...
    def __init__(self, __param0: TypeRegistry) -> None: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def register_dynamic_type(self, name: str) -> TypeHandle:
        """Registers a new type on-the-fly, presumably at runtime.  A new TypeHandle
        is returned if the typename was not seen before; otherwise the same
        TypeHandle that was last used for this typename is returned.
        """
    def record_derivation(self, child: TypeHandle | type, parent: TypeHandle | type) -> None:
        """Records that the type referenced by child inherits directly from the type
        referenced by parent.  In the event of multiple inheritance, this should be
        called once for each parent class.
        """
    def record_alternate_name(self, type: TypeHandle | type, name: str) -> None:
        """Indicates an alternate name for the same type.  This is particularly useful
        when a type has changed names, since the type is stored in a Bam file by
        name; setting the original name as the alternate will allow the type to be
        correctly read from old Bam files.
        """
    def record_python_type(self, type: TypeHandle | type, python_type) -> None:
        """Records the given Python type pointer in the type registry for the benefit
        of interrogate, which expects this to contain a Dtool_PyTypedObject.
        """
    def find_type(self, name: str) -> TypeHandle:
        """Looks for a previously-registered type of the given name.  Returns its
        TypeHandle if it exists, or TypeHandle::none() if there is no such type.
        """
    def find_type_by_id(self, id: int) -> TypeHandle:
        """Looks for a previously-registered type with the given id number (as
        returned by TypeHandle::get_index()). Returns its TypeHandle if it exists,
        or TypeHandle::none() if there is no such type.
        """
    def get_name(self, type: TypeHandle | type, object: TypedObject) -> str:
        """Returns the name of the indicated type.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def is_derived_from(self, child: TypeHandle | type, base: TypeHandle | type, child_object: TypedObject) -> bool:
        """Returns true if the first type is derived from the second type, false
        otherwise.

        The "child_object" pointer is an optional pointer to the TypedObject class
        that owns the child TypeHandle.  It is only used in case the TypeHandle is
        inadvertently undefined.

        This function definition follows the definitions for look_up() and
        freshen_derivations() just to maximize the chance the the compiler will be
        able to inline the above functions.  Yeah, a compiler shouldn't care, but
        there's a big different between "shouldn't" and "doesn't".
        """
    def get_num_typehandles(self) -> int:
        """Returns the total number of unique TypeHandles in the system."""
    def get_typehandle(self, n: int) -> TypeHandle:
        """Returns the nth TypeHandle in the system.  See get_num_typehandles()."""
    def get_num_root_classes(self) -> int:
        """Returns the number of root classes--that is, classes that do not inherit
        from any other classes--known in the system.
        """
    def get_root_class(self, n: int) -> TypeHandle:
        """Returns the nth root class in the system.  See get_num_root_classes()."""
    def get_num_parent_classes(self, child: TypeHandle | type, child_object: TypedObject) -> int:
        """Returns the number of parent classes that the indicated type is known to
        have.  This may then be used to index into get_parent_class().  The result
        will be 0 if this class does not inherit from any other classes, 1 if
        normal, single inheritance is in effect, or greater than one if multiple
        inheritance is in effect.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def get_parent_class(self, child: TypeHandle | type, index: int) -> TypeHandle:
        """Returns the nth parent class of this type.  The index should be in the
        range 0 <= index < get_num_parent_classes().
        """
    def get_num_child_classes(self, child: TypeHandle | type, child_object: TypedObject) -> int:
        """Returns the number of child classes that the indicated type is known to
        have.  This may then be used to index into get_child_class().

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    def get_child_class(self, child: TypeHandle | type, index: int) -> TypeHandle:
        """Returns the nth child class of this type.  The index should be in the range
        0 <= index < get_num_child_classes().
        """
    def get_parent_towards(self, child: TypeHandle | type, base: TypeHandle | type, child_object: TypedObject) -> TypeHandle:
        """Returns the parent of the indicated child class that is in a direct line of
        inheritance to the indicated ancestor class.  This is useful in the
        presence of multiple inheritance to try to determine what properties an
        unknown type may have.

        The "object" pointer is an optional pointer to the TypedObject class that
        owns this TypeHandle.  It is only used in case the TypeHandle is
        inadvertantly undefined.
        """
    @staticmethod
    def reregister_types() -> None:
        """Walks through the TypeRegistry tree and makes sure that each type that was
        previously registered is *still* registered.  This seems to get broken in
        certain circumstances when compiled against libc5--it is as if the static
        initializer stomps on the _type_handle values of each class after they've
        been registered.
        """
    def write(self, out: ostream) -> None:
        """Makes an attempt to format the entire TypeRegistry in a nice way that shows
        the derivation tree as intelligently as possible.
        """
    @staticmethod
    def ptr() -> TypeRegistry:
        """Returns the pointer to the global TypeRegistry object."""
    def get_typehandles(self) -> tuple[TypeHandle, ...]: ...
    def get_root_classes(self) -> tuple[TypeHandle, ...]: ...
    registerDynamicType = register_dynamic_type
    recordDerivation = record_derivation
    recordAlternateName = record_alternate_name
    recordPythonType = record_python_type
    findType = find_type
    findTypeById = find_type_by_id
    getName = get_name
    isDerivedFrom = is_derived_from
    getNumTypehandles = get_num_typehandles
    getTypehandle = get_typehandle
    getNumRootClasses = get_num_root_classes
    getRootClass = get_root_class
    getNumParentClasses = get_num_parent_classes
    getParentClass = get_parent_class
    getNumChildClasses = get_num_child_classes
    getChildClass = get_child_class
    getParentTowards = get_parent_towards
    reregisterTypes = reregister_types
    getTypehandles = get_typehandles
    getRootClasses = get_root_classes

class TypedObject:
    """This is an abstract class that all classes which use TypeHandle, and also
    provide virtual functions to support polymorphism, should inherit from.
    Each derived class should define get_type(), which should return the
    specific type of the derived class.  Inheriting from this automatically
    provides support for is_of_type() and is_exact_type().

    All classes that inherit directly or indirectly from TypedObject should
    redefine get_type() and force_init_type(), as shown below.  Some classes
    that do not inherit from TypedObject may still declare TypeHandles for
    themselves by defining methods called get_class_type() and init_type().
    Classes such as these may serve as base classes, but the dynamic type
    identification system will be limited.  Classes that do not inherit from
    TypedObject need not define the virtual functions get_type() and
    force_init_type() (or any other virtual functions).

    There is a specific layout for defining the overrides from this class.
    Keeping the definitions formatted just like these examples will allow
    someone in the future to use a sed (or similar) script to make global
    changes, if necessary.  Avoid rearranging the braces or the order of the
    functions unless you're ready to change them in every file all at once.

    What follows are some examples that can be used in new classes that you
    create.

    @par In the class definition (.h file):
    @code
    public:
      static TypeHandle get_class_type() {
        return _type_handle;
      }
      static void init_type() {
        <<<BaseClassOne>>>::init_type();
        <<<BaseClassTwo>>>::init_type();
        <<<BaseClassN>>>::init_type();
        register_type(_type_handle, "<<<ThisClassStringName>>>",
                      <<<BaseClassOne>>>::get_class_type(),
                      <<<BaseClassTwo>>>::get_class_type(),
                      <<<BaseClassN>>>::get_class_type());
      }
      virtual TypeHandle get_type() const {
        return get_class_type();
      }
      virtual TypeHandle force_init_type() {init_type(); return get_class_type();}

    private:
      static TypeHandle _type_handle;
    @endcode

    @par In the class .cxx file:
    @code
    TypeHandle <<<ThisClassStringName>>>::_type_handle;
    @endcode

    @par In the class config_<<<PackageName>>>.cxx file:
    @code
    ConfigureFn(config_<<<PackageName>>>) {
      <<<ClassOne>>>::init_type();
      <<<ClassTwo>>>::init_type();
      <<<ClassN>>>::init_type();
    }
    @endcode
    """

    DtoolClassDict: ClassVar[dict[str, Any]]
    @property
    def type(self) -> TypeHandle:
        """Returns the TypeHandle representing this object's type."""
    def get_type(self) -> TypeHandle:
        """Derived classes should override this function to return get_class_type()."""
    def get_type_index(self) -> int:
        """Returns the internal index number associated with this object's TypeHandle,
        a unique number for each different type.  This is equivalent to
        get_type().get_index().
        """
    def is_of_type(self, handle: TypeHandle | builtins.type) -> bool:
        """Returns true if the current object is or derives from the indicated type."""
    def is_exact_type(self, handle: TypeHandle | builtins.type) -> bool:
        """Returns true if the current object is the indicated type exactly."""
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getType = get_type
    getTypeIndex = get_type_index
    isOfType = is_of_type
    isExactType = is_exact_type
    getClassType = get_class_type
