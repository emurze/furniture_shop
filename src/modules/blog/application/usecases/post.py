from dataclasses import dataclass

from modules.blog.application.dtos.post import PostAddDTO, PostGetDTO
from modules.blog.application.ports.usecases import post as ports
from modules.blog.application.ports.uow import IBlogUnitOfWork


@dataclass(frozen=True, slots=True)
class AddPostUseCase(ports.IAddPostUseCase):
    uow: IBlogUnitOfWork

    async def execute(self, post: PostAddDTO) -> int:
        post_dict = post.model_dump()

        async with self.uow:
            post_id = await self.uow.posts.add(**post_dict)
            await self.uow.commit()

        return post_id


@dataclass(frozen=True, slots=True)
class GetPostUseCase(ports.IGetPostUseCase):
    uow: IBlogUnitOfWork

    async def execute(self, **kw) -> PostGetDTO:
        async with self.uow:
            post = await self.uow.posts.get(**kw)
            return PostGetDTO.model_validate(post)


@dataclass(frozen=True, slots=True)
class GetPostsUseCase(ports.IGetPostsUseCase):
    uow: IBlogUnitOfWork

    async def execute(self) -> list[PostGetDTO]:
        async with self.uow:
            posts = await self.uow.posts.list()
            return [PostGetDTO.model_validate(post) for post in posts]
