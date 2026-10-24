---
title: "CustomStreamPart"
description: "Stream part emitted for stream_mode=\"custom\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/CustomStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, customstreampart]
---

# CustomStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/CustomStreamPart)

Stream part emitted for `stream_mode="custom"`.

## Signature

```python
CustomStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['custom'],
    ns: list[str],
    data: Any,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['custom']` |
| `ns` | `list[str]` |
| `data` | `Any` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L803)
