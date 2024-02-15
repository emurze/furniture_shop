from modules.blog.application.ports.post.repo import IPostRepository
from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.application.ports.uow import IBlogUnitOfWork

# depends on shared uow implementation that hasn't low level dependencies
from shared.infra.sqlalchemy_orm.utils.uow import SqlAlchemyUnitOfWork


class BlogUnitOfWork(SqlAlchemyUnitOfWork, IBlogUnitOfWork):
    posts: type[IPostRepository]
    publishers: type[IPublisherRepository]
