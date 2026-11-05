---
title: "CheckpointPayload"
description: "Payload for a checkpoint event."
source: "https://reference.langchain.com/python/langgraph/types/CheckpointPayload"
category: "reference"
tags: [reference, langgraph, types, checkpointpayload]
---

# CheckpointPayload

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/CheckpointPayload)

Payload for a checkpoint event.

## Signature

```python
CheckpointPayload()
```

## Extends

- `TypedDict`
- `Generic[StateT]`

## Constructors

```python
__init__(
    config: RunnableConfig | None,
    metadata: CheckpointMetadata,
    values: StateT,
    next: list[str],
    parent_config: RunnableConfig | None,
    tasks: list[CheckpointTask],
)
```

| Name | Type |
|------|------|
| `config` | `RunnableConfig \| None` |
| `metadata` | `CheckpointMetadata` |
| `values` | `StateT` |
| `next` | `list[str]` |
| `parent_config` | `RunnableConfig \| None` |
| `tasks` | `list[CheckpointTask]` |

## Properties

- `config`
- `metadata`
- `values`
- `next`
- `parent_config`
- `tasks`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/types.py#L216)
