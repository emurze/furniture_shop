import logging

from api.config import app_config

LOG_FORMAT = "%(levelname)s  [%(module)s.%(funcName)s] %(message)s"


def configure_logging() -> None:
    log_level = str(app_config.log_level).upper()

    formatter = logging.Formatter(LOG_FORMAT)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logging.basicConfig(level=log_level, handlers=[handler])
