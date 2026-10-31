---
title: "Interrupt"
description: "Represents an interruption in the execution flow."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Interrupt"
category: "reference"
tags: [reference, langgraph-sdk, schema, interrupt]
---

# Interrupt

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Interrupt)

Represents an interruption in the execution flow.

## Signature

```python
Interrupt()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    value: Any,
    id: str,
    response_schema: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `value` | `Any` |
| `id` | `str` |
| `response_schema` | `NotRequired[dict[str, Any]]` |

## Properties

- `value`
- `id`
- `response_schema`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/schema.py#L291)
