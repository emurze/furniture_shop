from sqlalchemy.ext.asyncio import AsyncSession

from tests.integration.modules.blog.conftest import (
    make_publisher_and_post,
    get_pub_repo,
    get_post_repo,
)


async def test_publisher_posts(session: AsyncSession) -> None:
    publisher, post = await make_publisher_and_post()
    pub_repo = get_pub_repo(session)
    pub = await pub_repo.get_with_posts(id=publisher.id)

    assert pub.posts == [post]


async def test_post_publisher(session: AsyncSession) -> None:
    publisher, _ = await make_publisher_and_post()
    post_repo = get_post_repo(session)
    post = await post_repo.get_with_publisher()

    assert post.publisher == publisher
