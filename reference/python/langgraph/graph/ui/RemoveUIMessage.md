---
title: "RemoveUIMessage"
description: "A message type for removing UI components in LangGraph."
source: "https://reference.langchain.com/python/langgraph/graph/ui/RemoveUIMessage"
category: "reference"
tags: [reference, langgraph, graph, ui, removeuimessage]
---

# RemoveUIMessage

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/ui/RemoveUIMessage)

A message type for removing UI components in LangGraph.

This TypedDict represents a message that can be sent to remove a UI component
from the current state.

## Signature

```python
RemoveUIMessage()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['remove-ui'],
    id: str,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['remove-ui']` |
| `id` | `str` |

## Properties

- `type`
- `id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/graph/ui.py#L43)
