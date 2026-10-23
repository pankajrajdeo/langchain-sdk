---
title: "patch"
description: "Send a PATCH request."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/patch"
category: "reference"
tags: [reference, langgraph-sdk, sync, http, synchttpclient, patch]
---

# patch

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/http/SyncHttpClient/patch)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/_sync/http.py#L100)
