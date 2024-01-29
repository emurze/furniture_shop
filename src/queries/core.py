from sqlalchemy import text, Result, insert, select
from sqlalchemy.ext.asyncio import AsyncEngine

from models import metadata, worker_table


async def func(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        res: Result = await conn.execute(
            text("SELECT 1, 2, 3 UNION SELECT 3, 4, 6;")
        )
        print(f"{res.all()[0]}")


async def create_tables(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


async def insert_data(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        # statement = text("""
        #     INSERT INTO worker (id, username)
        #     VALUES (1, 'vlad')
        # """)
        statement = insert(worker_table).values(
            [
                {'id': 1, "username": "Hello"},
                {'id': 2, "username": "Hi"},
            ]
        )
        await conn.execute(statement)
        print('INSERTED')


async def select_data(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        selected = select(worker_table.c.id, worker_table.c.username)
        res = await conn.execute(selected)
        print(f'{res.all()=}')
