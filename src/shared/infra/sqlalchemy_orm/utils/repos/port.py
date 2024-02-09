import abc
from typing import TypeVar, Generic

T = TypeVar("T")


class IBaseRepository(Generic[T], abc.ABC):
    @abc.abstractmethod
    def add(self, obj: T) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, **kw) -> T:
        raise NotImplementedError()

    @abc.abstractmethod
    async def list(self) -> tuple[T, ...]:
        raise NotImplementedError()
