# Architecture Instructions
## Architectural Style
The solution follows:
```text
Modular Monolith
```
Current deployment direction:
```text
Single FastAPI Application
```
Agent communication is in-process.
No microservice deployment for V1.
---
Phase 1 uses a single IntentAgent runtime. The repository is currently a scaffold, so do not assume the FastAPI application or agent modules exist until verified in the working tree.
The first complete vertical slice is:
```text
Requirement → IntentAgent → StepAgent plan → ScriptAgent → Java + Selenium + TestNG assets
```
## Main Agent
MainAgent is a future orchestration component and will be introduced using:
```python
create_deep_agent(...)
```
MainAgent:
- Routes work
- Delegates work
- Coordinates workflow
Business logic belongs to subagents.
---
## Shared Code Rule
Shared code should contain only:
- Configuration
- Observability
- Model Factory
- Memory
- Checkpointing
- Cross-Agent Contracts
Everything else belongs to owning agents.
---
## Workflow
```text
Requirement
      |
      v
KnowledgeAgent (Optional)
      |
      v
IntentAgent
      |
      v
StepAgent
      |
      v
ReviewAgent (business and technical quality gates)
      |
      v
HITL
      |
      v
ScriptAgent
```
ScriptAgent initially renders Java + Selenium + TestNG assets from an `ApprovedExecutionPlan`. It does not perform browser automation, inspect the DOM, or discover locators. Additional renderers may be added later.