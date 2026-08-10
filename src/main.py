import logging

from src.shared.logging.config import get_logging_config
from src.shared.logging.factory import init_logger
from src.shared.llm.factory import get_chat_model

init_logger()
logger = logging.getLogger(get_logging_config().log_app_name)
logger.info("Starting main.py")
llm_model = get_chat_model()
response = llm_model.invoke(input="Tell me something about you")
print(response.content)
logger.info("Finished main.py")