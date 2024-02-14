from dataclasses import dataclass

from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.application.ports.publisher.usecases.get_publishers import (
    IGetPublishersUseCase,
)
from modules.blog.domain.entities.publisher import Publisher


@dataclass(frozen=True, slots=True)
class GetPublishersUseCase(IGetPublishersUseCase):
    repo: IPublisherRepository

    async def get_publishers(self) -> tuple[Publisher, ...]:
        return await self.repo.list()
