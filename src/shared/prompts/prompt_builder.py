from src.shared.skills import Skill
from src.agents.intent_agent.contracts import Requirement
from src.shared.prompts import PromptPackage


class PromptBuilder:
    def __init__(self, skill: Skill, requirement: Requirement):
        self.skill = skill
        self.requirement = requirement

    def build(
        self
    ) -> PromptPackage:

        system_prompt = f"""
        {self.skill.system}
        
        {self.skill.rules}
        
        {self.skill.examples}
        """.strip()

        user_prompt = self.requirement.requirement

        return PromptPackage(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )