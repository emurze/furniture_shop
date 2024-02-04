from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from api.config import config

async_engine = create_async_engine(config.db.get_dsn())
async_session_maker = async_sessionmaker()


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
