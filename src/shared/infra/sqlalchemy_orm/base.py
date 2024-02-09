from shared.infra.sqlalchemy_orm.core.base import Base
from shared.infra.sqlalchemy_orm.core import import_contracts
from shared.infra.sqlalchemy_orm.config.base import PATH, FILENAME

contracts = import_contracts.import_contracts(PATH, FILENAME)

base = Base(contracts)
