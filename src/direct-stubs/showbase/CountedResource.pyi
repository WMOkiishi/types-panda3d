from abc import ABCMeta, abstractmethod
from typing import ClassVar

class CountedResource(metaclass=ABCMeta):
    RESOURCE_COUNTER: ClassVar[int]
    RESOURCE_COUNTER_INIT_FAILED: ClassVar[bool]
    @classmethod
    def incrementCounter(cls) -> None: ...
    @classmethod
    def decrementCounter(cls) -> None: ...
    @classmethod
    def getCount(cls) -> int: ...
    @classmethod
    @abstractmethod
    def acquire(cls) -> None: ...
    @classmethod
    @abstractmethod
    def release(cls) -> None: ...
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...