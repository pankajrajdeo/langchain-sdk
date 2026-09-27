---
title: "tool_call"
description: "Create a tool call."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/tool_call"
category: "reference"
tags: [reference, langchain-core, messages, tool, tool_call]
---

# tool_call

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/tool_call)

Create a tool call.

## Signature

```python
tool_call(
    *,
    name: str,
    args: dict[str, Any],
    id: str | None,
) -> ToolCall
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name of the tool to be called. |
| `args` | `dict[str, Any]` | Yes | The arguments to the tool call as a dictionary. |
| `id` | `str \| None` | Yes | An identifier associated with the tool call. |

## Returns

`ToolCall`

The created tool call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/messages/tool.py#L242)
