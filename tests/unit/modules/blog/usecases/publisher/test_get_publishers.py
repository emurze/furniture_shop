from modules.blog.application.usecases.publisher.get_publishers import (
    GetPublishersUseCase,
)
from modules.blog.domain.entities.publisher import Publisher
from tests.unit.fakes.publisher.repo import PublisherFakeRepository


async def test_return_publishers() -> None:
    pub1 = Publisher(id=1, name="Publisher 1", city="Lersk")
    pub2 = Publisher(id=2, name="Publisher 2", city="Lersk")
    repo = PublisherFakeRepository([pub1, pub2])

    use_case = GetPublishersUseCase(repo)
    pubs = await use_case.get_publishers()

    assert Publisher(id=1, name="Publisher 1", city="Lersk") in pubs
    assert Publisher(id=1, name="Publisher 1", city="Lersk") in pubs
