---
title: "stream"
description: "Stream results using SSE."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/stream"
category: "reference"
tags: [reference, langgraph-sdk, async, http, httpclient, stream]
---

# stream

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/stream)

Stream results using SSE.

## Signature

```python
stream(
    self,
    path: str,
    method: str,
    *,
    json: dict[str, Any] | None = None,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> AsyncIterator[StreamPart]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/_async/http.py#L209)
