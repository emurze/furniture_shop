import asyncio
import os
import sys

from fastapi import FastAPI

from core.orm import create_tables, insert_data
from database import async_session, async_engine

sys.path.insert(1, os.path.join(sys.path[0], '..'))  # add absolute imports

app = FastAPI(
    title='trading'
)


async def main():
    await create_tables(async_engine)
    await insert_data(async_session)


if __name__ == '__main__':
    asyncio.run(main())
