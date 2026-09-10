---
title: "FileData"
description: "Data structure for storing file contents with metadata."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/FileData"
category: "reference"
tags: [reference, deepagents, backends, protocol, filedata]
---

# FileData

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/FileData)

Data structure for storing file contents with metadata.

## Signature

```python
FileData()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    content: str,
    encoding: str,
    created_at: NotRequired[str],
    modified_at: NotRequired[str],
)
```

| Name | Type |
|------|------|
| `content` | `str` |
| `encoding` | `str` |
| `created_at` | `NotRequired[str]` |
| `modified_at` | `NotRequired[str]` |

## Properties

- `content`
- `encoding`
- `created_at`
- `modified_at`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/protocol.py#L187)
