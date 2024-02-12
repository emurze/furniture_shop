import logging

from fastapi import FastAPI

from api.logging_conf import configure_logging
from api.routes.v1.posts.router import posts_router
from shared.infra.sqlalchemy_orm.base import base

configure_logging()
base.run_mappers()

app = FastAPI(
    title="Sample",
)
app.include_router(posts_router)


lg = logging.getLogger(__name__)


@app.get("/")
async def root() -> None:
    lg.info(base.metadata.tables)


# @app.on_event("startup")
