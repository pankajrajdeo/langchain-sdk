---
title: "awrite"
description: "Async version of write using native store async methods."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/awrite"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, awrite]
---

# awrite

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/awrite)

Async version of write using native store async methods.

This avoids sync calls in async context by using `store.aget`/`aput` directly.

## Signature

```python
awrite(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/backends/store.py#L450)
