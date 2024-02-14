from dataclasses import dataclass

from modules.blog.application.ports.post.usecases.get_post import (
    IGetPostUseCase,
)
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.domain.entities.post import Post


@dataclass(frozen=True, slots=True)
class GetPostUseCase(IGetPostUseCase):
    uow: IBlogUnitOfWork

    async def get_post(self, **kw) -> Post:
        async with self.uow:
            post = await self.uow.posts.get(**kw)
            return post
