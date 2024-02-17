from modules.blog.application.ports.uow import IBlogUnitOfWork
from tests.data.domain import PostModel


async def test_can_run_triggers(uow: IBlogUnitOfWork) -> None:
    post_dict = {
        "title": "Post 1",
        "content": "",
        "publisher_id": 1,
    }
    async with uow:
        await uow.posts.add(**post_dict)
        await uow.posts.add(**post_dict)
        await uow.posts.add(**post_dict)
        await uow.commit()

    post2_dict = {
        "title": "Post 4",
        "content": "",
        "publisher_id": 1,
        "draft": False,
    }
    async with uow:
        await uow.posts.add(**post2_dict)
        await uow.commit()

    posts = await uow.posts.list()

    assert len(posts) == 4
    assert PostModel(id=1, title="Post 1", content="", publisher_id=1) in posts
    assert PostModel(id=2, title="Post 1", content="", publisher_id=1) in posts
    assert PostModel(id=3, title="Post 1", content="", publisher_id=1) in posts
    assert PostModel(id=4, title="Post 4", content="", publisher_id=1) in posts


async def test_can_handle_many_transactions(uow: IBlogUnitOfWork) -> None:
    # COMMIT
    _dict1 = {"title": "Post 1", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**_dict1)
        await uow.commit()

    # ROLLBACK
    _dict2 = {"title": "Post 2", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**_dict2)

    # ROLLBACK
    _dict3 = {"title": "Post 3", "content": "", "publisher_id": 1}
    _dict4 = {"title": "Post 4", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**_dict3)
        await uow.posts.add(**_dict4)

    # COMMIT
    _dict5 = {"title": "Post 5", "content": "", "publisher_id": 1}
    _dict6 = {"title": "Post 6", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**_dict5)
        await uow.posts.add(**_dict6)
        await uow.commit()

    # COMMIT
    _dict7 = {"title": "Post 7", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**_dict7)
        await uow.commit()

    # ROLLBACK
    _dict8 = {"title": "Post 8", "content": "", "publisher_id": 1}
    async with uow:
        await uow.posts.add(**_dict8)

    posts = await uow.posts.list()

    assert len(posts) == 4
    assert PostModel(id=1, title="Post 1", content="", publisher_id=1) in posts
    assert PostModel(id=5, title="Post 5", content="", publisher_id=1) in posts
    assert PostModel(id=6, title="Post 6", content="", publisher_id=1) in posts
    assert PostModel(id=7, title="Post 7", content="", publisher_id=1) in posts
