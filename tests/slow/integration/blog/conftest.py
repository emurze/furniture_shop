import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.uow import BlogUnitOfWork
from modules.blog.infra.repos.post import PostRepository
from modules.blog.infra.repos.publisher import PublisherRepository


@pytest.fixture
def uow(session: AsyncSession) -> IBlogUnitOfWork:
    return BlogUnitOfWork(
        session_factory=lambda: session,
        posts=PostRepository,
        publishers=PublisherRepository,
    )


async def make_publisher(uow: IBlogUnitOfWork) -> int:
    data = {"name": "test", "city": "test"}

    async with uow:
        _id = await uow.publishers.add(**data)
        await uow.commit()

    return _id


async def make_post(uow: IBlogUnitOfWork) -> int:
    data = {"title": "DDD", "content": "", "publisher_id": 1}

    async with uow:
        _id = await uow.posts.add(**data)
        await uow.commit()

    return _id


async def make_publisher_and_post(uow: IBlogUnitOfWork) -> tuple[int, int]:
    publisher_data = {"name": "Vlad", "city": "test"}
    post_data = {"title": "DDD", "content": "", "publisher_id": 1}

    async with uow:
        publisher_id = await uow.publishers.add(**publisher_data)
        post_id = await uow.posts.add(**post_data)
        await uow.commit()

    return publisher_id, post_id
