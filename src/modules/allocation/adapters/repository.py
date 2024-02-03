from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass(frozen=True, slots=True)
class Repository:
    session: AsyncSession
