from fastapi import FastAPI

from api.routes.v1.posts.router import posts_router
from api.routes.v1.publishers.router import publishers_router

routes = (
    publishers_router,
    posts_router,
)


def set_routes(app: FastAPI, _routes: tuple | list = routes) -> None:
    for route in _routes:
        app.include_router(route)
