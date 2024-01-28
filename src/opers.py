from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine


async def func(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        res = await conn.execute(text("SELECT 1;"))
        print(res)
