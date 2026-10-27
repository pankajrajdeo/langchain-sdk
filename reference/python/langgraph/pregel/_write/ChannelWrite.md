---
title: "ChannelWrite"
description: "Implements the logic for sending writes to CONFIG_KEY_SEND. Can be used as a runnable or as a static method to call imperatively."
source: "https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite"
category: "reference"
tags: [reference, langgraph, pregel, write, channelwrite]
---

# ChannelWrite

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite)

Implements the logic for sending writes to CONFIG_KEY_SEND.
Can be used as a runnable or as a static method to call imperatively.

## Signature

```python
ChannelWrite(
    self,
    writes: Sequence[ChannelWriteEntry | ChannelWriteTupleEntry | Send],
    *,
    tags: Sequence[str] | None = None,
)
```

## Extends

- `RunnableCallable`

## Constructors

```python
__init__(
    self,
    writes: Sequence[ChannelWriteEntry | ChannelWriteTupleEntry | Send],
    *,
    tags: Sequence[str] | None = None,
)
```

| Name | Type |
|------|------|
| `writes` | `Sequence[ChannelWriteEntry \| ChannelWriteTupleEntry \| Send]` |
| `tags` | `Sequence[str] \| None` |

## Properties

- `writes`

## Methods

- [`get_name()`](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/get_name)
- [`do_write()`](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/do_write)
- [`is_writer()`](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/is_writer)
- [`get_static_writes()`](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/get_static_writes)
- [`register_writer()`](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/register_writer)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_write.py#L46)
