import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from collections.abc import AsyncIterator
from tests.slow.conftest import async_session_maker


@pytest.fixture
async def session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
