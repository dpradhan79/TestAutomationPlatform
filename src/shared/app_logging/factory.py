import logging
import sys

from src.shared.app_logging.config import AppLogging


def init_logger(app_logging: AppLogging | None = None) -> logging.Logger:
    if app_logging is None:
        app_logging = AppLogging()

    app_logging.log_file.parent.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    if root_logger.handlers:
        root_logger.handlers.clear()

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

    root_logger.addHandler(stdout_handler)
    root_logger.addHandler(file_handler)

    return root_logger

