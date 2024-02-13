from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from modules.blog.application.dtos.post import PostAddDTO
from modules.blog.application.usecases.post.add_post import AddPostUseCase
from modules.blog.application.usecases.post.get_post import GetPostUseCase
from modules.blog.application.usecases.post.get_posts import GetPostsUseCase
from modules.blog.domain.entities.post import Post
from modules.blog.infra.repos.post.sqlalchemy import PostRepository
from shared.infra.sqlalchemy_orm.db import get_session

posts_router = APIRouter(prefix="/posts", tags=["posts"])


@posts_router.get("/", response_model=tuple[Post, ...])
async def get_posts(session: AsyncSession = Depends(get_session)):
    repo = PostRepository(session)
    use_case = GetPostsUseCase(repo=repo)
    posts = await use_case.get_posts()
    return posts


@posts_router.get("/{post_id}", response_model=tuple[Post, ...])
async def get_post(post_id: int, session: AsyncSession = Depends(get_session)):
    repo = PostRepository(session)
    use_case = GetPostUseCase(repo=repo)
    post = await use_case.get_post(id=post_id)
    return post


@posts_router.post("/", response_model=None)
async def add_post(
    dto: PostAddDTO, session: AsyncSession = Depends(get_session)
):
    post = Post(
        id=dto.id,
        title=dto.title,
        content=dto.content,
        publisher_id=dto.publisher_id,
        draft=dto.draft,
    )
    repo = PostRepository(session)
    use_case = AddPostUseCase(repo=repo)
    use_case.add_post(post)
    await session.commit()
