---
title: "format_content_with_line_numbers"
description: "Format file content with line numbers."
source: "https://reference.langchain.com/python/deepagents/backends/utils/format_content_with_line_numbers"
category: "reference"
tags: [reference, deepagents, backends, utils, format_content_with_line_numbers]
---

# format_content_with_line_numbers

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/format_content_with_line_numbers)

Format file content with line numbers.

Chunks lines longer than `MAX_LINE_LENGTH` with continuation markers
(e.g., `5.1`, `5.2`). Line markers are separated from source content
with two spaces so source tabs cannot be confused with a gutter separator.

## Signature

```python
format_content_with_line_numbers(
    content: str | list[str],
    start_line: int = 1,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str \| list[str]` | Yes | File content as string or list of lines |
| `start_line` | `int` | No | Starting line number (default: `1`) |

## Returns

`str`

Formatted content with line numbers and continuation markers

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/utils.py#L208)
