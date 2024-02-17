from modules.blog.application.dtos import publisher as dtos
from modules.blog.application.dtos.publisher import PublisherGetDTO
from modules.blog.application.ports.uow import IBlogUnitOfWork
from tests.unit.blog.usecases.conftest import make_publisher, publisher_data
from modules.blog.application.usecases import publisher as use_cases


async def test_add_publisher(uow: IBlogUnitOfWork) -> None:
    _id = await make_publisher(uow)
    assert _id == 1


async def test_get_publisher(uow: IBlogUnitOfWork) -> None:
    await make_publisher(uow)
    use_case = use_cases.GetPublisherUseCase(uow)
    publisher = await use_case.execute(id=1)

    assert publisher == PublisherGetDTO(**({"id": 1} | publisher_data))


async def test_get_publishers(uow: IBlogUnitOfWork) -> None:
    await make_publisher(uow)
    await make_publisher(uow)

    use_case = use_cases.GetPublishersUseCase(uow)
    posts = await use_case.execute()

    assert posts == [
        dtos.PublisherGetDTO(**({"id": 1} | publisher_data)),
        dtos.PublisherGetDTO(**({"id": 2} | publisher_data)),
    ]
