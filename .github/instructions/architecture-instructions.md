# Architecture Instructions

## Architectural Style

The solution follows:

```text
Modular Monolith
```

Deployment:

```text
Single FastAPI Application
```

Agent communication is in-process.

No microservice deployment for V1.

---

## Main Agent

MainAgent is implemented using:

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
IntentGeneratorAgent
      |
      v
StepGeneratorAgent
      |
      v
ReviewAgent
      |
      v
HITL
      |
      v
ScriptAgent
```

```
