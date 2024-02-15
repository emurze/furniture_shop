from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.usecases.post.add_post import AddPostUseCase
from modules.blog.domain.entities.post import Post


async def test_can_add_post(uow: IBlogUnitOfWork) -> None:
    post = Post(id=2, title="Post", content="text", publisher_id=1)

    use_case = AddPostUseCase(uow)
    await use_case.add_post(post)

    retrieved_post = await uow.posts.get(id=2)
    assert post == retrieved_post
