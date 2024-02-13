import abc

from modules.blog.domain.entities.post import Post


class IAddPostUseCase(abc.ABC):
    @abc.abstractmethod
    def add_post(self, post: Post) -> None:
        ...
