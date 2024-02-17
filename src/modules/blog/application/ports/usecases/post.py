import abc

from modules.blog.application.dtos.post import PostAddDTO, PostGetDTO


class IAddPostUseCase(abc.ABC):
    @abc.abstractmethod
    async def execute(self, post: PostAddDTO) -> int:
        ...


class IGetPostUseCase(abc.ABC):
    @abc.abstractmethod
    async def execute(self, **kw) -> PostGetDTO:
        ...


class IGetPostsUseCase(abc.ABC):
    @abc.abstractmethod
    async def execute(self) -> list[PostGetDTO]:
        ...
