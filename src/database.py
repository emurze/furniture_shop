from sqlalchemy.ext.asyncio import create_async_engine

from config import config

async_engine = create_async_engine(
    config.db.get_dns(),
    echo=True,
)
