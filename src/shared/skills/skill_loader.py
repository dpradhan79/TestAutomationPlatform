from pathlib import Path

import yaml

from src.shared.skills import Skill


class SkillLoader:
    """
    Loads a skill directory
    and returns a validated Skill model.
    """

    def __init__(self, skills_root: Path):
        self._skills_root = skills_root

    def load(self, skill_name: str) -> Skill:

        skill_folder = self._skills_root / skill_name

        skill_md = skill_folder / "SKILL.md"
        system_md = skill_folder / "SYSTEM.md"
        rules_md = skill_folder / "RULES.md"
        examples_md = skill_folder / "EXAMPLES.md"

        skill_text = skill_md.read_text(encoding="utf-8")
        system_text = system_md.read_text(encoding="utf-8")
        rules_text = rules_md.read_text(encoding="utf-8")
        examples_text = examples_md.read_text(encoding="utf-8")

        metadata = self._parse_frontmatter(skill_text)
        skill: Skill = Skill.model_validate(
            Skill(
            name=metadata["name"],
            description=metadata["description"],
            owner=metadata["owner"],
            version=metadata["version"],
            system=system_text,
            rules=rules_text,
            examples=examples_text)
        )
        return skill

    @staticmethod
    def _parse_frontmatter(content: str) -> dict:

        lines = content.splitlines()

        if not lines or lines[0].strip() != "---":
            raise ValueError("Missing YAML front matter.")

        yaml_lines = []

        for line in lines[1:]:
            if line.strip() == "---":
                break

            yaml_lines.append(line)

        return yaml.safe_load("\n".join(yaml_lines))