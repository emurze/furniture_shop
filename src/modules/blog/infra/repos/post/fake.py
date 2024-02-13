from collections.abc import Sequence

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.domain.entities.post import Post


class PostFakeRepository(IPostRepository):
    def __init__(self, posts: Sequence[Post] | None = None) -> None:
        if posts is None:
            self._posts = set()
        else:
            self._posts = set(posts)

    def add(self, obj: Post) -> None:
        self._posts.add(obj)

    async def get(self, **kw) -> Post:
        return next(
            post
            for post in self._posts
            for k, v in kw.items()
            if getattr(post, k) == v
        )

    async def list(self) -> tuple[Post, ...]:
        return tuple(self._posts)

    async def get_with_publisher(self, **kw) -> Post:
        ...
