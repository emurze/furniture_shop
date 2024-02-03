from dataclasses import dataclass
from typing import Protocol


class IService(Protocol):
    pass


class IRepository(Protocol):
    pass


@dataclass(frozen=True, slots=True)
class Service(IService):
    repository: IRepository
