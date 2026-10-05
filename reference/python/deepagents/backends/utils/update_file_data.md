---
title: "update_file_data"
description: "Update FileData with new content, preserving creation timestamp."
source: "https://reference.langchain.com/python/deepagents/backends/utils/update_file_data"
category: "reference"
tags: [reference, deepagents, backends, utils, update_file_data]
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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/utils.py#L538)
