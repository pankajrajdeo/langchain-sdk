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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/stream/run_stream.py#L659)
