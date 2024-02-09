from sqlalchemy import select
from sqlalchemy.orm import joinedload

from modules.blog.application.ports.repos.post import IPostRepository
from modules.blog.domain.entities.post import Post
from shared.infra.sqlalchemy_orm.utils import SQLAlchemyRepositoryMixin


class PostRepository(SQLAlchemyRepositoryMixin[Post], IPostRepository):
    model = Post

    async def get_with_publisher(self) -> Post:
        query = select(Post).options(joinedload(Post.publisher))
        post = await self.session.execute(query)
        return post.unique().scalars().one()
