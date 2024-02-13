from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.domain.entities.publisher import Publisher
from shared.infra.sqlalchemy_orm.utils.repos.fake import FakeRepositoryMixin


class PublisherFakeRepository(
    FakeRepositoryMixin[Publisher],
    IPublisherRepository,
):
    async def get_with_posts(self, **kw) -> Publisher:
        ...
