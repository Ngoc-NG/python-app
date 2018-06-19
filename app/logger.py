import logging
from app.config import app_log_config_path, app_log_level
from logging.config import fileConfig

default_logger = logging.getLogger()
# override logger level from application.config
default_logger.setLevel(app_log_level)


def get_logger(name=None):
    if name:
        logger = logging.getLogger(name)
        # override logger level from application.config
        logger.setLevel(app_log_level)
        return logger
    else:
        return default_logger
