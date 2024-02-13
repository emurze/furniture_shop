from dataclasses import dataclass

from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.application.ports.publisher.usecases.add_publisher import (
    IAddPublisherUseCase,
)
from modules.blog.domain.entities.publisher import Publisher


@dataclass(frozen=True, slots=True)
class AddPublisherUseCase(IAddPublisherUseCase):
    repo: IPublisherRepository

    def add(self, publisher: Publisher) -> None:
        self.repo.add(publisher)
