---
title: "CheckpointStreamPart"
description: "Stream part emitted for stream_mode=\"checkpoints\"."
source: "https://reference.langchain.com/python/langgraph/types/CheckpointStreamPart"
category: "reference"
tags: [reference, langgraph, types, checkpointstreampart]
---

# CheckpointStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/CheckpointStreamPart)

Stream part emitted for `stream_mode="checkpoints"`.

## Signature

```python
CheckpointStreamPart()
```

## Extends

- `TypedDict`
- `Generic[StateT]`

## Constructors

```python
__init__(
    type: Literal['checkpoints'],
    ns: tuple[str, ...],
    data: CheckpointPayload[StateT],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['checkpoints']` |
| `ns` | `tuple[str, ...]` |
| `data` | `CheckpointPayload[StateT]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/types.py#L322)
