---
title: "finish"
description: "Notify the channel that the Pregel run is finishing."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/finish"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, finish]
---

# finish

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/finish)

Notify the channel that the Pregel run is finishing.

By default, no-op.

A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

## Signature

```python
finish(
    self,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/channels/base.py#L112)
