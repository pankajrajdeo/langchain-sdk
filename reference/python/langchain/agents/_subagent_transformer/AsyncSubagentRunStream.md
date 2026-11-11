---
title: "AsyncSubagentRunStream"
description: "Typed async handle for a nested named-agent execution."
source: "https://reference.langchain.com/python/langchain/agents/_subagent_transformer/AsyncSubagentRunStream"
category: "reference"
tags: [reference, langchain, agents, subagent_transformer, asyncsubagentrunstream]
---

# AsyncSubagentRunStream

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/AsyncSubagentRunStream)

Typed async handle for a nested named-agent execution.

## Signature

```python
AsyncSubagentRunStream(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
    cause: LifecycleCause | None = None,
)
```

## Extends

- `AsyncSubgraphRunStream`

## Constructors

```python
__init__(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
    cause: LifecycleCause | None = None,
) -> None
```

| Name | Type |
|------|------|
| `mux` | `StreamMux` |
| `path` | `tuple[str, ...]` |
| `graph_name` | `str \| None` |
| `trigger_call_id` | `str \| None` |
| `cause` | `LifecycleCause \| None` |

## Properties

- `name`
- `cause`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/_subagent_transformer.py#L84)
