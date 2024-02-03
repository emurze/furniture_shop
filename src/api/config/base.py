from dataclasses import dataclass, field

from api.config.app import AppConfig
from api.config.ports import DatabaseConfig
from database.postgres.config import PostgresConfig


@dataclass(frozen=True, slots=True)
class BaseConfig:
    app: AppConfig = field(default_factory=AppConfig)
    db: DatabaseConfig = field(default_factory=PostgresConfig)
