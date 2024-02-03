from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    project_title: str


config = AppConfig()
