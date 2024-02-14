from modules.blog.application.usecases.post.get_post import GetPostUseCase
from modules.blog.domain.entities.post import Post

#
# async def test_can_return_post() -> None:
#     post = Post(id=2, title="Post 2", content="text2", publisher_id=1)
#     repo = PostFakeRepository([post])
#
#     use_case = GetPostUseCase(repo)
#     post = await use_case.get_post(id=2)
#
#     assert post == Post(id=2, title="Post 2", content="text2", publisher_id=1)
