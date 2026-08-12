from pydantic import BaseModel, Field


class Requirement(BaseModel):
    """
    Natural language requirement supplied by the user.

    Phase-1:
    A single requirement string is sufficient.

    Future:
    This contract can be extended with:
    - request_id
    - correlation_id
    - source
    - metadata
    - attachments
    """

    requirement: str = Field(
        min_length=1,
        description="Natural language automation requirement."
    )