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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/channels/base.py#L40)
