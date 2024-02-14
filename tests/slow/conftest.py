from collections.abc import AsyncIterator

import pytest
from sqlalchemy import ColumnClause, NullPool, literal_column, text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from api.main import app
from shared.infra.sqlalchemy_orm.base import base
from shared.infra.sqlalchemy_orm.db import get_session
from shared.infra.sqlalchemy_orm.utils.helpers import suppress_echo
from tests.slow.config import db_config


async def get_test_session() -> AsyncIterator[AsyncSession]:
    async with async_session_maker() as session:
        yield session


base.run_mappers()

db_dsn = db_config.get_dsn()
async_engine = create_async_engine(db_dsn, echo=True, poolclass=NullPool)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

app.dependency_overrides[get_session] = get_test_session  # noqa


@pytest.fixture(scope="session", autouse=True)
async def prepare_database() -> None:
    """
    Recreate the database tables for each session
    """

    async with async_engine.begin() as conn:
        async with suppress_echo(async_engine):
            for table in base.metadata.sorted_tables:
                sanitized_table_name: ColumnClause = literal_column(table.name)
                stmt = text(
                    f"DROP TABLE IF EXISTS {sanitized_table_name} CASCADE"
                )
                await conn.execute(stmt)

        await conn.run_sync(base.metadata.create_all)


@pytest.fixture(scope="function", autouse=True)
async def clean_tables() -> None:
    """
    Clean tables data before run test function
    """

    async with async_session_maker() as session:
        for table in base.metadata.sorted_tables:
            sanitized_table_name: ColumnClause = literal_column(table.name)
            stmt = text(f"TRUNCATE TABLE {sanitized_table_name} CASCADE")
            await session.execute(stmt)

        await session.commit()
