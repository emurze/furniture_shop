from dataclasses import dataclass

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.post.usecases.get_posts import (
    IGetPostsUseCase,
)
from modules.blog.domain.entities.post import Post


@dataclass(frozen=True, slots=True)
class GetPostsUseCase(IGetPostsUseCase):
    repo: IPostRepository

    async def get_posts(self) -> tuple[Post, ...]:
        posts = await self.repo.list()
        return posts
