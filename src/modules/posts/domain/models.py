from dataclasses import dataclass


@dataclass
class Post:
    id: int
    title: str
    content: str
    draft: bool = False

    def validate_dict(self, **kwargs) -> bool:
        return all(
            [
                self.id == kwargs.get("id"),
                self.title == kwargs.get("title"),
                self.content == kwargs.get("content"),
                self.draft == kwargs.get("draft"),
            ]
        )
