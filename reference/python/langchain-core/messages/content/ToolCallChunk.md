---
title: "ToolCallChunk"
description: "A chunk of a tool call (yielded when streaming)."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ToolCallChunk"
category: "reference"
tags: [reference, langchain-core, messages, content, toolcallchunk]
---

# ToolCallChunk

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ToolCallChunk)

A chunk of a tool call (yielded when streaming).

When merging `ToolCallChunks` (e.g., via `AIMessageChunk.__add__`),
all string attributes are concatenated. Chunks are only merged if their
values of `index` are equal and not `None`.

Example:
```python
left_chunks = [ToolCallChunk(name="foo", args='{"a":', index=0)]
right_chunks = [ToolCallChunk(name=None, args="1}", index=0)]

(
    AIMessageChunk(content="", tool_call_chunks=left_chunks)
    + AIMessageChunk(content="", tool_call_chunks=right_chunks)
).tool_call_chunks == [ToolCallChunk(name="foo", args='{"a":1}', index=0)]
```

## Signature

```python
ToolCallChunk()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['tool_call_chunk'],
    id: str | None,
    name: str | None,
    args: str | None,
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['tool_call_chunk']` |
| `id` | `str \| None` |
| `name` | `str \| None` |
| `args` | `str \| None` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `name`
- `args`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/content.py#L291)
