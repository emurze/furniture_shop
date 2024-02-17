from shared.application.dto import DTOModel


class PostAddDTO(DTOModel):
    title: str
    content: str
    publisher_id: int
    draft: bool


class PostGetDTO(DTOModel):
    id: int
    title: str
    content: str
    publisher_id: int
    draft: bool
