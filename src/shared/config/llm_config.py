from functools import lru_cache

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class LLMConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    llm_model_provider: str = Field(default="ollama")
    llm_model_name: str = Field(default="qwen3")
    llm_model_temperature: float = Field(default=0.0)
    llm_model_max_tokens: int = Field(default=4096)


@lru_cache
def get_llm_config() -> LLMConfig:
    return LLMConfig()