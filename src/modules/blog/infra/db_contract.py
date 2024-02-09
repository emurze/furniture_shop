from modules.blog.infra.tables import start_mapper, mapper_registry
from shared.infra.sqlalchemy_orm import DBContract

contract = DBContract(
    metadata=mapper_registry.metadata,
    mapper_runner=start_mapper,
)
