---
title: "MessagesPartialStreamPart"
description: "Stream part emitted for partial message chunks (messages/partial)."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/MessagesPartialStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, messagespartialstreampart]
---

# MessagesPartialStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/MessagesPartialStreamPart)

Stream part emitted for partial message chunks (`messages/partial`).

## Signature

```python
MessagesPartialStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['messages/partial'],
    ns: list[str],
    data: list[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['messages/partial']` |
| `ns` | `list[str]` |
| `data` | `list[dict[str, Any]]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/schema.py#L759)
