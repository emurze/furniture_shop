from pydantic import BaseModel


class AddPublisherDTO(BaseModel):
    id: int
    name: str
    city: str
