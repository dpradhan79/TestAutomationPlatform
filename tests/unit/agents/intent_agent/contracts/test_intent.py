import pytest
from pydantic import ValidationError

from src.agents.intent_agent.contracts import Intent

@pytest.mark.intent_agent
@pytest.mark.unit
def test_intent_valid():
    intent = Intent(
        intent_no=1,
        intent="Open Salesforce homepage"
    )

    assert intent.intent_no == 1
    assert intent.intent == "Open Salesforce homepage"

@pytest.mark.intent_agent
@pytest.mark.unit
def test_intent_number_must_be_greater_than_zero():
    with pytest.raises(ValidationError):
        Intent(
            intent_no=0,
            intent="Open Salesforce homepage"
        )

@pytest.mark.intent_agent
@pytest.mark.unit
def test_intent_text_cannot_be_empty():
    with pytest.raises(ValidationError):
        Intent(
            intent_no=1,
            intent=""
        )

@pytest.mark.intent_agent
@pytest.mark.unit
def test_intent_missing_required_fields():
    with pytest.raises(ValidationError):
        Intent()