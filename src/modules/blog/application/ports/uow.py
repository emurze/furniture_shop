import abc

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.publisher.repo import IPublisherRepository


class IBlogUnitOfWork(abc.ABC):
    posts: IPostRepository
    publishers: IPublisherRepository

    @abc.abstractmethod
    async def __aenter__(self) -> None:
        ...

    @abc.abstractmethod
    async def __aexit__(self, *args) -> None:
        ...

    @abc.abstractmethod
    async def commit(self) -> None:
        ...

    @abc.abstractmethod
    async def rollback(self) -> None:
        ...
