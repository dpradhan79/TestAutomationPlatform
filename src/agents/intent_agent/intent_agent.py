import logging
from pathlib import Path

import httpx
from langchain.agents import create_agent

from src.agents.intent_agent.contracts import (
    Requirement,
    IntentResponse,
)
from src.shared.ai.prompts import PromptBuilder
from src.shared.ai.skills import SkillLoader
from src.shared.llm import get_chat_model, get_llm_config

logger = logging.getLogger(__name__)

class IntentAgent:
    """
    Converts a Requirement into an IntentResponse.
    """

    def __init__(
        self,
        skills_root: Path = Path(__file__).resolve().parents[0]/"skills",
        skill_name: str = "intent_extraction",
    ):
        self._name = self.__class__.__name__
        self._skill_name = skill_name
        self._model = get_chat_model()
        self._skill_loader = SkillLoader(skills_root)
        logger.info(f'{self._name} Initialized Successfully')

    async def invoke(
        self,
        requirement: Requirement,
    ) -> IntentResponse:
        logger.debug(f'Agent - {self._name} will be invoked')
        skill = self._skill_loader.load(
            self._skill_name
        )
        logger.debug(f'skill was loaded successfully')
        prompt_package = PromptBuilder(
            skill=skill,
            requirement=requirement,
        ).build()
        logger.debug(f'prompt package was built successfully with system prompt - '
                     f'{prompt_package.system_prompt}\n '
                     f'user prompt - {prompt_package.user_prompt}')
        agent = create_agent(
            model=self._model,
            response_format=IntentResponse,
            system_prompt=prompt_package.system_prompt,
            name=self._name
        )
        try:
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
        except httpx.ConnectError as e:
            logger.exception(f'Could Not Connect To LLM Model - {get_llm_config().llm_model_name}: \n {e}')
            raise e
        except Exception as e:
            logger.exception(f'Error occurred while invoking the agent: {e}')
            raise e

        structured_response = result["structured_response"]

        return structured_response