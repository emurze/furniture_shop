from pydantic import BaseModel


class PostRead(BaseModel):
    id: int
    title: str
    content: str
    draft: bool
