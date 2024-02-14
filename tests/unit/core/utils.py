from shared.infra.sqlalchemy_orm.utils.uow import utils


def set_repos(uow_instance) -> None:
    for attribute, repo_cls in utils.get_repos(uow_instance):
        setattr(uow_instance, attribute, utils.get_repo_instance(repo_cls))
