import logging
from pathlib import Path

from anyio.functools import lru_cache
from pydantic_settings import BaseSettings


class AppLogging(BaseSettings):
    """
    Logging configuration settings.

    This class defines the configuration settings for logging in the application.
    It uses Pydantic's BaseSettings to allow loading settings from environment
    variables or a .env file.

    Attributes:
        log_level (str): The logging level (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").
        log_format (str): The format of the log messages.
        log_file (str): The file path for logging output. If None, logs will be printed to stdout.
    """
    log_app_name: str = Path(__file__).resolve().parents[3].stem
    log_level: int = logging.DEBUG
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_date_format: str = "%a, %d %b %Y %H:%M:%S"
    log_file: Path = Path(__file__).resolve().parents[3] / "logs" / f"{log_app_name}.log"
    log_file_mode: str = "w"
@lru_cache
def get_app_logging() -> AppLogging:
    return AppLogging()