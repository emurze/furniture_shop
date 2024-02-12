from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from shared.infra.sqlalchemy_orm.database.config import db_config

async_engine = create_async_engine(db_config.get_dsn())
async_session_maker = async_sessionmaker(async_engine)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session
