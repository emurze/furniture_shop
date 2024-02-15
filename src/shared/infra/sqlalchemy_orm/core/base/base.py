from collections.abc import Iterable

from shared.infra.sqlalchemy_orm.core.base.ports import Contract
from shared.infra.sqlalchemy_orm.core.ports import MetaData
from shared.infra.sqlalchemy_orm.utils.helpers import combine_metadata


class Base:
    metadata: MetaData

    def __init__(self, contracts: Iterable[Contract]) -> None:
        self.metadata = combine_metadata(c.metadata for c in contracts)
        self.mappers = [c.mapper_runner for c in contracts]

    def run_mappers(self) -> None:
        for mapper in self.mappers:
            mapper()
