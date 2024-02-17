from sqlalchemy import select

from sqlalchemy.orm import joinedload

from modules.blog.application.ports.repos.post import IPostRepository
from modules.blog.domain.entities.post import Post
from shared.infra.sqlalchemy_orm.repo import SQLAlchemyRepositoryMixin


class PostRepository(SQLAlchemyRepositoryMixin, IPostRepository):
    model = Post

    async def get_with_publisher(self, **kw) -> Post:
        query = (
            select(Post).options(joinedload(Post.publisher)).filter_by(**kw)
        )
        post = await self.session.execute(query)
        return post.scalars().one()
