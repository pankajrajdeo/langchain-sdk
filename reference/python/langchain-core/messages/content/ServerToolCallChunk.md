---
title: "ServerToolCallChunk"
description: "A chunk of a server-side tool call (yielded when streaming)."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ServerToolCallChunk"
category: "reference"
tags: [reference, langchain-core, messages, content, servertoolcallchunk]
---

# ServerToolCallChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ServerToolCallChunk)

A chunk of a server-side tool call (yielded when streaming).

## Signature

```python
ServerToolCallChunk()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['server_tool_call_chunk'],
    name: NotRequired[str],
    args: NotRequired[str],
    id: NotRequired[str],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['server_tool_call_chunk']` |
| `name` | `NotRequired[str]` |
| `args` | `NotRequired[str]` |
| `id` | `NotRequired[str]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `name`
- `args`
- `id`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/content.py#L397)
