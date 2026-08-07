# GitHub Copilot Instructions

## Source Of Truth

Always read and follow:

```text
README.md
AGENTS.md
.github/instructions/*.md
```

README.md is the canonical architecture document.

AGENTS.md defines agent responsibilities and ownership boundaries.

At the start of every task, read `README.md` first, then `AGENTS.md`, then only the applicable scoped instruction files. Inspect the actual working-tree structure before assuming that a planned component exists; this repository is currently an architecture scaffold.

---

## Architecture Principles

This repository follows:

- DeepAgent Target Architecture with create_agent-first progression
- Agent Ownership Principle
- Skill Driven Design
- Renderer Pattern
- HITL Workflow
- Ollama First Development Strategy

The first complete vertical slice is the IntentAgent workflow through ScriptAgent rendering Java + Selenium + TestNG automation assets. DeepAgent orchestration and additional renderers are future extensions.

---

## Agent Ownership Rule

Agents are the primary architectural boundary.

Each agent owns:

```text
contracts
prompts
skills
services
tools
tests
```

Avoid introducing unnecessary shared components.

---

## AI Model Rule

All agents must consume:

```python
BaseChatModel
```

via:

```python
init_chat_model(...)
```

Do not directly bind the solution to:

- AzureChatOpenAI
- ChatOpenAI
- Bedrock-specific SDKs

---

## ScriptAgent Rule

ScriptAgent is a renderer.

ScriptAgent:

- MUST NOT perform browser automation
- MUST NOT inspect screenshots
- MUST NOT analyze DOM

ScriptAgent only renders:

```python
ApprovedExecutionPlan
```

into framework-specific automation assets.

---

## Code Generation Standards

Generate production-grade code.

Requirements:

- Type Hints
- Pydantic v2
- Async where applicable
- Dependency Injection
- Structured Logging
- Unit Tests
- Separation of Concerns

Platform implementation is Python-based and follows the repository runtime configuration. Generated automation assets initially target Java + Selenium + TestNG and must remain separate from the Python agent runtime.

---

## Skill Standards

Each skill follows:

```text
skill-name
│
├── skill.md
├── system.md
├── rules.md
├── examples.md
└── output-schema.md
```

Skill folder name MUST match:

```yaml
name:
```

inside skill.md.

---

## Tool Usage

Browser automation should be implemented through:

```text
Playwright Tool
```

wrapped by:

```text
BrowserAutomationService
```

Do not directly invoke Playwright from agents.
