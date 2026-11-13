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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/store.py#L451)
