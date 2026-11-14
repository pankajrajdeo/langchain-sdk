---
title: "edit"
description: "Edit a file by replacing string occurrences."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/edit"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/edit)

Edit a file by replacing string occurrences.

Returns `EditResult` on success or error.

## Signature

```python
edit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/store.py#L474)
