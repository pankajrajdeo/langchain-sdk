---
title: "AsyncSubgraphRunStream"
description: "Async handle for a discovered subgraph (extends AsyncGraphRunStream)."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/AsyncSubgraphRunStream"
category: "reference"
tags: [reference, langgraph, stream, run_stream, asyncsubgraphrunstream]
---

# AsyncSubgraphRunStream

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/run_stream/AsyncSubgraphRunStream)

Async handle for a discovered subgraph (extends `AsyncGraphRunStream`).

## Signature

```python
AsyncSubgraphRunStream(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
)
```

## Extends

- `AsyncGraphRunStream`
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/stream/run_stream.py#L702)
