import logging
from app.config import settings


def get_logger(name: str):

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(settings.LOG_LEVEL)

    return logger
