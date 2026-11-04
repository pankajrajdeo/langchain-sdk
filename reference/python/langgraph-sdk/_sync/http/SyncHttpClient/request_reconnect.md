---
title: "request_reconnect"
description: "Send a request that reconnects to its Location header if the response is cut off, with backoff between attempts."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/request_reconnect"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, request_reconnect]
---

# request_reconnect

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/request_reconnect)

Send a request that reconnects to its Location header if the response is
cut off, with backoff between attempts.

## Signature

```python
request_reconnect(
    self,
    path: str,
    method: str,
    *,
    json: dict[str, Any] | None = None,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
    reconnect_limit: int = 5,
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/_sync/http.py#L146)
