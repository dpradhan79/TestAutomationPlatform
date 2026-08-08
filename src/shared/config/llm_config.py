from functools import lru_cache
from typing import Optional

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class LLMConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    llm_base_url: Optional[str] = Field(default=None)
    llm_model_provider: Optional[str] = Field(default="ollama")
    llm_model_name: str = Field(default="qwen3")
    llm_model_temperature: Optional[float] = Field(default=0.0)
    llm_model_max_tokens: Optional[int] = Field(default=4096)


@lru_cache
def get_llm_config() -> LLMConfig:
    print(f'Loading LLMConfig from environment variables...default variables are returned as fallback')
    return LLMConfig()