from collections.abc import Callable

from shared.infra.sqlalchemy_orm.utils.uow.utils import set_repos
from shared.infra.sqlalchemy_orm.utils.uow.ports import IBaseUnitOfWork


class SqlAlchemyUnitOfWork(IBaseUnitOfWork):
    """
    Extend this class for a new unit of work

    Attributes example:
        posts: type[IPostRepository]
        publishers: type[IPublisherRepository]
    """

    def __init__(self, session_factory: Callable, **repos) -> None:
        self.session_factory = session_factory
        self._repos = repos

    async def __aenter__(self) -> None:
        self.session = self.session_factory()
        set_repos(self)

    async def __aexit__(self, *args) -> None:
        await self.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
