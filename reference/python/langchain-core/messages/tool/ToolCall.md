---
title: "ToolCall"
description: "Represents an AI's request to call a tool."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/ToolCall"
category: "reference"
tags: [reference, langchain-core, messages, tool, toolcall]
---

# ToolCall

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/ToolCall)

Represents an AI's request to call a tool.

## Signature

```python
ToolCall()
```

## Description

**Example:**

```python
{"name": "foo", "args": {"a": 1}, "id": "123"}
```

This represents a request to call the tool named `'foo'` with arguments
`{"a": 1}` and an identifier of `'123'`.

!!! note "Factory function"

`tool_call` may also be used as a factory to create a `ToolCall`. Benefits
include:

* Required arguments strictly validated at creation time

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    args: dict[str, Any],
    id: str | None,
    type: NotRequired[Literal['tool_call']],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `args` | `dict[str, Any]` |
| `id` | `str \| None` |
| `type` | `NotRequired[Literal['tool_call']]` |

## Properties

- `name`
- `args`
- `id`
- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/messages/tool.py#L206)
