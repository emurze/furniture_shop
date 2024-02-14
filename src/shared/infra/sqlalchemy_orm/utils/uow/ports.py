import abc
from typing import Protocol, Any


class IBaseUnitOfWork(abc.ABC):
    @abc.abstractmethod
    async def __aenter__(self) -> None:
        ...

    @abc.abstractmethod
    async def __aexit__(self, *args) -> None:
        ...

    @abc.abstractmethod
    async def commit(self) -> None:
        ...

    @abc.abstractmethod
    async def rollback(self) -> None:
        ...


class IOpenedUnitOfWork(Protocol):
    session: Any
