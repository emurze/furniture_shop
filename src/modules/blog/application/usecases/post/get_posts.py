from dataclasses import dataclass

from modules.blog.application.ports.post.usecases.get_posts import (
    IGetPostsUseCase,
)
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.domain.entities.post import Post


@dataclass(frozen=True, slots=True)
class GetPostsUseCase(IGetPostsUseCase):
    uow: IBlogUnitOfWork

    async def get_posts(self) -> tuple[Post, ...]:
        async with self.uow:
            posts = await self.uow.posts.list()
            return posts
