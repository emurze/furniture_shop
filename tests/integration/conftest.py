import os
from collections.abc import AsyncIterator

import pytest

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncConnection,
)

from api.config.ports import DatabaseConfig
from database.postgres.config import PostgresConfig


class TestConfig:
    db: DatabaseConfig = PostgresConfig(
        db_name=os.getenv("TEST_DB_NAME"),
        db_user=os.getenv("TEST_DB_USER"),
        db_pass=os.getenv("TEST_DB_PASS"),
        db_host=os.getenv("TEST_DB_HOST"),
        db_port=os.getenv("TEST_DB_PORT"),
    )


config = TestConfig()
async_engine = create_async_engine(config.db.get_dsn())
async_session_maker = async_sessionmaker(async_engine)


@pytest.fixture
async def session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session


@pytest.fixture
async def conn() -> AsyncIterator[AsyncConnection]:
    async with async_engine.begin() as conn:
        yield conn
