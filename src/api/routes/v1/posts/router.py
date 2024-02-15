import logging

from fastapi import APIRouter

from api.dependencies import BlogUOWDep
from modules.blog.application.dtos.post import PostAddDTO
from modules.blog.application.usecases.post.add_post import AddPostUseCase
from modules.blog.application.usecases.post.get_post import GetPostUseCase
from modules.blog.application.usecases.post.get_posts import GetPostsUseCase
from modules.blog.domain.entities.post import Post

lg = logging.getLogger(__name__)
posts_router = APIRouter(prefix="/posts", tags=["posts"])


@posts_router.get("/", response_model=tuple[Post, ...])
async def get_posts(uow: BlogUOWDep):
    use_case = GetPostsUseCase(uow)
    posts = await use_case.get_posts()
    return posts


@posts_router.get("/{post_id}", response_model=tuple[Post, ...])
async def get_post(post_id: int, uow: BlogUOWDep):
    use_case = GetPostUseCase(uow)
    post = await use_case.get_post(id=post_id)
    return post


@posts_router.post("/", response_model=None)
async def add_post(dto: PostAddDTO, uow: BlogUOWDep):
    post = Post(
        id=dto.id,
        title=dto.title,
        content=dto.content,
        publisher_id=dto.publisher_id,
        draft=dto.draft,
    )
    use_case = AddPostUseCase(uow)
    await use_case.add_post(post)
