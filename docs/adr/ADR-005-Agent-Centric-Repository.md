# ADR-005 Agent-Centric Repository Structure

## Status

Accepted

## Date

2026-08-05

## Context

A repository structure is required for long-term maintainability.

The platform will contain multiple independent agents.

## Decision

Agents are the primary architectural boundary.

## Ownership

Each agent owns:

- contracts
- prompts
- skills
- services
- tools
- tests

Example:

```text
intent_generator

├── contracts
├── prompts
├── skills
├── services
├── tools
└── tests
```

## Shared Layer

Shared code contains only:

- Settings
- Storage
- Observability
- LLM Factory
- Shared Contracts

## Benefits

- Clear ownership
- Easy maintenance
- Reduced coupling
- Easier onboarding
