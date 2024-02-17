from fastapi import APIRouter

from main.fastapi import BlogUOWDep
from modules.blog.application.dtos import publisher as dtos
from modules.blog.application.usecases import publisher as use_cases

publishers_router = APIRouter(prefix="/publishers", tags=["publishers"])


@publishers_router.get("/", response_model=list[dtos.PublisherGetDTO])
async def get_publishers(uow: BlogUOWDep):
    use_case = use_cases.GetPublishersUseCase(uow)
    publishers = await use_case.execute()
    return publishers


@publishers_router.get("/{publisher_id}", response_model=dtos.PublisherGetDTO)
async def get_publisher(publisher_id: int, uow: BlogUOWDep):
    use_case = use_cases.GetPublisherUseCase(uow)
    publisher = await use_case.execute(id=publisher_id)
    return publisher


@publishers_router.post("/", response_model=int)
async def add_publisher(dto: dtos.PublisherAddDTO, uow: BlogUOWDep):
    use_case = use_cases.AddPublisherUseCase(uow)
    publisher_id = await use_case.execute(dto)
    return publisher_id
