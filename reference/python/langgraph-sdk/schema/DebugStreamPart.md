---
title: "DebugStreamPart"
description: "Stream part emitted for stream_mode=\"debug\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/DebugStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, debugstreampart]
---

# DebugStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/DebugStreamPart)

Stream part emitted for `stream_mode="debug"`.

## Signature

```python
DebugStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['debug'],
    ns: list[str],
    data: DebugPayload,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['debug']` |
| `ns` | `list[str]` |
| `data` | `DebugPayload` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/schema.py#L836)
