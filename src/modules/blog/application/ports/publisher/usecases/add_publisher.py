import abc

from modules.blog.domain.entities.post import Post


class IAddPublisherUseCase(abc.ABC):
    @abc.abstractmethod
    def add(self, publisher: Post) -> None:
        ...
