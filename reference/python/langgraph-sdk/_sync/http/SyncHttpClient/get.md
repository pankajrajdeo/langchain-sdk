---
title: "get"
description: "Send a GET request."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/get"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, get]
---

# get

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/get)

Send a `GET` request.

## Signature

```python
get(
    self,
    path: str,
    *,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/_sync/http.py#L39)
