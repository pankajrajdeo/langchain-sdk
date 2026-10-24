---
title: "update_file_data"
description: "Update FileData with new content, preserving creation timestamp."
source: "https://reference.langchain.com/python/deepagents/backends/state/update_file_data"
category: "reference"
tags: [reference, deepagents, backends, state, update_file_data]
---

# update_file_data

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/update_file_data)

Update `FileData` with new content, preserving creation timestamp.

## Signature

```python
update_file_data(
    file_data: FileData,
    content: str,
) -> FileData
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_data` | `FileData` | Yes | Existing `FileData` dict |
| `content` | `str` | Yes | New content as string |

## Returns

`FileData`

Updated `FileData` dict

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/utils.py#L538)
