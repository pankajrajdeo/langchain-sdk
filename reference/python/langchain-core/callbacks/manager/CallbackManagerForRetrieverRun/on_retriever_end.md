---
title: "on_retriever_end"
description: "Run when retriever ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_end"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforretrieverrun, on_retriever_end]
---

# on_retriever_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_end)

Run when retriever ends running.

## Signature

```python
on_retriever_end(
    self,
    documents: Sequence[Document],
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | The retrieved documents. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L1251)
