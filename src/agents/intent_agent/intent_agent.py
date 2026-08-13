from pathlib import Path

from langchain.agents import create_agent

from src.agents.intent_agent.contracts import (
    Requirement,
    IntentResponse,
)
from src.shared.ai.prompts import PromptBuilder
from src.shared.ai.skills import SkillLoader
from src.shared.llm import get_chat_model


class IntentAgent:
    """
    Converts a Requirement into an IntentResponse.
    """

    def __init__(
        self,
        skills_root: Path,
        skill_name: str = "intent_extraction",
    ):
        self._skill_loader = SkillLoader(skills_root)
        self._skill_name = skill_name
        self._model = get_chat_model()

    async def invoke(
        self,
        requirement: Requirement,
    ) -> IntentResponse:

        skill = self._skill_loader.load(
            self._skill_name
        )

        prompt_package = PromptBuilder(
            skill=skill,
            requirement=requirement,
        ).build()

        agent = create_agent(
            model=self._model,
            response_format=IntentResponse,
            system_prompt=prompt_package.system_prompt,
        )

        result = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt_package.user_prompt,
                    }
                ]
            }
        )

        structured_response = result["structured_response"]

        return structured_response