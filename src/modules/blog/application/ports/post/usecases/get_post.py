import abc

from modules.blog.domain.entities.post import Post


class IGetPostUseCase(abc.ABC):
    @abc.abstractmethod
    async def get_post(self, **kw) -> Post:
        ...
