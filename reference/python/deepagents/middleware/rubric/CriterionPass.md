---
title: "CriterionPass"
description: "Per-criterion grader verdict when the criterion passes."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/CriterionPass"
category: "reference"
tags: [reference, deepagents, middleware, rubric, criterionpass]
---

# CriterionPass

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/CriterionPass)

Per-criterion grader verdict when the criterion passes.

## Signature

```python
CriterionPass()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: Annotated[str, Field(description=_CRITERION_NAME_DESCRIPTION)],
    passed: Literal[True],
)
```

| Name | Type |
|------|------|
| `name` | `Annotated[str, Field(description=_CRITERION_NAME_DESCRIPTION)]` |
| `passed` | `Literal[True]` |

## Properties

- `name`
- `passed`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/middleware/rubric.py#L186)
