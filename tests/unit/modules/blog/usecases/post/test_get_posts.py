from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.usecases.post.get_posts import GetPostsUseCase
from modules.blog.domain.entities.post import Post


async def test_return_posts(uow: IBlogUnitOfWork) -> None:
    post1 = Post(id=1, title="Post 1", content="text1", publisher_id=1)
    post2 = Post(id=2, title="Post 2", content="text2", publisher_id=1)
    async with uow:
        uow.posts.add(post1)
        uow.posts.add(post2)
        await uow.commit()

    use_case = GetPostsUseCase(uow)
    posts = await use_case.get_posts()

    assert Post(id=1, title="Post 1", content="text1", publisher_id=1) in posts
    assert Post(id=2, title="Post 2", content="text2", publisher_id=1) in posts
