---
title: "is_available"
description: "Return True if the channel is available (not empty), False otherwise."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/is_available"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, is_available]
---

# is_available

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/is_available)

Return `True` if the channel is available (not empty), `False` otherwise.

Subclasses should override this method to provide a more efficient
implementation than calling `get()` and catching `EmptyChannelError`.

## Signature

```python
is_available(
    self,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/channels/base.py#L75)
