from fastapi import APIRouter

from api.routes.v1.posts.schema import PostRead

posts_router = APIRouter(prefix="/blog", tags=["blog"])


@posts_router.get("/", response_model=list[PostRead])
def get_posts():
    return [{"id": 1, "title": "Post 1", "content": "1", "draft": False}]
