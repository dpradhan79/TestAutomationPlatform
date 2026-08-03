# AGENTS.md

## Purpose

This document defines:

- Agent responsibilities
- Agent ownership boundaries
- Agent inputs and outputs
- Delegation rules
- Tool ownership
- Skill ownership
- Memory usage
- Checkpoint strategy
- HITL workflow

README.md remains the canonical architecture document.

This file focuses on agent behavior and implementation responsibilities.

---

# Agent Hierarchy

```text
MainAgent (DeepAgent)
|
+-- KnowledgeAgent (Optional)
|
+-- IntentGeneratorAgent
|
+-- StepGeneratorAgent
|
+-- ReviewAgent
|
+-- ScriptAgent
```

MainAgent orchestrates the entire workflow.

Subagents should focus on a single responsibility.

---

# Core Architectural Rules

## Rule 1

Agents own their implementation assets.

Example:

```text
agent
│
├── contracts
├── prompts
├── skills
├── tools
├── services
└── tests
```

---

## Rule 2

Business logic should remain inside the owning agent.

Avoid:

```text
shared/god-services
```

---

## Rule 3

Shared modules should contain only:

```text
Configuration

Observability

ModelFactory

Memory

Checkpointing

Cross-Agent Contracts
```

---

## Rule 4

Agents communicate using strongly typed contracts.

Avoid:

```python
dict
```

Prefer:

```python
pydantic BaseModel
```

---

# MainAgent

## Purpose

System Orchestrator.

MainAgent is implemented using:

```python
create_deep_agent(...)
```

MainAgent performs:

- Planning
- Reasoning
- Delegation
- Routing
- State coordination
- Memory integration
- Checkpoint integration

MainAgent should contain minimal business logic.

Business logic belongs to subagents.

---

## Input

```python
Requirement
```

---

## Output

```python
GeneratedArtifact
```

or

```python
WorkflowResponse
```

---

## Subagents

```python
KnowledgeAgent

IntentGeneratorAgent

StepGeneratorAgent

ReviewAgent

ScriptAgent
```

---

# KnowledgeAgent

## Purpose

Requirement augmentation.

KnowledgeAgent enriches requirements using retrieved context.

---

## Status

Optional.

Can be disabled through configuration.

---

## Input

```python
Requirement
```

---

## Output

```python
AugmentedRequirement
```

---

## Responsibilities

- Knowledge retrieval
- Context enrichment
- Context summarization
- Hallucination reduction

---

## Future Sources

```text
PDF

JIRA

Azure DevOps

Confluence

SharePoint

Internal Wikis
```

---

## Folder

```text
knowledge_agent
│
├── contracts
├── prompts
├── skills
├── services
├── ingestion
├── retrieval
└── tests
```

---

# IntentGeneratorAgent

## Purpose

Convert requirements into business intents.

---

## Input

```python
Requirement
```

or

```python
AugmentedRequirement
```

---

## Output

```python
List[Intent]
```

---

## Responsibilities

- Requirement understanding
- Intent extraction
- Intent validation
- Intent normalization

---

## Example

Requirement:

```text
Login to application.
Search for iPhone.
Add item to cart.
Logout.
```

Output:

```python
[
    LoginIntent,
    SearchIntent,
    AddToCartIntent,
    LogoutIntent
]
```

---

## Folder

```text
intent_generator
│
├── contracts
├── prompts
├── skills
└── tests
```

---

# StepGeneratorAgent

## Purpose

Generate executable browser steps.

This is the most intelligence-heavy component of the system.

---

## Input

```python
List[Intent]
```

---

## Output

```python
List[ExecutedStep]
```

---

## Responsibilities

- Navigation planning
- DOM analysis
- Screenshot analysis
- Locator discovery
- Browser interaction
- Validation discovery

---

## Tools

Owns:

```text
Playwright Tool
```

---

## Allowed

```text
Browser navigation

Screenshot capture

DOM extraction

Playwright interaction
```

---

## Not Allowed

```text
Framework rendering
```

---

## Example Output

```python
ExecutedStep(
    intent="Login",
    action="CLICK",
    confidence=0.92
)
```

---

## Folder

```text
step_generator
│
├── contracts
├── prompts
├── skills
├── tools
├── services
└── tests
```

---

# ReviewAgent

## Purpose

Review generated steps before human intervention.

---

## Input

```python
List[ExecutedStep]
```

---

## Output

```python
ReviewReport
```

---

## Review Areas

### Assertions

Detect:

```text
Missing Assertions

Weak Assertions

Duplicate Assertions
```

---

### Locators

Detect:

```text
Weak XPath

Dynamic IDs

Fragile Selectors
```

---

### Confidence

Detect:

```text
Low Confidence Steps
```

---

### Navigation Issues

Detect:

```text
Missing Steps

Duplicate Steps

Ambiguous Actions
```

---

## Folder

```text
review_agent
│
├── contracts
├── prompts
├── skills
└── tests
```

---

# Human In The Loop

## Trigger

Human review happens after:

```text
ReviewAgent
```

---

## User Actions

```text
Approve

Reject

Modify

Add Step

Delete Step
```

---

## Output

```python
ApprovedExecutionPlan
```

---

# ScriptAgent

## Purpose

Renderer.

ScriptAgent converts approved execution plans into framework-specific assets.

---

## Important Rule

ScriptAgent is NOT a browser automation agent.

ScriptAgent:

❌ does not open browsers

❌ does not inspect DOM

❌ does not analyze screenshots
