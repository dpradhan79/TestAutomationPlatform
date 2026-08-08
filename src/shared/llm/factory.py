from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from shared.llm.config import LLMConfig, get_llm_config


def _build_init_chat_model_kwargs(config: LLMConfig) -> dict[str, object]:
    kwargs = {
        "model": config.llm_model_name,
        "model_provider": config.llm_model_provider,
        "temperature": config.llm_model_temperature,
        "base_url": config.llm_base_url,
        "max_tokens": config.llm_model_max_tokens,
        "timeout": config.llm_model_timeout,
    }
    return {key: value for key, value in kwargs.items() if value is not None and not (key in ['timeout'] and value==0)}


def get_chat_model(
    config: LLMConfig | None = None,
) -> BaseChatModel:

    if config is None:
        config = get_llm_config()
    kwargs = _build_init_chat_model_kwargs(config)
    return init_chat_model(**kwargs)
