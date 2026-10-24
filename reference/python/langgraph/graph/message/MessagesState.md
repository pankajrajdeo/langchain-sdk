---
title: "MessagesState"
description: "- TypedDict"
source: "https://reference.langchain.com/python/langgraph/graph/message/MessagesState"
category: "reference"
tags: [reference, langgraph, graph, message, messagesstate]
---

# MessagesState

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/message/MessagesState)

## Signature

```python
MessagesState()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    messages: Annotated[list[AnyMessage], add_messages],
)
```

| Name | Type |
|------|------|
| `messages` | `Annotated[list[AnyMessage], add_messages]` |

## Properties

- `messages`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/graph/message.py#L310)
