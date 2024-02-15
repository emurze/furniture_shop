import copy
from collections.abc import Iterator
from typing import Any

from shared.infra.sqlalchemy_orm.utils.uow import IBaseUnitOfWork
from tests.unit.core.utils import set_repos


class BaseFakeUnitOfWork(IBaseUnitOfWork):
    def __init__(self) -> None:
        self._suppress_rollback = False
        self._first = True
        self._last_state: list[tuple[Any, set]] = []

    async def __aenter__(self) -> None:
        """
        Set up repositories one time
        """

        if self._first:
            set_repos(self)
            self._last_state = [(repo, set()) for name, repo in self._repos]
            self._first = False

    async def __aexit__(self, *args) -> None:
        """
        Default rollback, but if commit then suppress it
        """

        if self._suppress_rollback:
            self._suppress_rollback = False
        else:
            await self.rollback()

    async def commit(self) -> None:
        """
        Accepts a new updated state on the repositories
        """

        self._last_state = [
            (repo, set(await repo.list())) for name, repo in self._repos
        ]
        self._suppress_rollback = True

    async def rollback(self) -> None:
        """
        Rollbacks the repositories to the last state
        """

        for repo, models in self._last_state:
            repo._models = copy.deepcopy(models)

    @property
    def _repos(self) -> Iterator[tuple[str, Any]]:
        """
        Retrieves repositories from all public attributes
        """

        yield from (
            (repo_name, getattr(self, repo_name))
            for repo_name in vars(self)
            if not repo_name.startswith("_")
        )
