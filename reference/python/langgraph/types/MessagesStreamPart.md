---
title: "MessagesStreamPart"
description: "Stream part emitted for stream_mode=\"messages\"."
source: "https://reference.langchain.com/python/langgraph/types/MessagesStreamPart"
category: "reference"
tags: [reference, langgraph, types, messagesstreampart]
---

# MessagesStreamPart

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/MessagesStreamPart)

Stream part emitted for `stream_mode="messages"`.

`data` is a 2-tuple of `(message, metadata)` where `message` is a
`BaseMessage` (e.g. `AIMessageChunk`) and `metadata` is a dict containing
keys like `langgraph_step`, `langgraph_node`, `langgraph_triggers`, etc.

## Signature

```python
MessagesStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['messages'],
    ns: tuple[str, ...],
    data: tuple[AnyMessage, dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['messages']` |
| `ns` | `tuple[str, ...]` |
| `data` | `tuple[AnyMessage, dict[str, Any]]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/types.py#L297)
