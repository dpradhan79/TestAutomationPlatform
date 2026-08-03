# Coding Standards

## Python

Version:

```text
Python 3.12+
```

---

## Typing

Mandatory:

```python
def process(step: ExecutedStep) -> ReviewReport:
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
