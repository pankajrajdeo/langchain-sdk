---
title: "get_history"
description: "Get the state history of a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/get_history"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, get_history]
---

# get_history

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/get_history)

Get the state history of a thread.

## Signature

```python
get_history(
    self,
    thread_id: str,
    *,
    limit: int = 10,
    before: str | Checkpoint | None = None,
    metadata: Mapping[str, Any] | None = None,
    checkpoint: Checkpoint | None = None,
    select: list[ThreadStateSelectField] | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> list[ThreadState]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024)
thread_state = await client.threads.get_history(
    thread_id="my_thread_id",
    limit=5,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to get the state history for. |
| `checkpoint` | `Checkpoint \| None` | No | Return states for this subgraph. If empty defaults to root. (default: `None`) |
| `limit` | `int` | No | The maximum number of states to return. (default: `10`) |
| `before` | `str \| Checkpoint \| None` | No | Return states before this checkpoint. (default: `None`) |
| `metadata` | `Mapping[str, Any] \| None` | No | Filter states by metadata key-value pairs. (default: `None`) |
| `select` | `list[ThreadStateSelectField] \| None` | No | Fields to include in the response. Use `values.<key>` to return a single state key (e.g. `values.messages`), which lets the server skip loading the rest of the state. Defaults to all fields. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`list[ThreadState]`

The state history of the thread.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/_async/threads.py#L708)
