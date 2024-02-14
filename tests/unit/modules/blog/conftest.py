import pytest

from modules.blog.application.ports.uow import IBlogUnitOfWork
from tests.unit.modules.blog.fakes.uow import BlogFakeUnitOfWork


@pytest.fixture
def uow() -> IBlogUnitOfWork:
    return BlogFakeUnitOfWork()
