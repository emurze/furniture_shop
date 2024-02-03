import abc
from typing import Protocol


class DatabaseConfig(Protocol):
    @abc.abstractmethod
    def get_dsn(self, driver: str = "") -> str:
        ...
