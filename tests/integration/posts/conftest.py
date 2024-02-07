from sqlalchemy.ext.asyncio import AsyncSession

from modules.posts.application.ports import IPostRepository
from modules.posts.infra.repositories.post import PostRepository


def get_post_repo(session: AsyncSession) -> IPostRepository:
    return PostRepository(session)
