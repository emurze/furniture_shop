import abc

from modules.blog.domain.entities.publisher import Publisher


class IGetPublishersUseCase(abc.ABC):
    @abc.abstractmethod
    async def get_publishers(self) -> tuple[Publisher, ...]:
        ...
