---
title: "FunctionDescription"
description: "Representation of a callable function to send to an LLM."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/FunctionDescription"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, functiondescription]
---

# FunctionDescription

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/function_calling/FunctionDescription)

Representation of a callable function to send to an LLM.

## Signature

```python
FunctionDescription()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    description: str,
    parameters: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `description` | `str` |
| `parameters` | `dict[str, Any]` |

## Properties

- `name`
- `description`
- `parameters`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/utils/function_calling.py#L64)
