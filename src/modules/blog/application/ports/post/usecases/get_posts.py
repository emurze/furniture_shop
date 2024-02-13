import abc

from modules.blog.domain.entities.post import Post


class IGetPostsUseCase(abc.ABC):
    @abc.abstractmethod
    async def get_posts(self) -> tuple[Post, ...]:
        ...
