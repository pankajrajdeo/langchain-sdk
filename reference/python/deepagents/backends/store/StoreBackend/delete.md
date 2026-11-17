---
title: "delete"
description: "Delete a file or directory from the store."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/delete"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/delete)

Delete a file or directory from the store.

Deleting a path removes the exact key `file_path` plus every key nested
under it (the prefix `file_path` + "/"), so a directory is removed
recursively. Wildcards (e.g. `*`) in `file_path` are treated literally.

## Signature

```python
delete(
    self,
    file_path: str,
) -> DeleteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Path of the file or directory to delete. |

## Returns

`DeleteResult`

`DeleteResult` with `file_path` on success, or an error if no key is
stored at or under it.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/store.py#L577)
