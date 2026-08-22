from pathlib import Path

from fastapi import APIRouter, Body

from src.agents.intent_agent import IntentAgent
from src.agents.intent_agent.contracts import (
    Requirement,
    IntentResponse,
)

intent_agent_router = APIRouter(
    prefix="/api/v1/intents",
    tags=["Intent Agent"],
)


@intent_agent_router.post(
    "/extract",
    response_model=IntentResponse,
)
async def extract_intents(
    requirement: Requirement = Body(
        default=Requirement(requirement="Open amazon india site. Search For samsung mobile and get the details about first mobile displayed.")
    )
) -> IntentResponse:
    intent_agent: IntentAgent = IntentAgent()
    response: IntentResponse = await intent_agent.invoke(
        requirement
    )
    return response