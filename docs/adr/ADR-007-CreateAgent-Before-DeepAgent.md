# ADR-007 CreateAgent Before DeepAgent

## Status

Accepted

## Date

2026-08-05

## Context

The platform ultimately intends to use DeepAgent orchestration.

However the first implementation contains only:

- IntentGeneratorAgent

There is no delegation requirement yet.

## Decision

Start with:

```python
create_agent()
```

for the IntentGeneratorAgent.

Introduce:

```python
create_deep_agent()
```

only when multiple collaborating agents exist.

## Migration Path

Phase 1:

```text
IntentGeneratorAgent
```

Phase 2:

```text
KnowledgeAgent
```

Phase 3:

```text
ReviewAgent
```

Phase 4:

```python
MainAgent = create_deep_agent(...)
```

## Benefits

- Reduced complexity
- Faster implementation
- Easier debugging
- Incremental evolution
