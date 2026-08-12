from pydantic import BaseModel, Field


class PromptPackage(BaseModel):
    system_prompt: str = Field(..., description='System Prompt For Agent')
    user_prompt: str = Field(..., description='User Prompt For Agent')