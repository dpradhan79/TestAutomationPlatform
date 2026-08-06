# ADR-011 Configurable HITL Policy

## Status

Accepted

## Date

2026-08-05

---

## Context

TestAutomationPlatform is designed as an Agentic AI platform capable of operating in both:

- Fully Autonomous Mode
- Human Governed Mode

Different organizations, teams, and use cases require different levels of human involvement.

Examples:

### Autonomous Organizations

May prefer:

```text
Requirement
    ↓
AI Processing
    ↓
Generated Artifacts
```

without human intervention.

### Enterprise Organizations

May prefer:

```text
Requirement
    ↓
AI Processing
    ↓
Human Validation
    ↓
Generated Artifacts
```

### Regulated Organizations

May require mandatory human approval because of:

- Regulatory requirements
- Audit requirements
- Governance requirements
- Internal compliance policies

A fixed HITL strategy would reduce platform adoption and architectural flexibility.

---

## Decision

Human-In-The-Loop (HITL) shall be configurable.

The platform shall support multiple operating modes that control when human involvement occurs.

HITL must be treated as a governance capability rather than a mandatory workflow dependency.

---

## Supported Modes

### disabled

Fully autonomous mode.

No human intervention is required.

Workflow proceeds automatically when quality thresholds are achieved.

Example:

```text
Generate
    ↓
Review
    ↓
Score
    ↓
Threshold Achieved
    ↓
Continue Workflow
```

---

### auto

Recommended default mode.

DeepAgent attempts autonomous improvement first.

Human involvement occurs only when:

- Quality threshold is not achieved
- Maximum iterations are reached
- Improvement becomes negligible

Example:

```text
Generate
    ↓
Review
    ↓
Improve
    ↓
Review
    ↓
Threshold Not Achieved
    ↓
HITL
```

---

### always

Human review is always required.

Every review gate invokes HITL.

Example:

```text
Review
    ↓
HITL
    ↓
Continue
```

regardless of achieved score.

---

### compliance

Future capability.

Human approval becomes mandatory due to:

- Regulatory requirements
- Organizational governance
- Audit requirements

Example domains:

- Banking
- Healthcare
- Government
- Insurance

---

## HITL Trigger Conditions

### Trigger 1

Quality threshold not achieved.

Example:

```text
Target Score = 90

Current Score = 81

Maximum Iterations Reached
```

Result:

```text
Invoke HITL
```

---

### Trigger 2

User explicitly requests HITL.

Configuration:

```yaml
hitl_mode: always
```

Result:

```text
Invoke HITL
```

regardless of score.

---

### Trigger 3

Compliance requirement.

Future capability.

Organization policy requires mandatory approval.

---

## Example Configuration

```yaml
hitl_mode: auto

intent_review:
  score_threshold: 0.90
  max_iterations: 5
  min_improvement_delta: 0.02

step_review:
  score_threshold: 0.90
  max_iterations: 5
  min_improvement_delta: 0.02

knowledge_retrieval:
  maximum_iterations: 3
  minimum_context_relevance_score: 0.85
```

The retrieval settings bound KnowledgeAgent context refinement and are independent of the Intent and Step review settings. The initial candidate counts as the first review evaluation. When a review loop terminates without meeting its threshold, the best valid candidate is retained and the workflow invokes HITL or returns a controlled rejection according to policy.

---

## Architectural Principle

The platform should remain:

```text
Agentic First
```

while supporting:

```text
Human Governed Execution
```

when required.

The platform should never be inherently dependent upon human intervention.

---

## Benefits

- Supports fully autonomous execution
- Supports enterprise governance
- Supports regulatory compliance
- Supports future operating models
- Reduces manual effort
- Improves architectural flexibility

---

## Risks

- Additional configuration complexity
- Multiple execution paths

---

## Mitigation

Provide:

- Sensible defaults
- Standard operating profiles
- Documentation
- Governance guidelines

---

## Consequences

HITL becomes a configurable governance mechanism rather than a mandatory workflow dependency.

This allows TestAutomationPlatform to operate as:

- Fully Autonomous Agentic Platform
- Assisted Platform
- Human Governed Platform

without requiring architectural changes.
