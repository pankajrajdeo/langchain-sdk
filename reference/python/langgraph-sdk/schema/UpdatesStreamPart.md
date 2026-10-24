---
title: "UpdatesStreamPart"
description: "Stream part emitted for stream_mode=\"updates\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/UpdatesStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, updatesstreampart]
---

# UpdatesStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/UpdatesStreamPart)

Stream part emitted for `stream_mode="updates"`.

## Signature

```python
UpdatesStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['updates'],
    ns: list[str],
    data: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['updates']` |
| `ns` | `list[str]` |
| `data` | `dict[str, Any]` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/schema.py#L748)
