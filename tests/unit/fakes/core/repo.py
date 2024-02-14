from collections.abc import Sequence
from typing import TypeVar

from shared.infra.sqlalchemy_orm.utils.repos.port import IBaseRepository

TP = TypeVar("TP")


class FakeRepositoryMixin(IBaseRepository[TP]):
    def __init__(self, models: Sequence[TP] | None = None) -> None:
        if models is None:
            self._models = set()
        else:
            self._models = set(models)

    def add(self, obj: TP) -> None:
        self._models.add(obj)

    async def get(self, **kw) -> TP:
        return next(
            post
            for post in self._models
            for k, v in kw.items()
            if getattr(post, k) == v
        )

    async def list(self) -> tuple[TP, ...]:
        return tuple(self._models)
