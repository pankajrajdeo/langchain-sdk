---
title: "BaseChannel"
description: "Base class for all channels."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel]
---

# BaseChannel

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel)

Base class for all channels.

## Signature

```python
BaseChannel(
    self,
    typ: Any,
    key: str = '',
)
```

## Extends

- `Generic[Value, Update, Checkpoint]`
- `ABC`

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

- `typ`
- `key`
- `ValueType`
- `UpdateType`

## Methods

- [`copy()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/copy)
- [`checkpoint()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/checkpoint)
- [`from_checkpoint()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/from_checkpoint)
- [`get()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/get)
- [`is_available()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/is_available)
- [`update()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/update)
- [`consume()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/consume)
- [`finish()`](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/finish)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/channels/base.py#L19)
