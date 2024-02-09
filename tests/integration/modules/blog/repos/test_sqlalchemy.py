from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from modules.blog.domain.entities.post import Post
from modules.blog.domain.entities.publisher import Publisher
from tests.integration.modules.blog.conftest import get_post_repo


async def test_repo_add(session: AsyncSession, pub: Publisher) -> None:
    post_repo = get_post_repo(session)
    post_repo.add(Post(id=1, title="DDD", content="EDD", publisher_id=pub.id))
    await session.commit()

    excepted = [Post(id=1, title="DDD", content="EDD", publisher_id=pub.id)]
    result = await session.execute(select(Post))
    assert excepted == result.scalars().all()


async def test_repo_get(session: AsyncSession, pub: Publisher) -> None:
    stmt = insert(Post).values(
        id=1, title="DDD", content="EDD", publisher_id=pub.id
    )
    await session.execute(stmt)
    await session.commit()

    post_repo = get_post_repo(session)
    post = await post_repo.get(title="DDD")
    assert post == Post(id=1, title="DDD", content="EDD", publisher_id=pub.id)


async def test_repo_list(session: AsyncSession, pub: Publisher) -> None:
    stmt = insert(Post).values(
        [
            {"id": 1, "title": "DDD", "content": "1", "publisher_id": pub.id},
            {"id": 2, "title": "DDD", "content": "2", "publisher_id": pub.id},
            {"id": 3, "title": "DDD", "content": "3", "publisher_id": pub.id},
        ]
    )
    await session.execute(stmt)
    await session.commit()

    post_repo = get_post_repo(session)
    posts = await post_repo.list()
    excepted = (
        Post(id=1, title="DDD", content="1", publisher_id=pub.id),
        Post(id=2, title="DDD", content="2", publisher_id=pub.id),
        Post(id=3, title="DDD", content="3", publisher_id=pub.id),
    )
    assert posts == excepted
