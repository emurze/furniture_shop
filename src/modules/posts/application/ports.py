import abc

from modules.posts.domain.models import Post


class IPostRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, obj: Post) -> None:
        ...

    @abc.abstractmethod
    async def get(self, **kwargs) -> Post:
        ...

    @abc.abstractmethod
    async def list(self) -> tuple[Post, ...]:
        ...
