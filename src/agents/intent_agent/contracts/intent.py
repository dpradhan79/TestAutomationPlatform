from pydantic import BaseModel, Field


class Intent(BaseModel):
    """
    Represents a single atomic business intent.

    Example:
    Open JP Morgan website

    Click Individual Investors

    Type 'retirement planning'
    into search box in header
    """

    intent_no: int = Field(
        ge=1,
        description="Sequential intent number."
    )

    intent: str = Field(
        min_length=1,
        description="Single atomic UI action with full semantic context preserved."
    )