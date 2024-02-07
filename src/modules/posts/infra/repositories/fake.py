from collections.abc import Iterable

from modules.posts.application.ports import IPostRepository
from modules.posts.domain.models import Post


class FakePostRepository(IPostRepository):
    def __init__(self, posts: Iterable[Post]) -> None:
        self._posts = set(posts)

    def add(self, obj: Post) -> None:
        self._posts.add(obj)

    async def get(self, **kw) -> Post:
        return next(post for post in self._posts if post.validate_dict(**kw))

    async def list(self) -> tuple[Post, ...]:
        return tuple(self._posts)
