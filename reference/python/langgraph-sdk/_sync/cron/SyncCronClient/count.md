---
title: "count"
description: "Count cron jobs matching filters."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/cron/SyncCronClient/count"
category: "reference"
tags: [reference, langgraph-sdk, sync, cron, synccronclient, count]
---

# count

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/cron/SyncCronClient/count)

Count cron jobs matching filters.

## Signature

```python
count(
    self,
    *,
    assistant_id: str | None = None,
    thread_id: str | None = None,
    metadata: Json = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> int
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str \| None` | No | Assistant ID to filter by. (default: `None`) |
| `thread_id` | `str \| None` | No | Thread ID to filter by. (default: `None`) |
| `metadata` | `Json` | No | Metadata to filter by. Exact match filter for each KV pair. !!! version-added "Added in Agent Server version 0.9.0" (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`int`

Number of crons matching the criteria.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/_sync/cron.py#L498)
