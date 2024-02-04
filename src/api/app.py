from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.config.base import config
from api.database import get_session
from modules.allocation.adapters.repository import Repository
from modules.allocation.services.service import Service

app = FastAPI(
    title=config.app.project_title,
)


@app.get("/")
async def root(session: AsyncSession = Depends(get_session)) -> str:
    repository = Repository(session=session)
    _ = Service(repository)
    return "Hello World!"
