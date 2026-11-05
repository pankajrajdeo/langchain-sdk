---
title: "request_reconnect"
description: "Send a request that reconnects to its Location header if the response is cut off, with backoff between attempts."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/request_reconnect"
category: "reference"
tags: [reference, langgraph-sdk, async, http, httpclient, request_reconnect]
---

# request_reconnect

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/request_reconnect)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/_async/http.py#L145)
