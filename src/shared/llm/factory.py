import logging
from functools import lru_cache

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

from shared.llm.config import LLMConfig, get_llm_config
logger = logging.getLogger(__name__)

def _build_init_chat_model_kwargs(config: LLMConfig) -> dict[str, object]:
    """Build keyword arguments for `init_chat_model()` from an `LLMConfig`."""
    kwargs = {
        "model": config.llm_model_name,
        "model_provider": config.llm_model_provider,
        "temperature": config.llm_model_temperature,
        "base_url": config.llm_base_url,
        "max_tokens": config.llm_model_max_tokens,
        "timeout": config.llm_model_timeout,
    }
    return {key: value for key, value in kwargs.items() if value is not None and not (key in ['timeout'] and value==0)}


@lru_cache(maxsize=32)
def _create_cached_chat_model(
    init_kwargs_items: tuple[tuple[str, object], ...],
) -> BaseChatModel:
    """Create and cache a chat model for the provided init kwargs."""
    kwargs = dict(init_kwargs_items)
    logger.debug("Creating new chat model with kwargs: %s", kwargs)
    return init_chat_model(**kwargs)


def clear_chat_model_cache() -> None:
    """Clear cached chat models; used by tests and optional runtime refresh flows."""
    _create_cached_chat_model.cache_clear()


def get_chat_model(
    config: LLMConfig | None = None,
) -> BaseChatModel:
    """Return a cached chat model for the active or provided configuration."""

    if config is None:
        config = get_llm_config()

    # Build a stable, hashable cache key from the init kwargs.
    init_kwargs = _build_init_chat_model_kwargs(config)
    init_kwargs_items = tuple((k, v) for k, v in init_kwargs.items())

    chat_model = _create_cached_chat_model(init_kwargs_items)
    return chat_model
