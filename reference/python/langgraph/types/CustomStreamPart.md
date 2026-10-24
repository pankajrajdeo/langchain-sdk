---
title: "CustomStreamPart"
description: "Stream part emitted for stream_mode=\"custom\"."
source: "https://reference.langchain.com/python/langgraph/types/CustomStreamPart"
category: "reference"
tags: [reference, langgraph, types, customstreampart]
---

# CustomStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/CustomStreamPart)

Stream part emitted for `stream_mode="custom"`.

`data` is whatever value was passed to `StreamWriter` inside a node.

## Signature

```python
CustomStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['custom'],
    ns: tuple[str, ...],
    data: Any,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['custom']` |
| `ns` | `tuple[str, ...]` |
| `data` | `Any` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/types.py#L310)
