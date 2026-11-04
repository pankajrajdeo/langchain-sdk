---
title: "HandlerResult"
description: "Type Alias in langgraph_sdk"
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/HandlerResult"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, handlerresult]
---

# HandlerResult

> **Type Alias** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/HandlerResult)

The result of a handler can be:
* None | True: accept the request.
* False: reject the request with a 403 error
* FilterType: filter to apply

## Signature

```python
HandlerResult = None | bool | FilterType
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/auth/types.py#L138)
