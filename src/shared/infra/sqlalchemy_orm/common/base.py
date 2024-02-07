from collections.abc import Iterable

from sqlalchemy import MetaData

from shared.infra.sqlalchemy_orm.common.ports import Contract
from shared.utils.combine_metadata import combine_metadata


class Base:
    metadata: MetaData

    def __init__(self, contracts: Iterable[Contract]) -> None:
        self.metadata = combine_metadata(c.metadata for c in contracts)
        self.mappers = [c.mapper_runner for c in contracts]

    def run_mappers(self) -> None:
        for mapper in self.mappers:
            mapper()
