import inspect
from collections.abc import Iterator
from typing import Any

from shared.infra.sqlalchemy_orm.utils.uow.ports import IOpenedUnitOfWork


def get_repo_instance(repo_cls: type, *args) -> Any:
    return repo_cls(*args)


def set_repos(uow_instance: IOpenedUnitOfWork) -> None:
    for attribute, repo_cls in get_repos(uow_instance):
        setattr(
            uow_instance,
            attribute,
            get_repo_instance(repo_cls, uow_instance.session),
        )


def get_repos(uow_instance: IOpenedUnitOfWork) -> Iterator[tuple]:
    _annotations = inspect.get_annotations(uow_instance.__class__)
    yield from (
        (attr, annotation.__metadata__[0])
        for attr, annotation in _annotations.items()
        if annotation.__metadata__
    )
