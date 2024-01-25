from fastapi import FastAPI
from sqlalchemy import text

from config import settings
from database import async_engine

app = FastAPI(
    title='Trading',
)


@app.get('/')
async def main() -> None:
    print(settings)

    # async with async_engine.connect() as conn:
    #     await conn.begin()
    #
    #     print(await conn.get_isolation_level())
    #
    #     query = text("SELECT 1 as lerka, 2 as vlad, 3 as borya;")
    #     result = await conn.execute(query)
    #
    #     for row in result:
    #         print(row.lerka, row.vlad)
    #
    #     await conn.commit()
