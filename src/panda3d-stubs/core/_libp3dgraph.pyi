from typing import Any, ClassVar, overload
from panda3d.core import PandaNode, Thread, TypeHandle, ostream

class DataGraphTraverser:
    """This object supervises the traversal of the data graph and the moving of
    data from one DataNode to its children.  The data graph is used to manage
    data from input devices, etc.  See the overview of the data graph in
    dataNode.h.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    @overload
    def __init__(self, current_thread: Thread = ...) -> None: ...
    @overload
    def __init__(self, __param0: DataGraphTraverser) -> None: ...
    def get_current_thread(self) -> Thread: ...
    def traverse(self, node: PandaNode) -> None: ...
    def collect_leftovers(self) -> None: ...
    getCurrentThread = get_current_thread
    collectLeftovers = collect_leftovers

class DataNode(PandaNode):
    """The fundamental type of node for the data graph.  The DataNode class is
    itself primarily intended as an abstract class; it defines no inputs and no
    outputs.  Most kinds of data nodes will derive from this to specify the
    inputs and outputs in the constructor.
    
    DataNode does not attempt to cycle its data with a PipelineCycler.  The
    data graph is intended to be used only within a single thread.
    """
    DtoolClassDict: ClassVar[dict[str, Any]]
    def __init__(self, name: str) -> None: ...
    def write_inputs(self, out: ostream) -> None: ...
    def write_outputs(self, out: ostream) -> None: ...
    def write_connections(self, out: ostream) -> None: ...
    @staticmethod
    def get_class_type() -> TypeHandle: ...
    writeInputs = write_inputs
    writeOutputs = write_outputs
    writeConnections = write_connections
    getClassType = get_class_type
