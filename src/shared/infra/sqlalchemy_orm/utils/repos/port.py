import abc
from typing import Protocol, Any


class Model(Protocol):
    id: Any


class IBaseRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, **kw) -> int:
        """Returns id"""

    @abc.abstractmethod
    async def get(self, **kw) -> Model:
        ...

    @abc.abstractmethod
    async def list(self) -> list[Model]:
        ...
