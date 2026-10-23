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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/channels/base.py#L69)
