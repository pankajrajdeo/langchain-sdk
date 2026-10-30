---
title: "merge_content"
description: "Merge multiple message contents."
source: "https://reference.langchain.com/python/langchain-core/messages/base/merge_content"
category: "reference"
tags: [reference, langchain-core, messages, base, merge_content]
---

# merge_content

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/base/merge_content)

Merge multiple message contents.

## Signature

```python
merge_content(
    first_content: str | list[str | dict[Any, Any]],
    contents: str | list[str | dict[Any, Any]] = (),
) -> str | list[str | dict[Any, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `first_content` | `str \| list[str \| dict[Any, Any]]` | Yes | The first `content`. Can be a string or a list. |
| `contents` | `str \| list[str \| dict[Any, Any]]` | No | The other `content`s. Can be a string or a list. (default: `()`) |

## Returns

`str | list[str | dict[Any, Any]]`

The merged content.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/base.py#L366)
