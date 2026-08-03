# Selector Strategy

## Selenium Priority

1. id
2. name
3. data-testid
4. data-qa
5. aria-label
6. css
7. xpath

---

## Playwright Priority

1. get_by_test_id
2. get_by_role
3. get_by_label
4. get_by_placeholder
5. get_by_text
6. locator(css)
7. locator(xpath)

---

## Anti Patterns

Avoid:

- Absolute XPath
- Dynamic IDs
- Index-based locators
- Long CSS chains

---

## Self Healing Readiness

StepGeneratorAgent should capture:

```python
locator

alt_locators
```

for future healing support.
