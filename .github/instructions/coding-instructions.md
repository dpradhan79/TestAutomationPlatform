# Coding Standards
## Python
Version:
```text
Python 3.14
```
Use `uv` with the repository `pyproject.toml` and committed `uv.lock` for Python dependency management. Do not rely on transitive packages as application dependencies; add implemented integrations to `pyproject.toml`.
---
## Typing
Mandatory:
```python
def process(step: ExecutedStep) -> ReviewResult:
    ...
```
Avoid untyped code.
---
## Pydantic
Use Pydantic v2.
Avoid raw dictionaries.
Prefer:
```python
BaseModel
```
contracts.
---
## Logging
Use structured logging.
Avoid:
```python
print(...)
```
---
## Async
Use async for:
- HTTP
- Playwright
- LLM Invocations
---
## SOLID
Apply:
- Single Responsibility
- Dependency Inversion
- Open/Closed Principle
## Generated Automation Assets
The platform implementation is Python. The first ScriptAgent output is Java + Selenium + TestNG, so generated assets must follow their target project conventions and remain separate from the Python agent runtime. ScriptAgent renders approved plans; it does not execute Selenium tests.