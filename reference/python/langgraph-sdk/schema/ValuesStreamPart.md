---
title: "ValuesStreamPart"
description: "Stream part emitted for stream_mode=\"values\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/ValuesStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, valuesstreampart]
---

# ValuesStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/ValuesStreamPart)

Stream part emitted for `stream_mode="values"`.

## Signature

```python
ValuesStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['values'],
    ns: list[str],
    data: dict[str, Any],
    interrupts: list[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['values']` |
| `ns` | `list[str]` |
| `data` | `dict[str, Any]` |
| `interrupts` | `list[dict[str, Any]]` |

## Properties

- `type`
- `ns`
- `data`
- `interrupts`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/schema.py#L735)
