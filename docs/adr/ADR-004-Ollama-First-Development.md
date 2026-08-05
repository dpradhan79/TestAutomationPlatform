# ADR-004 Ollama First Development

## Status

Accepted

## Date

2026-08-05

## Context

The platform requires local AI development without dependency on cloud-hosted models.

## Decision

Use Ollama as the primary development inference platform.

## Development Models

Examples:

- qwen3
- llama3
- deepseek-r1
- mistral

## Production Goal

Remain provider agnostic.

Future providers may include:

- Azure OpenAI
- OpenAI
- Anthropic
- Amazon Bedrock
- Vertex AI

## Architectural Rule

Application code must not directly depend on model vendor SDKs.

All LLM access must occur through:

```python
BaseChatModel
```

obtained via:

```python
init_chat_model(...)
```

## Benefits

- Offline development
- Cost optimization
- Faster experimentation
- Easier testing
