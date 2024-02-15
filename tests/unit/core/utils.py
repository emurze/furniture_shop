import inspect
from collections.abc import Iterator
from typing import Any


def set_repos(uow_instance) -> None:
    for attribute, repo_cls in _get_repos(uow_instance):
        setattr(uow_instance, attribute, _get_repo_instance(repo_cls))


def _get_repo_instance(repo_cls: type, *args) -> Any:
    return repo_cls(*args)


def _get_repos(uow_instance) -> Iterator[tuple]:
    _annotations = inspect.get_annotations(uow_instance.__class__)
    yield from (
        (attr, annotation.__metadata__[0])
        for attr, annotation in _annotations.items()
        if annotation.__metadata__
    )
