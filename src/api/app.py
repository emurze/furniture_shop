from fastapi import FastAPI

from api.routes.v1.posts.router import posts_router
from api.routes.v1.publishers.router import publishers_router

routes = (
    publishers_router,
    posts_router,
)


def get_app(_routes: tuple | list = routes) -> FastAPI:
    app = FastAPI(
        title="Sample",
    )

    for route in _routes:
        app.include_router(route)

    return app
