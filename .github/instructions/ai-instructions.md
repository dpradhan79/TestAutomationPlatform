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
IntentAgent:
Input:
```text
Requirement
```
Output:
```python
IntentResponse
```
---
StepAgent:
Input:
```python
ApprovedIntents
```
Output:
```python
List[ExecutedStep]
```
---
ReviewAgent:
Input:
```python
List[Intent]
```
or
```python
List[ExecutedStep]
```
Output:
```python
ReviewResult
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
The first renderer target is Java + Selenium + TestNG. ScriptAgent renders only from an `ApprovedExecutionPlan`; it does not perform browser automation or locator discovery.
---
Never pass full workflow context to every agent.