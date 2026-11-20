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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/errors.py#L112)
