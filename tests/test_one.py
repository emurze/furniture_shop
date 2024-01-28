from sqlalchemy.ext.asyncio import AsyncEngine

from opers import func


async def test_one(async_engine: AsyncEngine) -> None:
    await func(async_engine)
