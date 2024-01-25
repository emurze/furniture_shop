from collections.abc import Iterator

import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from config import settings


@pytest.fixture
def engine() -> Iterator[AsyncEngine]:
    engine = create_async_engine(settings.postgres_dsn)
    yield engine
    print('CLOSE')
