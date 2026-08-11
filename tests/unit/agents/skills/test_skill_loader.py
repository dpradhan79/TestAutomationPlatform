import pytest
from pathlib import Path

from src.shared.skills import Skill, SkillLoader

@pytest.mark.intent_agent
@pytest.mark.unit
def test_load_intent_extraction_skill():

    loader = SkillLoader(
        skills_root=Path("src/agents/intent_agent/skills")
    )

    skill: Skill = loader.load("intent_extraction")

    assert skill.name == "intent_extraction"
    assert skill.owner == "IntentAgent"

    assert len(skill.system.strip()) > 0
    assert len(skill.rules.strip()) > 0
    assert len(skill.examples.strip()) > 0