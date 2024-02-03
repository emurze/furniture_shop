from dataclasses import dataclass

from api.config.app import AppConfig
from api.config.ports import DatabaseConfig
from database.postgres.config import PostgresConfig


@dataclass(frozen=True, slots=True)
class BaseConfig:
    app: AppConfig = AppConfig()
    db: DatabaseConfig = PostgresConfig()
