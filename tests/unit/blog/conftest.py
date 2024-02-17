from typing import Annotated

import pytest

from modules.blog.application.ports.repos.post import IPostRepository
from modules.blog.application.ports.repos.publisher import IPublisherRepository
from modules.blog.application.ports.uow import IBlogUnitOfWork
from tests.data.domain import PostModel, PublisherModel
from tests.unit.utils.gens import id_gen
from tests.unit.utils.repo import FakeRepositoryMixin
from tests.unit.utils.uow import BaseFakeUnitOfWork


class PostFakeRepository(FakeRepositoryMixin, IPostRepository):
    model = PostModel
    field_gens = {
        "id": id_gen,
    }

    async def get_with_publisher(self, **kw) -> PostModel:
        ...


class PublisherFakeRepository(FakeRepositoryMixin, IPublisherRepository):
    model = PublisherModel
    field_gens = {
        "id": id_gen,
    }

    async def get_with_posts(self, **kw) -> PublisherModel:
        ...


class BlogFakeUnitOfWork(BaseFakeUnitOfWork, IBlogUnitOfWork):
    posts: Annotated[IPostRepository, PostFakeRepository]
    publishers: Annotated[IPublisherRepository, PublisherFakeRepository]


@pytest.fixture
def uow() -> IBlogUnitOfWork:
    return BlogFakeUnitOfWork()
