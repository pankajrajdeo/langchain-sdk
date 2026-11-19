---
title: "aedit"
description: "Async version of edit using native store async methods."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aedit"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, aedit]
---

# aedit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aedit)

Async version of edit using native store async methods.

This avoids sync calls in async context by using `store.aget`/`aput` directly.

## Signature

```python
aedit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/store.py#L536)
