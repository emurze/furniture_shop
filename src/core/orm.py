from collections.abc import Callable

from sqlalchemy.ext.asyncio import AsyncEngine

from core.models import worker_metadata, WorkerModel


async def create_tables(async_engine: AsyncEngine) -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(worker_metadata.drop_all)
        await conn.run_sync(worker_metadata.create_all)


async def insert_data(async_session: Callable) -> None:
    async with async_session() as session:
        w1 = WorkerModel(name="Vlad")
        w2 = WorkerModel(name="Lera")

        session.add(w1)
        await session.commit()
