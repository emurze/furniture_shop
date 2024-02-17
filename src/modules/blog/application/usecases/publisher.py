from dataclasses import dataclass

from modules.blog.application.dtos import publisher as dtos
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.ports.usecases import publisher as ports


@dataclass(frozen=True, slots=True)
class AddPublisherUseCase(ports.IAddPublisherUseCase):
    uow: IBlogUnitOfWork

    async def execute(self, publisher: dtos.PublisherAddDTO) -> int:
        pub_dict = publisher.model_dump()

        async with self.uow:
            _id = await self.uow.publishers.add(**pub_dict)
            await self.uow.commit()

        return _id


@dataclass(frozen=True, slots=True)
class GetPublisherUseCase(ports.IGetPublisherUseCase):
    uow: IBlogUnitOfWork

    async def execute(self, **kw) -> dtos.PublisherGetDTO:
        async with self.uow:
            publisher = await self.uow.publishers.get(**kw)
            return dtos.PublisherGetDTO.model_validate(publisher)


@dataclass(frozen=True, slots=True)
class GetPublishersUseCase(ports.IGetPublishersUseCase):
    uow: IBlogUnitOfWork

    async def execute(self) -> list[dtos.PublisherGetDTO]:
        async with self.uow:
            publishers = await self.uow.publishers.list()
            return [dtos.PublisherGetDTO.model_validate(p) for p in publishers]
