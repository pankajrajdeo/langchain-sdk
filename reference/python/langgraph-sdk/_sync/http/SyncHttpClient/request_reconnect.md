---
title: "request_reconnect"
description: "Send a request that automatically reconnects to Location header."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/request_reconnect"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, request_reconnect]
---

# request_reconnect

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/request_reconnect)

Send a request that automatically reconnects to Location header.

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/_sync/http.py#L138)
