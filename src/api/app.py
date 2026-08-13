from fastapi import FastAPI

from src.api import (
    intent_agent_router,
    health_router
)

app = FastAPI(
    title="Test Automation Platform",
    version="1.0.0",
    description="Backend Application Developed By Debasish Pradhan - www.linkedin.com/in/pradhandebasish"
)

app.include_router(
    intent_agent_router
)
app.include_router(
    health_router
)
