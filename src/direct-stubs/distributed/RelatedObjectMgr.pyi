from collections.abc import Callable, Sequence
from typing import ClassVar
from typing_extensions import TypeAlias

from ..directnotify.Notifier import Notifier
from ..showbase.DirectObject import DirectObject
from .ClientRepositoryBase import ClientRepositoryBase
from .DistributedObjectBase import DistributedObjectBase

_AllCallback: TypeAlias = Callable[[list[DistributedObjectBase | None]], object]
_EachCallback: TypeAlias = Callable[[DistributedObjectBase], object]
_TimeoutCallback: TypeAlias = Callable[[Sequence[int]], object]
_CallbackTuple: TypeAlias = tuple[
    _AllCallback | None,
    _EachCallback | None,
    _TimeoutCallback | None,
    list[int],
    Sequence[int],
    str | None,
]

class RelatedObjectMgr(DirectObject):
    notify: ClassVar[Notifier]
    doLaterSequence: ClassVar[int]
    cr: ClientRepositoryBase
    pendingObjects: dict[int, list[_CallbackTuple]]
    def __init__(self, cr: ClientRepositoryBase) -> None: ...
    def destroy(self) -> None: ...
    def requestObjects(
        self,
        doIdList: Sequence[int],
        allCallback: _AllCallback | None = None,
        eachCallback: _EachCallback | None = None,
        timeout: float | None = None,
        timeoutCallback: _TimeoutCallback | None = None,
    ) -> _CallbackTuple: ...
    def abortRequest(self, tuple: _CallbackTuple) -> None: ...
    def abortAllRequests(self) -> None: ...
