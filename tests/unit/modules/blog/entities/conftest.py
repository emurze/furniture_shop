from modules.blog.domain.entities.post import Post
from modules.blog.domain.entities.publisher import Publisher


def make_publisher_and_post() -> tuple[Publisher, Post]:
    pub = Publisher(id=1, name="Vlad", city="Lersk")
    post = Post(id=1, title="Post 1", content="text", publisher_id=pub.id)
    return pub, post
