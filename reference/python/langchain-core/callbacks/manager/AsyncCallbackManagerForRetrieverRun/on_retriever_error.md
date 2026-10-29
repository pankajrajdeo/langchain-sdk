---
title: "on_retriever_error"
description: "Run when retriever errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun/on_retriever_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforretrieverrun, on_retriever_error]
---

# on_retriever_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun/on_retriever_error)

Run when retriever errors.

## Signature

```python
on_retriever_error(
    self,
    error: BaseException,
    kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/callbacks/manager.py#L1361)
