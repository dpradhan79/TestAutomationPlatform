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

When the business quality threshold is achieved, the workflow produces `ApprovedIntents`. If the threshold is not achieved after the bounded improvement policy, HITL may approve, reject, modify, add, or remove intents.

### Review Gate 2

Technical Execution Review

```text
ApprovedIntents
    ↓
StepAgent
    ↓
ReviewAgent
    ↓
Step Quality Score
```

When the technical quality threshold is achieved, the workflow produces `ApprovedExecutionPlan`. If the threshold is not achieved after the bounded improvement policy, HITL may approve, reject, modify, add, or remove execution steps.

ReviewAgent evaluates and recommends; it does not directly modify artifacts. HITL is the governance boundary for human changes.

The review loops are finite and stage-specific. They terminate when the relevant threshold is met, the configured maximum iterations are reached, improvement stalls, or a timeout/resource budget is exceeded. No unapproved artifact may be passed to the next stage.
