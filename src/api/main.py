from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from api.logging_conf import configure_logging
from api.routing import set_routes
from shared.infra.sqlalchemy_orm.base import base

configure_logging()


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    base.run_mappers()
    yield


app = FastAPI(
    title="Sample",
    lifespan=lifespan,
)
set_routes(app)
