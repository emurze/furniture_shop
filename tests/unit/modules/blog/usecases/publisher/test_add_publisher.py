from modules.blog.application.usecases.publisher.add_publisher import (
    AddPublisherUseCase,
)
from modules.blog.domain.entities.publisher import Publisher
from modules.blog.infra.repos.publisher.fake import PublisherFakeRepository


async def test_can_add_post() -> None:
    publisher = Publisher(id=2, name="Vlad", city="Lersk")
    repo = PublisherFakeRepository()

    use_case = AddPublisherUseCase(repo)
    use_case.add(publisher)

    retrieved_pub = await repo.get(id=2)
    assert publisher == retrieved_pub
