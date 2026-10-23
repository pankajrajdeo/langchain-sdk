---
title: "check_empty_content"
description: "Check if content is empty and return warning message."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/check_empty_content"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, check_empty_content]
---

# check_empty_content

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/check_empty_content)

Check if content is empty and return warning message.

## Signature

```python
check_empty_content(
    content: str,
) -> str | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | Content to check |

## Returns

`str | None`

Warning message if empty, `None` otherwise

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/utils.py#L438)
