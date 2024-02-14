from shared.infra.sqlalchemy_orm.utils.uow import IBaseUnitOfWork
from tests.unit.core.utils import set_repos


class BaseFakeUnitOfWork(IBaseUnitOfWork):
    def __init__(self):
        self.session_called = False
        self.is_closed = False
        self.is_committed = False
        self.is_rolled_back = False

    async def __aenter__(self) -> None:
        self.session_called = True
        set_repos(self)

    async def __aexit__(self, *args) -> None:
        self.is_closed = True
        await self.rollback()

    async def commit(self) -> None:
        self.is_committed = True

    async def rollback(self) -> None:
        self.is_rolled_back = True
