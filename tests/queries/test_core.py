from unittest import skip

from sqlalchemy.ext.asyncio import AsyncEngine

from queries.core import func, insert_data, select_data


@skip
async def test_one(async_engine: AsyncEngine) -> None:
    await func(async_engine)


async def test_insert_item(async_engine: AsyncEngine) -> None:
    await insert_data(async_engine)
    await select_data(async_engine)
