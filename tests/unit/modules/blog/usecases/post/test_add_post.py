from modules.blog.application.usecases.post.add_post import AddPostUseCase
from modules.blog.domain.entities.post import Post
from modules.blog.infra.repos.post.fake import PostFakeRepository


async def test_can_add_post() -> None:
    post = Post(id=2, title="Post", content="text", publisher_id=1)
    repo = PostFakeRepository()

    use_case = AddPostUseCase(repo)
    use_case.add_post(post)

    retrieved_post = await repo.get(id=2)
    assert post == retrieved_post
