# ADR-008 Evaluation First Architecture

## Status

Accepted

## Date

2026-08-05

## Context

AI systems require objective quality measurement.

## Decision

Evaluation is a first-class architectural component.

## Framework

DeepEval

## Scope

IntentAgent outputs must be continuously evaluated.

## Metrics

- Relevance
- Completeness
- Correctness
- Coverage
- JSON Validity

## Repository Structure

```text
src/evaluations/deepeval
```

## Benefits

- Detect regressions
- Improve prompt quality
- Improve model selection
- Measure business impact
