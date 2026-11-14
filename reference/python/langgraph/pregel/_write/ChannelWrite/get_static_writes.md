---
title: "get_static_writes"
description: "Used to get conditional writes a writer declares for static analysis."
source: "https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/get_static_writes"
category: "reference"
tags: [reference, langgraph, pregel, write, channelwrite, get_static_writes]
---

# get_static_writes

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/get_static_writes)

Used to get conditional writes a writer declares for static analysis.

## Signature

```python
get_static_writes(
    runnable: Runnable,
) -> Sequence[tuple[str, Any, str | None]] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/_write.py#L136)
