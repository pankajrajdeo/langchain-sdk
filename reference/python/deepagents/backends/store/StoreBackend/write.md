---
title: "write"
description: "Write content to a file, creating it or overwriting it if it already exists."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/write"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/write)

Write content to a file, creating it or overwriting it if it already exists.

Returns `WriteResult` on success or error.

## Signature

```python
write(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/18930b5463c8a0a432353db5299af280f879973f/libs/deepagents/deepagents/backends/store.py#L428)
