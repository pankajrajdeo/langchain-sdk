---
title: "Operation"
description: "Logical operation over other directives."
source: "https://reference.langchain.com/python/langchain-core/structured_query/Operation"
category: "reference"
tags: [reference, langchain-core, structured_query, operation]
---

# Operation

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/structured_query/Operation)

Logical operation over other directives.

## Signature

```python
Operation(
    self,
    operator: Operator,
    arguments: list[FilterDirective],
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `operator` | `Operator` | Yes | The operator to use. |
| `arguments` | `list[FilterDirective]` | Yes | The arguments to the operator. |

## Extends

- `FilterDirective`

## Constructors

```python
__init__(
    self,
    operator: Operator,
    arguments: list[FilterDirective],
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `operator` | `Operator` |
| `arguments` | `list[FilterDirective]` |

## Properties

- `operator`
- `arguments`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/structured_query.py#L154)
