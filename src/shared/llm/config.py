import logging
from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


logger = logging.getLogger(__name__)

class LLMConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    llm_base_url: Optional[str] = Field(default=None)
    llm_model_provider: Optional[str] = Field(default="ollama")
    llm_model_name: str = Field(default="gpt-oss:20b")
    llm_model_temperature: Optional[float] = Field(default=0.0)
    llm_model_max_tokens: Optional[int] = Field(default=4096)
    llm_model_timeout: Optional[int]= Field(default=30)


@lru_cache
def get_llm_config() -> LLMConfig:
    msg = f'Loading LLMConfig from environment variables...default variables are returned as fallback'
    logger.info(msg)
    return LLMConfig()