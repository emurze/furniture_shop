from modules.blog.application.dtos.post import PostAddDTO
from modules.blog.application.dtos.publisher import PublisherAddDTO
from modules.blog.application.usecases import post as post_use_cases
from modules.blog.application.usecases import publisher as pub_use_cases

publisher_data = {
    "name": "Publisher 1",
    "city": "Lersk",
}
post_data = {
    "title": "Post 1",
    "content": "",
    "publisher_id": 1,
    "draft": False,
}


async def make_publisher(uow) -> int:
    dto = PublisherAddDTO(name="Publisher 1", city="Lersk")
    use_case = pub_use_cases.AddPublisherUseCase(uow)
    publisher_id = await use_case.execute(dto)
    return publisher_id


async def make_post(uow) -> int:
    dto = PostAddDTO(**post_data)
    use_case = post_use_cases.AddPostUseCase(uow)
    post_id = await use_case.execute(dto)
    return post_id
