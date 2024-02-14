from modules.blog.application.ports.publisher.repo import IPublisherRepository
from modules.blog.domain.entities.publisher import Publisher
from tests.unit.core.repo import FakeRepositoryMixin


class PublisherFakeRepository(
    FakeRepositoryMixin[Publisher],
    IPublisherRepository,
):
    async def get_with_posts(self, **kw) -> Publisher:
        ...
