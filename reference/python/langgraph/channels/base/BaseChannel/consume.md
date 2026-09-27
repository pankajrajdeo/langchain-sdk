---
title: "consume"
description: "Notify the channel that a subscribed task ran."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/consume"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, consume]
---

# consume

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/consume)

Notify the channel that a subscribed task ran.

By default, no-op.

A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

## Signature

```python
consume(
    self,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/channels/base.py#L101)
