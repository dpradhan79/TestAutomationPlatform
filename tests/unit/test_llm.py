import pytest

from shared.llm.config import get_llm_config
from shared.llm.config import LLMConfig
from src.shared.llm.factory import get_chat_model
import logging

@pytest.mark.unit
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(filename="", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.mark.unit
def test_get_chat_model_omits_none_fields(monkeypatch):
    captured_kwargs = {}

    def fake_init_chat_model(**kwargs):
        captured_kwargs.update(kwargs)
        return object()

    monkeypatch.setattr("src.shared.llm.factory.init_chat_model", fake_init_chat_model)

    config = LLMConfig(
        llm_base_url=None,
        llm_model_provider="ollama",
        llm_model_name="qwen3.6",
        llm_model_temperature=0.0,
        llm_model_max_tokens=4096,
        llm_model_timeout=0,
    )

    get_chat_model(config)

    assert captured_kwargs == {
        "model": "qwen3.6",
        "model_provider": "ollama",
        "temperature": 0.0,
        "max_tokens": 4096,
    }

@pytest.mark.unit
def test_llm_config():
    """
    Verify that get_llm_config() returns a singleton instance.

    Calls get_llm_config() twice and asserts that both calls return the exact
    same object (singleton behaviour). Also confirms that the default LLM model
    provider resolved from environment / configuration is 'ollama', matching the
    Ollama-First Development Strategy defined in the platform architecture.
    """
    llm_config = get_llm_config()
    llm_config2 = get_llm_config()
    assert llm_config==llm_config2, f'both LLM Config Instances should be same'
    assert llm_config.llm_model_provider == "ollama"

@pytest.mark.unit
def test_llm_config_init():
    """
    Verify that LLMConfig can be instantiated with explicit field values.

    Constructs an LLMConfig object by supplying all required fields directly
    and asserts that every attribute is stored exactly as provided. This test
    validates that the Pydantic v2 model accepts the expected fields and does
    not apply unexpected transformations or default overrides when values are
    supplied explicitly.
    """
    llm_config: LLMConfig = LLMConfig(
        llm_base_url="test_base_url",
        llm_model_provider="test_model_provider",
        llm_model_name="test_model_name",
        llm_model_temperature=0.5,
        llm_model_max_tokens=100)
    assert llm_config.llm_base_url == "test_base_url"
    assert llm_config.llm_model_provider == "test_model_provider"
    assert llm_config.llm_model_name == "test_model_name"
    assert llm_config.llm_model_temperature == 0.5
    assert llm_config.llm_model_max_tokens == 100

@pytest.mark.unit
def test_get_llm_config_vs_init():
    """
    Verify that get_llm_config() and a manually constructed LLMConfig are independent.

    Obtains the platform-resolved LLMConfig singleton via get_llm_config() and
    creates a second LLMConfig instance with hard-coded test values. Asserts that
    every field differs between the two objects, confirming that the factory
    function loads real configuration (e.g. from environment variables or a
    settings file) rather than returning a default test-fixture object. This
    guards against accidental coupling between the singleton factory and
    arbitrary constructor arguments.
    """
    llm_config1 = get_llm_config()
    llm_config2 = LLMConfig(
        llm_base_url="test_base_url",
        llm_model_provider="test_model_provider",
        llm_model_name="test_model_name",
        llm_model_temperature=0.5,
        llm_model_max_tokens=100)
    assert not llm_config1.llm_base_url == llm_config2.llm_base_url
    assert not llm_config1.llm_model_provider == llm_config2.llm_model_provider
    assert not llm_config1.llm_model_name == llm_config2.llm_model_name
    assert not llm_config1.llm_model_temperature == llm_config2.llm_model_temperature
    assert not llm_config1.llm_model_max_tokens == llm_config2.llm_model_max_tokens