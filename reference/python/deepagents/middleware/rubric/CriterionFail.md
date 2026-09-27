---
title: "CriterionFail"
description: "Per-criterion grader verdict when the criterion fails."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/CriterionFail"
category: "reference"
tags: [reference, deepagents, middleware, rubric, criterionfail]
---

# CriterionFail

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/CriterionFail)

Per-criterion grader verdict when the criterion fails.

## Signature

```python
CriterionFail()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: Annotated[str, Field(description=_CRITERION_NAME_DESCRIPTION)],
    passed: Literal[False],
    gap: Annotated[str, Field(description=_CRITERION_GAP_DESCRIPTION)],
)
```

| Name | Type |
|------|------|
| `name` | `Annotated[str, Field(description=_CRITERION_NAME_DESCRIPTION)]` |
| `passed` | `Literal[False]` |
| `gap` | `Annotated[str, Field(description=_CRITERION_GAP_DESCRIPTION)]` |

## Properties

- `name`
- `passed`
- `gap`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/middleware/rubric.py#L193)
