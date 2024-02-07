from collections.abc import Callable
from typing import Protocol, Optional

from sqlalchemy import MetaData


class Contract(Protocol):
    metadata: Optional[MetaData]
    mapper_runner: Optional[Callable]
