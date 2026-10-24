---
title: "LastValueAfterFinish"
description: "Stores the last value received, but only made available after finish(). Once made available, clears the value."
source: "https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish"
category: "reference"
tags: [reference, langgraph, channels, last_value, lastvalueafterfinish]
---

# LastValueAfterFinish

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish)

Stores the last value received, but only made available after finish().
Once made available, clears the value.

## Signature

```python
LastValueAfterFinish(
    self,
    typ: Any,
    key: str = '',
)
```

## Extends

- `Generic[Value]`
- `BaseChannel[Value, Value, tuple[Value, bool]]`

## Constructors

```python
__init__(
    self,
    typ: Any,
    key: str = '',
) -> None
```

| Name | Type |
|------|------|
| `typ` | `Any` |
| `key` | `str` |

## Properties

- `value`
- `finished`
- `ValueType`
- `UpdateType`

## Methods

- [`checkpoint()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/checkpoint)
- [`from_checkpoint()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/from_checkpoint)
- [`update()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/update)
- [`consume()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/consume)
- [`finish()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/finish)
- [`get()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/get)
- [`is_available()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValueAfterFinish/is_available)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/channels/last_value.py#L81)
