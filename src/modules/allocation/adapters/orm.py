from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.orm import registry

from modules.allocation.domain.models import OrderLine

mapper_registry = registry()

metadata = MetaData()

order_line_table = Table(
    "order_line",
    metadata,
    Column("order_ref", String, primary_key=True),
    Column("CKU", String),
    Column("quantity", Integer),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(
        OrderLine,
        order_line_table,
    )
