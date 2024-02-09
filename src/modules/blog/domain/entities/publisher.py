from dataclasses import dataclass, field
from typing import ClassVar

from modules.blog.domain.entities.post import Post


@dataclass
class Publisher:
    id: int
    name: str
    city: str

    posts: ClassVar[list[Post]]

    def publish(self, post: Post) -> None:
        post.publisher_id = self.id

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
