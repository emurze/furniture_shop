from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from shared.infra.sqlalchemy_orm.utils.repos.port import IBaseRepository, Model


class SQLAlchemyRepositoryMixin(IBaseRepository):
    model: type[Model]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, **kw) -> int:
        stmt = insert(self.model).values(**kw).returning(self.model.id)
        res_id = await self.session.execute(stmt)
        return res_id.scalar_one()

    async def get(self, **kw) -> Model:
        query = select(self.model).filter_by(**kw)
        res = await self.session.execute(query)
        return res.scalar_one()

    async def list(self) -> list[Model]:
        query = select(self.model)
        res = await self.session.execute(query)
        return list(res.scalars().all())
