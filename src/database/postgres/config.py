from pydantic import SecretStr, PositiveInt, PostgresDsn
from pydantic_settings import BaseSettings


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
                username=self.db_name,
                password=self.db_pass.get_secret_value(),
                host=f"{'furniture_shop'}{self.db_host}",
                port=self.db_port,
                path=self.db_name,
            )
        )


config = PostgresConfig()
