---
title: "get_updated_channels_from_tasks"
description: "Channel names written by an update_state superstep (excluding PUSH)."
source: "https://reference.langchain.com/python/langgraph/pregel/main/get_updated_channels_from_tasks"
category: "reference"
tags: [reference, langgraph, pregel, main, get_updated_channels_from_tasks]
---

# get_updated_channels_from_tasks

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/get_updated_channels_from_tasks)

Channel names written by an update_state superstep (excluding PUSH).

## Signature

```python
get_updated_channels_from_tasks(
    run_tasks: Iterable[Any],
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_checkpoint.py#L120)
