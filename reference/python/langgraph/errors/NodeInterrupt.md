---
title: "NodeInterrupt"
description: "Raised by a node to interrupt execution."
source: "https://reference.langchain.com/python/langgraph/errors/NodeInterrupt"
category: "reference"
tags: [reference, langgraph, errors, nodeinterrupt]
---

# NodeInterrupt

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/NodeInterrupt)

Raised by a node to interrupt execution.

## Signature

```python
NodeInterrupt(
    self,
    value: Any,
    id: str | None = None,
)
```

## Extends

- `GraphInterrupt`

## Constructors

```python
__init__(
    self,
    value: Any,
    id: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `value` | `Any` |
| `id` | `str \| None` |

## ⚠️ Deprecated

NodeInterrupt is deprecated. Please use [`interrupt`][langgraph.types.interrupt] instead.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/errors.py#L111)
