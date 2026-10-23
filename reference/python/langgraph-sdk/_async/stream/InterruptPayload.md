---
title: "InterruptPayload"
description: "Payload surfaced when the server requests human input for a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/InterruptPayload"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, interruptpayload]
---

# InterruptPayload

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/InterruptPayload)

Payload surfaced when the server requests human input for a thread.

## Signature

```python
InterruptPayload()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    interrupt_id: str,
    value: Any,
    namespace: list[str],
)
```

| Name | Type |
|------|------|
| `interrupt_id` | `str` |
| `value` | `Any` |
| `namespace` | `list[str]` |

## Properties

- `interrupt_id`
- `value`
- `namespace`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/_async/stream.py#L56)
