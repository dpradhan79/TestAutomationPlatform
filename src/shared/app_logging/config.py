import logging
from pathlib import Path

from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings


class _AppLogging(BaseSettings):

    """
    Logging configuration settings.

    This class defines the configuration settings for logging in the application.
    It uses Pydantic's BaseSettings to allow loading settings from environment
    variables or a .env file.

    Attributes:
        log_app_name (str): The name of the application for logging purposes.
        log_level (int): The logging level (e.g., logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL).
        log_format (str): The format of the log messages.
        log_date_format (str): The format of the date in log messages.
        log_file (Path): The file path for logging output. If None, logs will be printed to stdout.
        log_file_mode (str): The mode in which the log file is opened (e.g., "w" for write, "a" for append).
    """
    log_app_name: str = Path(__file__).resolve().parents[3].stem
    log_level: int = logging.DEBUG
    log_format: str = "%(asctime)s - %(name)s - %(module)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"
    log_date_format: str = "%a, %d %b %Y %H:%M:%S"
    log_file: Path = Path(__file__).resolve().parents[3] / "logs" / f"{log_app_name}.log"
    log_file_mode: str = "w"

    def model_post_init(self, context: Any, /) -> None:
        """
        Post-initialization method for the model.

        This method is called after the model is initialized. It can be used to perform
        additional setup or validation of the model's attributes.

        Args:
            context (Any): The context in which the model is being initialized.
        """
        log_file_dir = self.log_file.parent
        log_file_dir.mkdir(parents=True, exist_ok=True)

@lru_cache
def get_app_logging() -> _AppLogging:
    return _AppLogging()