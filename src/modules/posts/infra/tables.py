from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table
from sqlalchemy.orm import registry

from modules.posts.domain.models import Post

metadata = MetaData()
mapped_registry = registry()

post_table = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(256)),
    Column("content", String),
    Column("draft", Boolean, default=False),
)


def start_mapper() -> None:
    mapped_registry.map_imperatively(Post, post_table)
