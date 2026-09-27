---
title: "file_data_to_string"
description: "Convert current or legacy persisted file content to a string."
source: "https://reference.langchain.com/python/deepagents/backends/state/file_data_to_string"
category: "reference"
tags: [reference, deepagents, backends, state, file_data_to_string]
---

# file_data_to_string

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/file_data_to_string)

Convert current or legacy persisted file content to a string.

## Signature

```python
file_data_to_string(
    file_data: FileData,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_data` | `FileData` | Yes | File data whose content is a string or legacy list of strings. |

## Returns

`str`

Content as a single string.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/backends/utils.py#L498)
