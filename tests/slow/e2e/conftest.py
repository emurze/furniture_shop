from shared.infra.sqlalchemy_orm.db import get_session
from collections.abc import Iterator, AsyncIterator

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.testclient import TestClient

from api.main import app
from tests.slow.conftest import async_session_maker


@pytest.fixture(scope="function")
def client() -> Iterator[TestClient]:
    """
    Overrides the normal database access with test database,
    and yields a configured test client
    """

    async def override_session() -> AsyncIterator[AsyncSession]:
        async with async_session_maker() as new_session:
            yield new_session

    app.dependency_overrides[get_session] = override_session  # noqa

    with TestClient(app) as test_client:
        yield test_client
