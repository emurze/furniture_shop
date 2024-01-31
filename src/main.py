import asyncio
import os
import sys
import queries.models

from fastapi import FastAPI

from config import config
from queries.core import Core
from database import async_engine
from queries.dbapi import DBAPIEngine, DBAPI

sys.path.insert(1, os.path.join(sys.path[0], '..'))  # add absolute imports

app = FastAPI(
    title='trading'
)


async def run_core() -> None:
    core = Core(async_engine)

    await core.create_tables()
    await core.insert_data()
    await core.update_data()
    await core.delete_data()
    await core.select_data()


async def run_dbapi() -> None:
    aengine = DBAPIEngine(config.db.get_dsn(driver="postgresql"))
    dbapi = DBAPI(aengine)

    await dbapi.create_tables()
    await dbapi.insert_data()
    await dbapi.select_data()

    # DROP TABLE role
    # CREATE TABLE role
    # INSERT INTO role
    # SELECT * FROM role
    # res=[<Record id=1 name='Hi'>,
    #      <Record id=2 name='Hello'>,
    #      <Record id=3 name='Hey'>]


async def main() -> None:
    await run_dbapi()


if __name__ == '__main__':
    asyncio.run(main())
