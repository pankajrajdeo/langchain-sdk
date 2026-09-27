---
title: "patch"
description: "Send a PATCH request."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/patch"
category: "reference"
tags: [reference, langgraph-sdk, async, http, httpclient, patch]
---

# patch

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/patch)

Send a `PATCH` request.

## Signature

```python
patch(
    self,
    path: str,
    *,
    json: dict,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/_async/http.py#L100)
