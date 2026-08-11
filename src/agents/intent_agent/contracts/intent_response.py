from pydantic import BaseModel, Field

from src.agents.intent_agent.contracts.intent import Intent


class IntentResponse(BaseModel):
    """
    Structured output returned by IntentAgent.
    """

    version: str = Field(default="1.0", description="Version of the IntentResponse contract.")
    intents: list[Intent] = Field(
        default_factory=list,
        description="Ordered list of extracted intents."
    )