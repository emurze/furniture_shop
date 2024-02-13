from collections.abc import Callable
from dataclasses import dataclass
from typing import Optional

from shared.infra.sqlalchemy_orm.core.contract.ports import MetaData


@dataclass(frozen=True, slots=True)
class DBContract:
    metadata: Optional[MetaData] = None
    mapper_runner: Optional[Callable] = None
