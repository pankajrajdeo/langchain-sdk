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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/warnings.py#L13)
