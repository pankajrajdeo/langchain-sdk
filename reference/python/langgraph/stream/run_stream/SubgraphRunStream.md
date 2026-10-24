---
title: "SubgraphRunStream"
description: "Sync handle for a discovered subgraph (extends GraphRunStream)."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/SubgraphRunStream"
category: "reference"
tags: [reference, langgraph, stream, run_stream, subgraphrunstream]
---

# SubgraphRunStream

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/run_stream/SubgraphRunStream)

Sync handle for a discovered subgraph (extends `GraphRunStream`).

## Signature

```python
SubgraphRunStream(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
)
```

## Extends

- `GraphRunStream`
- `_SubgraphRunStreamMixin`

## Constructors

```python
__init__(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `mux` | `StreamMux` |
| `path` | `tuple[str, ...]` |
| `graph_name` | `str \| None` |
| `trigger_call_id` | `str \| None` |

## Properties

- `path`
- `graph_name`
- `trigger_call_id`
- `status`
- `error`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/stream/run_stream.py#L659)
