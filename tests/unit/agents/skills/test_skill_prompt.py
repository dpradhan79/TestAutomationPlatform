import pytest
from pathlib import Path

from src.shared.ai.prompts import Requirement, PromptPackage, PromptBuilder
from src.shared.ai.skills import Skill, SkillLoader

@pytest.mark.skill
@pytest.mark.unit
def test_load_intent_extraction_skill():

    loader = SkillLoader(
        skills_root=Path("src/agents/intent_agent/skills")
    )

    skill: Skill = loader.load("intent_extraction")

    assert skill.name == "intent_extraction"
    assert skill.description is not None
    assert skill.owner == "IntentAgent"

    assert skill.input_contract is not None
    assert skill.output_contract is not None
    assert skill.sections.get("Purpose") is not None
    assert skill.sections.get("Responsibilities") is not None
    assert skill.sections.get("Non Responsibilities") is not None

    assert skill.sections.get("Notes") is not None

    assert skill.system is not None
    assert skill.rules is not None
    assert skill.examples is not None

@pytest.mark.skill
@pytest.mark.unit
def test_skill_prompt_builder():

    loader = SkillLoader(
        skills_root=Path("src/agents/intent_agent/skills")
    )

    skill: Skill = loader.load("intent_extraction")

    requirement: Requirement = Requirement(
        requirement='Type retirement planning into the search box in the page header and press Enter.'
    )
    prompt: PromptPackage = PromptBuilder(skill = skill, requirement=requirement).build()
    assert prompt is not None
    assert prompt.system_prompt is not None
    assert prompt.user_prompt is not None
    assert prompt.system_prompt.index("Purpose") > -1, f'Purpose Not Found In Prompt'
    assert prompt.system_prompt.index("Responsibilities") > -1, f'Responsibilities Not Found In Prompt'
    assert prompt.system_prompt.index("Non Responsibilities") > -1, f'Non Responsibilities Not Found In Prompt'
    assert prompt.system_prompt.index("Notes") > -1, f'Notes Not Found In Prompt'
    assert prompt.user_prompt == requirement.requirement, f'User Prompt And Requirement Not Equal'