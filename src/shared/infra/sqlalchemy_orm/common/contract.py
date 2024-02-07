from collections.abc import Callable
from dataclasses import dataclass
from typing import Optional

from sqlalchemy import MetaData


@dataclass(frozen=True, slots=True)
class DBContract:
    metadata: Optional[MetaData] = None
    mapper_runner: Optional[Callable] = None
