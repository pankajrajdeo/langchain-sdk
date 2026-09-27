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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/_async/http.py#L187)
