from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.usecases.publisher.add_publisher import (
    AddPublisherUseCase,
)
from modules.blog.domain.entities.publisher import Publisher


async def test_can_add_post(uow: IBlogUnitOfWork) -> None:
    publisher = Publisher(id=2, name="Vlad", city="Lersk")

    use_case = AddPublisherUseCase(uow)
    await use_case.add(publisher)

    retrieved_pub = await uow.publishers.get(id=2)
    assert publisher == retrieved_pub
