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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/channels/base.py#L40)
