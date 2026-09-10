---
title: "default_tool_chunk_parser"
description: "Best-effort parsing of tool chunks."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/default_tool_chunk_parser"
category: "reference"
tags: [reference, langchain-core, messages, ai, default_tool_chunk_parser]
---

# default_tool_chunk_parser

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/default_tool_chunk_parser)

Best-effort parsing of tool chunks.

## Signature

```python
default_tool_chunk_parser(
    raw_tool_calls: list[dict[str, Any]],
) -> list[ToolCallChunk]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_tool_calls` | `list[dict[str, Any]]` | Yes | List of raw tool call dicts to parse. |

## Returns

`list[ToolCallChunk]`

List of parsed ToolCallChunk objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/tool.py#L386)
