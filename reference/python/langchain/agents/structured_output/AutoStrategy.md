---
title: "AutoStrategy"
description: "Automatically select the best strategy for structured output."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/AutoStrategy"
category: "reference"
tags: [reference, langchain, agents, structured_output, autostrategy]
---

# AutoStrategy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/AutoStrategy)

Automatically select the best strategy for structured output.

## Signature

```python
AutoStrategy(
    self,
    schema: type[SchemaT] | dict[str, Any],
)
```

## Extends

- `Generic[SchemaT]`

## Constructors

```python
__init__(
    self,
    schema: type[SchemaT] | dict[str, Any],
) -> None
```

| Name | Type |
|------|------|
| `schema` | `type[SchemaT] \| dict[str, Any]` |

## Properties

- `schema`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/structured_output.py#L458)
