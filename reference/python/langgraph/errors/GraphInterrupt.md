---
title: "GraphInterrupt"
description: "Raised when a subgraph is interrupted, suppressed by the root graph. Never raised directly, or surfaced to the user."
source: "https://reference.langchain.com/python/langgraph/errors/GraphInterrupt"
category: "reference"
tags: [reference, langgraph, errors, graphinterrupt]
---

# GraphInterrupt

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/GraphInterrupt)

Raised when a subgraph is interrupted, suppressed by the root graph.
Never raised directly, or surfaced to the user.

## Signature

```python
GraphInterrupt(
    self,
    interrupts: Sequence[Interrupt] = (),
)
```

## Extends

- `GraphBubbleUp`

## Constructors

```python
__init__(
    self,
    interrupts: Sequence[Interrupt] = (),
) -> None
```

| Name | Type |
|------|------|
| `interrupts` | `Sequence[Interrupt]` |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/errors.py#L103)
