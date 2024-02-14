from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.domain.entities.post import Post
from tests.unit.core.repo import FakeRepositoryMixin


class PostFakeRepository(FakeRepositoryMixin[Post], IPostRepository):
    async def get_with_publisher(self, **kw) -> Post:
        ...
