from shared.infra.sqlalchemy_orm.common.base import Base
from shared.infra.sqlalchemy_orm.utils.import_contracts import import_contracts
from shared.infra.sqlalchemy_orm.config.base import PATH, FILENAME

contracts = import_contracts(PATH, FILENAME)

base = Base(contracts)
