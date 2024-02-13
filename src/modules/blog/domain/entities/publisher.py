from dataclasses import dataclass
from typing import ClassVar

from modules.blog.domain.entities.post import Post


@dataclass
class Publisher:
    id: int
    name: str
    city: str
    posts: ClassVar[list[Post]]

    def __hash__(self) -> int:
        return hash(self.id)

    @staticmethod
    def edit(post: Post, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(post, key, value)

    @staticmethod
    def to_draft(post: Post) -> None:
        post.draft = True

    @staticmethod
    def from_draft(post: Post) -> None:
        post.draft = False
