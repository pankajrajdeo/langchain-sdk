---
title: "default_tool_parser"
description: "Best-effort parsing of tools."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/default_tool_parser"
category: "reference"
tags: [reference, langchain-core, messages, tool, default_tool_parser]
---

# default_tool_parser

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/default_tool_parser)

Best-effort parsing of tools.

## Signature

```python
default_tool_parser(
    raw_tool_calls: list[dict[str, Any]],
) -> tuple[list[ToolCall], list[InvalidToolCall]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_tool_calls` | `list[dict[str, Any]]` | Yes | List of raw tool call dicts to parse. |

## Returns

`tuple[list[ToolCall], list[InvalidToolCall]]`

A list of tool calls and invalid tool calls.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/tool.py#L349)
