from src.shared.config.llm_config import get_llm_config

def test_llm_config():
    llm_config = get_llm_config()
    assert llm_config.llm_model_provider == "ollama"
    # assert settings.llm_config.model == "qwen3"
    # assert settings.llm_config.temperature == 0.1
    #assert settings.model_max_tokens==2048