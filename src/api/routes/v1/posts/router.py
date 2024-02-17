from fastapi import APIRouter

from main.fastapi import BlogUOWDep
from modules.blog.application.dtos.post import PostAddDTO, PostGetDTO
from modules.blog.application.usecases import post as use_cases

posts_router = APIRouter(prefix="/posts", tags=["posts"])


@posts_router.get("/", response_model=list[PostGetDTO])
async def get_posts(uow: BlogUOWDep):
    use_case = use_cases.GetPostsUseCase(uow)
    posts = await use_case.execute()
    return posts


@posts_router.get("/{post_id}", response_model=PostGetDTO)
async def get_post(post_id: int, uow: BlogUOWDep):
    use_case = use_cases.GetPostUseCase(uow)
    post = await use_case.execute(id=post_id)
    return post


@posts_router.post("/", response_model=int)
async def add_post(dto: PostAddDTO, uow: BlogUOWDep):
    use_case = use_cases.AddPostUseCase(uow)
    post_id = await use_case.execute(dto)
    return post_id
