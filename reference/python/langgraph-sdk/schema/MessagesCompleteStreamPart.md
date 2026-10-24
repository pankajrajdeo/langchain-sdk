---
title: "MessagesCompleteStreamPart"
description: "Stream part emitted for complete messages (messages/complete)."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/MessagesCompleteStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, messagescompletestreampart]
---

# MessagesCompleteStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/MessagesCompleteStreamPart)

Stream part emitted for complete messages (`messages/complete`).

## Signature

```python
MessagesCompleteStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['messages/complete'],
    ns: list[str],
    data: list[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['messages/complete']` |
| `ns` | `list[str]` |
| `data` | `list[dict[str, Any]]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L770)
