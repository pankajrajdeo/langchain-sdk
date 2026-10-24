---
title: "AnyValue"
description: "Stores the last value received, assumes that if multiple values are received, they are all equal."
source: "https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue"
category: "reference"
tags: [reference, langgraph, channels, any_value, anyvalue]
---

# AnyValue

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue)

Stores the last value received, assumes that if multiple values are
received, they are all equal.

## Signature

```python
AnyValue(
    self,
    typ: Any,
    key: str = '',
)
```

## Extends

- `Generic[Value]`
- `BaseChannel[Value, Value, Value]`

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
- `ValueType`
- `UpdateType`

## Methods

- [`copy()`](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue/copy)
- [`from_checkpoint()`](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue/from_checkpoint)
- [`update()`](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue/update)
- [`get()`](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue/get)
- [`is_available()`](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue/is_available)
- [`checkpoint()`](https://reference.langchain.com/python/langgraph/channels/any_value/AnyValue/checkpoint)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/channels/any_value.py#L15)
