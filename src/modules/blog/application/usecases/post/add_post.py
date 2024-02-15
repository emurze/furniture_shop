from dataclasses import dataclass

from modules.blog.application.ports.post.usecases.add_post import (
    IAddPostUseCase,
)
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.domain.entities.post import Post


@dataclass(frozen=True, slots=True)
class AddPostUseCase(IAddPostUseCase):
    uow: IBlogUnitOfWork

    async def add_post(self, post: Post) -> None:
        async with self.uow:
            self.uow.posts.add(post)
            await self.uow.commit()
