---
title: "make_invalid_tool_call"
description: "Create an InvalidToolCall from a raw tool call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/make_invalid_tool_call"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, make_invalid_tool_call]
---

# make_invalid_tool_call

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/make_invalid_tool_call)

Create an `InvalidToolCall` from a raw tool call.

## Signature

```python
make_invalid_tool_call(
    raw_tool_call: dict[str, Any],
    error_msg: str | None,
) -> InvalidToolCall
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_tool_call` | `dict[str, Any]` | Yes | The raw tool call. |
| `error_msg` | `str \| None` | Yes | The error message. |

## Returns

`InvalidToolCall`

An `InvalidToolCall` instance with the error message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/output_parsers/openai_tools.py#L80)
