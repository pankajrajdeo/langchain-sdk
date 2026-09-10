---
title: "on_retriever_error"
description: "Run when retriever errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforretrieverrun, on_retriever_error]
---

# on_retriever_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_error)

Run when retriever errors.

## Signature

```python
on_retriever_error(
    self,
    error: BaseException,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L1276)
