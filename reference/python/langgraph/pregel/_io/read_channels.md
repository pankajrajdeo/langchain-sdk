---
title: "read_channels"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_io/read_channels"
category: "reference"
tags: [reference, langgraph, pregel, io, read_channels]
---

# read_channels

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/read_channels)

## Signature

```python
read_channels(
    channels: Mapping[str, BaseChannel],
    select: Sequence[str] | str,
    *,
    skip_empty: bool = True,
) -> dict[str, Any] | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_io.py#L38)
