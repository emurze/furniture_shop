import abc
from dataclasses import dataclass
from typing import Protocol

from pydantic import SecretStr, PositiveInt, PostgresDsn
from pydantic_settings import BaseSettings


class DatabaseConfig(Protocol):
    db_name: str
    db_user: str
    db_pass: SecretStr
    db_host: str
    db_port: int

    @abc.abstractmethod
    def get_dsn(self, driver: str) -> str:
        ...


class WebAPIConfig(Protocol):
    secret_key: SecretStr


class PostgresConfig(BaseSettings):
    db_name: str
    db_user: str
    db_pass: SecretStr
    db_host: str
    db_port: PositiveInt

    def get_dsn(self, driver: str = "postgresql+asyncpg") -> str:
        return str(
            PostgresDsn.build(
                scheme=driver,
                username=self.db_user,
                password=self.db_pass.get_secret_value(),
                host=self.db_host,
                port=self.db_port,
                path=self.db_name,
            )
        )


class FastAPIConfig(BaseSettings):
    secret_key: SecretStr


@dataclass(frozen=True, slots=True)
class BaseConfig:
    db: DatabaseConfig
    fastapi: WebAPIConfig


config = BaseConfig(
    db=PostgresConfig(),
    fastapi=FastAPIConfig(),
)
