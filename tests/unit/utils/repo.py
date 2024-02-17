import copy
from collections.abc import Sequence, Callable
from typing import Any as Model

from shared.infra.sqlalchemy_orm.utils.repos.port import IBaseRepository


class FakeRepositoryMixin(IBaseRepository):
    """
    field_gens is mapped triggers
    """

    field_gens: dict[str, Callable]
    model: type[Model]

    def __init__(self, models: Sequence[dict] | None = None) -> None:
        if models is None:
            self._models = []
        else:
            self._models = list(self.model(**kw) for kw in models)

        self._init_gens()

    async def add(self, **kw) -> int:
        """
        Appends item created from kwargs to storage
        """

        kw_gen_values = self._run_triggers(kw)
        instance = self.model(**kw_gen_values)

        self._models.append(instance)

        return instance.id

    async def get(self, **kw) -> Model:
        """
        Retrieves one item from models
        """

        return next(
            post
            for post in self._models
            for k, v in kw.items()
            if getattr(post, k) == v
        )

    async def list(self) -> list[Model]:
        return self._models

    def _run_triggers(self, kw: dict) -> dict:
        """
        Runs triggers to add generated fields and their corresponding values
        into a new kwargs
        """

        new_kw = copy.deepcopy(kw)

        for field, gen in self._field_gens.items():
            if not new_kw.get(field):
                new_kw[field] = next(gen)

        return new_kw

    def _init_gens(self) -> None:
        """
        Copies triggers to produce independent generators for each instance
        """

        _field_gens = copy.deepcopy(self.field_gens)

        for field, gen in _field_gens.items():
            _field_gens[field] = gen()

        self._field_gens: dict = _field_gens
