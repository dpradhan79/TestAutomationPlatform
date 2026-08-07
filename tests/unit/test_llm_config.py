from src.shared.config.llm_config import get_llm_config

def test_llm_config():
    llm_config = get_llm_config()
    llm_config2 = get_llm_config()
    assert llm_config==llm_config2, f'both LLM Config Instances should be same'
    assert llm_config.llm_model_provider == "ollama"
