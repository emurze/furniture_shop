from dataclasses import dataclass

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.post.usecases.get_post import (
    IGetPostUseCase,
)
from modules.blog.domain.entities.post import Post


@dataclass(frozen=True, slots=True)
class GetPostUseCase(IGetPostUseCase):
    repo: IPostRepository

    async def get_post(self, **kw) -> Post:
        post = await self.repo.get(**kw)
        return post
