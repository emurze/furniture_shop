from typing import cast, Any

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from modules.blog.application.ports.repos.publisher import IPublisherRepository
from modules.blog.domain.entities.publisher import Publisher
from shared.infra.sqlalchemy_orm.utils import SQLAlchemyRepositoryMixin


class PublisherRepository(
    SQLAlchemyRepositoryMixin[Publisher],
    IPublisherRepository,
):
    model = Publisher

    async def get_with_posts(self, **kw) -> Publisher:
        publisher_posts = cast(Any, Publisher.posts)
        query = (
            select(Publisher)
            .options(selectinload(publisher_posts))
            .filter_by(**kw)
        )

        res = await self.session.execute(query)
        return res.scalars().one()
