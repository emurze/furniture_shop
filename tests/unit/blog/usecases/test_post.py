from modules.blog.application.dtos.post import PostGetDTO
from modules.blog.application.ports.uow import IBlogUnitOfWork
from modules.blog.application.usecases import post as use_cases
from tests.unit.blog.usecases.conftest import make_post, post_data


async def test_add_post(uow: IBlogUnitOfWork) -> None:
    post_id = await make_post(uow)
    assert post_id == 1


async def test_get_post(uow: IBlogUnitOfWork) -> None:
    await make_post(uow)
    use_case = use_cases.GetPostUseCase(uow)
    post = await use_case.execute(id=1)

    assert post == PostGetDTO(**({"id": 1} | post_data))


async def test_get_posts(uow: IBlogUnitOfWork) -> None:
    await make_post(uow)
    await make_post(uow)

    use_case = use_cases.GetPostsUseCase(uow)
    posts = await use_case.execute()

    assert posts == [
        PostGetDTO(**({"id": 1} | post_data)),
        PostGetDTO(**({"id": 2} | post_data)),
    ]
