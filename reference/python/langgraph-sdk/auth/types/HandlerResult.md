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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/auth/types.py#L138)
