# AI Instructions

## Frameworks

Preferred:

- LangChain
- LangGraph
- DeepAgents
- LangSmith

---

## Models

Use:

```python
init_chat_model(...)
```

Return:

```python
BaseChatModel
```

Agents should be model-agnostic.

---

## Token Optimization

IntentGeneratorAgent:

Input:

```text
Requirement
```

Output:

```python
Intent[]
```

---

StepGeneratorAgent:

Input:

```python
Intent[]
```

Output:

```python
ExecutedStep[]
```

---

ReviewAgent:

Input:

```python
ExecutedStep[]
```

Output:

```python
ReviewReport
```

---

ScriptAgent:

Input:

```python
ApprovedExecutionPlan
```

Output:

```python
GeneratedArtifact
```

---

Never pass full workflow context to every agent.
