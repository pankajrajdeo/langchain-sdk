---
title: "Send"
description: "Represents a message to be sent to a specific node in the graph."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Send"
category: "reference"
tags: [reference, langgraph-sdk, schema, send]
---

# Send

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Send)

Represents a message to be sent to a specific node in the graph.

This type is used to explicitly send messages to nodes in the graph, typically
used within Command objects to control graph execution flow.

## Signature

```python
Send()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    node: str,
    input: dict[str, Any] | None,
)
```

| Name | Type |
|------|------|
| `node` | `str` |
| `input` | `dict[str, Any] \| None` |

## Properties

- `node`
- `input`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L877)
