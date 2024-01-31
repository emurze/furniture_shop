import os

import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from config import PostgresConfig
from queries.models import metadata

test_db_config = PostgresConfig(
    db_name=os.getenv('TEST_DB_NAME'),
    db_user=os.getenv('TEST_DB_USER'),
    db_pass=os.getenv('TEST_DB_PASS'),
    db_host=os.getenv('TEST_DB_HOST'),
    db_port=os.getenv('TEST_DB_PORT'),
)

_dsn = test_db_config.get_dsn()
_async_engine = create_async_engine(_dsn, echo=True)


def get_async_engine() -> AsyncEngine:
    dsn = test_db_config.get_dsn()
    return create_async_engine(dsn, echo=True)


@pytest.fixture(scope="session", autouse=True)
async def create_and_drop_tables() -> None:
    async with _async_engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

    yield

    async with _async_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture
def async_engine() -> AsyncEngine:
    return get_async_engine()
