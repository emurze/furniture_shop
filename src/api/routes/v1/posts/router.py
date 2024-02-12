from fastapi import APIRouter

from modules.blog.application.dtos.post import PostRead

posts_router = APIRouter(prefix="/blog", tags=["blog"])


@posts_router.get("/", response_model=list[PostRead])
def get_posts():
    return [{"id": 1, "title": "Post 1", "content": "1", "draft": False}]
