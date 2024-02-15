from fastapi import APIRouter

from main.fastapi import BlogUOWDep
from modules.blog.application.dtos.publisher import AddPublisherDTO
from modules.blog.application.usecases.publisher.add_publisher import (
    AddPublisherUseCase,
)
from modules.blog.application.usecases.publisher.get_publishers import (
    GetPublishersUseCase,
)
from modules.blog.domain.entities.publisher import Publisher

publishers_router = APIRouter(prefix="/publishers", tags=["publishers"])


@publishers_router.get("/", response_model=tuple[Publisher, ...])
async def get_publishers(uow: BlogUOWDep):
    use_case = GetPublishersUseCase(uow)
    publishers = await use_case.get_publishers()
    return publishers


@publishers_router.post("/")
async def add_publisher(dto: AddPublisherDTO, uow: BlogUOWDep) -> None:
    publisher = Publisher(
        id=dto.id,
        name=dto.name,
        city=dto.city,
    )
    use_case = AddPublisherUseCase(uow)
    await use_case.add(publisher)
