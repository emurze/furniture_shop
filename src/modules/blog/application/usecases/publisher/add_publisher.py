from dataclasses import dataclass

from modules.blog.application.ports.publisher.usecases.add_publisher import (
    IAddPublisherUseCase,
)
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.domain.entities.publisher import Publisher


@dataclass(frozen=True, slots=True)
class AddPublisherUseCase(IAddPublisherUseCase):
    uow: IBlogUnitOfWork

    async def add(self, publisher: Publisher) -> None:
        async with self.uow:
            self.uow.publishers.add(publisher)
            await self.uow.commit()
