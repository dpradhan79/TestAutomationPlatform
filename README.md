# TestAutomationPlatform

Production-grade Agentic AI Platform for transforming business requirements into executable test automation assets using autonomous, quality-driven, multi-agent workflows.

---

## Document Status


| Property                        | Value                             |
| ------------------------------- | --------------------------------- |
| Document Type                   | Architecture Handbook             |
| Project                         | TestAutomationPlatform            |
| Status                          | Active Development                |
| Current Phase                   | Phase 1 – IntentAgent Foundation |
| Architecture Style              | Agentic AI Platform               |
| Current Runtime                 | create_agent()                    |
| Future Runtime                  | create_deep_agent()               |
| Canonical Architecture Document | README.md                         |
| Last Updated                    | 2026-08-05                        |

---

## Executive Summary

TestAutomationPlatform is a production-grade Agentic AI Platform intended to transform business requirements into executable automation assets.

The platform is being built incrementally, beginning with a production-grade IntentAgent and evolving into a fully autonomous enterprise test engineering platform through specialized agents, orchestration, autonomous quality loops, knowledge augmentation, governance controls, and framework-specific artifact generation.

The long-term vision is to create a platform capable of:

```text
Requirement
    ↓

Knowledge Acquisition
    ↓

Intent Understanding
    ↓

Intent Validation
    ↓

Execution Planning
    ↓

Execution Validation
    ↓

Automation Artifact Generation
    ↓

Enterprise Governance
```

while remaining:

- LLM Agnostic
- Cloud Agnostic
- Vendor Agnostic
- Framework Agnostic

---

## Current Status Dashboard


| Area                | Status      |
| ------------------- | ----------- |
| IntentAgent         | In Progress |
| KnowledgeAgent      | Planned     |
| MainAgent           | Planned     |
| ReviewAgent         | Planned     |
| StepAgent           | Planned     |
| ScriptAgent         | Planned     |
| PostgreSQL          | Planned     |
| PGVector            | Planned     |
| LangSmith           | Planned     |
| DeepEval            | Planned     |
| Azure AI Foundry    | Planned     |
| Enterprise Security | Planned     |
| Multi-Tenancy       | Planned     |

---

## Quick Navigation


| Topic                     | Current Status                                  |
| ------------------------- | ----------------------------------------------- |
| Current Development Focus | IntentAgent                                     |
| Current Phase             | Phase 1                                         |
| Next Phase                | KnowledgeAgent                                  |
| Planned Orchestrator      | MainAgent (DeepAgent)                           |
| Current Runtime           | create_agent()                                  |
| Future Runtime            | create_deep_agent()                             |
| Persistence Platform      | PostgreSQL + PGVector                           |
| Current LLM Strategy      | Ollama                                          |
| Long-Term Goal            | Autonomous Enterprise Test Engineering Platform |

---

## Table of Contents

### Platform Overview

- #vision
- #problem-statement
- Design Principles
- #documentation-strategy
- #current-project-status
- #current-development-focus
- #platform-maturity-model

### Platform Architecture

- Current Architecture
- #target-architecture
- #agent-interaction-model
- #end-to-end-workflow
- #agent-responsibilities

### Quality And Governance

- #dual-review-gate-architecture
- #autonomous-quality-improvement-loop
- #configurable-hitl-policy
- #quality-scoring-framework

### Agent Framework

- #architecture-principles
- #agent-design-principles
- #skill-architecture
- #skill-lifecycle
- #agent-contract-strategy
- #agent-internal-architecture

### Context And Memory

- #context-management-strategy
- #memory-strategy
- #checkpoint-strategy
- #persistence-strategy

### Platform Infrastructure

- Tool Architecture
- #renderer-architecture
- #llm-strategy
- #prompt-management-strategy
- #observability-strategy
- #platform-evaluation-plan

### Implementation

- #repository-structure
- #planned-phases

### Governance

- #architecture-documentation-roadmap
- Architecture Decision Records
- #future-enhancements
- #canonical-architecture-document
---

## Vision

TestAutomationPlatform is a production-grade Agentic AI Platform designed to transform business requirements into executable automation assets.

The platform is being built to:

- Learn and master DeepAgents
- Learn and master LangGraph
- Learn and master LangSmith
- Learn and master Azure AI Foundry
- Explore Agentic Architectures
- Explore Autonomous Systems
- Explore Human-In-The-Loop Governance
- Explore Enterprise Quality Gates
- Explore RAG and Knowledge Augmentation
- Build reusable enterprise agent frameworks
- Build a cloud-neutral AI platform
- Build an Autonomous Test Engineering Platform

The platform should progressively reduce manual effort while increasing automation quality, consistency, and governance.

---

## Problem Statement

Traditional test automation development requires significant manual effort.

Typical activities include:

- Requirement Analysis
- Business Understanding
- Domain Understanding
- Knowledge Gathering
- Test Design
- Automation Design
- Framework Implementation
- Review Activities
- Approval Activities
- Governance Activities

These activities are often distributed across multiple teams and stakeholders, resulting in delays, inconsistencies, and quality variations.

The objective of TestAutomationPlatform is to progressively automate these activities using specialized AI agents while maintaining enterprise-grade quality, governance, observability, auditability, and scalability.

---

## Design Principles

The platform must remain:

- LLM Agnostic
- Cloud Agnostic
- Vendor Agnostic
- Framework Agnostic
- Agent Driven
- Skill Driven
- Evaluation Driven
- Review Driven
- Observable
- Secure
- Extensible
- Enterprise Ready

Guiding Principles:

- MainAgent owns orchestration.
- Agents own business capabilities.
- Skills own reusable behavior.
- ReviewAgent owns quality validation.
- HITL owns governance.
- ScriptAgent owns rendering.
- KnowledgeAgent owns enterprise knowledge augmentation.
- Business logic must remain independent of LLM vendors.
- Architecture should support autonomous execution and governed execution.

---

## Documentation Strategy

README.md currently serves as:

- Architecture Handbook
- Platform Blueprint
- Engineering Guide
- Developer Onboarding Guide
- Context Recovery Document
- Roadmap
- Canonical Architecture Reference

The architecture is still evolving rapidly.

To avoid documentation fragmentation during the foundation phase, all architecture information is maintained inside README.md.

When the platform matures, selected sections may be extracted into dedicated architecture documents.

Planned future documents:

```text
docs/
│
└── architecture
    │
    ├── application_architecture.md
    ├── agent_architecture.md
    ├── skill_framework.md
    ├── context_management.md
    ├── memory_strategy.md
    ├── persistence_strategy.md
    ├── review_and_governance.md
    ├── evaluation_strategy.md
    ├── deployment_architecture.md
    ├── security_architecture.md
    └── observability_architecture.md
```

Until architecture stabilizes:

```text
README.md
```

remains the single source of truth.

---

## Current Development Focus

Current implementation focuses exclusively on:

```text
IntentAgent
```

IntentAgent will become the blueprint for all future agents.

Phase 1 establishes reusable standards for:

- Agent Creation
- Skill Architecture
- Prompt Engineering
- Context Management
- Observability
- Evaluation
- Persistence
- API Design
- Docker Deployment
- CI/CD Integration

Only after IntentAgent reaches production readiness will additional agents be introduced.

---

## Platform Maturity Model

### Level 0 – Single Agent

```text
IntentAgent
```

---

### Level 1 – Knowledge Enhanced

```text
KnowledgeAgent
+
IntentAgent
```

---

### Level 2 – Agent Orchestration

```text
MainAgent
+
KnowledgeAgent
+
IntentAgent
```

---

### Level 3 – Business Quality Gate

```text
ReviewAgent
+
Intent Quality Score
+
Conditional HITL
```

---

### Level 4 – Execution Planning

```text
StepAgent
```

---

### Level 5 – Technical Quality Gate

```text
ReviewAgent
+
Step Quality Score
+
Conditional HITL
```

---

### Level 6 – Automation Artifact Generation

```text
ScriptAgent
```

---

### Level 7 – Enterprise Platform

```text
Azure AI Foundry
Enterprise Governance
Security
Compliance
Multi-Tenancy
```

---

## Current Project Status

The project is currently in the Architecture and Design phase.

No production implementation has started yet.

The current objective is to:

- Finalize platform architecture
- Finalize agent boundaries
- Finalize repository structure
- Finalize skill framework
- Finalize persistence strategy
- Finalize governance model
- Finalize implementation roadmap

### Current Stage

```text
Architecture Discovery
        ↓

Architecture Definition
        ↓

Repository Planning
        ↓

Implementation Planning
        ↓

Phase 1 Development
```

### Completed

- High-Level Platform Architecture
- Multi-Agent Architecture Definition
- Agent Responsibility Definition
- Skill Architecture Definition
- Context Management Strategy
- Memory Strategy
- Persistence Strategy
- Governance Strategy
- Repository Blueprint
- Phase Roadmap
- ADR Planning

### In Progress

- Architecture Refinement
- README Architecture Handbook
- ADR Authoring
- Implementation Planning

### Not Yet Started

- IntentAgent Development
- KnowledgeAgent Development
- MainAgent Development
- ReviewAgent Development
- StepAgent Development
- ScriptAgent Development

### Next Milestone

```text
Phase 1

IntentAgent Foundation
```
---

### Development Progress

#### Current Phase

```text
Phase 1 of 8
IntentAgent Foundation
```

#### Phase Roadmap

```text
[✓] Architecture & Design
[➜] Phase 1 - IntentAgent Foundation
[ ] Phase 2 - KnowledgeAgent
[ ] Phase 3 - MainAgent (DeepAgent)
[ ] Phase 4 - Intent Review + HITL
[ ] Phase 5 - StepAgent
[ ] Phase 6 - Step Review + HITL
[ ] Phase 7 - ScriptAgent
[ ] Phase 8 - Enterprise Platform
```

#### Current Objective

```text
Establish all reusable platform standards through IntentAgent:

- Agent Architecture
- Skill Framework
- Contract Framework
- Context Management
- FastAPI Integration
- Evaluation Framework
- Observability Framework
- Docker Deployment
```

#### Next Milestone

```text
Phase 2 – KnowledgeAgent
```

---

## Current Architecture

The current implementation intentionally focuses on a single production-grade agent.

The goal is to establish reusable design patterns before introducing orchestration and additional agents.

### Current Scope

```text
User
    │
    ▼

FastAPI
    │
    ▼

IntentAgent
    │
    ▼

create_agent()
    │
    ▼

Ollama
    │
    ▼

Intent[]
```

### Current Responsibilities

FastAPI

- API Endpoints
- Request Validation
- Dependency Injection
- OpenAPI Documentation

IntentAgent

- Requirement Understanding
- Intent Extraction
- Structured Output Generation
- Intent Normalization

create_agent()

- Agent Runtime
- Tool Integration
- Skill Integration
- Structured Responses

Ollama

- Local LLM Runtime
- Model Hosting
- Inference

### Current Objective

Build a production-ready IntentAgent that establishes standards for:

- Agent Design
- Skill Design
- Context Management
- Evaluation
- Observability
- Persistence
- Deployment

before introducing additional agents.

---

## Target Architecture

The target architecture evolves into a multi-agent platform orchestrated by MainAgent.

### Future Architecture

```text
User
    │
    ▼

FastAPI
    │
    ▼

MainAgent (DeepAgent)
    │
    ├── KnowledgeAgent
    │
    ├── IntentAgent
    │
    ├── ReviewAgent
    │
    ├── StepAgent
    │
    ├── ReviewAgent
    │
    └── ScriptAgent
```

### Architectural Principles

MainAgent

- Orchestrates workflows
- Delegates responsibilities
- Owns agent coordination
- Owns autonomous quality loops
- Owns checkpoint recovery
- Owns memory orchestration

Sub Agents

- Own business capabilities
- Operate independently
- Remain reusable
- Remain testable

ReviewAgent

- Owns quality validation
- Owns quality scoring
- Owns recommendations

HITL

- Owns governance
- Owns approval workflows
- Remains configurable

---

## Agent Interaction Model

### Current Interaction Model

```text
FastAPI
    │
    ▼

IntentAgent
```

Single-agent architecture.

No orchestration.

No downstream agents.

---

### Future Interaction Model

```text
MainAgent
    │
    ├── KnowledgeAgent
    │
    ├── IntentAgent
    │
    ├── ReviewAgent
    │
    ├── StepAgent
    │
    ├── ReviewAgent
    │
    └── ScriptAgent
```

### Ownership Model

MainAgent owns:

- Workflow orchestration
- Routing
- Delegation
- Quality loops
- Memory
- Checkpoints

KnowledgeAgent owns:

- Enterprise knowledge retrieval
- RAG
- Context augmentation

IntentAgent owns:

- Business understanding
- Intent extraction

ReviewAgent owns:

- Quality validation
- Quality scoring
- Recommendation generation

StepAgent owns:

- Execution planning
- Locator planning
- Assertion planning

ScriptAgent owns:

- Framework rendering
- Artifact generation

---

## End-To-End Workflow

The target platform workflow is shown below.

```text
Requirement
    │
    ▼

KnowledgeAgent
    │
    ▼

Augmented Requirement
    │
    ▼

IntentAgent
    │
    ▼

Intent[]
    │
    ▼

ReviewAgent
    │
    ▼

Intent Quality Score
    │
    ▼

Autonomous Improvement Loop
    │
    ▼

Conditional HITL
    │
    ▼

Approved Intents
    │
    ▼

StepAgent
    │
    ▼

Executed Steps
    │
    ▼

ReviewAgent
    │
    ▼

Step Quality Score
    │
    ▼

Autonomous Improvement Loop
    │
    ▼

Conditional HITL
    │
    ▼

Approved Execution Plan
    │
    ▼

ScriptAgent
    │
    ▼

Generated Automation Assets
```

### Workflow Philosophy

The platform validates outputs before forwarding them to downstream agents.

Every major artifact passes through:

```text
Generate
    ↓

Review
    ↓

Score
    ↓

Improve
```

before becoming input to the next stage.

This minimizes error propagation across the workflow.

---

## Agent Responsibilities

The platform adopts a strict ownership model.

Each agent owns a clearly defined responsibility.

No agent should perform responsibilities owned by another agent.

### Agent Responsibility Matrix


| Agent          | Primary Responsibility      |
| -------------- | --------------------------- |
| MainAgent      | Orchestration               |
| KnowledgeAgent | Knowledge Augmentation      |
| IntentAgent    | Requirement Understanding   |
| ReviewAgent    | Quality Validation          |
| StepAgent      | Execution Planning          |
| ScriptAgent    | Automation Asset Generation |

---

## MainAgent

### Purpose

MainAgent is the orchestration layer of the platform.

### Planned Runtime

```text
create_deep_agent(...)
```

### Responsibilities

- Workflow Planning
- Agent Routing
- Agent Delegation
- Checkpoint Management
- Memory Coordination
- Autonomous Improvement Loops
- HITL Coordination

### Ownership

MainAgent never generates business artifacts directly.

MainAgent coordinates agents which generate business artifacts.

---

## KnowledgeAgent

### Purpose

Enhance requirements using enterprise knowledge.

### Inputs

```text
Requirement
```

### Sources

- PDF
- Confluence
- JIRA
- Azure DevOps
- SharePoint
- Internal Documentation

### Outputs

```text
AugmentedRequirement
```

### Responsibilities

- Retrieval
- Augmentation
- Knowledge Validation
- Context Assembly

### Bounded Retrieval Improvement Loop

Knowledge retrieval may be refined when the retrieved context does not meet the configured relevance threshold. This loop is separate from the downstream Intent and Step quality-improvement loops.

The retrieval policy is configurable and must remain finite:

```yaml
knowledge_retrieval:
  maximum_iterations: 3
  minimum_context_relevance_score: 0.85
```

For each iteration, KnowledgeAgent may refine the query or retrieval parameters and retrieve context again. The loop terminates when:

- Context relevance is at least `0.85`.
- `maximum_iterations` is reached.
- A configured timeout or resource budget is reached.

When the threshold is not achieved, KnowledgeAgent returns the best available context with an explicit retrieval-quality result or requests escalation according to workflow policy. It must not invoke an unbounded self-retry loop.

---

## IntentAgent

### Purpose

Convert requirements into structured business intents.

### Inputs

```text
Requirement
```

or

```text
AugmentedRequirement
```

### Outputs

```text
Intent[]
```

### Responsibilities

- Requirement Understanding
- Intent Extraction
- Intent Normalization
- Intent Structuring
- Business Interpretation

### Current Development Status

```text
Active Development
```

IntentAgent is the current platform focus.

---

## ReviewAgent

### Purpose

Measure quality of generated artifacts.

### Inputs

May receive:

```text
Intent[]
```

or

```text
List[ExecutedStep]
```

### Outputs

```text
ReviewResult
```

### Responsibilities

- Quality Analysis
- Scoring
- Recommendations
- Improvement Guidance

### Operating Principle

ReviewAgent never modifies artifacts.

ReviewAgent only:

- Evaluates
- Scores
- Recommends

---

## StepAgent

### Purpose

Transform approved intents into executable automation plans.

### Inputs

```text
ApprovedIntents
```

### Outputs

```text
List[ExecutedStep]
```

### Responsibilities

- Navigation Planning
- Step Planning
- Locator Discovery
- Assertion Discovery
- Execution Strategy

### Future Integrations

- Playwright
- Browser Automation Service
- DOM Inspection
- Screenshot Analysis

---

## ScriptAgent

### Purpose

Generate framework-specific automation assets.

### Inputs

```text
ApprovedExecutionPlan
```
## Dual Review Gate Architecture

The platform introduces two independent quality gates.

The objective is to ensure that downstream agents consume high-quality inputs and do not amplify errors generated upstream.

---

### Review Gate #1

#### Business Understanding Validation

Purpose:

```text
Validate WHAT to test
```

Workflow:

```text
Requirement
      │
      ▼

KnowledgeAgent
      │
      ▼

AugmentedRequirement
      │
      ▼

IntentAgent
      │
      ▼

Intent[]
      │
      ▼

ReviewAgent
      │
      ▼

Intent Quality Score
```

Review Focus Areas:

- Requirement Coverage
- Intent Accuracy
- Intent Completeness
- Intent Ambiguity
- Hallucination Detection
- Business Alignment
- Confidence

Output:

```text
ApprovedIntents
```

or

```text
Intent Improvement Required
```

---

### Review Gate #2

#### Technical Validation

Purpose:

```text
Validate HOW to test
```

Workflow:

```text
ApprovedIntents
      │
      ▼

StepAgent
      │
      ▼

List[ExecutedStep]
      │
      ▼

ReviewAgent
      │
      ▼

Step Quality Score
```

Review Focus Areas:

- Navigation Quality
- Step Coverage
- Locator Quality
- Assertion Quality
- Execution Flow
- Maintainability
- Automation Readiness

Output:

```text
ApprovedExecutionPlan
```

or

```text
Step Improvement Required
```

---

### Why Two Review Gates?

The platform intentionally separates:

```text
Business Understanding
```

from

```text
Execution Planning
```

A business misunderstanding should be identified before execution planning begins.

Likewise, poor execution planning should be identified before code generation begins.

This significantly reduces downstream error propagation.

---

## Autonomous Quality Improvement Loop

One of the primary design goals of the platform is autonomous quality improvement.

The platform should attempt to improve its own outputs before requesting human intervention.

Traditional workflow:

```text
Generate
    ↓
Human Review
```

TestAutomationPlatform workflow:

```text
Generate
    ↓
Review
    ↓
Improve
    ↓
Review
    ↓
Improve
    ↓
Review
    ↓
Governance Decision
```

---

### DeepAgent Improvement Strategy

DeepAgent uses ReviewAgent outputs to drive autonomous refinement.

Workflow:

```text
Generate Output
      │
      ▼

ReviewAgent
      │
      ▼

Score
      │
      ▼

Threshold Achieved?

      YES
           │
           ▼

      Continue Workflow

      NO
           │
           ▼

      Improve Output
           │
           ▼

      Re-Review
```

This continues until:

- Target threshold is achieved
- Maximum iterations reached
- Improvement stalls
- HITL policy requires user involvement

The initial candidate counts as the first evaluation. The loop is finite: it must stop before another improvement attempt when the configured maximum, stall threshold, timeout, or resource budget is reached. The best valid candidate is retained if a later attempt scores lower.

---

### MainAgent Orchestration Loop

```text
Generate Output
       │
       ▼

ReviewAgent
       │
       ▼

Quality Score
       │
       ▼

Threshold Met?

YES
  │
  ▼

Continue Workflow

NO
  │
  ▼

Improve Output

  │
  ▼

Review Again
```

This loop represents the core operating model of MainAgent (DeepAgent).

MainAgent continues autonomous refinement until:

- Target quality threshold achieved
- Maximum iteration limit reached
- Improvement becomes insignificant
- HITL policy triggers human involvement
---

### Finite Improvement Loop Contract

Each Intent and Step quality-review loop is bounded by configuration. The initial generated artifact counts as the first candidate evaluation. A loop must not begin another improvement attempt when its configured maximum has been reached.

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

The loop continues only while all of the following are true:

- The score is below the stage threshold.
- Iterations remain.
- Improvement has not stalled.
- The timeout and resource budgets have not been exceeded.
- HITL is not required by policy.

The loop terminates when any one of those conditions is false. The best valid candidate and its review result must be retained; an unsuccessful later attempt must not replace a higher-scoring candidate. If the threshold is still not achieved after termination, the stage escalates to HITL or returns a controlled rejection according to the configured policy.

`min_improvement_delta` is measured against the previous best score. Scores and thresholds use the normalized `0.0–1.0` scale in contracts and configuration; reports may display the same values as percentages.

Retrieval termination and quality-review termination are independent: KnowledgeAgent uses its retrieval policy before downstream generation, while ReviewAgent/MainAgent use stage-specific policies after generation.

### Autonomous Improvement Principles

The platform should:

- Improve before escalating
- Learn before asking
- Optimize before involving users

Users should review high-quality outputs instead of first-pass outputs whenever possible.

---

## Configurable HITL Policy

Human-In-The-Loop (HITL) is treated as a governance capability rather than a mandatory workflow dependency.

The platform supports autonomous operation and governed operation.

---

### HITL Modes

#### Disabled

Fully autonomous execution.

Workflow:

```text
Generate
    ↓
Review
    ↓
Improve
    ↓
Continue
```

No human intervention required.

---

#### Auto

Recommended default mode.

Workflow:

```text
Generate
    ↓
Review
    ↓
Improve
    ↓

Threshold Achieved?

YES → Continue

NO → HITL
```

Human review occurs only when autonomous improvement cannot achieve the desired score.

---

#### Always

Human review is always required.

Workflow:

```text
Generate
    ↓
Review
    ↓
HITL
```

This mode is suitable for strict governance environments.

---

#### Compliance (Future)

Future operating mode.

Used when organizations require mandatory approvals because of:

- Regulatory requirements
- Security policies
- Enterprise governance
- Audit requirements

---

### HITL Trigger Conditions

HITL may be invoked when:

#### Trigger 1

Quality threshold is not achieved.

Example:

```text
Target Score = 90

Current Score = 84

Max Iterations = 5
```

Result:

```text
Invoke HITL
```

---

#### Trigger 2

User explicitly requires approval.

Example:

```yaml
hitl_mode: always
```

---

#### Trigger 3

Compliance rules require approval.

Future capability.

---

### Recommended Platform Thresholds

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
```

### Threshold Interpretation

| Score Range | Outcome |
|------------|----------|
| 0.95 - 1.00 | Excellent |
| 0.90 - 0.94 | Acceptable |
| 0.80 - 0.89 | Improvement Recommended |
| Below 0.80 | Requires Improvement |

---


## Quality Scoring Framework

Every major artifact generated by the platform should be accompanied by measurable quality metrics.

The purpose is to provide objective evidence regarding whether an artifact is suitable for downstream consumption.

---

### Intent Quality Score (IQS)

Intent Quality Score measures business understanding quality.

Range:

```text
0 - 100
```

---

#### Intent Quality Dimensions

##### Coverage Score

Measures:

```text
Did the generated intents cover the requirement?
```

Weight (Initial):

```text
30%
```

---

##### Accuracy Score

Measures:

```text
Did the agent correctly interpret the requirement?
```

Weight:

```text
25%
```

---

##### Completeness Score

Measures:

```text
Were important intents missed?
```

Weight:

```text
20%
```

---

##### Ambiguity Score

Measures:

```text
How clear are the intents?
```

Weight:

```text
15%
```

---

##### Confidence Score

Measures:

```text
Model confidence in generated intents.
```

Weight:

```text
10%
```

---

### Intent Quality Example

```json
{
  "intent_score": 92,
  "coverage": 96,
  "accuracy": 94,
  "completeness": 90,
  "ambiguity": 88,
  "confidence": 93
}
```

---

## Step Quality Score (SQS)

Step Quality Score measures automation design quality.

Range:

```text
0 - 100
```

---

### Step Quality Dimensions

#### Coverage Score

Measures:

```text
Did all approved intents translate into executable steps?
```

Weight:

```text
20%
```

---

#### Locator Quality Score

Measures:

```text
Locator stability
Locator resiliency
Locator maintainability
```

Weight:

```text
20%
```

---

#### Assertion Quality Score

Measures:

```text
Quality of validations
Quality of checkpoints
```

Weight:

```text
25%
```

---

#### Flow Quality Score

Measures:

```text
Navigation correctness
Execution correctness
```

Weight:

```text
15%
```

---

#### Maintainability Score

Measures:

```text
Readability
Reuse Potential
Long-Term Maintainability
```

Weight:

```text
10%
```

---

#### Confidence Score

Measures:

```text
Model confidence
```

Weight:

```text
10%
```

---

### Step Quality Example

```json
{
  "step_score": 95,
  "coverage": 95,
  "locators": 94,
  "assertions": 96,
  "flow": 93,
  "maintainability": 94,
  "confidence": 95
}
```

---

## ReviewAgent Outputs

ReviewAgent should never only return:

```text
Pass
Fail
```

Instead it should generate rich review metadata.

Example:

```json
{
  "overall_score": 92,
  "strengths": [],
  "weaknesses": [],
  "findings": [],
  "recommendations": [],
  "improvement_actions": []
}
```

---

## User Feedback And Continuous Learning

Review and HITL activities create valuable organizational knowledge.

Future versions of the platform will persist:

- Review Findings
- User Corrections
- Approved Outputs
- Rejected Outputs
- Review Scores
- Improvement Histories

into:

```text
PostgreSQL + PGVector
```

This enables:

- Organizational Learning
- Pattern Detection
- Knowledge Growth
- Improved Future Generations

---

## Governance Model

Governance exists to ensure trust without preventing autonomy.

Ownership Model:

| Capability | Owner |
|------------|--------|
| Generation | Agent |
| Validation | ReviewAgent |
| Improvement | MainAgent |
| Approval | HITL |
| Audit | Persistence Layer |
| Learning | Memory Layer |

This separation ensures that the platform remains scalable, observable, auditable, and enterprise-ready.

---
## Architecture Principles

These principles govern all current and future architectural decisions.

### AP-001 Agent First

Business capabilities should be implemented as agents.

---

### AP-002 Review Before Progression

Generated outputs must be reviewed before becoming inputs to downstream agents.

---

### AP-003 Quality Driven

Quality scores drive workflow progression decisions.

---

### AP-004 Skill Driven

Business behavior should reside within skills, not source code.

---

### AP-005 Contract Driven

Agent communication must use strongly typed contracts.

---

### AP-006 Autonomy Before HITL

The platform should attempt autonomous improvement before requesting human intervention.

---

### AP-007 Persistence By Default

Important workflow artifacts must be persisted.

---

### AP-008 Observability By Default

Every significant action must be traceable.

---

### AP-009 LLM Agnostic

Business capabilities must remain independent of model providers.

---

### AP-010 Enterprise Ready

Every architectural decision should consider:

- Scale
- Governance
- Auditability
- Security
- Enterprise Adoption
---

## Agent Design Principles

All agents within the platform must adhere to a common set of architectural principles.

The objective is to ensure:

- Consistency
- Reusability
- Maintainability
- Testability
- Scalability

---

### Principle 1 - Single Responsibility

Each agent owns one primary business capability.

Examples:

```text
KnowledgeAgent
    → Knowledge Retrieval

IntentAgent
    → Intent Generation

ReviewAgent
    → Quality Validation

StepAgent
    → Execution Planning

ScriptAgent
    → Artifact Generation
```

Agents should not perform responsibilities owned by other agents.

---

### Principle 2 - Contract Driven

Every agent communicates using structured contracts.

Agents should never exchange:

```text
Unstructured Text
```

Instead they exchange:

```text
Pydantic Models
```

Benefits:

- Validation
- Versioning
- Reliability
- Agent Interoperability

---

### Principle 3 - Skill Driven

Business behavior should be externalized into skills.

Agents should contain:

```text
Orchestration Logic
```

Skills should contain:

```text
Behavior
Rules
Examples
Domain Knowledge
```

---

### Principle 4 - Provider Agnostic

Agents must never be tightly coupled to a specific provider.

Avoid:

```text
AzureOpenAI(...)
```

Prefer:

```text
BaseChatModel
```

or

```text
init_chat_model(...)
```

---

### Principle 5 - Evaluation First

Every agent must be measurable.

Success is determined through:

- Quality Scores
- DeepEval Metrics
- ReviewAgent Scores
- User Feedback

---

### Principle 6 - Observable By Default

Every agent interaction must be traceable.

Minimum observability:

- Request ID
- Correlation ID
- Agent Name
- Latency
- Token Usage
- Model
- Execution Status

---

## Skill Architecture

Skills are first-class architecture components.

Skills represent reusable intelligence.

Skills are not code modules.

Skills contain:

- Instructions
- Rules
- Examples
- Constraints
- Output Expectations

---

### Skill Philosophy

Business behavior should live inside skills.

Business behavior should not be hardcoded inside agent implementations.

Example:

Instead of:

```python
prompt = "Extract business intents..."
```

Use:

```text
skills/intent-extraction/
```

which contains:

- Instructions
- Rules
- Examples
- Schemas

---

### Skill Structure

Every skill follows the same structure.

```text
skill-name/
│
├── skill.md
├── system.md
├── rules.md
├── examples.md
└── output-schema.md
```

---

### skill.md

Purpose:

Skill metadata.

Example responsibilities:

- Name
- Description
- Owner Agent
- Version
- Status

---

### system.md

Purpose:

Defines agent identity and behavior.

Examples:

- Persona
- Expertise
- Role
- Behavioral Guidelines

---

### rules.md

Purpose:

Defines constraints and quality rules.

Examples:

- Must not hallucinate
- Must produce structured outputs
- Must validate required fields

---

### examples.md

Purpose:

Few-shot learning examples.

Contains:

- Sample Inputs
- Expected Outputs
- Edge Cases

---

### output-schema.md

Purpose:

Defines expected structured output.

Example:

```json
{
  "intent_id": "",
  "intent_name": "",
  "description": ""
}
```

---

## Skill Lifecycle

Every skill follows the same execution path.

```text
Request
    │
    ▼

SkillLoader
    │
    ▼

Skill Files
    │
    ▼

PromptBuilder
    │
    ▼

Agent Runtime
    │
    ▼

Structured Output
```

---

### Skill Processing Flow

```text
Requirement
      │
      ▼

Context Manager
      │
      ▼

Skill Loader
      │
      ▼

Prompt Builder
      │
      ▼

create_agent()
      │
      ▼

Model
      │
      ▼

Contract Validation
      │
      ▼

Agent Output
```

---

## Agent Contract Strategy

All agent communication must use strongly typed contracts.

---

### Benefits

- Type Safety
- Validation
- Versioning
- Better Testing
- Better Documentation

---

### Core Platform Contracts

Future contract catalog.

```text
contracts/
│
├── requirement.py
├── augmented_requirement.py
├── intent.py
├── intent_review.py
├── approved_intent.py
├── executed_step.py
├── step_review.py
├── approved_execution_plan.py
├── artifact.py
└── review_result.py
```

---

### Versioning Strategy

All major contracts should support versioning.

Example:

```text
Intent V1

Intent V2

Intent V3
```

without breaking downstream consumers.

---

## Agent Internal Architecture

Every agent should follow a common implementation pattern.

```text
Agent
│
├── Contracts
│
├── Skills
│
├── SkillLoader
│
├── PromptBuilder
│
├── ContextManager
│
├── Agent Runtime
│
└── Tests
```

---

### Standard Agent Folder Structure

```text
agent_name/
│
├── agent.py
├── skill_loader.py
├── prompt_builder.py
├── context_manager.py
│
├── contracts/
│
├── skills/
│
├── prompts/
│
├── evaluators/
│
└── tests/
```

---

## Future Skill Catalog

The README intentionally includes future skills to prevent architectural drift and ensure they are not forgotten later.

---

### IntentAgent Skills

```text
intent_agent/
│
└── skills/
    │
    ├── intent-extraction/
    ├── business-analysis/
    ├── acceptance-criteria-analysis/
    ├── intent-normalization/
    ├── intent-validation/
    └── ambiguity-detection/
```

Purpose:

- Extract business intent
- Analyze requirements
- Normalize outputs
- Reduce ambiguity

---

### KnowledgeAgent Skills

```text
knowledge_agent/
│
└── skills/
    │
    ├── pdf-ingestion/
    ├── jira-ingestion/
    ├── ado-ingestion/
    ├── confluence-ingestion/
    ├── sharepoint-ingestion/
    ├── chunk-generation/
    ├── embedding-generation/
    ├── semantic-retrieval/
    └── requirement-augmentation/
```

Purpose:

- Ingest enterprise knowledge
- Generate embeddings
- Retrieve context
- Augment requirements

---

### ReviewAgent Skills

```text
review_agent/
│
└── skills/
    │
    ├── intent-review/
    ├── step-review/
    ├── coverage-analysis/
    ├── confidence-analysis/
    ├── score-generation/
    ├── recommendation-generation/
    └── governance-review/
```

Purpose:

- Evaluate outputs
- Score outputs
- Recommend improvements

---

### StepAgent Skills

```text
step_agent/
│
└── skills/
    │
    ├── navigation-planning/
    ├── execution-planning/
    ├── locator-discovery/
    ├── locator-validation/
    ├── assertion-discovery/
    ├── screenshot-analysis/
    ├── dom-analysis/
    └── workflow-generation/
```

Purpose:

- Generate execution plans
- Discover locators
- Generate assertions

---

### ScriptAgent Skills

```text
script_agent/
│
└── skills/
    │
    ├── selenium-testng/
    ├── selenium-cucumber/
    ├── playwright-python/
    ├── playwright-typescript/
    ├── robot-framework/
    ├── rest-assured/
    ├── appium/
    └── framework-validation/
```

Purpose:

- Generate framework-specific automation assets

---

## Skill Ownership Model

Every skill has one owner.

Example:

| Skill | Owning Agent |
|---------|---------|
| intent-extraction | IntentAgent |
| semantic-retrieval | KnowledgeAgent |
| score-generation | ReviewAgent |
| navigation-planning | StepAgent |
| playwright-python | ScriptAgent |

Ownership ensures:

- Clear 
## Context Management Strategy

Context is one of the most important assets within the platform.

The quality of agent outputs directly depends on the quality of context provided to the agent.

The platform adopts the principle:

```text
Better Context
    =
Better Decisions
```

---

### Context Ownership

Context ownership is intentionally separated.

| Component | Responsibility |
|------------|------------|
| MainAgent | Orchestration Context |
| Individual Agents | Business Context |
| KnowledgeAgent | Knowledge Context |
| ReviewAgent | Review Context |
| Persistence Layer | Historical Context |

---

### Context Sources

Agent context may be assembled from:

- Requirements
- User Inputs
- Enterprise Knowledge
- Previous Agent Outputs
- Runtime Metadata
- Configuration Data
- Session State
- Historical Learning Data

---

### Context Model

```text
Requirement
+
Knowledge
+
Configuration
+
Metadata
+
Previous Agent Output
+
Memory
=
AgentContext
```

---

### Context Lifecycle

```text
Input
    │
    ▼

Context Assembly
    │
    ▼

Context Enrichment
    │
    ▼

Agent Invocation
    │
    ▼

Agent Output
    │
    ▼

Context Persistence
```

---

### Context Goals

The platform should:

- Minimize hallucination
- Improve consistency
- Improve repeatability
- Improve traceability
- Improve output quality

---

## Memory Strategy

The platform supports multiple memory layers.

Not all memory serves the same purpose.

---

### Memory Categories

```text
Session Memory

Long-Term Memory

Knowledge Memory

Learning Memory
```

---

## Session Memory

Session Memory exists only for an active execution.

Purpose:

- Track workflow state
- Track execution progress
- Track current decisions

Examples:

```text
Current Workflow

Current Agent

Current Request

Previous Agent Responses

Active Quality Scores
```

---

### Session Memory Ownership

Primary Owner:

```text
MainAgent
```

---

## Long-Term Memory

Long-Term Memory persists beyond a single execution.

Purpose:

- Historical Recall
- User Pattern Detection
- Cross-Session Learning

Examples:

```text
Past Reviews

Past Decisions

Historical Executions

Historical Artifacts
```

---

## Knowledge Memory

Knowledge Memory stores enterprise information.

Primary Owner:

```text
KnowledgeAgent
```

Examples:

```text
Confluence

JIRA

Azure DevOps

SharePoint

PDF Documentation

Runbooks
```

---

## Learning Memory

Learning Memory stores experience generated by the platform.

Purpose:

```text
Learn From Reviews

Learn From Corrections

Learn From User Feedback
```

Examples:

```text
Rejected Outputs

Approved Outputs

Review Findings

Improvement Histories

Score Improvements
```

---

## Memory Architecture

```text
Session Memory
        │
        ▼

Long-Term Memory
        │
        ▼

Learning Memory
        │
        ▼

Knowledge Memory
```

Together these memory layers help future executions become progressively more effective.

---

## Checkpoint Strategy

Checkpointing becomes critical once DeepAgent orchestration is introduced.

---

### Purpose

Support:

- Pause
- Resume
- Recovery
- Failure Handling
- Human Review
- Governance Workflows

---

### Future Checkpoint Technology

Planned:

```text
LangGraph Checkpoints
```

---

### Checkpoint Lifecycle

```text
Start Workflow
      │
      ▼

Agent Execution
      │
      ▼

Checkpoint Save
      │
      ▼

Continue Workflow

or

Pause Workflow

or

Resume Workflow
```

---

### Checkpoint Contents

Examples:

```text
Current State

Current Agent

Review Results

Quality Scores

Workflow Metadata

Memory State

Routing Decisions
```

---

### Checkpoint Benefits

- Reliability
- Recoverability
- Auditability
- Governance Support
- Long Running Workflow Support

---

## Persistence Strategy

The platform standardizes on:

```text
PostgreSQL + PGVector
```

This decision is intentional.

The platform should not manage:

```text
Relational Database
+
Vector Database
+
Document Database
```

as separate products unless absolutely necessary.

PGVector enables a unified platform.

---

## Persistence Principles

The persistence layer must support:

- Structured Data
- Semi-Structured Data
- Vector Embeddings
- Auditability
- Governance
- Scalability

---

## PostgreSQL Responsibilities

PostgreSQL stores structured platform data.

Examples:

### Configuration

```text
System Configuration

Agent Configuration

Model Configuration
```

---

### Requests

```text
User Requests

Execution Requests

API Requests
```

---

### Audit

```text
User Actions

Governance Actions

Approval Workflows
```

---

### Metadata

```text
Execution Metadata

Workflow Metadata

Agent Metadata
```

---

### Checkpoints

```text
Workflow Checkpoints

Recovery Points
```

---

### Quality History

```text
Intent Scores

Step Scores

Review History
```

---

## PGVector Responsibilities

PGVector stores embeddings and semantic memory.

Examples:

### Knowledge Base

```text
Confluence

JIRA

SharePoint

Internal Documentation
```

---

### RAG

```text
Retrieved Context

Augmented Context
```

---

### Long-Term Learning

```text
Past Corrections

Past Reviews

Past Improvements
```

---

### Semantic Search

```text
Similarity Search

Context Retrieval

Historical Artifact Retrieval
```

---

### Agent Memory

Future capability.

Examples:

```text
Intent Learning

Review Learning

Execution Learning
```

---

## Knowledge Storage Architecture

Future Architecture:

```text
Knowledge Sources
        │
        ▼

KnowledgeAgent
        │
        ▼

Chunking
        │
        ▼

Embeddings
        │
        ▼

PGVector
        │
        ▼

Semantic Retrieval
        │
        ▼

Requirement Augmentation
```

---

## Retrieval Augmented Generation (RAG)

KnowledgeAgent uses RAG to improve IntentAgent quality.

Goal:

```text
Reduce Hallucination

Improve Accuracy

Improve Business Understanding
```

Workflow:

```text
Requirement
        │
        ▼

Knowledge Retrieval
        │
        ▼

Relevant Context
        │
        ▼

IntentAgent
```

---

## Learning Architecture

A future differentiator of the platform.

The platform should continuously learn from its own executions.

---

### Learning Inputs

Examples:

```text
Review Findings

User Feedback

Quality Scores

Corrections

Governance Decisions
```

---

### Learning Pipeline

```text
Generated Output
        │
        ▼

ReviewAgent
        │
        ▼

User Feedback
        │
        ▼

Persistence
        │
        ▼

PGVector
        │
        ▼

Future Retrieval
```

---

### Learning Objectives

The platform should progressively:

- Reduce Hallucination
- Reduce Review Effort
- Increase Accuracy
- Increase Score Quality
- Increase Automation Readiness

---

## Audit & Traceability Strategy

Enterprise systems require traceability.

Every major workflow should be traceable.

---

### Traceable Entities

```text
Requirement

AugmentedRequirement

Intent

ReviewResult

ExecutedSteps

ApprovedExecutionPlan

GeneratedArtifacts
```

---

### Stored Information

Examples:

```text
Request ID

Correlation ID

Agent Name

Model Used

Prompt Version

Skill Version

Review Scores

User Actions
```

---

### Benefits

- Compliance
- Governance
- Root Cause Analysis
- Debugging
- Observability
- Enterprise Adoption

---

## Data Architecture Summary

The platform standardizes on:

```text
Context
+
Memory
+
Checkpointing
+
PostgreSQL
+
PGVector
+
RAG
+
Learning
```

to create an enterprise-ready foundation capable of supporting both:

```text
Autonomous Agentic Workflows
```

and

```text
Governed Enterprise Workflows
```

at scale.

---
## Tool Architecture

Tools provide real-world interaction capabilities to agents.

Agents reason.

Tools execute.

This separation ensures:

- Clean Architecture
- Better Testing
- Reusable Components
- Better Governance

---

### Tool Design Principles

Agents should:

```text
Think
Plan
Decide
```

Tools should:

```text
Execute
Observe
Return Results
```

---

### Tool Categories

The platform supports the following tool categories.

```text
Browser Tools

Knowledge Tools

Evaluation Tools

Persistence Tools

Observability Tools

Utility Tools
```

---

### Tool Ownership

| Tool Category | Primary Owner |
|--------------|--------------|
| Browser Tools | StepAgent |
| Knowledge Tools | KnowledgeAgent |
| Evaluation Tools | ReviewAgent |
| Persistence Tools | MainAgent |
| Observability Tools | Platform |
| Rendering Tools | ScriptAgent |

---

## Browser Automation Architecture

Browser automation is intentionally owned by StepAgent.

IntentAgent should never directly interact with browsers.

ScriptAgent should never directly interact with browsers.

---

### Browser Automation Workflow

```text
ApprovedIntents
        │
        ▼

StepAgent
        │
        ▼

BrowserAutomationService
        │
        ▼

Playwright
        │
        ▼

Application Under Test
```

---

### Browser Responsibilities

The browser capability is responsible for:

- Page Navigation
- DOM Inspection
- Screenshot Capture
- Element Discovery
- Locator Validation
- Workflow Exploration

---

### Browser Outputs

Examples:

```text
DOM Structure

Page Metadata

Screenshots

Locators

Navigation Paths

Element Information
```

---

## BrowserAutomationService

Browser automation should be abstracted behind a service layer.

Avoid:

```text
StepAgent
    ↓
Playwright
```

Prefer:

```text
StepAgent
    ↓
BrowserAutomationService
    ↓
Playwright
```

---

### Benefits

- Cleaner Design
- Easier Testing
- Future Tool Replacement
- Framework Independence

---

### Future Browser Engines

Current:

```text
Playwright
```

Future:

```text
Browser Use

Selenium

Custom Browser Services

Cloud Browser Platforms
```

---

## Playwright Strategy

Playwright is the initial browser automation platform.

Reasons:

- Modern Architecture
- Multi-Browser Support
- Strong Python Support
- Fast Execution
- Reliable Locators
- Screenshot Support

---

### Planned Browser Capabilities

```text
Navigate

Inspect DOM

Extract Elements

Take Screenshots

Capture Network Logs

Execute Actions

Validate Locators
```

---

## Renderer Architecture

ScriptAgent acts as a renderer.

ScriptAgent should focus exclusively on:

```text
Transforming
Execution Plans
Into
Framework Assets
```

---

### Renderer Workflow

```text
ApprovedExecutionPlan
        │
        ▼

ScriptAgent
        │
        ▼

Renderer Skill
        │
        ▼

Framework Assets
```

---

### Renderer Separation Principle

StepAgent decides:

```text
WHAT TO EXECUTE
```

ScriptAgent decides:

```text
HOW TO REPRESENT IT
```

---

### Renderer Catalog

Initial Renderers:

```text
Selenium TestNG

Selenium Cucumber

Playwright Python

Playwright TypeScript
```

Future Renderers:

```text
Robot Framework

Karate

REST Assured

Appium

Cypress
```

---

### Generated Assets

Examples:

```text
Page Objects

Test Classes

Feature Files

Utilities

Framework Configuration

Execution Configuration
```

---

## LLM Strategy

The platform follows an LLM-agnostic strategy.

Agents should never depend on a specific provider SDK.

---

### Current Development Strategy

Development platform:

```text
Ollama
```

Benefits:

- Local Execution
- Privacy
- No Usage Costs
- Rapid Experimentation

---

### Recommended Development Models

Current candidates:

```text
Qwen

Llama

DeepSeek

Mistral
```

---

### Provider Abstraction

Agents must consume:

```text
BaseChatModel
```

or

```text
init_chat_model(...)
```

rather than provider-specific implementations.

---

### Future Providers

```text
Azure OpenAI

OpenAI

Anthropic

AWS Bedrock

Google Vertex AI
```

---

### Model Routing Strategy (Future)

Future versions may dynamically route requests.

Example:

```text
IntentAgent
      ↓
Best Model

ReviewAgent
      ↓
Best Model

ScriptAgent
      ↓
Best Model
```

Goals:

- Better Performance
- Lower Cost
- Higher Accuracy

---

## Prompt Management Strategy

Prompting is treated as a platform capability.

Prompts should not be scattered throughout the codebase.

---

### Prompt Categories

```text
System Prompts

Task Prompts

Review Prompts

Evaluation Prompts

Rendering Prompts
```

---

### Future Prompt Structure

```text
prompts/
│
├── system/
├── task/
├── review/
├── evaluation/
└── rendering/
```

---

### Prompt Principles

Prompts should be:

- Versioned
- Testable
- Reusable
- Observable

---

## Observability Strategy

Observability is a first-class architecture capability.

Every significant operation should be traceable.

---

### Objectives

Support:

- Debugging
- Governance
- Performance Analysis
- Quality Analysis
- Cost Analysis

---

### Observability Stack

Planned stack:

```text
LangSmith

Structured Logging

OpenTelemetry
```

---

### Observability Data

Every execution should capture:

```text
Request ID

Correlation ID

Workflow ID

Agent Name

Model

Latency

Execution Status

Token Usage

Cost

Quality Scores
```

---

### Traceability Workflow

```text
Request
    │
    ▼

MainAgent
    │
    ▼

Agents
    │
    ▼

ReviewAgent
    │
    ▼

Persistence Layer
```

Every step should be traceable.

---

### LangSmith Strategy

LangSmith becomes the primary observability platform for:

- Agent Execution
- Prompt Tracing
- Model Analysis
- Performance Analysis
- Cost Analysis

---

## Platform Evaluation Plan

Evaluation is a mandatory platform capability.

If outputs cannot be measured, they cannot be improved.

---

### Evaluation Principles

The platform must support:

- Measurement
- Benchmarking
- Regression Detection
- Comparative Analysis

---

### Evaluation Ownership

| Area | Owner |
|--------|--------|
| Intent Quality | ReviewAgent |
| Step Quality | ReviewAgent |
| Model Evaluation | DeepEval |
| Benchmarking | Evaluation Framework |
| User Feedback | HITL |

---

## DeepEval Strategy

Primary evaluation framework:

```text
DeepEval
```

---

### Planned Evaluation Metrics

Intent Agent:

```text
Correctness

Relevancy

Completeness

Structured Output Quality
```

---

Step Agent:

```text
Coverage

Locator Quality

Assertion Quality

Execution Quality
```

---

Knowledge Agent:

```text
Retrieval Quality

Context Relevancy

Augmentation Quality
```

---

## Evaluation Datasets

Future repository structure:

```text
evaluations/
│
├── datasets/
├── benchmarks/
├── regression/
├── reports/
└── deepeval/
```

---

### Evaluation Lifecycle

```text
Build Agent
      │
      ▼

Create Dataset
      │
      ▼

Run Evaluation
      │
      ▼

Generate Scores
      │
      ▼

Improve Agent
```

---

## Benchmark Strategy

Benchmarks will be maintained for:

```text
Intent Generation

Knowledge Retrieval

Execution Planning

Review Quality

Artifact Generation
```

---

## Regression Testing Strategy

Every major release should validate:

```text
Current Version

vs

Previous Version
```

to ensure quality is not degraded.

---

### Regression Dimensions

Examples:

```text
Accuracy

Coverage

Latency

Cost

Quality Scores

Human Feedback
```

---

## Technical Foundation Summary

The technical foundation of the platform consists of:

```text
Tools
+
Browser Automation
+
LLM Abstraction
+
Prompt Management
+
Observability
+
Evaluation
+
Quality Measurement
```

These capabilities provide the foundation for building reliable, measurable, scalable, and enterprise-ready agentic workflows.

---
## Repository Structure

The repository structure below represents the target-state architecture.

Important:

This structure intentionally includes:

- Current components
- Planned components
- Future components
- Placeholder files
- Placeholder folders

The objective is to prevent architectural drift and ensure important platform capabilities are not forgotten during implementation.

---

### Target Repository Structure

```text
TestAutomationPlatform
│
├── README.md
├── AGENTS.md
├── PROJECT_CONTEXT.md
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
│
├── .github
│   │
│   ├── copilot-instructions.md
│   │
│   ├── workflows
│   │   ├── ci.yml
│   │   ├── cd.yml
│   │   ├── quality-gates.yml
│   │   └── release.yml
│   │
│   └── instructions
│       └── repository-guidelines.md
│
├── docs
│   │
│   ├── architecture
│   │   │
│   │   ├── application_architecture.md
│   │   ├── agent_architecture.md
│   │   ├── skill_framework.md
│   │   ├── context_management.md
│   │   ├── memory_strategy.md
│   │   ├── persistence_strategy.md
│   │   ├── review_and_governance.md
│   │   ├── evaluation_strategy.md
│   │   ├── deployment_architecture.md
│   │   ├── security_architecture.md
│   │   └── observability_architecture.md
│   │
│   ├── runbooks
│   │   ├── local_development.md
│   │   ├── deployment.md
│   │   ├── troubleshooting.md
│   │   └── disaster_recovery.md
│   │
│   └── adr
│       ├── ADR-001-DeepAgent-Architecture.md
│       ├── ADR-002-Agent-Ownership.md
│       ├── ADR-003-PGVector-Persistence-Strategy.md
│       ├── ADR-004-Ollama-First-Development.md
│       ├── ADR-005-Agent-Centric-Repository.md
│       ├── ADR-006-README-Canonical-Source.md
│       ├── ADR-007-CreateAgent-Before-DeepAgent.md
│       ├── ADR-008-Evaluation-First-Architecture.md
│       ├── ADR-009-HITL-Governance-Strategy.md
│       ├── ADR-010-Autonomous-Quality-Improvement-Loop.md
│       └── ADR-011-Configurable-HITL-Policy.md
│
├── infra
│   │
│   ├── docker
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   │
│   ├── azure
│   │   ├── foundry
│   │   ├── aca
│   │   ├── aks
│   │   └── storage
│   │
│   ├── kubernetes
│   │
│   └── terraform
│
├── governance
│   │
│   ├── policies
│   ├── hitl
│   ├── quality_thresholds
│   ├── risk_management
│   └── compliance
│
├── prompts
│   │
│   ├── system
│   ├── task
│   ├── review
│   ├── evaluation
│   └── rendering
│
├── evaluations
│   │
│   ├── datasets
│   ├── benchmarks
│   ├── regression
│   ├── reports
│   └── deepeval
│
├── data
│   │
│   ├── uploads
│   ├── knowledge
│   ├── embeddings
│   ├── samples
│   └── generated_artifacts
│
├── tests
│   │
│   ├── unit
│   ├── integration
│   ├── e2e
│   ├── evaluation
│   └── performance
│
└── src
    │
    ├── api
    │   ├── app.py
    │   ├── dependencies.py
    │   └── routers
    │
    ├── shared
    │   │
    │   ├── llm
    │   ├── observability
    │   ├── persistence
    │   ├── evaluation
    │   ├── prompts
    │   ├── contracts
    │   ├── context
    │   ├── memory
    │   ├── checkpoints
    │   ├── scoring
    │   ├── governance
    │   ├── skills
    │   ├── workflows
    │   └── security
    │
    ├── agents
    │   │
    │   ├── main_agent
    │   ├── knowledge_agent
    │   ├── intent_agent
    │   ├── review_agent
    │   ├── step_agent
    │   ├── script_agent
    │   │
    │   ├── planner_agent
    │   ├── evaluator_agent
    │   ├── memory_agent
    │   └── governance_agent
    │
    └── evaluations
```

---

## Planned Phases

The platform will be implemented incrementally.

Each phase introduces new capabilities while preserving previous functionality.

---

### Phase 1 - IntentAgent Foundation

Objective:

Establish the foundational implementation patterns that will be reused by every future agent.

#### Agent Creation

- create_agent()
- Structured Outputs
- Pydantic Contracts
- Agent Lifecycle Standards

#### Contract-First Implementation

Phase 1 begins with versioned Pydantic v2 contracts before agent runtime wiring. The initial contract set is:

```text
Requirement
Intent
IntentResponse
```

`IntentAgent` consumes `Requirement` and returns a validated `IntentResponse` containing `Intent[]`. The same contract-first approach will be extended to `AugmentedRequirement`, `ReviewResult`, `ApprovedIntents`, `List[ExecutedStep]`, `ApprovedExecutionPlan`, and generated artifacts in later phases. `create_agent()` must receive and return these typed models rather than unvalidated dictionaries.

#### Skill Framework

- SkillLoader
- PromptBuilder
- skill.md
- system.md
- rules.md
- examples.md
- output-schema.md

#### Context Management

- ContextManager
- Context Assembly
- Runtime Context
- Prompt Context

#### LLM Layer

- Ollama
- BaseChatModel
- init_chat_model()

#### Persistence

- PostgreSQL
- PGVector

#### Observability

- LangSmith
- Structured Logging

#### API

- FastAPI
- OpenAPI

#### Evaluation

- DeepEval
- Evaluation Datasets

#### Deployment

- Docker
- Docker Compose
- CI/CD

#### Deliverable

```text
Requirement
    ↓
IntentAgent
    ↓
Intent[]
```

---

### Phase 2 - KnowledgeAgent

Objective:

Improve business understanding and reduce hallucination.

#### Knowledge Sources

- PDF
- JIRA
- Azure DevOps
- Confluence
- SharePoint

#### Knowledge Pipeline

- Chunking
- Embeddings
- Retrieval
- RAG

#### Deliverable

```text
Requirement
+
Knowledge
↓
Augmented Requirement
```

---

### Phase 3 - MainAgent (DeepAgent)

Objective:

Introduce orchestration and autonomous workflows.

#### Capabilities

- create_deep_agent()
- Routing
- Delegation
- Quality Loops
- Checkpoint Coordination
- Memory Coordination

#### Deliverable

```text
MainAgent
    ↓
KnowledgeAgent
    ↓
IntentAgent
```

---

### Phase 4 - Intent Review + HITL

Objective:

Create the Business Quality Gate.

#### Review Capabilities

- Intent Scoring
- Coverage Analysis
- Ambiguity Detection
- Hallucination Detection

#### HITL Capabilities

- Approve
- Reject
- Add Intent
- Modify Intent
- Remove Intent

#### Deliverable

```text
ApprovedIntents
```

---

### Phase 5 - StepAgent

Objective:

Generate execution-ready automation plans.

#### Capabilities

- Navigation Planning
- Locator Discovery
- Assertion Discovery
- Execution Planning
- Workflow Generation

#### Deliverable

```text
List[ExecutedStep]
```

---

### Phase 6 - Step Review + HITL

Objective:

Create the Technical Quality Gate.

#### Review Capabilities

- Locator Review
- Assertion Review
- Flow Review
- Coverage Review

#### HITL Capabilities

- Approve Steps
- Modify Steps
- Add Steps
- Remove Steps

#### Deliverable

```text
ApprovedExecutionPlan
```

---

### Phase 7 - ScriptAgent

Objective:

Generate framework-specific automation assets.

#### Initial Renderers

- Selenium TestNG
- Selenium Cucumber
- Playwright Python
- Playwright TypeScript

#### Future Renderers

- Robot Framework
- Karate
- REST Assured
- Appium

#### Deliverable

```text
Automation Assets
```
---

### Phase 8 - Enterprise Platform

Objective:

Enterprise-readiness.

#### Platform Features

- Azure AI Foundry
- Entra ID
- Governance
- Audit
- Compliance
- Multi-Tenancy
- AKS
- Azure Container Apps
- KEDA

---

### Phase Exit Criteria

A phase should only be considered complete when its exit criteria are satisfied.

#### Phase 1 Exit Criteria

- IntentAgent implemented
- create_agent() operational
- SkillLoader implemented
- PromptBuilder implemented
- Structured Outputs operational
- FastAPI operational
- Docker deployment operational
- Baseline DeepEval suite available

#### Phase 2 Exit Criteria

- Knowledge ingestion operational
- Chunking implemented
- Embedding generation implemented
- PGVector retrieval operational
- Requirement augmentation operational

#### Phase 3 Exit Criteria

- MainAgent operational
- create_deep_agent() operational
- Agent delegation operational
- Routing operational
- Checkpointing operational

#### Phase 4 Exit Criteria

- IntentReview workflow operational
- Intent scoring operational
- HITL approval operational

#### Phase 5 Exit Criteria

- StepAgent operational
- Locator discovery operational
- Assertion discovery operational
- Execution planning operational

#### Phase 6 Exit Criteria

- Step review operational
- Technical approval workflow operational
- Technical score generation operational

#### Phase 7 Exit Criteria

- ScriptAgent operational
- Minimum two renderers implemented
- Artifact generation operational

#### Phase 8 Exit Criteria

- Azure deployment operational
- Enterprise governance operational
- Authentication operational
- Audit framework operational

---

## Architecture Documentation Roadmap

As the platform matures, dedicated architecture documents will be extracted from this README.

Future documents:

```text
application_architecture.md

agent_architecture.md

skill_framework.md

context_management.md

memory_strategy.md

persistence_strategy.md

review_and_governance.md

evaluation_strategy.md

deployment_architecture.md

security_architecture.md

observability_architecture.md
```

Until architecture stabilizes:

```text
README.md
```

remains the canonical architecture handbook.

---

## Architecture Decision Records

Current ADRs:

```text
ADR-001 DeepAgent Architecture

ADR-002 Agent Ownership

ADR-003 PGVector Persistence Strategy

ADR-004 Ollama First Development

ADR-005 Agent-Centric Repository

ADR-006 README Canonical Source

ADR-007 CreateAgent Before DeepAgent

ADR-008 Evaluation First Architecture

ADR-009 HITL Governance Strategy

ADR-010 Autonomous Quality Improvement Loop

ADR-011 Configurable HITL Policy
```

---

## Future Enhancements

Potential future capabilities:

### Agent Enhancements

- PlannerAgent
- EvaluatorAgent
- GovernanceAgent
- MemoryAgent
- DeploymentAgent
- IntentReviewAgent
- StepReviewAgent

### Review Architecture Evolution

Future versions may decompose ReviewAgent into:

```text
IntentReviewAgent

StepReviewAgent

SecurityReviewAgent

GovernanceReviewAgent
```

This decomposition should occur only when the single ReviewAgent implementation becomes difficult to maintain or scale.

### Platform Enhancements

- Multi-Agent Collaboration
- Adaptive Planning
- Model Routing
- Cost Optimization
- Autonomous Recovery

### Learning Enhancements

- Continuous Learning
- Historical Feedback Learning
- Review-Based Learning
- Organizational Learning

### Enterprise Enhancements

- Multi-Tenant Isolation
- Enterprise Policy Engine
- Compliance Framework
- Cost Governance
- Usage Analytics

---

## Canonical Architecture Document

README.md currently serves as:

- Architecture Handbook
- Platform Blueprint
- Engineering Guide
- Implementation Roadmap
- Context Recovery Document

All implementation decisions should remain aligned with this document.

Any significant architectural change should:

1. Update the relevant ADR.
2. Update the relevant README section.
3. Update repository structure if required.
4. Update planned phases if required.

This ensures the architecture, implementation, and roadmap remain synchronized over time.

---

## Final Vision

The long-term objective is to evolve from:

```text
Single Agent
```

to

```text
Knowledge Enhanced Multi-Agent Platform
```

to

```text
Autonomous Quality-Gated Platform
```

to

```text
Enterprise Agentic Test Engineering Platform
```

capable of:

```text
Understanding Requirements

Acquiring Knowledge

Generating Intents

Reviewing Outputs

Improving Outputs

Planning Execution

Generating Automation Assets

Learning Continuously

Operating Autonomously

Supporting Enterprise Governance
```

while remaining:

```text
LLM Agnostic

Cloud Agnostic

Vendor Agnostic

Framework Agnostic
```

and ready for long-term enterprise adoption.

---
