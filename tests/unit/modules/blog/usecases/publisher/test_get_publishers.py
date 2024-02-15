from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.usecases.publisher.get_publishers import (
    GetPublishersUseCase,
)
from modules.blog.domain.entities.publisher import Publisher


async def test_return_publishers(uow: IBlogUnitOfWork) -> None:
    pub1 = Publisher(id=1, name="Publisher 1", city="Lersk")
    pub2 = Publisher(id=2, name="Publisher 2", city="Lersk")
    async with uow:
        uow.publishers.add(pub1)
        uow.publishers.add(pub2)
        await uow.commit()

    use_case = GetPublishersUseCase(uow)
    pubs = await use_case.get_publishers()

    assert Publisher(id=1, name="Publisher 1", city="Lersk") in pubs
    assert Publisher(id=1, name="Publisher 1", city="Lersk") in pubs
