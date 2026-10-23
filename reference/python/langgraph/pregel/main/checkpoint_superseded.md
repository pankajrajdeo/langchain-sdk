---
title: "checkpoint_superseded"
description: "Whether the thread has moved past saved, the checkpoint config addressed."
source: "https://reference.langchain.com/python/langgraph/pregel/main/checkpoint_superseded"
category: "reference"
tags: [reference, langgraph, pregel, main, checkpoint_superseded]
---

# checkpoint_superseded

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/checkpoint_superseded)

Whether the thread has moved past `saved`, the checkpoint `config` addressed.

A checkpoint with a child is never the latest put, so this misses none. A
leaf of an abandoned branch counts as well; telling it apart would mean
listing the thread to look for children, which the saver can't do cheaply.

## Signature

```python
checkpoint_superseded(
    saver: BaseCheckpointSaver,
    config: RunnableConfig,
    saved: CheckpointTuple,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_checkpoint.py#L174)
