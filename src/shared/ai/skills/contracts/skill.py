from typing import Optional

from pydantic import BaseModel, Field


class Skill(BaseModel):
    """
    Fully loaded skill definition.
    """

    name: str = Field(
        min_length=1,
        description="Unique skill name."
    )

    description: str = Field(
        min_length=1,
        description="Skill description."
    )

    owner: str = Field(
        min_length=1,
        description="Owning agent."
    )

    version: str = Field(
        min_length=1,
        description="Skill version."
    )

    input_contract: Optional[str] = Field(
        default=None,
        description="Agent Input"
    )
    output_contract: Optional[str] = Field(
        default=None,
        description="Agent Output"
    )

    sections: dict[str, str] = Field(
        default_factory=dict,
        description='dictionary for all sections in markdown file helpful for agent'
    )

    system: str = Field(
        min_length=1,
        description="System instructions."
    )

    rules: str = Field(
        min_length=1,
        description="Behavioral rules."
    )

    examples: str = Field(
        min_length=1,
        description="Few shot examples."
    )