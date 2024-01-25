from pydantic import SecretStr, PositiveInt, PostgresDsn, Field, AliasPath
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource


class Settings(BaseSettings, frozen=True):
    secret_key: SecretStr
    db_name: str
    db_user: str
    db_pass: SecretStr = Field(init_var=False)
    db_host: str
    db_port: PositiveInt
    driver: str = "postgresql+asyncpg"

    @property
    def postgres_dsn(self) -> str:
        return str(
            PostgresDsn.build(
                scheme=self.driver,
                username=self.db_user,
                password=self.db_pass.get_secret_value(),
                host=self.db_host,
                port=self.db_port,
                path=self.db_name,
            )
        )


settings = Settings()
