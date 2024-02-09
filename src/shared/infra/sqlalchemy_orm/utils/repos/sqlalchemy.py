from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shared.infra.sqlalchemy_orm.utils.repos.port import IBaseRepository

TR = TypeVar("TR")


class SQLAlchemyRepositoryMixin(IBaseRepository[TR]):
    model: type[TR]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def add(self, obj: TR) -> None:
        self.session.add(obj)

    async def get(self, **kw) -> TR:
        query = select(self.model).filter_by(**kw)
        res = await self.session.execute(query)
        return res.scalars().one()

    async def list(self) -> tuple[TR, ...]:
        res = await self.session.execute(select(self.model))
        return tuple(res.scalars().all())
