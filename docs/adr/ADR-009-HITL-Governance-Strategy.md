# ADR-009 Human-In-The-Loop Governance Strategy

## Status

Accepted

## Date

2026-08-05

## Context

The platform generates business and technical artifacts that may require human validation before being consumed by downstream agents.

Human review is valuable for:

- Business validation
- Technical validation
- Governance
- Compliance
- Enterprise adoption

However mandatory human review for every workflow reduces the autonomy of the platform.

A balance is required between autonomous execution and human oversight.

## Decision

Human-In-The-Loop (HITL) shall be treated as a configurable governance capability.

The platform will support:

- Fully Autonomous Execution
- Quality-Gated Human Review
- Always-On Human Review

## Review Stages

The platform supports two review stages.

### Review Gate 1

Business Understanding Review

```text
KnowledgeAgent
    ↓
IntentAgent
    ↓
ReviewAgent
    ↓
Intent Quality Score
```
