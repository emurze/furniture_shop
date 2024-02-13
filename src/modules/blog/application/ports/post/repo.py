import abc

from modules.blog.domain.entities.post import Post


class IPostRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, obj: Post) -> None:
        ...

    @abc.abstractmethod
    async def get(self, **kw) -> Post:
        ...

    @abc.abstractmethod
    async def list(self) -> tuple[Post, ...]:
        ...

    @abc.abstractmethod
    async def get_with_publisher(self, **kw) -> Post:
        ...
