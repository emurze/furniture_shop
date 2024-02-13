from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from modules.blog.application.dtos.publisher import AddPublisherDTO
from modules.blog.application.usecases.publisher.add_publisher import (
    AddPublisherUseCase,
)
from modules.blog.domain.entities.publisher import Publisher
from modules.blog.infra.repos.publisher.sqlalchemy import PublisherRepository
from shared.infra.sqlalchemy_orm.db import get_session

publishers_router = APIRouter(prefix="/publishers", tags=["publishers"])


@publishers_router.post("/")
async def add_publisher(
    dto: AddPublisherDTO,
    session: AsyncSession = Depends(get_session),
) -> None:
    publisher = Publisher(
        id=dto.id,
        name=dto.name,
        city=dto.city,
    )
    repo = PublisherRepository(session)
    use_case = AddPublisherUseCase(repo)
    use_case.add(publisher)
    await session.commit()
