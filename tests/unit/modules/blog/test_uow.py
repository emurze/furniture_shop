from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.domain.entities.post import Post


async def test_rollback(uow: IBlogUnitOfWork) -> None:
    post1 = Post(id=1, title="title1", content="content1", publisher_id=1)
    post2 = Post(id=2, title="title2", content="content2", publisher_id=1)
    async with uow:
        uow.posts.add(post1)
        uow.posts.add(post2)

    posts = await uow.posts.list()
    assert posts == ()


async def test_commit_then_rollback(uow: IBlogUnitOfWork) -> None:
    post1 = Post(id=1, title="title1", content="text1", publisher_id=1)
    post2 = Post(id=2, title="title2", content="text2", publisher_id=1)
    async with uow:
        uow.posts.add(post1)
        uow.posts.add(post2)
        await uow.commit()

    post3 = Post(id=3, title="DDD", content="DDD", publisher_id=1)
    async with uow:
        uow.posts.add(post3)

    posts = await uow.posts.list()
    assert Post(id=1, title="title1", content="text1", publisher_id=1) in posts
    assert Post(id=2, title="title2", content="text2", publisher_id=1) in posts
    assert Post(id=3, title="DDD", content="DDD", publisher_id=1) not in posts


async def test_rollback_2commits_3rollbacks_commit_rollback_commit(
    uow: IBlogUnitOfWork,
) -> None:
    # ROLLBACK
    post1 = Post(id=1, title="DDD", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post1)

    posts1 = await uow.posts.list()
    assert Post(id=1, title="DDD", content="", publisher_id=1) not in posts1

    # COMMIT
    post2 = Post(id=2, title="DDD2", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post2)
        await uow.commit()

    posts2 = await uow.posts.list()
    assert Post(id=2, title="DDD2", content="", publisher_id=1) in posts2

    # COMMIT
    post3 = Post(id=3, title="DDD3", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post3)
        await uow.commit()

    posts3 = await uow.posts.list()
    assert Post(id=2, title="DDD2", content="", publisher_id=1) in posts3
    assert Post(id=3, title="DDD3", content="", publisher_id=1) in posts3

    # ROLLBACK
    post4 = Post(id=4, title="DDD4", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post4)

    posts4 = await uow.posts.list()
    assert Post(id=4, title="DDD4", content="", publisher_id=1) not in posts4

    # ROLLBACK
    post5 = Post(id=5, title="DDD5", content="", publisher_id=1)
    post6 = Post(id=6, title="DDD6", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post5)
        uow.posts.add(post6)

    posts5 = await uow.posts.list()
    assert Post(id=5, title="DDD5", content="", publisher_id=1) not in posts5
    assert Post(id=6, title="DDD6", content="", publisher_id=1) not in posts5

    # ROLLBACK
    post7 = Post(id=7, title="DDD7", content="", publisher_id=1)
    post8 = Post(id=8, title="DDD8", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post7)
        uow.posts.add(post8)

    posts6 = await uow.posts.list()
    assert Post(id=7, title="DDD7", content="", publisher_id=1) not in posts6
    assert Post(id=8, title="DDD8", content="", publisher_id=1) not in posts6

    # COMMIT
    post9 = Post(id=9, title="DDD9", content="", publisher_id=1)
    post10 = Post(id=10, title="DDD10", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post9)
        uow.posts.add(post10)
        await uow.commit()

    posts7 = await uow.posts.list()
    assert Post(id=9, title="DDD9", content="", publisher_id=1) in posts7
    assert Post(id=10, title="DDD10", content="", publisher_id=1) in posts7

    # ROLLBACK
    post11 = Post(id=11, title="DDD11", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post11)

    posts8 = await uow.posts.list()
    assert Post(id=11, title="DDD11", content="", publisher_id=1) not in posts8

    # COMMIT
    post12 = Post(id=12, title="TDD", content="", publisher_id=1)
    async with uow:
        uow.posts.add(post12)
        await uow.commit()

    posts9 = await uow.posts.list()
    assert Post(id=12, title="TDD", content="", publisher_id=1) in posts9

    # RESULT
    posts10 = await uow.posts.list()
    assert len(posts10) == 5
    assert Post(id=2, title="DDD2", content="", publisher_id=1) in posts10
    assert Post(id=3, title="DDD3", content="", publisher_id=1) in posts10
    assert Post(id=9, title="DDD9", content="", publisher_id=1) in posts10
    assert Post(id=10, title="DDD10", content="", publisher_id=1) in posts10
    assert Post(id=12, title="TDD", content="", publisher_id=1) in posts10
