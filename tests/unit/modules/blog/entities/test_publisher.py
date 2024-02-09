from modules.blog.domain.entities.post import Post
from modules.blog.domain.entities.publisher import Publisher
from tests.unit.modules.blog.entities.conftest import make_publisher_and_post


def test_publish() -> None:
    publisher = Publisher(id=1, name="Vlad", city="Lersk")
    post = Post(id=1, title="Post 1", content="text")
    publisher.publish(post)
    assert post.publisher_id == 1


def test_to_draft() -> None:
    publisher, post = make_publisher_and_post()
    publisher.to_draft(post)
    assert post.draft is True


def test_from_draft() -> None:
    publisher, post = make_publisher_and_post()
    publisher.from_draft(post)
    assert post.draft is False


def test_edit() -> None:
    publisher, post = make_publisher_and_post()
    publisher.edit(post, content="new content", draft=True)

    assert post.content == "new content"
    assert post.draft is True
