# ADR-012

## Title

LLM Factory and IntentAgent Foundation

## Status

Accepted

## Context

The platform follows:

- LLM Agnostic
- Provider Agnostic
- Cloud Agnostic

Multiple agents will require model access:

- IntentAgent
- KnowledgeAgent
- ReviewAgent
- StepAgent
- ScriptAgent

Direct provider usage inside agents would create coupling.

## Decision

Introduce:

shared/config
shared/llm

All agents obtain models through:

get_chat_model()

Internally the factory uses:

init_chat_model()

## Consequences

Benefits:

- Provider Agnostic
- Centralized Configuration
- Easier Testing
- Easier Future Migration