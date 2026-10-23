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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/utils.py#L538)
