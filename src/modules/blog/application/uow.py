from modules.blog.application.ports.repos.post import IPostRepository
from modules.blog.application.ports.repos.publisher import IPublisherRepository
from modules.blog.application.ports.uow import IBlogUnitOfWork

from shared.application.uow import BaseUnitOfWork


class BlogUnitOfWork(BaseUnitOfWork, IBlogUnitOfWork):
    posts: type[IPostRepository]
    publishers: type[IPublisherRepository]
