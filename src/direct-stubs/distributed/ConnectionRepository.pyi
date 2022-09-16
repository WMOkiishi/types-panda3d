__all__ = ['ConnectionRepository', 'GCTrigger']

from _typeshed import StrOrBytesPath
from collections.abc import Callable, Iterable, Sequence, Mapping
from typing import Any, ClassVar
from typing_extensions import Literal

from panda3d.core import Datagram, DatagramIterator, HTTPChannel, HTTPClient, PythonTask, RecorderController
from panda3d.direct import CConnectionRepository
from ..directnotify.Notifier import Notifier
from .DoCollectionManager import DoCollectionManager
from .DoInterestManager import DoInterestManager

class ConnectionRepository(DoInterestManager, DoCollectionManager, CConnectionRepository):
    taskPriority: ClassVar[int]
    taskChain: ClassVar[str | None]
    CM_HTTP: ClassVar[Literal[0]]
    CM_NET: ClassVar[Literal[1]]
    CM_NATIVE: ClassVar[Literal[2]]
    gcNotify: ClassVar[Notifier]
    GarbageCollectTaskName: ClassVar[str]
    GarbageThresholdTaskName: ClassVar[str]
    uniqueId: int
    config: Any
    connectMethod: int
    connectHttp: None
    http: HTTPClient | None
    private__di: DatagramIterator
    recorder: RecorderController | None
    readerPollTaskObj: PythonTask | None
    dcSuffix: str
    def __init__(self, connectMethod: int, config: Any, hasOwnerView: bool = False, threadedNet: bool | None = None) -> None: ...
    def generateGlobalObject(
        self,
        doId: int,
        dcname: str,
        value: Mapping[str, Iterable[Any]] | None = None,
    ) -> Any: ...
    def readDCFile(self, dcFileNames: str | Iterable[StrOrBytesPath] | None = None) -> None: ...
    def importModule(self, dcImports, moduleName: str, importSymbols: Sequence[str]) -> None: ...
    def getServerAddress(self) -> str: ...
    def connect(
        self,
        serverList: Sequence[str],
        successCallback: Callable[..., object] | None = None,
        successArgs: Iterable[Any] = ...,
        failureCallback: Callable[..., object] | None = None,
        failureArgs: Iterable[Any] = ...,
    ) -> None: ...
    def httpConnectCallback(
        self,
        ch: HTTPChannel,
        serverList: Sequence[str],
        serverIndex: int,
        successCallback: Callable[..., object],
        successArgs: Iterable[Any],
        failureCallback: Callable[..., object],
        failureArgs: Iterable[Any],
    ) -> None: ...
    def checkHttp(self) -> HTTPClient: ...
    def startReaderPollTask(self) -> None: ...
    def stopReaderPollTask(self) -> None: ...
    def readerPollUntilEmpty(self, task: object) -> Literal[1]: ...
    def readerPollOnce(self) -> bool: ...
    def handleReaderOverflow(self) -> None: ...
    def lostConnection(self) -> None: ...
    def handleDatagram(self, di: DatagramIterator) -> None: ...
    def send(self, datagram: Datagram) -> None: ...
    def pullNetworkPlug(self) -> None: ...
    def networkPlugPulled(self) -> bool: ...
    def restoreNetworkPlug(self) -> None: ...
    def uniqueName(self, idString: str) -> str: ...

class GCTrigger: ...
