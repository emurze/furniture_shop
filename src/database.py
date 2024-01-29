from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from config import config

async_engine = create_async_engine(
    config.db.get_dsn(),
    echo=True,
)

async_session = async_sessionmaker(
    async_engine,
    autobegin=True,
)


class Base(DeclarativeBase):
    pass
