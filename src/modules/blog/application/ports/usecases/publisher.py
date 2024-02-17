import abc

from modules.blog.application.dtos import publisher as dtos


class IGetPublishersUseCase(abc.ABC):
    @abc.abstractmethod
    async def execute(self) -> list[dtos.PublisherGetDTO]:
        ...


class IGetPublisherUseCase(abc.ABC):
    @abc.abstractmethod
    async def execute(self, **kw) -> dtos.PublisherGetDTO:
        ...


class IAddPublisherUseCase(abc.ABC):
    @abc.abstractmethod
    async def execute(self, publisher: dtos.PublisherAddDTO) -> int:
        ...
