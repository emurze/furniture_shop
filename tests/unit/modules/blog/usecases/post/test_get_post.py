from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.usecases.post.get_post import GetPostUseCase
from modules.blog.domain.entities.post import Post


async def test_can_return_post(uow: IBlogUnitOfWork) -> None:
    post1 = Post(id=2, title="Post 2", content="text2", publisher_id=1)
    async with uow:
        uow.posts.add(post1)
        await uow.commit()

    use_case = GetPostUseCase(uow)
    post2 = await use_case.get_post(id=2)

    assert post2 == Post(id=2, title="Post 2", content="text2", publisher_id=1)
