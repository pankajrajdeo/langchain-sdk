---
title: "get_relative_path"
description: "Get the path of the file as a relative path to the package directory."
source: "https://reference.langchain.com/python/langchain-core/_api/path/get_relative_path"
category: "reference"
tags: [reference, langchain-core, api, path, get_relative_path]
---

# get_relative_path

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/path/get_relative_path)

Get the path of the file as a relative path to the package directory.

## Signature

```python
get_relative_path(
    file: Path | str,
    *,
    relative_to: Path = PACKAGE_DIR,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file` | `Path \| str` | Yes | The file path to convert. |
| `relative_to` | `Path` | No | The base path to make the file path relative to. (default: `PACKAGE_DIR`) |

## Returns

`str`

The relative path as a string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/_api/path.py#L11)
