import inspect

from collections.abc import Iterator
from typing import Any

from shared.application.uow.ports import IOpenedUnitOfWork


def set_repos(uow_instance: IOpenedUnitOfWork) -> None:
    for attribute, repo_cls in _get_repos(uow_instance):
        setattr(
            uow_instance,
            attribute,
            _get_repo_instance(repo_cls, uow_instance.session),
        )


def _get_repo_instance(repo_cls: type, *args) -> Any:
    return repo_cls(*args)


def _get_repos(uow_instance: IOpenedUnitOfWork) -> Iterator[tuple[str, Any]]:
    yield from (
        (attr_name, getattr(uow_instance, "_repos").get(attr_name))
        for attr_name, annotation in inspect.get_annotations(
            uow_instance.__class__
        ).items()
        if annotation.__name__ in ("Type", "type")
    )
