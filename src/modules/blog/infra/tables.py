import sqlalchemy as sa
from sqlalchemy.orm import registry, relationship

from modules.blog.domain.entities.post import Post
from modules.blog.domain.entities.publisher import Publisher

mapper_registry = registry()

post_table = sa.Table(
    "post",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(256)),
    sa.Column("content", sa.String),
    sa.Column(
        "publisher_id",
        sa.Integer,
        sa.ForeignKey("publisher.id", ondelete="CASCADE"),
    ),
    sa.Column("draft", sa.Boolean, default=False),
)

publisher_table = sa.Table(
    "publisher",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String),
    sa.Column("city", sa.String),
)


def start_mapper() -> None:
    mapper_registry.map_imperatively(
        Post,
        post_table,
        properties={
            "publisher": relationship(
                Publisher,
                back_populates="posts",
                innerjoin=True,
            )
        },
    )
    mapper_registry.map_imperatively(
        Publisher,
        publisher_table,
        properties={
            "posts": relationship(
                Post,
                back_populates="publisher",
            )
        },
    )
