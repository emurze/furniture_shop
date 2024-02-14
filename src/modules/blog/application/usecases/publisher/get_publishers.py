from dataclasses import dataclass

from modules.blog.application.ports.publisher.usecases.get_publishers import (
    IGetPublishersUseCase,
)
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.domain.entities.publisher import Publisher


@dataclass(frozen=True, slots=True)
class GetPublishersUseCase(IGetPublishersUseCase):
    uow: IBlogUnitOfWork

    async def get_publishers(self) -> tuple[Publisher, ...]:
        async with self.uow:
            return await self.uow.publishers.list()
