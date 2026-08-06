# AGENTS.md

## Purpose

This document defines:

- Agent responsibilities
- Agent ownership boundaries
- Agent inputs and outputs
- Delegation rules
- Review responsibilities
- Quality gate responsibilities
- Skill ownership
- Tool ownership
- HITL responsibilities

README.md remains the canonical architecture document.

AGENTS.md focuses on agent behavior, ownership, and implementation responsibilities.

---

## Development Status


| Agent          | Status              |
| -------------- | ------------------- |
| IntentAgent    | Phase 1 Foundation |
| KnowledgeAgent | Planned             |
| MainAgent      | Planned             |
| ReviewAgent    | Planned             |
| StepAgent      | Planned             |
| ScriptAgent    | Planned             |

Current implementation phase:

```text
Phase 1 – IntentAgent Foundation
```

---

## Target Agent Hierarchy

```text
MainAgent (DeepAgent)
│
├── KnowledgeAgent
├── IntentAgent
├── ReviewAgent
├── StepAgent
└── ScriptAgent
```

MainAgent orchestrates workflows.

Subagents own business capabilities.

The current Phase 1 runtime is `FastAPI → IntentAgent → create_agent()`. `MainAgent (DeepAgent)` is the target orchestration architecture introduced after the leaf-agent contracts and runtime patterns are established.

The current development model runtime is Ollama. Model access remains provider-agnostic through `BaseChatModel` obtained via `init_chat_model(...)`.

---

## Agent Ownership Matrix


| Agent          | Primary Ownership   |
| -------------- | ------------------- |
| MainAgent      | Orchestration       |
| KnowledgeAgent | Knowledge Retrieval |
| IntentAgent    | Intent Generation   |
| ReviewAgent    | Quality Validation  |
| StepAgent      | Execution Planning  |
| ScriptAgent    | Artifact Rendering  |

---

## Core Implementation Rules

### Rule 1 – Single Responsibility

Each agent owns one business capability.

Agents should not assume responsibilities owned by other agents.

---

### Rule 2 – Contract Driven

Agents communicate using strongly typed contracts.

Avoid `dict`; prefer `BaseModel`.

Phase 1 is contract-first: define versioned Pydantic v2 models before wiring `IntentAgent` into `create_agent()`. The initial flow is `Requirement → IntentResponse`, where `IntentResponse` contains the validated `List[Intent]`. Each agent owns its contracts, prompts, skills, services, tools, and tests.

---

### Rule 3 – Skill Driven

Business behavior belongs in skills.

Business behavior should not be hardcoded into agent implementations.

---

### Rule 4 – LLM Agnostic

Agents must not depend on provider-specific SDKs.

Prefer `BaseChatModel` obtained through `init_chat_model(...)`.

---

### Rule 5 – Review Before Progression

Generated artifacts must be reviewed before becoming downstream inputs.

---

### Rule 6 – Autonomy Before HITL

The platform should attempt autonomous improvement before requesting human intervention.

---

## MainAgent

### Purpose

Workflow orchestrator.

### Planned Runtime

`create_deep_agent(...)`

### Responsibilities

- Workflow orchestration
- Agent delegation
- Agent routing
- Quality loop execution
- HITL coordination
- Memory coordination
- Checkpoint coordination

### Input

```text
Requirement
```

### Output

```text
WorkflowResponse
```

### Important Rule

MainAgent should contain minimal business logic.

Business logic belongs to subagents.

---

## KnowledgeAgent

### Purpose

Enhance requirements using enterprise knowledge.

### Input

```text
Requirement
```

### Output

```text
AugmentedRequirement
```

### Responsibilities

- Knowledge retrieval
- Context enrichment
- Requirement augmentation
- Hallucination reduction

### Bounded Retrieval Improvement Loop

KnowledgeAgent may refine retrieval when context relevance is below the configured threshold. The loop is finite and independently configured from Intent and Step quality-review loops.

```yaml
knowledge_retrieval:
  maximum_iterations: 3
  minimum_context_relevance_score: 0.85
```

The loop stops when the relevance threshold is met, the maximum iterations are reached, or a timeout/resource budget is exceeded. KnowledgeAgent must return an explicit retrieval-quality result or escalate according to workflow policy; it must not retry indefinitely.

When the relevance threshold is not achieved, the best available context must be retained and returned with its retrieval-quality result or escalated according to workflow policy.

### Future Knowledge Sources

- PDF
- Confluence
- JIRA
- Azure DevOps
- SharePoint
- Internal Wikis

---

## IntentAgent

### Purpose

Convert requirements into structured business intents.

### Input

```text
Requirement
```

or

```text
AugmentedRequirement
```

### Output

```text
List[Intent]
```

### Responsibilities

- Requirement understanding
- Intent extraction
- Intent normalization
- Intent validation
- Business interpretation

### Current Development Status

```text
Phase 1 Foundation
```

---

## ReviewAgent

### Purpose

Validate generated artifacts.

### Inputs

```text
List[Intent]
```

or

```text
List[ExecutedStep]
```

### Output

```text
ReviewResult
```

### Responsibilities

- Intent review
- Step review
- Quality scoring
- Recommendation generation
- Validation feedback

### Important Rule

ReviewAgent does not modify artifacts.

ReviewAgent only:

- Evaluates
- Scores
- Recommends

---

## StepAgent

### Purpose

Transform approved intents into executable automation plans.

### Input

```text
ApprovedIntents
```

### Output

```text
List[ExecutedStep]
```

### Responsibilities

- Navigation planning
- Workflow planning
- Locator discovery
- Assertion discovery
- Execution planning

### Tool Ownership

```text
Browser Automation Tools
```

### Browser Capabilities

- Navigation
- DOM inspection
- Screenshot capture
- Locator discovery
- Locator validation

Browser access must use the service boundary:

```text
StepAgent
    ↓
BrowserAutomationService
    ↓
Playwright
```

### Important Rule

StepAgent owns browser interaction.

ScriptAgent must never interact directly with browsers.

---

## ScriptAgent

### Purpose

Generate framework-specific automation assets.

### Input

```text
ApprovedExecutionPlan
```

Intent actions apply only to the business gate; step actions apply only to the technical gate. If approval is rejected or cannot be reached, the artifact is controlled as rejected and must not be passed to the next agent.

IntentAgent evaluation is first-class and uses the platform evaluation framework, initially DeepEval, with coverage, relevance, completeness, correctness, and structured-output validity checks.

### Output

```text
Automation Assets
```

### Responsibilities

- Framework rendering
- Artifact generation
- Template generation

### Important Rule

ScriptAgent is a renderer.

ScriptAgent:

- Does not open browsers
- Does not inspect DOM
- Does not analyze screenshots
- Does not discover locators

---

## Quality Gate Architecture

### Review Gate 1

Business Quality Gate.

```text
KnowledgeAgent
        ↓

IntentAgent
        ↓

ReviewAgent
        ↓

Intent Quality Score
        ↓

Autonomous Improvement Loop
        ↓

Conditional HITL
        ↓

ApprovedIntents
```

---

### Review Gate 2

Technical Quality Gate.

```text
StepAgent
      ↓

ReviewAgent
      ↓

Step Quality Score
      ↓

Autonomous Improvement Loop
      ↓

Conditional HITL
      ↓

ApprovedExecutionPlan
```

---

## MainAgent Autonomous Quality Loop

```text
Generate Output
        ↓

ReviewAgent
        ↓

Quality Score
        ↓

Threshold Met?

YES
  ↓
Continue Workflow

NO
  ↓
Improve Output
  ↓
Review Again
```

MainAgent repeats improvement cycles until:

- Target quality achieved
- Maximum iterations reached
- Improvement stalls
- Timeout or resource budget is reached
- HITL policy triggered

The initial candidate counts as the first evaluation. The best valid candidate must be retained, and a later lower-scoring candidate must not replace it. Review loops use stage-specific thresholds and limits; KnowledgeAgent retrieval limits are configured separately.

Example stage configuration:

```yaml
intent_review:
  score_threshold: 0.90
  max_iterations: 5
  min_improvement_delta: 0.02

step_review:
  score_threshold: 0.90
  max_iterations: 5
  min_improvement_delta: 0.02
```

Review scores and thresholds use the normalized `0.0–1.0` scale. The retrieval policy is independent:

```yaml
knowledge_retrieval:
  maximum_iterations: 3
  minimum_context_relevance_score: 0.85
```

---

## HITL Policy

Supported modes:

- Disabled
- Auto
- Always
- Compliance (Future)

### Human Actions

- Approve
- Reject
- Modify
- Add
- Remove

### Output

```text
ApprovedIntents
```

for the business quality gate, or:

```text
ApprovedExecutionPlan
```

---

## Skill Ownership

```text
KnowledgeAgent
    └── Knowledge Skills

IntentAgent
    └── Intent Skills

ReviewAgent
    └── Review Skills

StepAgent
    └── Execution Skills

ScriptAgent
    └── Renderer Skills
```

---

## Tool Ownership


| Tool Category       | Owner          |
| ------------------- | -------------- |
| Browser Tools       | StepAgent      |
| Knowledge Tools     | KnowledgeAgent |
| Evaluation Tools    | ReviewAgent    |
| Rendering Tools     | ScriptAgent    |
| Persistence Tools   | MainAgent      |
| Observability Tools | Platform       |

The persistence strategy is PostgreSQL with PGVector for workflow artifacts, checkpoints, request history, evaluation results, knowledge retrieval, and future semantic memory.

---

## Future Agent Evolution

Future decomposition may introduce:

```text
IntentReviewAgent

StepReviewAgent

SecurityReviewAgent

GovernanceReviewAgent
```

This decomposition should occur only when ReviewAgent becomes difficult to scale or maintain.

---

## Final Principle

```text
MainAgent Orchestrates

KnowledgeAgent Enhances

IntentAgent Understands

ReviewAgent Validates

StepAgent Plans

ScriptAgent Renders
```

Each agent owns a single responsibility.

No agent should perform responsibilities owned by another agent.
