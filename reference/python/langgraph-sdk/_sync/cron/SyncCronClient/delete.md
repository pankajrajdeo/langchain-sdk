---
title: "delete"
description: "Delete a cron."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/cron/SyncCronClient/delete"
category: "reference"
tags: [reference, langgraph-sdk, sync, cron, synccronclient, delete]
---

# delete

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/cron/SyncCronClient/delete)

Delete a cron.

## Signature

```python
delete(
    self,
    cron_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:8123")
client.crons.delete(
    cron_id="cron_to_delete"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cron_id` | `str` | Yes | The cron ID to delete. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/_sync/cron.py#L284)
