import pytest
from pydantic import ValidationError

from src.agents.intent_agent.contracts import Requirement

@pytest.mark.contract
@pytest.mark.unit
def test_requirement_valid():
    requirement = Requirement(
        requirement="Login to Salesforce application"
    )

    assert requirement.requirement == "Login to Salesforce application"

@pytest.mark.contract
@pytest.mark.unit
def test_requirement_empty_string():
    with pytest.raises(ValidationError):
        Requirement(
            requirement=""
        )

@pytest.mark.contract
@pytest.mark.unit
def test_requirement_missing_field():
    with pytest.raises(ValidationError):
        Requirement()

@pytest.mark.contract
@pytest.mark.unit
def test_validate_schema():
    requirement = Requirement(
        requirement="Login to Salesforce application"
    )
    obj_req: Requirement = Requirement.model_validate(requirement)
    assert obj_req.requirement == "Login to Salesforce application", f'Requirement Does not match'

