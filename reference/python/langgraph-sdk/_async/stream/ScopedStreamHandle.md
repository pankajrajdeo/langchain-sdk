---
title: "ScopedStreamHandle"
description: "Scoped streaming handle for one discovered child invocation."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/ScopedStreamHandle"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, scopedstreamhandle]
---

# ScopedStreamHandle

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/ScopedStreamHandle)

Scoped streaming handle for one discovered child invocation.

## Signature

```python
ScopedStreamHandle(
    self,
    *,
    thread: AsyncThreadStream,
    path: tuple[str, ...],
    graph_name: str | None,
    trigger_call_id: str | None,
    max_queue_size: int = 0,
)
```

## Constructors

```python
__init__(
    self,
    *,
    thread: AsyncThreadStream,
    path: tuple[str, ...],
    graph_name: str | None,
    trigger_call_id: str | None,
    max_queue_size: int = 0,
) -> None
```

| Name | Type |
|------|------|
| `thread` | `AsyncThreadStream` |
| `path` | `tuple[str, ...]` |
| `graph_name` | `str \| None` |
| `trigger_call_id` | `str \| None` |
| `max_queue_size` | `int` |

## Properties

- `path`
- `namespace`
- `graph_name`
- `trigger_call_id`
- `status`
- `error`
- `messages`
- `tool_calls`
- `subgraphs`
- `subagents`
- `extensions`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/_async/stream.py#L556)
