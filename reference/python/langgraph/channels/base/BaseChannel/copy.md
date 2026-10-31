---
title: "copy"
description: "Return a copy of the channel."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/copy"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, copy]
---

# copy

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/copy)

Return a copy of the channel.

By default, delegates to `checkpoint()` and `from_checkpoint()`.

Subclasses can override this method with a more efficient implementation.

## Signature

```python
copy(
    self,
) -> Self
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/channels/base.py#L40)
