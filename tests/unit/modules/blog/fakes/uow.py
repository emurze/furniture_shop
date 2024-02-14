from typing import Annotated

from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.application.ports.uow import IBlogUnitOfWork
from tests.unit.core.uow import BaseFakeUnitOfWork
from tests.unit.modules.blog.fakes.post.repo import PostFakeRepository
from tests.unit.modules.blog.fakes.publisher.repo import (
    PublisherFakeRepository,
)


class BlogFakeUnitOfWork(BaseFakeUnitOfWork, IBlogUnitOfWork):
    posts: Annotated[IPostRepository, PostFakeRepository]
    publishers: Annotated[IPublisherRepository, PublisherFakeRepository]
