from modules.blog.application.ports.uow import IBlogUnitOfWork
from tests.data.domain import PostModel
from tests.slow.integration.blog import conftest as utils
from tests.slow.integration.blog.conftest import make_publisher_and_post


async def test_add_item(uow: IBlogUnitOfWork) -> None:
    await utils.make_publisher(uow)

    post_data = {"id": 1, "title": "hello", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**post_data)
        await uow.commit()

    async with uow:
        post = await uow.posts.get(id=1)
        assert post == PostModel(**post_data)


async def test_get_item(uow: IBlogUnitOfWork) -> None:
    await utils.make_publisher_and_post(uow)

    async with uow:
        post = await uow.posts.get(id=1)
        assert post == PostModel(id=1, title="DDD", content="", publisher_id=1)


async def test_list_items(uow: IBlogUnitOfWork) -> None:
    await utils.make_publisher_and_post(uow)
    await utils.make_post(uow)

    async with uow:
        posts = await uow.posts.list()
        assert posts == [
            PostModel(id=1, title="DDD", content="", publisher_id=1),
            PostModel(id=2, title="DDD", content="", publisher_id=1),
        ]


async def test_publisher_posts(uow: IBlogUnitOfWork) -> None:
    await make_publisher_and_post(uow)
    async with uow:
        publisher = await uow.publishers.get_with_posts(id=1)
        assert publisher.posts[0].id == 1


async def test_posts_publisher(uow: IBlogUnitOfWork) -> None:
    await make_publisher_and_post(uow)
    async with uow:
        post = await uow.posts.get_with_publisher(id=1)
        assert post.publisher.id == 1
