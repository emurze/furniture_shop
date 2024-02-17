import pytest
from sqlalchemy import ColumnClause, NullPool, literal_column, text
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from shared.infra.sqlalchemy_orm.base import base
from shared.infra.sqlalchemy_orm.utils.helpers import suppress_echo
from tests.slow.config import db_config

db_dsn = db_config.get_dsn()
async_engine = create_async_engine(db_dsn, echo=True, poolclass=NullPool)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


@pytest.fixture(scope="function", autouse=True)
async def clean_tables() -> None:
    """
    Clean tables data before run test function
    """

    async with async_engine.begin() as conn:
        await conn.run_sync(base.metadata.drop_all)
        await conn.run_sync(base.metadata.create_all)
        await conn.commit()
