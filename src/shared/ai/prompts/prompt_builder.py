from src.shared.ai.skills import Skill
from src.shared.ai.prompts import PromptPackage, Requirement


class PromptBuilder:
    def __init__(self, skill: Skill, requirement: Requirement):
        self.skill = skill
        self.requirement = requirement

    def build(
        self
    ) -> PromptPackage:

        system_prompt = f"""
        
        <Purpose> 
        {self.skill.sections.get("Purpose") if self.skill.sections.get("Purpose") is not None else ""} 
        </Purpose>
        
        <Responsibilities>
        {self.skill.sections.get("Responsibilities") if self.skill.sections.get("Responsibilities") is not None else ""}
        </Responsibilities>
        
        <Non Responsibilities>
        {self.skill.sections.get("Non Responsibilities") if self.skill.sections.get("Non Responsibilities") is not None else ""}
         </Non Responsibilities>
        
        <Notes>
        {self.skill.sections.get("Notes") if self.skill.sections.get("Notes") is not None else ""}
        </Notes>
        
        <System Prompt>
        {self.skill.system}
        </System Prompt>
        
        <Rules>
        {self.skill.rules}
        </Rules>
        
        <Examples>
        {self.skill.examples}
        </Examples>
        """.strip()

        user_prompt = self.requirement.requirement

        return PromptPackage(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )