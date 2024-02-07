from modules.posts.infra.tables import metadata, start_mapper
from shared.infra.sqlalchemy_orm import DBContract

contract = DBContract(
    metadata=metadata,
    mapper_runner=start_mapper,
)
