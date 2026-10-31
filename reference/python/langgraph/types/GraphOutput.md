---
title: "GraphOutput"
description: "Typed container returned by invoke() / ainvoke() with version=\"v2\"."
source: "https://reference.langchain.com/python/langgraph/types/GraphOutput"
category: "reference"
tags: [reference, langgraph, types, graphoutput]
---

# GraphOutput

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/GraphOutput)

Typed container returned by `invoke()` / `ainvoke()` with `version="v2"`.

## Signature

```python
GraphOutput(
    self,
    value: OutputT,
    interrupts: tuple[Interrupt, ...] = (),
)
```

## Extends

- `Generic[OutputT]`

## Constructors

```python
__init__(
    self,
    value: OutputT,
    interrupts: tuple[Interrupt, ...] = (),
) -> None
```

| Name | Type |
|------|------|
| `value` | `OutputT` |
| `interrupts` | `tuple[Interrupt, ...]` |

## Properties

- `value`
- `interrupts`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/types.py#L379)
