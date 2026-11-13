---
title: "update_file_data"
description: "Update FileData with new content, preserving creation timestamp."
source: "https://reference.langchain.com/python/deepagents/backends/store/update_file_data"
category: "reference"
tags: [reference, deepagents, backends, store, update_file_data]
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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/utils.py#L538)
