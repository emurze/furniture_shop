from typing import Annotated

from fastapi import Depends

from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.uow import BlogUnitOfWork
from shared.infra.sqlalchemy_orm.db import async_session_maker


def get_blog_unit_of_work() -> IBlogUnitOfWork:
    return BlogUnitOfWork(async_session_maker)


BlogUOWDep = Annotated[IBlogUnitOfWork, Depends(get_blog_unit_of_work)]
