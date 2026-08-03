# ADR-001 DeepAgent Architecture

## Status

Accepted

## Context

The platform requires:

- Planning
- Routing
- Delegation
- Tool Usage
- Memory
- Checkpointing

## Decision

Use:

```python
create_deep_agent(...)
```

as the system orchestrator.

## Consequences

Pros:

- Aligns with LangGraph ecosystem
- Reduced custom orchestration
- Native checkpoint support
- Native tool support

Cons:

- Dependency on DeepAgent abstraction
