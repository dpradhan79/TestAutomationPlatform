---
name: intent_extraction
description:
  Converts natural language test automation requirements into
  structured business intents while preserving semantic meaning,
  action sequencing, and contextual information.

owner: IntentAgent
version: "1.0"
status: active

input_contract: Requirement
output_contract: IntentResponse
---

# Intent Extraction Skill

## Purpose

Convert natural language requirements into structured business intents.

## Responsibilities

- Requirement Understanding
- Intent Extraction
- Intent Normalization
- Intent Sequencing
- Context Preservation

## Non Responsibilities

- Browser Automation
- Locator Discovery
- DOM Analysis
- Execution Planning
- Test Script Generation
- Quality Evaluation

## Notes

This skill focuses exclusively on understanding what the user
intends to perform in the application.

The skill does not determine how automation should be implemented.