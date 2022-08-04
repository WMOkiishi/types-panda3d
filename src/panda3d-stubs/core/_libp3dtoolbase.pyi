from collections.abc import Sequence
from typing import Any, ClassVar, Literal, TypeAlias, final, overload
from panda3d.core import ostream

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
    def get_total_alloc() -> int: ...
    @staticmethod
    def get_total_used() -> int: ...
    @staticmethod
    def get_total_unused() -> int: ...
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
    DtoolClassDict: ClassVar[dict[str, Any]]
    MC_singleton: ClassVar[Literal[0]]
    MC_array: ClassVar[Literal[1]]
    MC_deleted_chain_active: ClassVar[Literal[2]]
    MC_deleted_chain_inactive: ClassVar[Literal[3]]
    MC_limit: ClassVar[Literal[4]]
    @property
    def index(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def parent_classes(self) -> Sequence[TypeHandle]: ...
    @property
    def child_classes(self) -> Sequence[TypeHandle]: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __param0: TypeHandle) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, __other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __lt__(self, other: TypeHandle) -> bool: ...
    def __le__(self, other: TypeHandle) -> bool: ...
    def __gt__(self, other: TypeHandle) -> bool: ...
    def __ge__(self, other: TypeHandle) -> bool: ...
    @staticmethod
    def make(classobj: type) -> TypeHandle: ...
    def compare_to(self, other: TypeHandle) -> int: ...
    def get_hash(self) -> int: ...
    def get_name(self, object: TypedObject = ...) -> str: ...
    def is_derived_from(self, parent: TypeHandle, object: TypedObject = ...) -> bool: ...
    def get_num_parent_classes(self, object: TypedObject = ...) -> int: ...
    def get_parent_class(self, index: int) -> TypeHandle: ...
    def get_num_child_classes(self, object: TypedObject = ...) -> int: ...
    def get_child_class(self, index: int) -> TypeHandle: ...
    def get_parent_towards(self, ancestor: TypeHandle, object: TypedObject = ...) -> TypeHandle: ...
    def get_memory_usage(self, memory_class: _TypeHandle_MemoryClass) -> int: ...
    def inc_memory_usage(self, memory_class: _TypeHandle_MemoryClass, size: int) -> None: ...
    def dec_memory_usage(self, memory_class: _TypeHandle_MemoryClass, size: int) -> None: ...
    def get_index(self) -> int: ...
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
    MCSingleton = MC_singleton
    MCArray = MC_array
    MCDeletedChainActive = MC_deleted_chain_active
    MCDeletedChainInactive = MC_deleted_chain_inactive
    MCLimit = MC_limit

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
    def register_dynamic_type(self, name: str) -> TypeHandle: ...
    def record_derivation(self, child: TypeHandle, parent: TypeHandle) -> None: ...
    def record_alternate_name(self, type: TypeHandle, name: str) -> None: ...
    def record_python_type(self, type: TypeHandle, python_type: Any) -> None: ...
    def find_type(self, name: str) -> TypeHandle: ...
    def find_type_by_id(self, id: int) -> TypeHandle: ...
    def get_name(self, type: TypeHandle, object: TypedObject) -> str: ...
    def is_derived_from(self, child: TypeHandle, base: TypeHandle, child_object: TypedObject) -> bool: ...
    def get_num_typehandles(self) -> int: ...
    def get_typehandle(self, n: int) -> TypeHandle: ...
    def get_num_root_classes(self) -> int: ...
    def get_root_class(self, n: int) -> TypeHandle: ...
    def get_num_parent_classes(self, child: TypeHandle, child_object: TypedObject) -> int: ...
    def get_parent_class(self, child: TypeHandle, index: int) -> TypeHandle: ...
    def get_num_child_classes(self, child: TypeHandle, child_object: TypedObject) -> int: ...
    def get_child_class(self, child: TypeHandle, index: int) -> TypeHandle: ...
    def get_parent_towards(self, child: TypeHandle, base: TypeHandle, child_object: TypedObject) -> TypeHandle: ...
    @staticmethod
    def reregister_types() -> None: ...
    def write(self, out: ostream) -> None: ...
    @staticmethod
    def ptr() -> TypeRegistry: ...
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
    def type(self) -> TypeHandle: ...
    def get_type(self) -> TypeHandle: ...
    def get_type_index(self) -> int: ...
    def is_of_type(self, handle: TypeHandle) -> bool: ...
    def is_exact_type(self, handle: TypeHandle) -> bool: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    getType = get_type
    getTypeIndex = get_type_index
    isOfType = is_of_type
    isExactType = is_exact_type
    getClassType = get_class_type
