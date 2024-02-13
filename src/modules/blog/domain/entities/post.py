from dataclasses import dataclass
from typing import Any, ClassVar


@dataclass
class Post:
    id: int
    title: str
    content: str
    publisher_id: int
    draft: bool = False
    publisher: ClassVar[Any]

    def __hash__(self) -> int:
        return hash(self.id)

    def validate_dict(self, **kwargs) -> bool:
        return all(
            [
                self.id == kwargs.get("id"),
                self.title == kwargs.get("title"),
                self.content == kwargs.get("content"),
                self.publisher_id == kwargs.get("publisher_id"),
                self.draft == kwargs.get("draft"),
            ]
        )
