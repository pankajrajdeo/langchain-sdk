---
title: "get_state_history"
description: "Get the state history of a thread."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/get_state_history"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, get_state_history]
---

# get_state_history

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/get_state_history)

Get the state history of a thread.

This method calls `POST /threads/{thread_id}/history`.

## Signature

```python
get_state_history(
    self,
    config: RunnableConfig,
    *,
    filter: dict[str, Any] | None = None,
    before: RunnableConfig | None = None,
    limit: int | None = None,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Iterator[StateSnapshot]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | A `RunnableConfig` that includes `thread_id` in the `configurable` field. |
| `filter` | `dict[str, Any] \| None` | No | Metadata to filter on. (default: `None`) |
| `before` | `RunnableConfig \| None` | No | A `RunnableConfig` that includes checkpoint metadata. (default: `None`) |
| `limit` | `int \| None` | No | Max number of states to return. (default: `None`) |

## Returns

`Iterator[StateSnapshot]`

States of the thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/remote.py#L508)
