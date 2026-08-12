from pathlib import Path

import yaml

from src.shared.ai.skills import Skill


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

        metadata, markdown_body = self._parse_frontmatter(skill_text)

        sections = self._parse_sections(markdown_body)

        return Skill(
            name=metadata["name"],
            description=metadata["description"],
            owner=metadata["owner"],
            version=str(metadata["version"]),
            input_contract=metadata.get("input_contract"),
            output_contract=metadata.get("output_contract"),
            sections=sections,
            system=system_text,
            rules=rules_text,
            examples=examples_text,
        )

    @staticmethod
    def _parse_frontmatter(content: str) -> tuple[dict, str]:

        lines = content.splitlines()

        if not lines or lines[0].strip() != "---":
            raise ValueError("Missing YAML front matter.")

        yaml_lines = []
        end_index = None

        for index, line in enumerate(lines[1:], start=1):

            if line.strip() == "---":
                end_index = index
                break

            yaml_lines.append(line)

        if end_index is None:
            raise ValueError("Invalid YAML front matter.")

        metadata = yaml.safe_load("\n".join(yaml_lines))

        body = "\n".join(lines[end_index + 1:]).strip()

        return metadata, body

    @staticmethod
    def _parse_sections(content: str) -> dict[str, str]:

        sections: dict[str, str] = {}

        current_section = None
        current_content: list[str] = []

        for line in content.splitlines():

            stripped_line = line.strip()

            if stripped_line.startswith("## "):

                if current_section:
                    sections[current_section] = "\n".join(
                        current_content
                    ).strip()

                current_section = (
                    stripped_line.removeprefix("## ")
                    .strip()
                    # .lower()
                    # .replace("-", "_")
                    # .replace(" ", "_")
                )

                current_content = []

                continue

            if current_section:
                current_content.append(line)

        if current_section:
            sections[current_section] = "\n".join(
                current_content
            ).strip()

        return sections