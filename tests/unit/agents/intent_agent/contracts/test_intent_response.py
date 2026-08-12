import pytest

from src.agents.intent_agent.contracts import (
    Intent,
    IntentResponse,
)

@pytest.mark.contract
@pytest.mark.unit
def test_intent_response_with_single_intent():
    response = IntentResponse(
        intents=[
            Intent(
                intent_no=1,
                intent="Open Salesforce homepage"
            )
        ]
    )

    assert len(response.intents) == 1
    assert response.intents[0].intent_no == 1

@pytest.mark.contract
@pytest.mark.unit
def test_intent_response_with_multiple_intents():
    response = IntentResponse(
        intents=[
            Intent(
                intent_no=1,
                intent="Open Salesforce homepage"
            ),
            Intent(
                intent_no=2,
                intent="Click Login button"
            ),
        ]
    )

    assert len(response.intents) == 2

@pytest.mark.contract
@pytest.mark.unit
def test_intent_response_empty_list():
    response = IntentResponse()

    assert response.intents == []