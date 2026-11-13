---
title: "get"
description: "Return the current value of the channel."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/get"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, get]
---

# get

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/get)

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

## Signature

```python
get(
    self,
) -> Value
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/channels/base.py#L69)
