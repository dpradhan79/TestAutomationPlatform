import logging
import sys
from src.shared.logging.config import get_logging_config


def init_logger():
    """Initialize the root logger with a stream handler and a file handler.

    Attaches handlers to the root logger so that all module-level loggers
    (e.g. ``shared.llm.factory``) propagate their records here automatically.
    Using a named application logger instead of the root logger would create a
    separate hierarchy that never receives records from ``logging.getLogger(__name__)``
    calls in submodules.
    """
    app_logging = get_logging_config()
    logger = logging.getLogger(app_logging.log_app_name)          # root logger — parent of every module logger
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter(
        fmt=app_logging.log_format,
        datefmt=app_logging.log_date_format,
    )

    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        filename=app_logging.log_file,
        mode=app_logging.log_file_mode,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)
