---
title: "LangGraphDeprecationWarning"
description: "A LangGraph specific deprecation warning."
source: "https://reference.langchain.com/python/langgraph/warnings/LangGraphDeprecationWarning"
category: "reference"
tags: [reference, langgraph, warnings, langgraphdeprecationwarning]
---

# LangGraphDeprecationWarning

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/warnings/LangGraphDeprecationWarning)

A LangGraph specific deprecation warning.

## Signature

```python
LangGraphDeprecationWarning(
    self,
    message: str,
    args: object = (),
    *,
    since: tuple[int, int],
    expected_removal: tuple[int, int] | None = None,
)
```

## Description

Inspired by the Pydantic `PydanticDeprecationWarning` class, which sets a great standard
for deprecation warnings with clear versioning information.

## Extends

- `DeprecationWarning`

## Constructors

```python
__init__(
    self,
    message: str,
    args: object = (),
    *,
    since: tuple[int, int],
    expected_removal: tuple[int, int] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `message` | `str` |
| `args` | `object` |
| `since` | `tuple[int, int]` |
| `expected_removal` | `tuple[int, int] \| None` |

## Properties

- `message`
- `since`
- `expected_removal`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/warnings.py#L13)
