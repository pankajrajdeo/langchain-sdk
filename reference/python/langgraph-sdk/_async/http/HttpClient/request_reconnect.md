---
title: "request_reconnect"
description: "Send a request that automatically reconnects to Location header."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/request_reconnect"
category: "reference"
tags: [reference, langgraph-sdk, async, http, httpclient, request_reconnect]
---

# request_reconnect

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/request_reconnect)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/_async/http.py#L138)
