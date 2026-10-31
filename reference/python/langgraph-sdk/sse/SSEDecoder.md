---
title: "SSEDecoder"
description: "- has_data - last_event_id"
source: "https://reference.langchain.com/python/langgraph-sdk/sse/SSEDecoder"
category: "reference"
tags: [reference, langgraph-sdk, sse, ssedecoder]
---

# SSEDecoder

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/sse/SSEDecoder)

## Signature

```python
SSEDecoder(
    self,
    *,
    last_event_id: str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    *,
    last_event_id: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `last_event_id` | `str \| None` |

## Properties

- `has_data`
- `last_event_id`

## Methods

- [`decode()`](https://reference.langchain.com/python/langgraph-sdk/sse/SSEDecoder/decode)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/sse.py#L74)
