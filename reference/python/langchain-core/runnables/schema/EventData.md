---
title: "EventData"
description: "Data associated with a streaming event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/EventData"
category: "reference"
tags: [reference, langchain-core, runnables, schema, eventdata]
---

# EventData

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/EventData)

Data associated with a streaming event.

## Signature

```python
EventData()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    input: Any,
    error: NotRequired[BaseException],
    output: Any,
    chunk: Any,
    tool_call_id: NotRequired[str | None],
)
```

| Name | Type |
|------|------|
| `input` | `Any` |
| `error` | `NotRequired[BaseException]` |
| `output` | `Any` |
| `chunk` | `Any` |
| `tool_call_id` | `NotRequired[str \| None]` |

## Properties

- `input`
- `error`
- `output`
- `chunk`
- `tool_call_id`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/runnables/schema.py#L13)
