from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from modules.posts.domain.models import Post
from tests.integration.posts.conftest import get_post_repo


async def test_repository_add(session: AsyncSession) -> None:
    post_repo = get_post_repo(session)
    post_repo.add(Post(id=1, title="Hello", content="Hello world!"))
    await session.commit()

    excepted = [Post(id=1, title="Hello", content="Hello world!")]
    result = await session.execute(select(Post))
    assert excepted == result.scalars().all()


async def test_repository_get(session: AsyncSession) -> None:
    stmt = insert(Post).values(id=1, title="Hello", content="Hello")
    await session.execute(stmt)
    await session.commit()

    post_repo = get_post_repo(session)
    post = await post_repo.get(title="Hello")
    assert post == Post(id=1, title="Hello", content="Hello")


async def test_repository_list(session: AsyncSession) -> None:
    stmt = insert(Post).values(
        [
            {"id": 1, "title": "Hello", "content": "Hello"},
            {"id": 2, "title": "Hello2", "content": "Hello2"},
            {"id": 3, "title": "Hello3", "content": "Hello3"},
        ]
    )
    await session.execute(stmt)
    await session.commit()

    post_repo = get_post_repo(session)
    posts = await post_repo.list()
    excepted = (
        Post(id=1, title="Hello", content="Hello"),
        Post(id=2, title="Hello2", content="Hello2"),
        Post(id=3, title="Hello3", content="Hello3"),
    )
    assert posts == excepted
