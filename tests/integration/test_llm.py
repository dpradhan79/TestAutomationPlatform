import pytest

from src.shared.llm.factory import get_chat_model


@pytest.mark.integration
@pytest.mark.skip(reason="Requires a running LLM endpoint; enable explicitly when live integration testing is desired.")
def test_llm_invoke_streaming():
    """
    Placeholder test for end-to-end LLM invocation via the factory-produced model.

    This test will verify that a model obtained through the LLM factory can
    successfully process a prompt and return a non-empty response. Implementation
    is deferred until the LLM factory and BaseChatModel integration are ready
    for runtime testing against the Ollama endpoint.
    """
    llm_model = get_chat_model()
    for chunk in llm_model.stream(input="Hello, can you summarize LangChain and how to use react agent in python tech stack for me?"):
        try:
            print(chunk.content, end='', flush=True)
            assert chunk.content is not None
        except Exception as e:
            print(f"Error invoking LLM model: {e}")
            assert False, f"LLM invocation failed with exception: {e}"

def test_llm_invoke():
    llm_model = get_chat_model()
    response = llm_model.invoke(input="Tell me something about you")
    print(response.content)
    assert response.content is not None
    assert response.content != ""
