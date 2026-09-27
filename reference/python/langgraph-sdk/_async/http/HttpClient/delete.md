---
title: "delete"
description: "Send a DELETE request."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/delete"
category: "reference"
tags: [reference, langgraph-sdk, async, http, httpclient, delete]
---

# delete

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/http/HttpClient/delete)

Send a `DELETE` request.

## Signature

```python
delete(
    self,
    path: str,
    *,
    json: Any | None = None,
    params: QueryParamTypes | None = None,
    headers: Mapping[str, str] | None = None,
    on_response: Callable[[httpx.Response], None] | None = None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/_async/http.py#L121)
