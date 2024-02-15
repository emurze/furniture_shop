from collections.abc import AsyncIterator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from shared.infra.sqlalchemy_orm.base import base
from tests.slow.conftest import async_session_maker

base.run_mappers()


@pytest.fixture(scope="function")
async def session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
