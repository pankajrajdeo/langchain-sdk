---
title: "DebugStreamPart"
description: "Stream part emitted for stream_mode=\"debug\"."
source: "https://reference.langchain.com/python/langgraph/types/DebugStreamPart"
category: "reference"
tags: [reference, langgraph, types, debugstreampart]
---

# DebugStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/DebugStreamPart)

Stream part emitted for `stream_mode="debug"`.

## Signature

```python
DebugStreamPart()
```

## Extends

- `TypedDict`
- `Generic[StateT]`

## Constructors

```python
__init__(
    type: Literal['debug'],
    ns: tuple[str, ...],
    data: DebugPayload[StateT],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['debug']` |
| `ns` | `tuple[str, ...]` |
| `data` | `DebugPayload[StateT]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/types.py#L344)
