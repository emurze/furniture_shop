from dataclasses import dataclass

from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncEngine

from database import Base
from queries.models import WorkerModel, ResumeModel
from queries.utils import suppress_echo


@dataclass(frozen=True, slots=True)
class Core:
    """
    SQLAlchemy core api:

        Engine.pool.acquire() as conn_proxy  # ConnectionProxy

        * engine.connect() as conn
            - begin
            - rollback

        + engine.begin() as conn
            - begin
            - commit

        + injection feature
            - :name
            - stmt = stmt.bindparams(name=...)

        row_query = text(...)  # use injection feature
        query = select.values()
        stmt = insert().values()
        stmt = delete().values().filter_by()
        stmt = update().values().filter_by()

        result = await conn_proxy.execute(stmt | query)

        conn_proxy.release()

    DBAPI api:

        pool.acquire() as conn

        ...low_api_code...

        await conn.execute("...")

        pool.release(conn)

    """

    engine: AsyncEngine

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            async with suppress_echo(self.engine):
                await conn.run_sync(Base.metadata.drop_all)

            await conn.run_sync(Base.metadata.create_all)

    async def insert_data(self) -> None:
        async with self.engine.begin() as conn:
            stmt = (
                insert(WorkerModel)
                .values(
                    [
                        {"name": "Vlados"},
                        {"name": "Lerka"},
                        {"name": "Pluton"},
                        {"name": "Borya"},
                        {"name": "Murad"},
                        {"name": "Dzimka"},
                        {"name": "Evka"},
                    ]
                )
            )
            await conn.execute(stmt)

        async with self.engine.begin() as conn:
            stmt = (
                insert(ResumeModel)
                .values(
                    [
                        {
                            "title": "Vlados Paperos guy",
                            "workload": "fulltime",
                            "worker_id": 1,
                        },
                        {
                            "title": "Lerka Burger King",
                            "workload": "parttime",
                            "worker_id": 2,
                        },
                        {
                            "title": "Plancton",
                            "workload": "fulltime",
                            "worker_id": 3,
                        },
                        {
                            "title": "Bum guy",
                            "workload": "fulltime",
                            "worker_id": 4,
                        },
                        {
                            "title": "Murad Tanks",
                            "workload": "parttime",
                            "worker_id": 5,
                        },
                        {
                            "title": "Dzimka Hero",
                            "workload": "fulltime",
                            "worker_id": 6,
                        },
                        {
                            "title": "Future Lerka",
                            "workload": "parttime",
                            "worker_id": 7,
                        },
                    ]
                )
            )
            await conn.execute(stmt)

    async def delete_data(self) -> None:
        async with self.engine.begin() as conn:
            stmt = delete(WorkerModel).filter_by(id=1)
            await conn.execute(stmt)

    async def update_data(self) -> None:
        async with self.engine.begin() as conn:
            stmt = (
                update(WorkerModel)
                .values(name='VLADOS PAPEROS')
                .filter_by(id=2)
            )
            await conn.execute(stmt)

    async def select_data(self) -> None:
        async with self.engine.begin() as conn:
            query = select(WorkerModel)

            res = await conn.execute(query)

            for item in res:
                print(item)
