import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.domain.entities.post import Post
from modules.blog.domain.entities.publisher import Publisher
from modules.blog.infra.repos.post.sqlalchemy import PostRepository
from modules.blog.infra.repos.publisher.sqlalchemy import PublisherRepository
from tests.slow.conftest import async_session_maker


def get_post_repo(session: AsyncSession) -> IPostRepository:
    return PostRepository(session)


def get_pub_repo(session: AsyncSession) -> IPublisherRepository:
    return PublisherRepository(session)


@pytest.fixture
async def pub() -> Publisher:
    pub_data = {"id": 1, "name": "test", "city": "test"}
    pub = Publisher(**pub_data)

    async with async_session_maker() as new_session:
        pub_repo = get_pub_repo(new_session)
        pub_repo.add(pub)
        await new_session.commit()

    return Publisher(**pub_data)


async def make_publisher_and_post() -> tuple[Publisher, Post]:
    publisher_data = {"id": 1, "name": "Vlad", "city": "test"}
    post_data = {"id": 1, "title": "DDD", "content": "text", "publisher_id": 1}

    publisher = Publisher(**publisher_data)
    post = Post(**post_data)

    async with async_session_maker() as new_session:
        pub_repo = get_pub_repo(new_session)
        post_repo = get_post_repo(new_session)
        pub_repo.add(publisher)
        post_repo.add(post)
        await new_session.commit()

    return Publisher(**publisher_data), Post(**post_data)
