from tests.data.domain import PublisherModel, PostModel


def make_publisher_and_post() -> tuple[PublisherModel, PostModel]:
    pub = PublisherModel(id=1, name="Vlad", city="Lersk")
    post = PostModel(id=1, title="Post 1", content="text", publisher_id=pub.id)
    return pub, post
