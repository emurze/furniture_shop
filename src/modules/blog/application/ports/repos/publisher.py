import abc

from modules.blog.domain.entities.publisher import Publisher


class IPublisherRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, obj: Publisher) -> None:
        ...

    @abc.abstractmethod
    async def get(self, **kw) -> Publisher:
        ...

    @abc.abstractmethod
    async def list(self) -> tuple[Publisher, ...]:
        ...

    @abc.abstractmethod
    async def get_with_posts(self, **kw) -> Publisher:
        ...
