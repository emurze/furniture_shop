from pydantic import BaseModel


class PostGetDTO(BaseModel):
    id: int
    title: str
    content: str
    publisher_id: int
    draft: bool


class PostAddDTO(BaseModel):
    id: int
    title: str
    content: str
    publisher_id: int
    draft: bool
