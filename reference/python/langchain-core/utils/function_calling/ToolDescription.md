---
title: "ToolDescription"
description: "Representation of a callable function to the OpenAI API."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/ToolDescription"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, tooldescription]
---

# ToolDescription

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/function_calling/ToolDescription)

Representation of a callable function to the OpenAI API.

## Signature

```python
ToolDescription()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['function'],
    function: FunctionDescription,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['function']` |
| `function` | `FunctionDescription` |

## Properties

- `type`
- `function`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/utils/function_calling.py#L77)
