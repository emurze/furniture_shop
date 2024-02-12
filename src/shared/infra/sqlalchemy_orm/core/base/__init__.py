from shared.infra.sqlalchemy_orm.core.base.config import PATH, FILENAME
from shared.infra.sqlalchemy_orm.core.base import import_contracts
from shared.infra.sqlalchemy_orm.core.base.base import Base


def get_base() -> Base:
    contracts = import_contracts.import_contracts(PATH, FILENAME)
    return Base(contracts)


__all__ = ("get_base",)
