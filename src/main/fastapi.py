from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.uow import BlogUnitOfWork
from shared.infra.sqlalchemy_orm.db import get_session
from modules.blog.infra.repos.post.sqlalchemy import PostRepository
from modules.blog.infra.repos.publisher.sqlalchemy import PublisherRepository


def get_blog_unit_of_work(
    session: AsyncSession = Depends(get_session),
) -> IBlogUnitOfWork:
    return BlogUnitOfWork(
        session_factory=lambda: session,
        posts=PostRepository,
        publishers=PublisherRepository,
    )


BlogUOWDep = Annotated[IBlogUnitOfWork, Depends(get_blog_unit_of_work)]
