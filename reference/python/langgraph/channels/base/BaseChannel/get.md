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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/channels/base.py#L69)
