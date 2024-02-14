from typing import Annotated

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.infra.repos.post.sqlalchemy import PostRepository
from modules.blog.infra.repos.publisher.sqlalchemy import PublisherRepository
from shared.infra.sqlalchemy_orm.utils.uow import SqlAlchemyUnitOfWork


class BlogUnitOfWork(SqlAlchemyUnitOfWork, IBlogUnitOfWork):
    posts: Annotated[IPostRepository, PostRepository]
    publishers: Annotated[IPublisherRepository, PublisherRepository]
