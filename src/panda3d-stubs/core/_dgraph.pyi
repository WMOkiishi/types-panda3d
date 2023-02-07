from typing import Any, ClassVar, overload
from typing_extensions import Self

from panda3d.core._dtoolutil import ostream
from panda3d.core._pgraph import PandaNode
from panda3d.core._pipeline import Thread

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
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, __memo: object) -> Self: ...
    def get_current_thread(self) -> Thread:
        """Returns the currently-executing thread object, as passed to the
        DataGraphTraverser constructor.
        """
    def traverse(self, node: PandaNode) -> None:
        """Starts the traversal of the data graph at the indicated root node."""
    def collect_leftovers(self) -> None:
        """Pick up any nodes that didn't get completely traversed.  These must be
        nodes that have multiple parents, with at least one parent completely
        outside of the data graph.
        """
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

    def write_inputs(self, out: ostream) -> None:
        """Writes to the indicated ostream a list of all the inputs this DataNode
        might expect to receive.
        """
    def write_outputs(self, out: ostream) -> None:
        """Writes to the indicated ostream a list of all the outputs this DataNode
        might generate.
        """
    def write_connections(self, out: ostream) -> None:
        """Writes to the indicated ostream a list of all the connections currently
        showing between this DataNode and its parent(s).
        """
    writeInputs = write_inputs
    writeOutputs = write_outputs
    writeConnections = write_connections
