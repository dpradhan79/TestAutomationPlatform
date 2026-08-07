from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from src.shared.config.llm_config import LLMConfig, get_llm_config


def get_chat_model(
    config: LLMConfig | None = None,
) -> BaseChatModel:

    if config is None:
        llm_config = get_llm_config()

        config = LLMConfig(
            llm_model_provider=llm_config.llm_model_provider,
            llm_model_name=llm_config.llm_model_name,
            llm_model_temperature=llm_config.llm_model_temperature,
            llm_model_max_tokens=llm_config.llm_model_max_tokens
        )

    return init_chat_model(
        model=config.llm_model_name,
        model_provider=config.llm_model_provider,
        temperature=config.llm_model_temperature

    )