from pathlib import Path

import pytest

from src.agents.intent_agent import IntentAgent
from src.agents.intent_agent.contracts import (
    Requirement,
    IntentResponse,
)


@pytest.mark.intent_agent
@pytest.mark.integration
@pytest.mark.asyncio
async def test_intent_agent_generates_intents():

    agent = IntentAgent(
        skills_root=Path(
            "src/agents/intent_agent/skills"
        )
    )

    requirement = Requirement(
        requirement="""
        Open amazon india site. Search For samsung mobile and get the details about first mobile displayed.

        """
    )

    response = await agent.invoke(
        requirement
    )
    assert response is not None, f'Intent Agent response found None'
    assert isinstance(
        response,
        IntentResponse,
    ), f'Intent Agent response is {type(response)}, Should be IntentResponse Type'

    assert len(
        response.intents
    ) > 0, f'Intent Agent response is empty'