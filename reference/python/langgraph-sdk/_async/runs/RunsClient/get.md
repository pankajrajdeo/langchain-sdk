---
title: "get"
description: "Get a run."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/get"
category: "reference"
tags: [reference, langgraph-sdk, async, runs, runsclient, get]
---

# get

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/runs/RunsClient/get)

Get a run.

## Signature

```python
get(
    self,
    thread_id: str,
    run_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Run
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
run = await client.runs.get(
    thread_id="thread_id_to_delete",
    run_id="run_id_to_delete",
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The thread ID to get. |
| `run_id` | `str` | Yes | The run ID to get. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Run`

`Run` object.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/_async/runs.py#L906)
