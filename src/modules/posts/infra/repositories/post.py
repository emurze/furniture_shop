from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from modules.posts.application.ports import IPostRepository
from modules.posts.domain.models import Post


@dataclass(frozen=True, slots=True)
class PostRepository(IPostRepository):
    session: AsyncSession

    def add(self, obj: Post) -> None:
        self.session.add(obj)

    async def get(self, **kw) -> Post:
        query = select(Post).filter_by(**kw)
        res = await self.session.execute(query)
        return res.scalars().one()

    async def list(self) -> tuple[Post, ...]:
        res = await self.session.execute(select(Post))
        return tuple(res.scalars().all())
