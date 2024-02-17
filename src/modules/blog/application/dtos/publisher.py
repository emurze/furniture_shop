from shared.application.dto import DTOModel


class PublisherAddDTO(DTOModel):
    name: str
    city: str


class PublisherGetDTO(DTOModel):
    id: int
    name: str
    city: str
