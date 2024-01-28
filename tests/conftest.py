import os

import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from config import PostgresConfig

test_db_config = PostgresConfig(
    db_name=os.getenv('TEST_DB_NAME'),
    db_user=os.getenv('TEST_DB_USER'),
    db_pass=os.getenv('TEST_DB_PASS'),
    db_host=os.getenv('TEST_DB_HOST'),
    db_port=os.getenv('TEST_DB_PORT'),
)


@pytest.fixture
def async_engine() -> AsyncEngine:
    dsn = test_db_config.get_dsn()
    return create_async_engine(dsn, echo=True)
