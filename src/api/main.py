from api.app import get_app
from api.logging_conf import configure_logging
from shared.infra.sqlalchemy_orm.base import base

configure_logging()
base.run_mappers()
app = get_app()
