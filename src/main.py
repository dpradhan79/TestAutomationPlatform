import logging

from src.shared.logging import get_logging_config
from src.shared.logging.factory import init_logger
import uvicorn
from src.api.app import app

init_logger()
logger = logging.getLogger(get_logging_config().log_app_name)

if __name__ == "__main__":

    logger.info("Starting main.py")
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="debug"
    )
    logger.info("Finished main.py")