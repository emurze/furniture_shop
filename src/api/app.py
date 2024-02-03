from fastapi import FastAPI, Depends
from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import AsyncSession

from api.config import config as c
from api.database import get_session
from modules.allocation.adapters.repository import Repository
from modules.allocation.services.service import Service

app = FastAPI(
    title=c.project_title,
)


@app.get('/')
async def root(session: AsyncSession = Depends(get_session)) -> Response:
    repository = Repository(session=session)
    service = Service(repository)
    return Response()
