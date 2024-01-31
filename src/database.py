from typing import Annotated

from sqlalchemy import String
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

str256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str256: String(256)
    }
