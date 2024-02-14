from collections.abc import AsyncIterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from shared.infra.sqlalchemy_orm.db import get_session

from api.main import app
from tests.slow.conftest import async_session_maker


async def get_test_session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_session] = get_test_session  # noqa


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
