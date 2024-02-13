from dataclasses import dataclass

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.post.usecases.add_post import (
    IAddPostUseCase,
)
from modules.blog.domain.entities.post import Post


@dataclass(frozen=True, slots=True)
class AddPostUseCase(IAddPostUseCase):
    repo: IPostRepository

    def add_post(self, post: Post) -> None:
        self.repo.add(post)
