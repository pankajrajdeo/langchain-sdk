---
title: "ReplayState"
description: "Tracks which subgraphs have already loaded their pre-replay checkpoint."
source: "https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState"
category: "reference"
tags: [reference, langgraph, internal, replay, replaystate]
---

# ReplayState

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState)

Tracks which subgraphs have already loaded their pre-replay checkpoint.

During a parent replay, each subgraph's first invocation should restore the
checkpoint from before the replay point. Subsequent invocations of the same
subgraph (e.g. in a loop) should use normal checkpoint loading so they pick
up freshly created checkpoints.

The single `ReplayState` instance is shared by reference across all derived
configs within one parent execution.

## Signature

```python
ReplayState(
    self,
    checkpoint_id: str,
)
```

## Constructors

```python
__init__(
    self,
    checkpoint_id: str,
) -> None
```

| Name | Type |
|------|------|
| `checkpoint_id` | `str` |

## Properties

- `checkpoint_id`

## Methods

- [`get_checkpoint()`](https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState/get_checkpoint)
- [`aget_checkpoint()`](https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState/aget_checkpoint)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_replay.py#L14)
